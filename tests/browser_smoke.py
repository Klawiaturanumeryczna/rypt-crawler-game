from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
needle = "function loop(){"
assert needle in HTML, "Could not locate game loop for test instrumentation"
instrumentation = """function loop(){
window.__smoke=()=>({state,x:player?player.x:null,y:player?player.y:null,shots:shots.length,floor,roomNo,hp:player?player.hp:null,maxHp:player?player.maxHp:null,coins,drops:drops.filter(d=>!d.gone).map(d=>d.type),shop:doors.some(d=>d.shop),keys:Array.from(keys),mouseDown:mouse.down,frame,movement:player?player.movement:null,fireMode:player?player.fireMode:null,items:player?player.items.length:null});
window.__testExit=(r,t)=>{const old={roomNo,floorExitPending,floorExitSpawned,doors,random:Math.random};roomNo=r;floorExitPending=false;floorExitSpawned=false;doors=[{shop:false},{shop:false},{shop:false},{shop:false}];Math.random=()=>t;rollFloorExit();const result=floorExitPending;Math.random=old.random;roomNo=old.roomNo;floorExitPending=old.floorExitPending;floorExitSpawned=old.floorExitSpawned;doors=old.doors;return result};
window.__testRoom2=()=>{roomNo=1;nextRoom(2);return doors.some(d=>d.shop)};
window.__testPendingExitRoom=()=>{roomNo=1;floor=1;floorExitPending=true;floorExitSpawned=false;nextRoom(2);return doors.some(d=>d.floorExit)&&!floorExitPending};
window.__testBossClear=()=>{enemies=[];doorOpen=false;floorExitSpawned=false;doors=[{side:'top',x:W/2,y:room.y,type:DANE_GRY.drzwi.zlote,shop:false},{side:'bottom',x:W/2,y:room.y+room.h,type:DANE_GRY.drzwi.zlote,shop:false},{side:'left',x:room.x,y:room.y+room.h/2,type:DANE_GRY.drzwi.zlote,shop:false},{side:'right',x:room.x+room.w,y:room.y+room.h/2,type:DANE_GRY.drzwi.zlote,shop:false}];player.x=W/2;player.y=H/2;state='play';update();return {doorOpen,floorExitSpawned,floor,roomNo}};
window.__testRoom30=()=>{roomNo=29;floor=1;floorExitPending=false;floorExitSpawned=false;floorBonusClaimed=false;nextRoom(2);return {allExits:doors.every(d=>d.floorExit),bonus:floorBonusClaimed,item:drops.some(d=>d.type==='item')}};
window.__testRestart=()=>startRun();
window.__testShopPurchase=()=>{coins=2;player.hp=2;state='play';openShop();updateHud();return {state,coins,hp:player.hp,buttonDisabled:document.getElementById('buyHeart').disabled}};
window.__testBossTransition=()=>{roomNo=30;floor=1;floorExitPending=false;enemies=[];doorOpen=false;floorExitSpawned=true;doors=[{side:'top',x:W/2,y:room.y,type:DANE_GRY.drzwi.zlote,floorExit:true,shop:false},{side:'bottom',x:W/2,y:room.y+room.h,type:DANE_GRY.drzwi.zlote,shop:false},{side:'left',x:room.x,y:room.y+room.h/2,type:DANE_GRY.drzwi.zlote,shop:false},{side:'right',x:room.x+room.w,y:room.y+room.h/2,type:DANE_GRY.drzwi.zlote,shop:false}];player.x=W/2;player.y=room.y;state='play';update();return {floor,roomNo,doorOpen,floorExitSpawned,bosses:enemies.filter(e=>e.type==='boss').length,drops:drops.map(d=>d.type)}};

window.__testFireModes=()=>{const old={mode:player.fireMode,cooldown:player.cooldown,shots};const result={};for(const mode of Object.keys(FIRE_MODES)){shots=[];player.cooldown=0;player.fireMode=mode;shoot(1,0);result[mode]={count:shots.length,size:shots[0]?.r,speed:Math.hypot(shots[0]?.vx||0,shots[0]?.vy||0),mode:shots[0]?.mode}}player.fireMode=old.mode;player.cooldown=old.cooldown;shots=old.shots;return result};
window.__testItemPickup=()=>{const oldDrops=drops,oldX=player.x,oldY=player.y,oldItems=player.items;const item={id:'pickup-test',numer:1,kategoria:'active',typ:1,nazwa:'Test pickup',ikona:'❗',opis:'test'};const d={x:player.x+50,y:player.y,r:17,type:'item',item};drops=[d];keys.clear();update();const remainsNearby=drops.includes(d)&&!d.gone;player.x=d.x-player.r-d.r-2;player.y=d.y;update();const collected=d.gone&&player.items.includes(item);drops=oldDrops;player.x=oldX;player.y=oldY;player.items=oldItems;updateHud();return {remainsNearby,collected}};
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
    page.wait_for_timeout(50)
    assert page.evaluate("window.__smoke()['state']") == "firingChoice", "Start should open the firing-style selection"
    assert page.locator("#fireChoices .moveChoice").count() == 4, "Expected four firing-style choices"
    assert page.locator("#fireChoices .choiceGlyph").count() == 4, "Firing styles should show visual previews"
    page.locator("#fireChoices .moveChoice").nth(1).click()
    assert page.evaluate("window.__smoke()['state']") == "movementChoice", "Choosing a firing style should open movement-style selection"
    assert page.locator("#moveChoices .moveChoice").count() == 6, "Expected six movement-style choices"
    assert page.locator("#moveChoices .choiceGlyph").count() == 6, "Movement styles should show six visual previews"
    page.locator("#moveChoices .moveChoice").first.click()
    page.wait_for_timeout(100)
    start = page.evaluate("window.__smoke()")
    assert start["state"] == "play", f"Start failed after completing onboarding: {start}"
    assert not page.locator("#overlay").is_visible()
    assert start["drops"].count("heart") == 3, f"Expected 3 starting hearts: {start}"
    assert start["drops"].count("coin") == 2, f"Expected 2 starting coins: {start}"
    assert start["drops"].count("item") == 0, f"Starting room must not contain item pickups: {start}"
    fire = page.evaluate("window.__testFireModes()")
    assert fire["spread"]["count"] == 3, f"Spread must fire three projectiles: {fire}"
    assert fire["precision"]["size"] > fire["standard"]["size"], f"Precision projectile should be visibly larger: {fire}"
    assert fire["rapid"]["size"] < fire["standard"]["size"] and fire["rapid"]["speed"] > fire["standard"]["speed"], f"Rapid fire must use smaller, faster projectiles: {fire}"
    pickup = page.evaluate("window.__testItemPickup()")
    assert pickup["remainsNearby"], f"Items should not auto-pick up from a distance: {pickup}"
    assert pickup["collected"], f"Walking into an item should collect it without pressing E: {pickup}"

    assert not errors, f"Browser errors: {errors}"
    print("PASS: startup pickups; full-HP heart persistence; guaranteed shop and heart purchase; per-room exit rolls; next-room exit; room-30 bonus; start-of-floor boss and boss-room transition; active-item kill accounting; movement; shooting; pause/resume; restart; no browser errors")
    browser.close()
