import distro
import psutil
import wmctrl
ram = psutil.virtual_memory().total
swap = psutil.swap_memory().total

def to_humanreadable(bytes):
	unitIndex = 0
	units = ["B","KB","MB","GB","TB"]
	while 1000 <= bytes:
		bytes /= 1000
		unitIndex += 1
	return f"{round(bytes)}{units[unitIndex]}"

colors = {
	"arch":"\u001b[36;1m",
	"manjaro":"\u001b[32;1m"
}

logos = {
	"arch":["  /\   "," /  \  ","/_/\_\ "],
	"manjaro":["|־־ | ","| | | ","| | | "]
}

def get_longest_line():
    longestlength = 0
    for line in logos[distro.id()]:
        if len(line) > longestlength:
            longestlength = len(line)
    return longestlength

def get_color():
	try:
		color = colors[distro.id()]
	except:
		color = "\u001b[37m"
	return "\u001b[1m"+color

reset = "\u001b[0m"

def get_wm(name):
    wm = wmctrl.os.environ.get('DESKTOP_SESSION')
    if "/" in wm:
        wm = wm.split("/")[len(wm.split("/"))-1]
        isde="de"
        if wm in ["openbox"]:
            isde="wm"
    else:
        isde = "wm"

    if name == True:
        return wm
    else:
        return isde

def print_info():
    try:
        logo = logos[distro.id()]
    except:
        logo = ["  ??   ","?????? ","  ??   "]
    print(f" {get_color()}{logo[0]}{reset} | {get_color()}os{reset}   {distro.id()}")
    print(f" {get_color()}{logo[1]}{reset} | {get_color()}ram{reset}  {to_humanreadable(ram)}")
    print(f" {get_color()}{logo[2]}{reset} | {get_color()}swap{reset} {to_humanreadable(swap)}")
    print(f" {' '*get_longest_line()} | {get_color()}{get_wm(False)}{reset}   {get_wm(True)}")

print_info()
