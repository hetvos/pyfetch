import distro
import psutil
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
	"manjaro":"\u001b[32;1m",
	"gentoo":"\u001b[35;1m"
}

logos = {
	"arch":["  /\   ",
		" /' \  ",
		"/_/\_\ "],
	"manjaro":["|־־ | ",
		   "| | | ",
		   "| | | "],
	"gentoo":["  ---  ",
		  " \ 0 \ ",
		  " /__/  "]
}

def get_color():
	try:
		color = colors[distro.id()]
	except:
		color = "\u001b[37m"
	return "\u001b[1m"+color

reset = "\u001b[0m"

def print_info():
	try:
		logo = logos[distro.id()]
	except:
		logo = ["  ??   ","?????? ","  ??   "]
	print(f" {get_color()}{logo[0]}{reset} | {get_color()}os{reset}   {distro.id()}")
	print(f" {get_color()}{logo[1]}{reset} | {get_color()}ram{reset}  {to_humanreadable(ram)}")
	print(f" {get_color()}{logo[2]}{reset} | {get_color()}swap{reset} {to_humanreadable(swap)}")

print_info()
