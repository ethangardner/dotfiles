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
	"apt-get install -y git-core", 
	"apt-get install -y subversion",
	"apt-get install -y libapache2-svn",
	"apt-get install -y imagemagick --fix-missing", 
	"easy_install mechanize", 
	"easy_install beautifulsoup4",
	"easy_install markdown",
	"apt-get install -y python-imaging",
	"apt-get install -y ruby-sass",
	"apt-get install -y ruby-compass",
	"apt-get install -y ruby-haml",
	"apt-get install -y openjdk-7-jre"
]

class FreshInstall():
	"""docstring for FreshInstall"""
	def __init__(self):
		self.packages = packages
		self.loadPackages(packages)

	def loadPackages(self, packages):
		if _platform == "linux" or _platform == "linux2":
			packages = '; '.join(packages)
			# print packages
			subprocess.Popen(packages, shell=True)		
	
	def installSymlinks(self):
		folder = '.' + os.sep + '.dotfiles'
		files = os.listdir(folder)
		ignored = [".git", "README.md", "install.py"]

		for filename in files:
			if filename not in ignored:
				command = 'ln -s ' + folder + os.sep + filename + ' ./' + filename
				subprocess.Popen(command.split(), stdout=subprocess.PIPE)

if __name__ == "__main__":
    go = FreshInstall()
    go.installSymlinks()