from pathlib import Path

SOURCE = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
checks = {
    "canvas exists": '<canvas id="game"' in SOURCE,
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
    "shop heart price and healing": "Serce kosztuje 2 monety" in SOURCE and "coins-=2" in SOURCE and "player.hp+2" in SOURCE,
    "all 30 items have named labels, not placeholders": all(f"'{n}'" in SOURCE for n in ["Mała Apteczka","Sakiewka","Fala Uderzeniowa","Impuls Oczyszczający","Tarcza Eteryczna","Gwiezdna Salwa","Znak Egzekucji","Wielka Apteczka","Złota Sakwa","Fala Oczyszczenia","Lekkie Buty","Buty Wiatru","Nagolenniki Witalności","Sprinterskie Nagolenniki","Skóra Widmo","Buty Wędrowca","Stalowe Obcasy","Nagolenniki Życia","Buty Błyskawicy","Strażnicze Nagolenniki","Ciężki Pocisk","Rdzeń Mocy","Cewka Szybkostrzelna","Soczewka Prędkości","Kaliber Rozszerzony","Mechanizm Gatlinga","Komora Odrzutu","Pocisk Oblężniczy","Napęd Hiperprzestrzenny","Niszczyciel"]) and "Placeholder — przedmiot" not in SOURCE and "nazwa:'Item '+" not in SOURCE,
    "item pickup requires physical contact": "else if(d.type==='item'&&d.item){" in SOURCE and "d.item&&keys.has('e')" not in SOURCE,
    "pickup instructions do not require E": "wejdź w przedmiot, aby go podnieść" in SOURCE and "naciśnij E, aby go podnieść" not in SOURCE and '<span class="key">E</span> podnieś przedmiot' not in SOURCE,
    "starting room has no item offers": "WYBÓR PRZEDMIOTÓW" not in SOURCE and "if(roomNo===1&&floor===1&&!shopRoom)" in SOURCE,
    "firing styles have distinct visuals and projectile behavior": all(x in SOURCE for x in ("fire-precision","fire-spread","fire-rapid","shotSpeed=player.shotSpeed*mode.speed","s.mode==='rapid'")),
    "movement styles have distinct handling and silhouettes": all(x in SOURCE for x in ("player.movement==='drifter'","player.movement==='momentum'","player.movement==='twitch'","move-juggernaut","m==='hopper'")),
    "active item consumes item": "player.items=player.items.filter(x=>x!==item)" in SOURCE,
    "pause and restart": "state='paused'" in SOURCE and "startRun()" in SOURCE,
    "animation loop": "requestAnimationFrame(loop)" in SOURCE,
    "persistent profile schema and safe storage": "cryptCrawlerProfileV1" in SOURCE and "function loadMetaProfile()" in SOURCE and "function saveMetaProfile()" in SOURCE,
    "item discoveries persist on pickup": "recordItemDiscovery(d.item)" in SOURCE and "metaProfile.discoveredItems" in SOURCE,
    "death records run losses": "const run=recordRunDeath()" in SOURCE and "coinsLost:coins" in SOURCE and "itemsLost:player?player.items.map(item=>item.nazwa):[]" in SOURCE,
    "codex shows persistent progress": "KODEKS / TRWAŁY POSTĘP" in SOURCE and "function showCodex()" in SOURCE,
    "run start opens firing-style choice": "showFiringChoice()" in SOURCE and "state='firingChoice'" in SOURCE,
    "firing-style choice leads to movement choice": "showMovementChoice(true)" in SOURCE and "state='movementChoice'" in SOURCE,
}
failed = [name for name, passed in checks.items() if not passed]
for name, passed in checks.items():
    print(("PASS" if passed else "FAIL") + "  " + name)
if failed:
    raise SystemExit(f"{len(failed)} source check(s) failed: {', '.join(failed)}")
print(f"\nAll {len(checks)} source checks passed. Source size: {len(SOURCE)} chars.")
