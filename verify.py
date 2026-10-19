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
    "pickup requires E": "keys.has('e')" in SOURCE,
    "active item consumes item": "player.items=player.items.filter(x=>x!==item)" in SOURCE,
    "pause and restart": "state='paused'" in SOURCE and "startRun()" in SOURCE,
    "animation loop": "requestAnimationFrame(loop)" in SOURCE,
}
failed = [name for name, passed in checks.items() if not passed]
for name, passed in checks.items():
    print(("PASS" if passed else "FAIL") + "  " + name)
if failed:
    raise SystemExit(f"{len(failed)} source check(s) failed: {', '.join(failed)}")
print(f"\nAll {len(checks)} source checks passed. Source size: {len(SOURCE)} chars.")
