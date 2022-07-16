import psutil, ctypes
from Module.Module import *

class Game():
    ProcessID = 0
    Handle = 0


    def GetProcessID(Name):
        for Process in psutil.process_iter():
            if Process.name() == Name:
                return Process.pid


    def Connect(Name):
        Game.ProcessID = Game.GetProcessID(Name)

        if (Game.ProcessID):
            Game.Handle = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, Game.ProcessID)

        return Game.ProcessID