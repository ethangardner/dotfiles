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
	# Source Control
	"apt-get install -y git-core", 
	"apt-get install -y subversion",
	"apt-get install -y libapache2-svn",
	# Utilities
	"apt-get install -y curl",
	"apt-get install -y siege",
	"apt-get install -y imagemagick --fix-missing", 
	"apt-get install -y phantomjs", 
	"apt-get install -y ack", 
	# Python Packages
	"easy_install mechanize", 
	"easy_install beautifulsoup4",
	"easy_install markdown",
	"apt-get install -y python-imaging",
	# Ruby Gems
	"\curl -L https://get.rvm.io | bash -s stable --ruby"
	"apt-get install -y ruby-sass",
	"apt-get install -y ruby-compass",
	"apt-get install -y ruby-haml",
	# Java
	"apt-get install -y openjdk-7-jre",
	# Node JS
	"apt-get install -y python-software-properties python g++ make",
	"add-apt-repository ppa:chris-lea/node.js",
	"apt-get update",
	"apt-get install -y nodejs npm",
	# "ln -s /usr/bin/nodejs /usr/bin/node"
]

class FreshInstall():
	"""FreshInstall is responsible for the general setup of a
	new Ubuntu Linux development machine. """
	def __init__(self):
		self.packages = packages
		self.loadPackages(packages)

	def loadPackages(self, packages):
		if _platform == "linux" or _platform == "linux2":
			packages = '; '.join(packages)
			subprocess.Popen(packages, shell=True)

	
	def installSymlinks(self):
		folder = '.' + os.sep + '.dotfiles'
		files = os.listdir(folder)
		ignored = [".git", "README.md", "install.py"]

		for filename in files:
			if filename not in ignored:
				command = 'ln -s ' + folder + os.sep + filename + ' .' + os.sep + filename
				subprocess.Popen(command.split(), stdout=subprocess.PIPE)

if __name__ == "__main__":
    go = FreshInstall()
    go.installSymlinks()
