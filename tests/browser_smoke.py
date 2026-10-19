from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
needle = "function loop(){"
assert needle in HTML, "Could not locate game loop for test instrumentation"
instrumentation = """function loop(){
window.__smoke=()=>({state,x:player?player.x:null,y:player?player.y:null,shots:shots.length,floor,roomNo,hp:player?player.hp:null,maxHp:player?player.maxHp:null,coins,drops:drops.filter(d=>!d.gone).map(d=>d.type),shop:doors.some(d=>d.shop),keys:Array.from(keys),mouseDown:mouse.down,frame});
window.__testExit=(r,t)=>{const old={roomNo,floorExitPending,floorExitSpawned,doors,random:Math.random};roomNo=r;floorExitPending=false;floorExitSpawned=false;doors=[{shop:false},{shop:false},{shop:false},{shop:false}];Math.random=()=>t;rollFloorExit();const result=floorExitPending;Math.random=old.random;roomNo=old.roomNo;floorExitPending=old.floorExitPending;floorExitSpawned=old.floorExitSpawned;doors=old.doors;return result};
window.__testRoom2=()=>{roomNo=1;nextRoom(2);return doors.some(d=>d.shop)};
window.__testPendingExitRoom=()=>{roomNo=1;floor=1;floorExitPending=true;floorExitSpawned=false;nextRoom(2);return doors.some(d=>d.floorExit)&&!floorExitPending};
window.__testBossClear=()=>{enemies=[];doorOpen=false;floorExitSpawned=false;doors=[{side:'top',x:W/2,y:room.y,type:DANE_GRY.drzwi.zlote,shop:false},{side:'bottom',x:W/2,y:room.y+room.h,type:DANE_GRY.drzwi.zlote,shop:false},{side:'left',x:room.x,y:room.y+room.h/2,type:DANE_GRY.drzwi.zlote,shop:false},{side:'right',x:room.x+room.w,y:room.y+room.h/2,type:DANE_GRY.drzwi.zlote,shop:false}];player.x=W/2;player.y=H/2;state='play';update();return {doorOpen,floorExitSpawned,floor,roomNo}};
window.__testRoom30=()=>{roomNo=29;floor=1;floorExitPending=false;floorExitSpawned=false;floorBonusClaimed=false;nextRoom(2);return {allExits:doors.every(d=>d.floorExit),bonus:floorBonusClaimed,item:drops.some(d=>d.type==='item')}};
window.__testRestart=()=>startRun();
window.__testShopPurchase=()=>{coins=2;player.hp=2;state='play';openShop();updateHud();return {state,coins,hp:player.hp,buttonDisabled:document.getElementById('buyHeart').disabled}};
window.__testBossTransition=()=>{roomNo=30;floor=1;floorExitPending=false;enemies=[];doorOpen=false;floorExitSpawned=true;doors=[{side:'top',x:W/2,y:room.y,type:DANE_GRY.drzwi.zlote,floorExit:true,shop:false},{side:'bottom',x:W/2,y:room.y+room.h,type:DANE_GRY.drzwi.zlote,shop:false},{side:'left',x:room.x,y:room.y+room.h/2,type:DANE_GRY.drzwi.zlote,shop:false},{side:'right',x:room.x+room.w,y:room.y+room.h/2,type:DANE_GRY.drzwi.zlote,shop:false}];player.x=W/2;player.y=room.y;state='play';update();return {floor,roomNo,doorOpen,floorExitSpawned,bosses:enemies.filter(e=>e.type==='boss').length,drops:drops.map(d=>d.type)}};

window.__testActiveDamage=()=>{const oldEnemies=enemies,oldItems=player.items,oldKills=kills,oldChain=killChain;const target={x:player.x+120,y:player.y,r:10,hp:1,maxHp:1,speed:0,rola:'chase',type:'chaser',phase:0,dashTimer:100,dashFrames:0,cooldown:100,hit:0};enemies=[target];const item={numer:3,kategoria:'active',nazwa:'Test'};player.items=[item];useActiveItem(item);const result=target.hp<=0&&kills===oldKills+1&&killChain===oldChain+1;enemies=oldEnemies;player.items=oldItems;updateHud();return result};
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
    assert page.evaluate("window.__testActiveDamage()") is True, "Active damage did not count a kill through the shared death path"
    shop = page.evaluate("window.__testShopPurchase()")
    assert shop["state"] == "shop" and shop["coins"] == 2 and shop["hp"] == 2 and not shop["buttonDisabled"], f"Shop setup failed: {shop}"
    page.locator("#buyHeart").click()
    purchased = page.evaluate("window.__smoke()")
    assert purchased["coins"] == 0 and purchased["hp"] == 4, f"Heart purchase failed: {purchased}"
    page.locator("#startBtn").click()
    boss_transition = page.evaluate("window.__testBossTransition()")
    assert boss_transition["floor"] == 2 and boss_transition["roomNo"] == 1 and boss_transition["bosses"] == 1 and not boss_transition["drops"], f"Floor 2 should begin with a boss and no repeated starting supplies: {boss_transition}"
    boss_clear = page.evaluate("window.__testBossClear()")
    assert boss_clear["doorOpen"] and not boss_clear["floorExitSpawned"] and boss_clear["floor"] == 2 and boss_clear["roomNo"] == 1, f"Clearing the floor boss should open the route to room 2, not the next floor: {boss_clear}"
    page.evaluate("window.__testRestart()")
    assert page.evaluate("window.__testExit(1, 0.03)") is True, "5% roll should set pending exit at roll 3%"
    assert page.evaluate("window.__testPendingExitRoom()") is True, "Successful roll should place the exit in the next room"
    assert page.evaluate("window.__testExit(1, 0.07)") is False, "5% roll should reject roll 7%"
    assert page.evaluate("window.__testExit(19, 0.94)") is True, "95% roll should set pending exit at roll 94%"
    assert page.evaluate("window.__testExit(19, 0.96)") is False, "95% roll should reject roll 96%"
    assert all(page.evaluate(f"window.__testExit(20, {roll})") is True for roll in (0.01, 0.5, 0.99)), "Room 20 exit roll should always succeed and place exit in room 21"
    room30 = page.evaluate("window.__testRoom30()")
    assert room30["allExits"] and room30["bonus"] and room30["item"], f"Room 30 should guarantee all exits and a bonus item: {room30}"

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
    page.mouse.move(canvas["x"] + canvas["width"] * .8, canvas["y"] + canvas["height"] * .2)
    page.mouse.down()
    page.wait_for_timeout(60)
    shooting = page.evaluate("window.__smoke()")
    page.mouse.up()
    assert shooting["mouseDown"] is True, f"Mouse button was not registered: {shooting}"
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
    print("PASS: startup pickups; full-HP heart persistence; guaranteed shop and heart purchase; per-room exit rolls; next-room exit; room-30 bonus; start-of-floor boss and boss-room transition; active-item kill accounting; movement; shooting; pause/resume; restart; no browser errors")
    browser.close()
