import distro
import psutil
ram = psutil.virtual_memory().total
swap = psutil.swap_memory().total

def to_humanreadable(bytes):
	unitIndex = 0
	units = ["B","KiB","MiB","GiB","TiB"]
	while 1024 <= bytes:
		bytes /= 1024
		unitIndex += 1
	return f"{round(bytes)}{units[unitIndex]}"

colors = {
	"arch":"\u001b[36;1m",
	"manjaro":"\u001b[32;1m",
	"gentoo":"\u001b[35;1m",
	"fedora":"\u001b[34;1m",
}

logos = {
	"arch":["  /\\   ",
			" /  \\  ",
			"/_/\\_\\ "],
	"manjaro":["|־־ | ",
		   	   "| | | ",
			   "| | | "],
	"gentoo":["  ---  ",
		  	  " \\ 0 \\ ",
		  	  " /__/  "],
	"ubuntu":["/----\\",
			  "| () |",
			  "\\----/"],
	"fedora":["  ,--",
			  ",-|- ",
			  "\\_|  "],
	"darwin":[" _/_ ", "|   |", "`---´"],
}

names = {
	"darwin": "macos",
}

def get_color():
	try:
		color = colors[distro.id()]
	except:
		color = "\u001b[37m"
	return "\u001b[1m"+color

def get_name():
	try:
		return names[distro.id()]
	except:
		return distro.id()

def get_logo():
	try:
		return logos[distro.id()]
	except:
		return ["  ??   ","?????? ","  ??   "]

reset = "\u001b[0m"

def print_info():
	logo = get_logo()
	color = get_color()
	print(f" {color}{logo[0]}{reset} | {get_color()}os{reset}   {get_name()}")
	print(f" {color}{logo[1]}{reset} | {get_color()}ram{reset}  {to_humanreadable(ram)}")
	print(f" {color}{logo[2]}{reset} | {get_color()}swap{reset} {to_humanreadable(swap)}")

print_info()
