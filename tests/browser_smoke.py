from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
needle = "function loop(){"
assert needle in HTML, "Could not locate game loop for test instrumentation"
instrumentation = """function loop(){
window.__smoke=()=>({state,x:player?player.x:null,y:player?player.y:null,shots:shots.length,floor,roomNo,hp:player?player.hp:null,maxHp:player?player.maxHp:null,coins,drops:drops.filter(d=>!d.gone).map(d=>d.type),shop:doors.some(d=>d.shop),keys:Array.from(keys)});
window.__testExit=(r,t)=>{const old={roomNo,floorExitRoll,floorExitSpawned,doors};roomNo=r;floorExitRoll=t;floorExitSpawned=false;doors=[{shop:false},{shop:false},{shop:false},{shop:false}];rollFloorExit();const result=doors.map(d=>!!d.floorExit);roomNo=old.roomNo;floorExitRoll=old.floorExitRoll;floorExitSpawned=old.floorExitSpawned;doors=old.doors;return result};
window.__testRoom2=()=>{roomNo=1;nextRoom(2);return doors.some(d=>d.shop)};
window.__testRestart=()=>startRun();
window.__testFullHealthHeart=()=>{const d=drops.find(d=>d.type==='heart'&&!d.gone);if(!d)return false;player.hp=player.maxHp;player.x=d.x;player.y=d.y;player.invuln=999;update();return drops.some(x=>x===d&&!x.gone)};
"""
HTML = HTML.replace(needle, instrumentation, 1)

errors = []
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1200, "height": 900})
    page.on("pageerror", lambda exc: errors.append("PAGE: " + str(exc)))
    page.on("console", lambda msg: errors.append("CONSOLE: " + msg.text) if msg.type == "error" else None)
    page.set_content(HTML, wait_until="load")
    page.wait_for_timeout(100)
    assert page.title() == "Crypt Crawler — prototyp"
    assert page.locator("canvas#game").count() == 1
    assert page.locator("#overlay").is_visible()
    assert page.evaluate("typeof window.__smoke") == "function", f"Game script did not initialize: {errors}"

    page.locator("#startBtn").click()
    page.wait_for_timeout(100)
    start = page.evaluate("window.__smoke()")
    assert start["state"] == "play", f"Start failed: {start}"
    assert not page.locator("#overlay").is_visible()
    assert start["drops"].count("heart") == 3, f"Expected 3 starting hearts: {start}"
    assert start["drops"].count("coin") == 2, f"Expected 2 starting coins: {start}"

    assert page.evaluate("window.__testFullHealthHeart()") is True, "Heart pickup vanished at full HP"
    assert page.evaluate("window.__testRoom2()") is True, "Shop is not guaranteed in room 2"
    assert page.evaluate("window.__testExit(1, 0.03)").count(True) == 1, "5% threshold should allow exit at roll 3%"
    assert page.evaluate("window.__testExit(1, 0.07)").count(True) == 0, "5% threshold should reject roll 7%"
    assert page.evaluate("window.__testExit(19, 0.94)").count(True) == 1, "95% threshold should allow exit at roll 94%"
    assert page.evaluate("window.__testExit(19, 0.96)").count(True) == 0, "95% threshold should reject roll 96%"
    assert all(page.evaluate(f"window.__testExit(20, {roll})") for roll in (0.01, 0.5, 0.99)), "Room 20 must guarantee the exit"

    page.evaluate("window.__testRestart()")
    page.wait_for_timeout(100)
    start = page.evaluate("window.__smoke()")
    page.bring_to_front()
    page.locator("canvas#game").click(position={"x": 100, "y": 100})
    page.keyboard.down("d")
    page.wait_for_timeout(350)
    moved = page.evaluate("window.__smoke()")
    page.keyboard.up("d")
    assert "d" in moved["keys"], f"Keyboard input was not registered: {moved}"
    assert moved["x"] > start["x"] + 20, f"Movement failed: {start} -> {moved}"

    canvas = page.locator("#game").bounding_box()
    page.mouse.move(canvas["x"] + canvas["width"] * .8, canvas["y"] + canvas["height"] * .5)
    page.mouse.down()
    page.wait_for_timeout(300)
    page.mouse.up()
    shooting = page.evaluate("window.__smoke()")
    assert shooting["shots"] > 0, f"Shooting failed: {shooting}"

    page.keyboard.press("p")
    assert page.locator("#overlay").is_visible(), "Pause overlay did not appear"
    assert page.locator("#overlayTitle").inner_text() == "PAUZA"
    page.keyboard.press("p")
    assert not page.locator("#overlay").is_visible(), "Resume failed"

    page.keyboard.press("r")
    reset = page.evaluate("window.__smoke()")
    assert reset["state"] == "play" and reset["floor"] == 1 and reset["roomNo"] == 1, f"Restart failed: {reset}"
    assert not errors, f"Browser errors: {errors}"
    print("PASS: startup pickups; full-HP heart persistence; guaranteed shop; cumulative exit thresholds; room-20 exit; movement; shooting; pause/resume; restart; no browser errors")
    browser.close()
