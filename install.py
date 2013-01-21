#!/usr/bin/env python
import os
import subprocess
from sys import platform as _platform

'''
Run this file from your home directory. 
It installs some commonly used packages and 
symlinks files to the .dotfiles directory so 
they can be placed under version control
'''

packages = [
	"apt-get update",
	"apt-get install -y git-core", # Source control
	"apt-get install -y subversion",
	"apt-get install -y libapache2-svn",
	"apt-get install imagemagick --fix-missing", 
	"easy_install mechanize", #Python packages
	"easy_install beautifulsoup4",
	"apt-get install python-imaging"
]

if _platform == "linux" or _platform == "linux2":
	for package in packages:
		package = package + ';'
	subprocess.Popen(package, shell=True)

folder = '.' + os.sep + '.dotfiles'
files = os.listdir(folder)

ignored = [".git", "README.md", "install.py"]

for filename in files:
	if filename not in ignored:
		command = 'ln -s ' + folder + os.sep + filename + ' ./' + filename
		subprocess.Popen(command.split(), stdout=subprocess.PIPE)
