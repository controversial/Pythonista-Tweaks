''' Methods relating to the console '''

from globals import *
from console import *

@on_main_thread
def getConsoleFont():
	"""Return the font size and name that is currently active for the console"""
	consoleVC.view()
	font = consoleVC.outputFont()
	d=font.fontDescriptor()
	font = [str(d.objectForKey_(a)) for a in ('NSFontNameAttribute','NSFontSizeAttribute')]
	font[1]=int(font[1])
	return font

@on_main_thread
def getDefaultFont():
	"""Get the user default for console font"""
	return [str(userDefaults.stringForKey_('OutputFontName')), userDefaults.integerForKey_('OutputFontSize')]