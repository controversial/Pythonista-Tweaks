
""" Module level utility functions- wrappers around objc_util code that expose
new functionaility in the app. """


@on_main_thread
def setBadgeString(s):
    """Set the badge on the app icon to be a certain string"""
	app.setApplicationBadgeString_(s)

@on_main_thread
def setBadgeNumber(i):
	"""Set the badge on the app icon to be a certain number"""
	app.setApplicationIconBadgeNumber_(i)

@on_main_thread
def clearBadge():
	"""Clear the badge on the app icon"""
	app.setApplicationBadgeString_("")
	app.setApplicationBadgeNumber_(0)


@on_main_thread
def openURL(s):
	"""Open a url in a way that works through appex. This is useful for using
	URL schemes to open other apps with data gained from appex."""
	app._openURL_(nsurl(s))

@on_main_thread
def getConsoleFont():
	"""Return the font size and name that is currently active for the console"""
	consoleVC.view()
	return consoleVC.outputFont()

@on_main_thread
def getDefaultFont():
	"""Get the user default for console font"""
	return [str(userDefaults.stringForKey_('OutputFontName')), userDefaults.integerForKey_('OutputFontSize')]
