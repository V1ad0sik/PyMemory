from Module.Game import *
from Module.Memory import *
from Module.Offsets import *


if (Game.Connect("csgo.exe")):
    print("--------------------------\n")
    print(f"> Game = {hex(Game.Client)}")
    print(f"> Handle = {hex(Game.ProcessID)}\n")
    print(f"> client.dll = {hex(Game.Client)}")
    print(f"> engine.dll = {hex(Game.Engine)}")
    print("--------------------------\n")

    for i in range(0, 31):
        Entity = Memory.Read.int(Game.Client + Offsets.Signatures.dwEntityList  + (i * 0x10))

        if (Entity):
            Health = Memory.Read.int(Entity + Offsets.Netvars.m_iHealth)

            print(f"[{i + 1}] Entity health = {Health}")