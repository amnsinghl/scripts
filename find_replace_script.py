import os
import fileinput
import sys

# script to find lines which contains search expresion
# and in that line replace "replace" with "withs"
def replaceAll(filepath,searchExp,replace, withs):
	print(filepath)
	for line in fileinput.input(filepath, inplace=1):
		if searchExp in line:
			line = line.replace(replace, withs)
		sys.stdout.write(line)

# traverse all the files in the path
for root, dirs, files in os.walk("C:\\Projects\\aman\\"):
	for file in files:
		if file.endswith("build.gradle"):
			str = os.path.join(root, file)
			replaceAll(str,"aman" , "si", "singhal")
