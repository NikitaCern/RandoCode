import os
import sys, subprocess

n = int(input("Ready to create a file-system on your Desktop?\nYES(1) NO(0)"))

add_to_path = ["\\Aup", "\\lab_darbi"]

path = os.path.expanduser('~/Desktop')

file_location = os.getcwd()

if n == 1:
	try:
		for add in add_to_path:
			path = path + add
			os.mkdir(path)
			os.chdir(path)
			print(path)
	except OSError:
		print("Failed to create folder %s!!" % path)

input("Almost done!\nPress Enter to continue...")

os.remove(file_location + "\\startup.py")
