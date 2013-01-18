#!/usr/bin/env python
import os
import subprocess

folder = '.' + os.sep + '.dotfiles'
files = os.listdir(folder)

ignored = [".git", "README.md", "install.py"]

for filename in files:
	if filename not in  ignored:
		command = 'ln -s ' + folder + os.sep + filename + ' ./' + filename
		subprocess.Popen(command.split(), stdout=subprocess.PIPE)