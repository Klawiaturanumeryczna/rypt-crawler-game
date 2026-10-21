from pathlib import Path

SOURCE = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
checks = {
    "canvas exists": '<canvas id="game"' in SOURCE,
    "high visibility in-game HP bar": "ctx.fillText('HP '+player.hp+'/'+player.maxHp" in SOURCE,
    "door labels are large and offset inside room": "ctx.font='bold 20px monospace'" in SOURCE and "ly=room.y+31" in SOURCE,
    "item pickups do not flood the event feed": "PRZEDMIOT ZEBRANY" not in SOURCE and "log('STATYSTYKA — przedmioty: '+oldItems" not in SOURCE and "KODEKS — nowo odkryty przedmiot" not in SOURCE,
    "movement input": "keys.has('w')" in SOURCE and "keys.has('d')" in SOURCE,
    "shooting via arrows and mouse": "keys.has('arrowright')" in SOURCE and "mouse.down" in SOURCE,
    "enemy archetypes": all(f"{name}:" in SOURCE for name in ("chaser", "spitter", "brute", "dasher", "hexer", "boss")),
    "fixed 30-room maximum": "function maxRoomsForFloor(f){return 30}" in SOURCE,
    "per-room exit roll": "Math.random()<chance" in SOURCE and "floorExitPending=true" in SOURCE,
    "room-20 roll guarantees exit in room 21": "const chance=Math.min(1,roomNo*.05)" in SOURCE and "if(floorExitPending&&roomNo>1)" in SOURCE,
    "exit appears in next room": "if(floorExitPending&&roomNo>1)" in SOURCE and "exitDoor.floorExit=true" in SOURCE,
    "guaranteed room-30 exit": "if(roomNo>=maxRoomsForFloor(floor))" in SOURCE and "doors.forEach(d=>d.floorExit=true)" in SOURCE,
    "room-30 bonus reward": "if(roomNo>=maxRoomsForFloor(floor))" in SOURCE and "floorBonusClaimed=true" in SOURCE,
    "boss starts floors 2+": "const bossRoom=floor>1&&roomNo===1;" in SOURCE,
    "boss room skips floor-exit roll": "if(!(floor>1&&roomNo===1))rollFloorExit();" in SOURCE,
    "starting supplies only on first floor": "if(roomNo===1&&floor===1&&!shopRoom)" in SOURCE,
    "starting pickups": "i<3;i++)drops.push" in SOURCE and "i<2;i++)drops.push" in SOURCE,
    "guaranteed shop in room 2": "roomNo===2&&roomNo<maxRoomsForFloor(floor)" in SOURCE,
    "shop is a physical room with walk-up heart and item offers": "SKLEP — podejdź do oferty" in SOURCE and "type:'shopHeart',price:2" in SOURCE and "type:'shopItem',item:passiveOffer,price:4" in SOURCE and "type:'shopItem',item:activeOffer,price:5" in SOURCE and "coins-=d.price||2" in SOURCE and "coins-=d.price||0" in SOURCE and "player.hp+2" in SOURCE and "buyHeart" not in SOURCE,
    "all 31 items have named labels, not placeholders": all(f"'{n}'" in SOURCE for n in ["Mała Apteczka","Sakiewka","Fala Uderzeniowa","Impuls Oczyszczający","Tarcza Eteryczna","Gwiezdna Salwa","Znak Egzekucji","Wielka Apteczka","Złota Sakwa","Fala Oczyszczenia","Lekkie Buty","Buty Wiatru","Nagolenniki Witalności","Sprinterskie Nagolenniki","Skóra Widmo","Buty Wędrowca","Stalowe Obcasy","Nagolenniki Życia","Buty Błyskawicy","Strażnicze Nagolenniki","Ciężki Pocisk","Rdzeń Mocy","Cewka Szybkostrzelna","Soczewka Prędkości","Kaliber Rozszerzony","Mechanizm Gatlinga","Komora Odrzutu","Pocisk Oblężniczy","Napęd Hiperprzestrzenny","Niszczyciel","Amulet Ostatniej Szansy"]) and "Placeholder — przedmiot" not in SOURCE and "nazwa:'Item '+" not in SOURCE,
    "item pickup requires physical contact": "else if(d.type==='item'&&d.item){" in SOURCE and "d.item&&keys.has('e')" not in SOURCE,
    "pickup instructions do not require E": "wejdź w przedmiot, aby go podnieść" in SOURCE and "naciśnij E, aby go podnieść" not in SOURCE and '<span class="key">E</span> podnieś przedmiot' not in SOURCE,
    "starting room has no item offers": "WYBÓR PRZEDMIOTÓW" not in SOURCE and "if(roomNo===1&&floor===1&&!shopRoom)" in SOURCE,
    "seven starter weapons have distinct projectile behavior": all(x in SOURCE for x in ("fire-precision","fire-spread","fire-rapid","Salwa","Przebijający","Wybuchowy","pattern:'burst'","pierce:2","explosive:true","shotSpeed=player.shotSpeed*mode.speed")),
    "starter weapons show damage, DPS and explicit pros/cons": "weaponStats" in SOURCE and "Obrażenia / pocisk:" in SOURCE and "DPS teoretyczny:" in SOURCE and "mode.tradeoff" in SOURCE and "Math.round(17*mode.rate)" in SOURCE,
    "spread and burst raw DPS are not inflated by projectile count": "damage:.5,rate:1.5,pattern:'spread'" in SOURCE and "damage:.32,rate:1.65,pattern:'burst'" in SOURCE,
    "movement styles have distinct handling, pros/cons and real Juggernaut defense": all(x in SOURCE for x in ("player.movement==='drifter'","player.movement==='momentum'","player.movement==='twitch'","move-juggernaut","m==='hopper'","40% mniej obrażeń","dmg*.6")),
    "active item consumes item": "player.items=player.items.filter(x=>x!==item)" in SOURCE,
    "pause and restart": "state='paused'" in SOURCE and "startRun()" in SOURCE,
    "animation loop": "requestAnimationFrame(loop)" in SOURCE,
    "automatic rescue item is a one-use fatal-hit save": "kategoria:'rescue'" in SOURCE and "player.hp=1" in SOURCE and "player.items.splice(rescueIndex,1)" in SOURCE,
    "persistent profile schema and safe storage": "cryptCrawlerProfileV1" in SOURCE and "function loadMetaProfile()" in SOURCE and "function saveMetaProfile()" in SOURCE,
    "item discoveries persist on pickup": "recordItemDiscovery(d.item)" in SOURCE and "metaProfile.discoveredItems" in SOURCE,
    "death records run losses": "const run=recordRunDeath()" in SOURCE and "coinsLost:coins" in SOURCE and "itemsLost:player?player.items.map(item=>item.nazwa):[]" in SOURCE,
    "codex UI is deferred while saved profile code is preserved": "profileBtn=null;" in SOURCE and "function showCodex()" in SOURCE and "profileBtn=document.createElement('button')" not in SOURCE,
    "run start opens firing-style choice": "showFiringChoice()" in SOURCE and "state='firingChoice'" in SOURCE,
    "firing-style choice leads to movement choice": "showMovementChoice(true)" in SOURCE and "state='movementChoice'" in SOURCE,
}
failed = [name for name, passed in checks.items() if not passed]
for name, passed in checks.items():
    print(("PASS" if passed else "FAIL") + "  " + name)
if failed:
    raise SystemExit(f"{len(failed)} source check(s) failed: {', '.join(failed)}")
print(f"\nAll {len(checks)} source checks passed. Source size: {len(SOURCE)} chars.")
