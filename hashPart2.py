#MIDN Megan Fields & MIDN Luke Loehr, SY402 - Section 3321

#Lab 8: Understanding the Host's integrity
#	Part 1 - create a script that will recursively walk through all the files on a file system.
#	Configure the program to define certain files/directories as  unhashable so they'll be
#	ignored. /dev, /proc, /run, /sys, /tmp, /var/lib, & /var/run  should not be hashed.
#	Focus on making a program to walk through the system, print out the filenames & their paths
#	and label & skip printing the unhashable files from above.

#	Part 2 - Integrate SHA-256 into the program to hash each file/directory as it moves through
#	the system. Make use of hashlib.

#	Part 3 - Store the file/directory & its  hash info to be available for future runs. At a
#	minimum, store the filename w/ full path, hash, & date/time the file was last observed.

# 	Part 4 - Configure the program to be able to run and update the information it pulls
#	about the filesystem. Upon completion of running, it should print out the new files &
#	any changes found within the filesystem (including new files, modified files, and
#	missing files)

#	Part 5 (EC) - Configure the program to detect any files that are moved. Detail where the
#	file is now, its original location, & the time of the last scan in the last location.

#Works Cited:
#Used to freshen up what a recursive statement is:
#	https://realpython.com/lessons/defining-recursive-function/


#!/usr/bin/python

import sys
import csv
from datetime import datetime
from datetime import date
import hashlib
import os

def main():
	runWalk = walk_recursive()
	print(runWalk)

#Part 2: Integrate SHA256

unhashables = ["dir", "proc", "run", "sys", "tmp", "var"]
recipieForDisaster = []

def walk_recursive():
	for dirpath, dirs, files in os.walk(".", topdown = False):
		for name in files: #check the files
			print(os.path.join(dirpath, name))	#print the path for the file
			hashFile = hashIn256(name) #hash the filename
		for name in dirs: #check the dirs
			for dirName in unhashables:
				if (name == dirName):
					recipieForDisaster.append(dirName)
				if (name == "lib" or name == "run"):
					#need the full path now
					check1 = os.path.join(dirpath, filename)
					if ("var" in check1):
						recipieForDisaster.append("var/"+filename)

			print(os.path.join(dirpath, name))	#print the path for the dir
			hashDir = hashIn256(filename) #hash the directory

	print(recipieForDisaster) #check which dirs we caught


#Hash SHA256 Function
def hashIn256(filename):
	h1 = hash(filename) #builds a hash object
	h2 = hashlib.sha256() #buils a sha256 object
	byteString = filename.encode() #encode() turns a string into an array of ints
	h2.update(byteString) #sends the string to the hash function
	hex = h2.hexdigest() #sends the string to the hash function
	#print(hex)



#Main function to run
main()
