import os

#Available default keywords are:\nhey google, hey siri, pico clock, americano, 
#hey barista, computer, grapefruit, grasshopper, jarvis, terminator, picovoice, bumblebee, porcupine, alexa, blueberry, ok google
START_WORD = ["jarvis", "alexa", "computer"]
ACCESS_KEY = "3rXSA8EZIAa9DqGoomCvvqVBdQkGAKZt7lIPOTTmauMMPSn7K11uuA=="

dirPath = os.path.dirname(os.path.realpath(__file__))
sounds = dirPath + "\\sounds"

commands_dict = {
    'commands': {
        'openYoutube': ['youtube', 'open youtube', 'յուտուբ', 'յութուբ', 'մյացրա յութուբ', 'ютуб'],
        'openYandex': ['yandex', 'open yandex', 'яндекс'],
        'openSteam': ['steam', 'open steam', 'стим', 'ստիմ', 'մյացրա steam'],
        'openVscode': ['vs code', 'code', 'код', 'կոդ', 'vscode', 'vescode'],
        'openEpicGames': ['epic games', 'epic', 'epicgames'],
        'gtaRp': ['gtarp'],
        'weather': ['погода', 'weather', 'եղանակ'],
        'time': ['время', 'time', 'ժամանակ', 'ժամ'],
        'openDiscord': ['discord', 'дискорд', 'рткрой дискорд', 'рткрой discord'],
        "openMinecraft": ["minecraft", "майнкрафт"],
        'screenShot': ['screenshot', 'скриншот', 'сделай скриншот'],
    }
}

steam = "C:\\Program Files (x86)\\Steam\\steam.exe"
discord = "C:\\Users\\Karen Ghazaryan\\AppData\\Local\\Discord\\Update.exe"
vsCode = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
minecraft = "C:\\Users\\Karen Ghazaryan\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
epicGames = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
gtaRp = "C:\\Program Files (x86)\\GTA5RP\\GTA5RPLauncher.exe"