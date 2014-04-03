

import sublime, sublime_plugin
import os
import subprocess
import thread
import sys
 
 

PLUGIN_DIRECTORY = os.getcwd().replace(os.path.normpath(os.path.join(os.getcwd(), '..', '..')) + os.path.sep, '').replace(os.path.sep, '/')
PLUGIN_PATH = os.getcwd().replace(os.path.join(os.getcwd(), '..', '..') + os.path.sep, '').replace(os.path.sep, '/')

class ConvertJsonCommand(sublime_plugin.WindowCommand):
	def run(self):
		path=self.window.active_view().file_name()
		jsPath=os.path.join(PLUGIN_PATH,"converter.js")
		cmdStr="node "+"\""+jsPath+"\""+" \""+path+"\""
		proce = subprocess.Popen(cmdStr ,shell=True,stdout=subprocess.PIPE)
		output=proce.communicate()[0].decode("utf-8")
		print cmdStr
		newView=self.window.new_file()
		newView.set_syntax_file("Packages/XML/XML.tmLanguage")
		edit = newView.begin_edit()
		newView.insert(edit, newView.size(), output)
		newView.end_edit(edit)
		pass