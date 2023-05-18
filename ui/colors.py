import platform, os, sys, string

is_windows = True if platform.system() == "Windows" else False

if is_windows:
    os.system("title NEO-GRABBER @ github.com/i64-sudo/Neo-Grabber")

def clear():
    if is_windows:
        os.system("cls")
    else:
        os.system("clear")

def pause():
    if is_windows:
        os.system(f"pause >nul")
    else:
        input()

def leave():
    try:
        sys.exit()
    except:
        exit()

def error(error):
    print(red(f"        [!] Error : {error}"), end="")
    pause(); clear(); leave()

def red(text):
    os.system(""); faded = ""
    for line in text.splitlines():
        green = 250
        for character in line:
            green -= 5
            if green < 0:
                green = 0
            faded += (f"\033[38;2;255;{green};0m{character}\033[0m")
        faded += "\n"
    return faded

def blue(text):
    os.system(""); faded = ""
    for line in text.splitlines():
        green = 0
        for character in line:
            green += 3
            if green > 255:
                green = 255
            faded += (f"\033[38;2;0;{green};255m{character}\033[0m")
        faded += "\n"
    return faded

def water(text):
    os.system(""); faded = ""
    green = 10
    for line in text.splitlines():
        faded += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
        if not green == 255:
            green += 15
            if green > 255:
                green = 255
    return faded

def purple(text):
    os.system("")
    faded = ""
    down = False

    for line in text.splitlines():
        red = 40
        for character in line:
            if down:
                red -= 3
            else:
                red += 3
            if red > 254:
                red = 255
                down = True
            elif red < 1:
                red = 30
                down = False
            faded += (f"\033[38;2;{red};0;220m{character}\033[0m")
    return faded

class ui:
    banner = f"""
             __    _  _______  _______         _______  ___      ___   _______  _______  _______  ______   
            |  |  | ||       ||       |       |       ||   |    |   | |       ||       ||       ||    _ |  
            |   |_| ||    ___||   _   | ____  |       ||   |    |   | |    _  ||    _  ||    ___||   | ||  
            |       ||   |___ |  | |  ||____| |       ||   |    |   | |   |_| ||   |_| ||   |___ |   |_||_ 
            |  _    ||    ___||  |_|  |       |      _||   |___ |   | |    ___||    ___||    ___||    __  |
            | | |   ||   |___ |       |       |     |_ |       ||   | |   |    |   |    |   |___ |   |  | |
            |_|  |__||_______||_______|       |_______||_______||___| |___|    |___|    |_______||___|  |_|
                                    Answer with either (y/Y) or (n/N) for Yes & No

                                            {purple(f"[>] Running with Python {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}")}

"""
    sv = f"                                            "