"""Methods relating to the console."""

from objc_util import on_main_thread

from . import shared

__all__ = [
	"getConsoleFont",
	"getDefaultFont",
]

@on_main_thread
def getConsoleFont():
	"""Return the font name and size that is currently active for the console."""
	
	shared.consoleVC.view()
	desc = shared.consoleVC.outputFont().fontDescriptor()
	font = [str(desc.objectForKey_(a)) for a in ("NSFontNameAttribute", "NSFontSizeAttribute")]
	font[1] = int(font[1])
	return tuple(font)

@on_main_thread
def getDefaultFont():
	"""Get the user default for console font."""
	
	return (
		str(shared.userDefaults.stringForKey_("OutputFontName")),
		shared.userDefaults.integerForKey_("OutputFontSize"),
	)