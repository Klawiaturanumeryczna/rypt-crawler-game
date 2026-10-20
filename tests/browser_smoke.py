from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
needle = "function loop(){"
assert needle in HTML, "Could not locate game loop for test instrumentation"
instrumentation = """function loop(){
window.__smoke=()=>({state,x:player?player.x:null,y:player?player.y:null,shots:shots.length,floor,roomNo,hp:player?player.hp:null,maxHp:player?player.maxHp:null,coins,drops:drops.filter(d=>!d.gone).map(d=>d.type),shop:doors.some(d=>d.shop),keys:Array.from(keys),mouseDown:mouse.down,frame,movement:player?player.movement:null,fireMode:player?player.fireMode:null,items:player?player.items.length:null});
window.__testEnemyHpScaling=()=>{const saved={floor,roomTier,random:Math.random,profile:metaProfile};Math.random=()=>0.5;const sample=(f,t,type)=>{floor=f;roomTier=t;return createEnemy(type,100,100).hp};const result={chaserFloor1:sample(1,2,'chaser'),chaserFloor3:sample(3,2,'chaser'),bruteEasy:sample(1,1,'brute'),bruteHard:sample(1,3,'brute'),bossFloor2:sample(2,2,'boss')};floor=saved.floor;roomTier=saved.roomTier;Math.random=saved.random;metaProfile=saved.profile;return result};
window.__testItemCatalogue=()=>({count:WSZYSTKIE_PRZEDMIOTY.length,unique:new Set(WSZYSTKIE_PRZEDMIOTY.map(i=>i.nazwa)).size,names:WSZYSTKIE_PRZEDMIOTY.map(i=>i.nazwa),placeholders:WSZYSTKIE_PRZEDMIOTY.filter(i=>i.nazwa.startsWith('Item ')||/Placeholder/i.test(i.opis||'')).length,icons:WSZYSTKIE_PRZEDMIOTY.filter(i=>!i.ikona).length});
window.__testMetaProgression=()=>{const saved={profile:metaProfile,player,coins,kills,floor,roomNo,state};metaProfile=freshMetaProfile();player={items:[WSZYSTKIE_PRZEDMIOTY[0],WSZYSTKIE_PRZEDMIOTY[1]],movement:'runner',fireMode:'standard'};coins=7;kills=4;floor=3;roomNo=12;recordItemDiscovery(player.items[0]);recordEnemyDiscovery('boss');const summary=recordRunDeath();const result={discovered:metaProfile.discoveredItems.slice(),enemies:metaProfile.discoveredEnemies.slice(),deaths:metaProfile.totalDeaths,coinsLost:summary.coinsLost,itemsLost:summary.itemsLost,bestFloor:metaProfile.bestFloor,bestRoom:metaProfile.bestRoom};metaProfile=saved.profile;player=saved.player;coins=saved.coins;kills=saved.kills;floor=saved.floor;roomNo=saved.roomNo;state=saved.state;return result};
window.__testRescueItem=()=>{const saved={profile:metaProfile,player,coins,kills,floor,roomNo,state};metaProfile=freshMetaProfile();player={x:W/2,y:H/2,r:13,speed:3.15,hp:1,maxHp:6,damage:1,fireRate:17,shotSpeed:7.3,shotSize:5,luck:1,invuln:0,invulnDuration:65,cooldown:0,steps:0,stepProgress:0,items:[DANE_GRY.przedmioty.ratunkowe[0]],activeItemIndex:0,movement:'runner',fireMode:'standard',speedBonus:0,step:1,vx:0,vy:0,dashCooldown:0,dashFrames:0,dashDirX:0,dashDirY:0};coins=5;kills=2;floor=1;roomNo=3;state='play';hitPlayer(1);const result={hp:player.hp,state,itemRemaining:player.items.some(item=>item.kategoria==='rescue'),deaths:metaProfile.totalDeaths,coins};metaProfile=saved.profile;player=saved.player;coins=saved.coins;kills=saved.kills;floor=saved.floor;roomNo=saved.roomNo;state=saved.state;updateHud();return result};
window.__testExit=(r,t)=>{const old={roomNo,floorExitPending,floorExitSpawned,doors,random:Math.random};roomNo=r;floorExitPending=false;floorExitSpawned=false;doors=[{shop:false},{shop:false},{shop:false},{shop:false}];Math.random=()=>t;rollFloorExit();const result=floorExitPending;Math.random=old.random;roomNo=old.roomNo;floorExitPending=old.floorExitPending;floorExitSpawned=old.floorExitSpawned;doors=old.doors;return result};
window.__testRoom2=()=>{roomNo=1;nextRoom(2);return doors.some(d=>d.shop)};
window.__testPendingExitRoom=()=>{roomNo=1;floor=1;floorExitPending=true;floorExitSpawned=false;nextRoom(2);return doors.some(d=>d.floorExit)&&!floorExitPending};
window.__testBossClear=()=>{enemies=[];doorOpen=false;floorExitSpawned=false;doors=[{side:'top',x:W/2,y:room.y,type:DANE_GRY.drzwi.zlote,shop:false},{side:'bottom',x:W/2,y:room.y+room.h,type:DANE_GRY.drzwi.zlote,shop:false},{side:'left',x:room.x,y:room.y+room.h/2,type:DANE_GRY.drzwi.zlote,shop:false},{side:'right',x:room.x+room.w,y:room.y+room.h/2,type:DANE_GRY.drzwi.zlote,shop:false}];player.x=W/2;player.y=H/2;state='play';update();return {doorOpen,floorExitSpawned,floor,roomNo}};
window.__testRoom30=()=>{roomNo=29;floor=1;floorExitPending=false;floorExitSpawned=false;floorBonusClaimed=false;nextRoom(2);return {allExits:doors.every(d=>d.floorExit),bonus:floorBonusClaimed,item:drops.some(d=>d.type==='item')}};
window.__testRestart=()=>startRun();
window.__testShopPurchase=()=>{const old={coins,hp:player.hp,state};coins=2;player.hp=2;state='play';openShop();const buttonDisabled=document.getElementById('buyHeart').disabled;document.getElementById('buyHeart').click();const result={state,coins,hp:player.hp,buttonDisabled};coins=old.coins;player.hp=old.hp;state=old.state;$('overlay').classList.add('hidden');updateHud();return result};
window.__testBossTransition=()=>{roomNo=30;floor=1;floorExitPending=false;enemies=[];doorOpen=false;floorExitSpawned=true;doors=[{side:'top',x:W/2,y:room.y,type:DANE_GRY.drzwi.zlote,floorExit:true,shop:false},{side:'bottom',x:W/2,y:room.y+room.h,type:DANE_GRY.drzwi.zlote,shop:false},{side:'left',x:room.x,y:room.y+room.h/2,type:DANE_GRY.drzwi.zlote,shop:false},{side:'right',x:room.x+room.w,y:room.y+room.h/2,type:DANE_GRY.drzwi.zlote,shop:false}];player.x=W/2;player.y=room.y;state='play';update();return {floor,roomNo,doorOpen,floorExitSpawned,bosses:enemies.filter(e=>e.type==='boss').length,drops:drops.map(d=>d.type)}};

window.__testFireModes=()=>{const old={mode:player.fireMode,cooldown:player.cooldown,damage:player.damage,fireRate:player.fireRate,shots};const result={};for(const mode of Object.keys(FIRE_MODES)){shots=[];player.cooldown=0;player.fireMode=mode;player.damage=FIRE_MODES[mode].damage;player.fireRate=Math.max(6,Math.round(17*FIRE_MODES[mode].rate));shoot(1,0);const interval=player.fireRate;result[mode]={count:shots.length,size:shots[0]?.r,speed:Math.hypot(shots[0]?.vx||0,shots[0]?.vy||0),mode:shots[0]?.mode,pierce:shots[0]?.pierce||0,explosive:!!shots[0]?.explosive,damage:shots[0]?.damage,interval,dps:shots.length*(shots[0]?.damage||0)/interval}}player.fireMode=old.mode;player.cooldown=old.cooldown;player.damage=old.damage;player.fireRate=old.fireRate;shots=old.shots;return result};
window.__testProjectileEffects=()=>{const saved={player:{...player},state,frame,doorOpen,doors,enemies,shots,enemyShots,drops,particles,roomEnvironment,environmentPatches,fireSources,floorExitPending,floorExitSpawned,keys:[...keys],mouseDown:mouse.down};const run=(mode,targets)=>{state='play';doorOpen=true;doors=[];enemies=targets.map(t=>({x:t.x,y:t.y,r:10,hp:10,maxHp:10,type:'chaser',rola:'chase',speed:0,hit:0}));shots=[{x:W/2,y:H/2,vx:0,vy:0,r:5,life:10,damage:mode==='pierce'?1.05:.9,mode, pierce:mode==='pierce'?2:0,explosive:mode==='explosive'}];enemyShots=[];drops=[];particles=[];roomEnvironment=null;environmentPatches=[];fireSources=[];keys.clear();mouse.down=false;player.x=room.x+room.w-50;player.y=room.y+room.h-50;update();return enemies.map(e=>Number((10-e.hp).toFixed(3)))};const cx=W/2,cy=H/2;const piercing=run('pierce',[{x:cx,y:cy},{x:cx,y:cy},{x:cx,y:cy},{x:cx,y:cy}]);const explosive=run('explosive',[{x:cx,y:cy},{x:cx+50,y:cy},{x:cx+95,y:cy}]);Object.assign(player,saved.player);state=saved.state;frame=saved.frame;doorOpen=saved.doorOpen;doors=saved.doors;enemies=saved.enemies;shots=saved.shots;enemyShots=saved.enemyShots;drops=saved.drops;particles=saved.particles;roomEnvironment=saved.roomEnvironment;environmentPatches=saved.environmentPatches;fireSources=saved.fireSources;floorExitPending=saved.floorExitPending;floorExitSpawned=saved.floorExitSpawned;keys.clear();saved.keys.forEach(k=>keys.add(k));mouse.down=saved.mouseDown;return {piercing,explosive}};
window.__testWeaponSelection=()=>{const saved={...player},result={};for(const [key,mode] of Object.entries(FIRE_MODES)){showFiringChoice();const button=document.querySelector('#fireChoices .fire-'+key);if(!button)throw new Error('Missing firing choice button: '+key);button.click();result[key]={mode:player.fireMode,damage:player.damage,fireRate:player.fireRate,state};}Object.assign(player,saved);showFiringChoice();return result};
window.__testMovementFeel=()=>{
 const saved={movement:player.movement,speedBonus:player.speedBonus,step:player.step,vx:player.vx,vy:player.vy,x:player.x,y:player.y,keys:[...keys],state,frame,doorOpen,doors,enemies,shots,enemyShots,drops,particles,roomEnvironment,environmentPatches,fireSources,floorExitPending,floorExitSpawned};
 state='play';doorOpen=true;doors=[];enemies=[];shots=[];enemyShots=[];drops=[];particles=[];roomEnvironment=null;environmentPatches=[];fireSources=[];
 const sample=mode=>{const speed=MOVEMENT_TYPES[mode].speed;player.x=W/2;player.y=H/2;player.movement=mode;player.speedBonus=0;player.step=1;player.vx=0;player.vy=0;keys.clear();keys.add('d');let accelerationFrames=0;while(accelerationFrames<60&&Math.abs(player.vx)<speed*.95){update();accelerationFrames++}const reached95=Math.abs(player.vx)>=speed*.95;for(let i=0;i<25;i++)update();keys.delete('d');keys.add('a');let reversalFrames=0;while(reversalFrames<20&&player.vx>=0){update();reversalFrames++}keys.clear();player.x=W/2;player.y=H/2;player.vx=0;player.vy=0;keys.add('d');for(let i=0;i<40;i++)update();keys.clear();let coastDistance=0;const coastX=player.x;for(let i=0;i<20;i++){const x=player.x;update();coastDistance+=Math.abs(player.x-x)}const coastNet=Math.abs(player.x-coastX);player.x=W/2;player.y=H/2;player.vx=0;player.vy=0;player.hopTimer=0;player.hopFrames=0;player.twitchTimer=0;player.twitchFrames=0;keys.add('d');keys.add('s');for(let i=0;i<60;i++)update();const diagonalSpeed=Math.hypot(player.vx,player.vy);keys.clear();return {reached95,accelerationFrames,coastDistance:Number(coastDistance.toFixed(3)),coastNet:Number(coastNet.toFixed(3)),reversalFrames,diagonalSpeed:Number(diagonalSpeed.toFixed(3)),targetSpeed:speed}};
 const result={runner:sample('runner'),drifter:sample('drifter'),momentum:sample('momentum'),hopper:sample('hopper'),twitch:sample('twitch'),juggernaut:sample('juggernaut')};
 player.movement=saved.movement;player.speedBonus=saved.speedBonus;player.step=saved.step;player.vx=saved.vx;player.vy=saved.vy;player.x=saved.x;player.y=saved.y;keys.clear();saved.keys.forEach(k=>keys.add(k));state=saved.state;frame=saved.frame;doorOpen=saved.doorOpen;doors=saved.doors;enemies=saved.enemies;shots=saved.shots;enemyShots=saved.enemyShots;drops=saved.drops;particles=saved.particles;roomEnvironment=saved.roomEnvironment;environmentPatches=saved.environmentPatches;fireSources=saved.fireSources;floorExitPending=saved.floorExitPending;floorExitSpawned=saved.floorExitSpawned;updateHud();return result;
};
window.__testMovementBursts=()=>{
 const saved={movement:player.movement,speedBonus:player.speedBonus,step:player.step,vx:player.vx,vy:player.vy,x:player.x,y:player.y,keys:[...keys],state,frame,doorOpen,doors,enemies,shots,enemyShots,drops,particles,roomEnvironment,environmentPatches,fireSources,floorExitPending,floorExitSpawned};
 state='play';doorOpen=true;doors=[];enemies=[];shots=[];enemyShots=[];drops=[];particles=[];roomEnvironment=null;environmentPatches=[];fireSources=[];
 const sample=(mode,frames)=>{const speed=MOVEMENT_TYPES[mode].speed;player.x=W/2;player.y=H/2;player.movement=mode;player.speedBonus=0;player.step=1;player.vx=0;player.vy=0;player.hopTimer=0;player.hopFrames=0;player.twitchTimer=0;player.twitchFrames=0;keys.clear();keys.add('d');const values=[];for(let i=1;i<=frames;i++){update();values.push({frame:i,speed:Math.hypot(player.vx,player.vy)})}const burst=values.filter(v=>v.speed>speed*1.5);const result={baseline:Number(speed.toFixed(3)),maxSpeed:Number(Math.max(...values.map(v=>v.speed)).toFixed(3)),burstFrames:burst.length,firstBurstFrame:burst[0]?.frame??null,lastBurstFrame:burst[burst.length-1]?.frame??null};return result};
 const result={hopper:sample('hopper',32),twitch:sample('twitch',44)};
 player.movement=saved.movement;player.speedBonus=saved.speedBonus;player.step=saved.step;player.vx=saved.vx;player.vy=saved.vy;player.x=saved.x;player.y=saved.y;keys.clear();saved.keys.forEach(k=>keys.add(k));state=saved.state;frame=saved.frame;doorOpen=saved.doorOpen;doors=saved.doors;enemies=saved.enemies;shots=saved.shots;enemyShots=saved.enemyShots;drops=saved.drops;particles=saved.particles;roomEnvironment=saved.roomEnvironment;environmentPatches=saved.environmentPatches;fireSources=saved.fireSources;floorExitPending=saved.floorExitPending;floorExitSpawned=saved.floorExitSpawned;updateHud();return result;
};
window.__testMovementPhysics=()=>{
 const saved={movement:player.movement,speedBonus:player.speedBonus,step:player.step,vx:player.vx,vy:player.vy,x:player.x,y:player.y,dashCooldown:player.dashCooldown,dashFrames:player.dashFrames,dashDirX:player.dashDirX,dashDirY:player.dashDirY,invuln:player.invuln,cooldown:player.cooldown,keys:[...keys],state,frame,doorOpen,doors,enemies,shots,enemyShots,drops,particles,roomEnvironment,environmentPatches,fireSources,floorExitPending,floorExitSpawned};
 state='play';doorOpen=true;doors=[];enemies=[];shots=[];enemyShots=[];drops=[];particles=[];roomEnvironment=null;environmentPatches=[];fireSources=[];
 const sample=(mode,shift=false,coast=false)=>{player.x=W/2;player.y=H/2;player.movement=mode;player.speedBonus=0;player.step=1;player.vx=0;player.vy=0;player.dashCooldown=0;player.dashFrames=0;player.dashDirX=0;player.dashDirY=0;keys.clear();keys.add('d');if(shift)keys.add('shift');const x0=player.x;update();const first=player.x-x0;const vx=player.vx;let coastDistance=null;if(coast){keys.clear();const x1=player.x;update();coastDistance=player.x-x1}return {first,vx,coast:coastDistance,speed:MOVEMENT_TYPES[mode].speed}};
 const result={runner:sample('runner',false,true),drifter:sample('drifter',false,true),momentum:sample('momentum',false,true),hopper:sample('hopper',true),twitch:sample('twitch',true),juggernaut:sample('juggernaut')};
 player.movement=saved.movement;player.speedBonus=saved.speedBonus;player.step=saved.step;player.vx=saved.vx;player.vy=saved.vy;player.x=saved.x;player.y=saved.y;player.dashCooldown=saved.dashCooldown;player.dashFrames=saved.dashFrames;player.dashDirX=saved.dashDirX;player.dashDirY=saved.dashDirY;player.invuln=saved.invuln;player.cooldown=saved.cooldown;keys.clear();saved.keys.forEach(k=>keys.add(k));state=saved.state;frame=saved.frame;doorOpen=saved.doorOpen;doors=saved.doors;enemies=saved.enemies;shots=saved.shots;enemyShots=saved.enemyShots;drops=saved.drops;particles=saved.particles;roomEnvironment=saved.roomEnvironment;environmentPatches=saved.environmentPatches;fireSources=saved.fireSources;floorExitPending=saved.floorExitPending;floorExitSpawned=saved.floorExitSpawned;updateHud();return result;
};
window.__testItemPickup=()=>{const oldDrops=drops,oldX=player.x,oldY=player.y,oldItems=player.items;const item={id:'pickup-test',numer:1,kategoria:'active',typ:1,nazwa:'Test pickup',ikona:'❗',opis:'test'};const d={x:player.x+50,y:player.y,r:17,type:'item',item};drops=[d];keys.clear();update();const remainsNearby=drops.includes(d)&&!d.gone;player.x=d.x-player.r-d.r-2;player.y=d.y;update();const collected=d.gone&&player.items.includes(item);drops=oldDrops;player.x=oldX;player.y=oldY;player.items=oldItems;updateHud();return {remainsNearby,collected}};
window.__testAllPassiveItems=()=>{
 const keys=['hp','maxHp','step','speed','speedBonus','movement','fireRate','invulnDuration','damage','shotSpeed','shotSize'];
 const saved=Object.fromEntries(keys.map(k=>[k,player[k]]));
 const baseSpeed=MOVEMENT_TYPES.runner.speed;
 const run=(category,n)=>{
  player.hp=4;player.maxHp=6;player.step=1;player.speedBonus=0;player.movement='runner';player.speed=baseSpeed;player.fireRate=10;player.invulnDuration=30;player.damage=1;player.shotSpeed=5;player.shotSize=4;
  applyPassiveItem({id:category+n,numer:n,kategoria:category,nazwa:'Test '+category+' '+n});
  return {hp:player.hp,maxHp:player.maxHp,step:Number(player.step.toFixed(2)),speed:Number(player.speed.toFixed(2)),speedBonus:Number(player.speedBonus.toFixed(2)),fireRate:player.fireRate,invulnDuration:player.invulnDuration,damage:Number(player.damage.toFixed(2)),shotSpeed:Number(player.shotSpeed.toFixed(2)),shotSize:player.shotSize};
 };
 const result={baseSpeed:Number(baseSpeed.toFixed(2)),legs:{},shot:{}};
 for(let n=1;n<=10;n++){result.legs[n]=run('legs',n);result.shot[n]=run('shot',n)}
 keys.forEach(k=>player[k]=saved[k]);updateHud();return result;
};
window.__testActiveDamage=()=>{const old={enemies,items:player.items,kills,killChain,killChainTimer,drops,particles};const target={x:player.x+120,y:player.y,r:10,hp:1,maxHp:1,speed:0,rola:'chase',type:'chaser',phase:0,dashTimer:100,dashFrames:0,cooldown:100,hit:0};enemies=[target];const item={numer:3,kategoria:'active',nazwa:'Test'};player.items=[item];useActiveItem(item);const result=target.hp<=0&&kills===old.kills+1&&killChain===old.killChain+1;enemies=old.enemies;player.items=old.items;kills=old.kills;killChain=old.killChain;killChainTimer=old.killChainTimer;drops=old.drops;particles=old.particles;updateHud();return result};
window.__testAllActiveItems=()=>{
 const saved={hp:player.hp,maxHp:player.maxHp,coins,items:player.items,activeItemIndex:player.activeItemIndex,shots,enemyShots,enemies,kills,killChain,killChainTimer,particles};
 const target=(xOffset,hp=20)=>({x:player.x+xOffset,y:player.y,r:10,hp,maxHp:hp,speed:0,rola:'chase',type:'chaser',phase:0,dashTimer:100,dashFrames:0,cooldown:100,hit:0});
 const run=(n,setup=()=>{})=>{enemies=[];shots=[];enemyShots=[];particles=[];player.hp=1;player.maxHp=6;player.invuln=0;coins=0;const item={numer:n,kategoria:'active',nazwa:'Test active '+n};player.items=[item];setup();useActiveItem(item);return {hp:player.hp,coins,invuln:player.invuln,shotCount:shots.length,enemyShotCount:enemyShots.length,enemyHp:enemies.map(e=>e.hp),consumed:!player.items.includes(item)}};
 const result={
  1:run(1),
  2:run(2),
  3:run(3,()=>{enemies=[target(40)]}),
  4:run(4,()=>{enemyShots=[{life:10},{life:10}]}),
  5:run(5),
  6:run(6),
  7:run(7,()=>{enemies=[target(30),target(100)]}),
  8:run(8),
  9:run(9),
  10:run(10,()=>{enemies=[target(40),target(100)];enemyShots=[{life:10},{life:10}]})
 };
 player.hp=saved.hp;player.maxHp=saved.maxHp;coins=saved.coins;player.items=saved.items;player.activeItemIndex=saved.activeItemIndex;shots=saved.shots;enemyShots=saved.enemyShots;enemies=saved.enemies;kills=saved.kills;killChain=saved.killChain;killChainTimer=saved.killChainTimer;particles=saved.particles;updateHud();return result;
};
window.__testFullHealthHeart=()=>{const old={drops,x:player.x,y:player.y,hp:player.hp,invuln:player.invuln};const d=drops.find(d=>d.type==='heart'&&!d.gone);if(!d)return false;player.hp=player.maxHp;player.x=d.x;player.y=d.y;player.invuln=999;update();const result=drops.some(x=>x===d&&!x.gone);drops=old.drops;player.x=old.x;player.y=old.y;player.hp=old.hp;player.invuln=old.invuln;updateHud();return result};
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

    assert page.locator("#profileBtn").count() == 0, "Codex UI should remain deferred until meta-progression is designed"

    page.locator("#startBtn").click()
    page.wait_for_timeout(50)
    assert page.evaluate("window.__smoke()['state']") == "firingChoice", "Start should open the firing-style selection"
    assert page.locator("#fireChoices .moveChoice").count() == 7, "Expected seven distinct starter weapons"
    assert page.locator("#fireChoices .choiceGlyph").count() == 7, "Every starter weapon should show a visual preview"
    assert page.locator("#fireChoices .weaponStats").count() == 7, "Every starter weapon should show damage and firing interval"
    selection = page.evaluate("window.__testWeaponSelection()")
    expected_weapons = {"precision": (1.25, 20), "standard": (1.0, 17), "spread": (0.40, 21), "rapid": (0.72, 12), "burst": (0.25, 24), "pierce": (1.05, 22), "explosive": (0.9, 23)}
    for key, (damage, interval) in expected_weapons.items():
        assert selection[key]["mode"] == key and abs(selection[key]["damage"] - damage) < 0.001 and selection[key]["fireRate"] == interval and selection[key]["state"] == "movementChoice", f"Selecting {key} must apply its real damage and cadence before movement choice: {selection}"
    assert "Odstęp między strzałami: 24 klatek" in page.locator("#fireChoices .fire-burst").inner_text(), "Salwa should communicate its slower firing interval"
    assert "Obrażenia / pocisk: ×0.25" in page.locator("#fireChoices .fire-burst").inner_text(), "Salwa should communicate per-projectile damage"
    page.locator("#fireChoices .moveChoice").nth(1).click()
    assert page.evaluate("window.__smoke()['state']") == "movementChoice", "Choosing a firing style should open movement-style selection"
    assert page.locator("#moveChoices .moveChoice").count() == 6, "Expected six movement-style choices"
    assert page.locator("#moveChoices .choiceGlyph").count() == 6, "Movement styles should show six visual previews"
    page.locator("#moveChoices .moveChoice").first.click()
    page.wait_for_timeout(100)
    start = page.evaluate("window.__smoke()")
    assert start["state"] == "play", f"Start failed after completing onboarding: {start}"
    controls = page.locator(".controls").inner_text().lower()
    assert "wejdź w przedmiot" in controls and "e podnieś przedmiot" not in controls and "naciśnij e" not in controls, f"Controls must explain contact pickup without E: {controls}"
    assert not page.locator("#overlay").is_visible()
    assert start["drops"].count("heart") == 3, f"Expected 3 starting hearts: {start}"
    assert start["drops"].count("coin") == 2, f"Expected 2 starting coins: {start}"
    assert start["drops"].count("item") == 0, f"Starting room must not contain item pickups: {start}"
    enemy_hp = page.evaluate("window.__testEnemyHpScaling()")
    assert enemy_hp == {"chaserFloor1": 2, "chaserFloor3": 3, "bruteEasy": 4, "bruteHard": 8, "bossFloor2": 69}, f"Enemy HP should follow floor scaling, door-tier multipliers, and the separate boss formula: {enemy_hp}"

    fire = page.evaluate("window.__testFireModes()")
    assert fire["spread"]["count"] == 3, f"Spread must fire three projectiles: {fire}"
    assert fire["precision"]["size"] > fire["standard"]["size"], f"Precision projectile should be visibly larger: {fire}"
    assert fire["rapid"]["size"] < fire["standard"]["size"] and fire["rapid"]["speed"] > fire["standard"]["speed"], f"Rapid fire must use smaller, faster projectiles: {fire}"
    assert fire["burst"]["count"] == 5, f"Salwa must fire five projectiles: {fire}"
    assert fire["pierce"]["pierce"] == 2, f"Przebijający must pass through multiple enemies: {fire}"
    assert fire["explosive"]["explosive"], f"Wybuchowy must carry its area-damage behavior: {fire}"
    assert fire["spread"]["dps"] <= fire["standard"]["dps"] * 1.1, f"Spread should not have clearly higher raw single-target DPS than the standard weapon: {fire}"
    assert fire["burst"]["dps"] <= fire["standard"]["dps"], f"Salwa should trade lower per-projectile damage for multi-target coverage, not outperform standard on raw DPS: {fire}"
    impacts = page.evaluate("window.__testProjectileEffects()")
    assert impacts["piercing"][:3] == [1.05, 1.05, 1.05] and impacts["piercing"][3] == 0, f"Piercing shot should hit at most three targets: {impacts}"
    assert impacts["explosive"] == [0.9, 0.54, 0], f"Explosive shot should hit its primary target and nearby enemies within 72px only: {impacts}"
    assert page.evaluate("window.__testFullHealthHeart()"), "A heart pickup must remain on the ground at full health"
    assert page.evaluate("window.__testExit(1, 0.01)"), "A low roll should trigger the room-1 exit chance"
    assert not page.evaluate("window.__testExit(1, 0.99)"), "A high roll should fail the room-1 exit chance"
    assert page.evaluate("window.__testExit(20, 0.99)"), "Room 20 should guarantee the exit roll"
    assert page.evaluate("window.__testRoom2()"), "Room 2 should contain the guaranteed shop door"
    assert page.evaluate("window.__testPendingExitRoom()"), "A successful exit roll should place the exit in the next room"
    room30 = page.evaluate("window.__testRoom30()")
    assert room30["allExits"] and room30["bonus"] and room30["item"], f"Room 30 should guarantee exits and a bonus item: {room30}"
    shop = page.evaluate("window.__testShopPurchase()")
    assert not shop["buttonDisabled"] and shop["coins"] == 0 and shop["hp"] == 4, f"Shop heart purchase should spend 2 coins and heal 2 HP: {shop}"
    assert page.evaluate("window.__testActiveDamage()"), "An active item kill must increment kill and streak counters"
    active = page.evaluate("window.__testAllActiveItems()")
    assert active["1"]["hp"] == 3 and active["1"]["consumed"], f"Active item 1 must heal 1 heart and be consumed: {active['1']}"
    assert active["2"]["coins"] == 2 and active["2"]["consumed"], f"Active item 2 must grant 2 coins and be consumed: {active['2']}"
    assert active["3"]["enemyHp"] == [16] and active["3"]["consumed"], f"Active item 3 must damage every enemy: {active['3']}"
    assert active["4"]["enemyShotCount"] == 0 and active["4"]["consumed"], f"Active item 4 must clear enemy projectiles: {active['4']}"
    assert active["5"]["invuln"] >= 120 and active["5"]["consumed"], f"Active item 5 must grant 2 seconds of invulnerability: {active['5']}"
    assert active["6"]["shotCount"] == 8 and active["6"]["consumed"], f"Active item 6 must fire eight projectiles: {active['6']}"
    assert active["7"]["enemyHp"] == [10, 20] and active["7"]["consumed"], f"Active item 7 must damage only the nearest enemy: {active['7']}"
    assert active["8"]["hp"] == 5 and active["8"]["consumed"], f"Active item 8 must heal 2 hearts: {active['8']}"
    assert active["9"]["coins"] == 3 and active["9"]["consumed"], f"Active item 9 must grant 3 coins: {active['9']}"
    assert active["10"]["enemyHp"] == [18, 18] and active["10"]["enemyShotCount"] == 0 and active["10"]["consumed"], f"Active item 10 must damage all enemies and clear projectiles: {active['10']}"
    passive = page.evaluate("window.__testAllPassiveItems()")
    legs, shot = passive["legs"], passive["shot"]
    assert abs(legs["1"]["step"] - 1.10) < 0.001 and abs(legs["2"]["step"] - 1.20) < 0.001 and abs(legs["6"]["step"] - 1.15) < 0.001 and abs(legs["9"]["step"] - 1.25) < 0.001, f"Movement items must apply the documented step bonuses: {legs}"
    assert legs["3"]["maxHp"] == 8 and legs["3"]["hp"] == 6 and legs["8"]["maxHp"] == 8 and legs["8"]["hp"] == 6, f"Vitality items must increase max HP and heal: {legs}"
    assert abs(legs["4"]["speed"] - (passive["baseSpeed"] + 0.20)) < 0.001 and legs["4"]["fireRate"] == 11 and abs(legs["10"]["speed"] - (passive["baseSpeed"] + 0.15)) < 0.001 and legs["10"]["invulnDuration"] == 50, f"Leg items 4 and 10 must apply their mixed trade-offs: {legs}"
    assert legs["5"]["invulnDuration"] == 40 and legs["9"]["fireRate"] == 12 and abs(legs["7"]["damage"] - 1.25) < 0.001, f"Leg passive items must apply their defensive/offensive effects: {legs}"
    assert abs(shot["1"]["damage"] - 1.25) < 0.001 and abs(shot["2"]["damage"] - 1.50) < 0.001 and abs(shot["7"]["damage"] - 1.25) < 0.001 and abs(shot["10"]["damage"] - 2.00) < 0.001, f"Shot damage items must apply documented bonuses: {shot}"
    assert shot["3"]["fireRate"] == 8 and shot["6"]["fireRate"] == 7 and shot["7"]["fireRate"] == 11 and shot["10"]["fireRate"] == 12, f"Shot cadence items must apply documented trade-offs: {shot}"
    assert shot["4"]["shotSpeed"] == 6 and shot["9"]["shotSpeed"] == 6.5 and shot["5"]["shotSize"] == 5 and shot["8"]["shotSize"] == 6 and shot["8"]["shotSpeed"] == 4.5, f"Shot speed/size items must apply documented effects: {shot}"
    movement_feel = page.evaluate("window.__testMovementFeel()")
    assert movement_feel["runner"]["accelerationFrames"] == 1 and movement_feel["runner"]["reached95"], f"Runner should retain instant directional response: {movement_feel}"
    assert movement_feel["drifter"]["reached95"] and movement_feel["drifter"]["accelerationFrames"] <= 14, f"Drifter should reach near-cruising speed without feeling sluggish: {movement_feel}"
    assert movement_feel["momentum"]["reached95"] and movement_feel["momentum"]["accelerationFrames"] <= 22, f"Momentum should accelerate gradually but reach cruising speed in a reasonable time: {movement_feel}"
    assert movement_feel["drifter"]["reversalFrames"] <= 4 and movement_feel["momentum"]["reversalFrames"] <= 6, f"Inertia styles should preserve glide while still responding to deliberate direction changes: {movement_feel}"
    assert movement_feel["drifter"]["coastDistance"] > movement_feel["momentum"]["coastDistance"] > 0, f"Drifter should retain a longer coast than Momentum, with both preserving some glide: {movement_feel}"
    assert abs(movement_feel["runner"]["diagonalSpeed"] - movement_feel["runner"]["targetSpeed"]) < 0.01, f"Diagonal movement should not be faster than straight movement: {movement_feel}"
    for mode in ("drifter", "momentum", "twitch", "juggernaut"):
        assert abs(movement_feel[mode]["diagonalSpeed"] - movement_feel[mode]["targetSpeed"]) < 0.01, f"{mode} diagonal cruising speed should match straight-line cruising speed: {movement_feel}"
    assert abs(movement_feel["hopper"]["diagonalSpeed"] - movement_feel["hopper"]["targetSpeed"] * 0.72) < 0.01, f"Hopper diagonal cruising speed should match its non-burst speed: {movement_feel}"
    
    bursts = page.evaluate("window.__testMovementBursts()")
    assert bursts["hopper"]["firstBurstFrame"] == 26 and bursts["hopper"]["burstFrames"] == 6, f"Hopper should perform its six-frame automatic boost on the 26th moving frame: {bursts}"
    assert bursts["twitch"]["firstBurstFrame"] == 38 and bursts["twitch"]["burstFrames"] == 4, f"Twitch should perform its four-frame automatic boost on the 38th moving frame: {bursts}"
    
    movement = page.evaluate("window.__testMovementPhysics()")
    assert movement["runner"]["first"] > movement["drifter"]["first"] > 0, f"Drifter should accelerate into movement instead of instantly reaching full speed: {movement}"
    assert movement["momentum"]["first"] > 0 and movement["momentum"]["first"] < movement["drifter"]["first"], f"Momentum style should start with slower acceleration: {movement}"
    assert movement["runner"]["coast"] == 0 and movement["drifter"]["coast"] > 0 and movement["momentum"]["coast"] > 0, f"Drifter and momentum should retain movement after input release while runner stops: {movement}"
    assert movement["hopper"]["first"] != movement["runner"]["first"] and movement["twitch"]["first"] != movement["runner"]["first"], f"Hopper and twitch should have distinct automatic movement: {movement}"
    assert movement["juggernaut"]["first"] != movement["runner"]["first"], f"Juggernaut should have a distinct movement speed: {movement}"
    meta = page.evaluate("window.__testMetaProgression()")
    assert meta["discovered"] == ["active1"] and meta["enemies"] == ["boss"], f"Codex should retain item/enemy discoveries: {meta}"
    assert meta["deaths"] == 1 and meta["coinsLost"] == 7 and meta["itemsLost"] == ["Mała Apteczka", "Sakiewka"], f"Death should record run losses: {meta}"
    assert meta["bestFloor"] == 1 and meta["bestRoom"] == 1, f"Fresh profile should start with baseline record: {meta}"

    rescue = page.evaluate("window.__testRescueItem()")
    assert rescue["hp"] == 1 and rescue["state"] == "play" and not rescue["itemRemaining"] and rescue["deaths"] == 0, f"Rescue amulet should be consumed and leave player at 1 HP without ending run: {rescue}"

    catalogue = page.evaluate("window.__testItemCatalogue()")
    assert catalogue["count"] == 31 and catalogue["unique"] == 31, f"All 31 items should have distinct names: {catalogue}"
    assert catalogue["placeholders"] == 0 and catalogue["icons"] == 0, f"Item catalogue should have no placeholders or missing icons: {catalogue}"

    pickup = page.evaluate("window.__testItemPickup()")
    assert pickup["remainsNearby"], f"Items should not auto-pick up from a distance: {pickup}"
    assert pickup["collected"], f"Walking into an item should collect it without pressing E: {pickup}"

    bossClear = page.evaluate("window.__testBossClear()")
    assert bossClear["doorOpen"], f"Clearing a room should open its doors: {bossClear}"
    bossTransition = page.evaluate("window.__testBossTransition()")
    assert bossTransition["floor"] == 2 and bossTransition["roomNo"] == 1 and bossTransition["bosses"] == 1, f"Descending should start floor 2 with its boss in room 1: {bossTransition}"
    page.evaluate("window.__testRestart()")
    assert page.evaluate("window.__smoke()['state']") == "firingChoice", "Restart should reset the run and reopen firing-style selection"
    assert not errors, f"Browser errors: {errors}"
    print("PASS: enemy HP scaling by floor and door tier; startup pickups; full-HP heart persistence; shop purchase; exit probabilities and placement; room-30 bonus; boss-room clearing and floor transition; named 30-item catalogue; all ten active-item effects; all 20 passive-item effects; active-item kill accounting; six movement physics styles; movement acceleration, coast, reversal, diagonal speed and automatic burst cadence; shooting; restart; no browser errors")
    browser.close()
