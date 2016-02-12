
""" Module level utility functions- wrappers around objc_util code that expose
new functionaility in the app. """


@on_main_thread
def setBadgeString(badgestring):
    """Set the badge on the app icon to be a certain string"""
	app.setApplicationBadgeString_(badgestring)

@on_main_thread
def setBadgeNumber(num):
	"""Set the badge on the app icon to be a certain number"""
	app.setApplicationIconBadgeNumber_(num)

@on_main_thread
def clearBadge():
	"""Clear the badge on the app icon"""
	app.setApplicationBadgeString_("")
	app.setApplicationBadgeNumber_(0)


@on_main_thread
def openURL(url):
	"""Open a url in a way that works through appex. This is useful for using
	URL schemes to open other apps with data gained from appex."""
	app._openURL_(nsurl(url))

@on_main_thread
def getConsoleFont():
	"""Return the font size and name that is currently active for the console"""
	consoleVC.view()
	return consoleVC.outputFont()

@on_main_thread
def getDefaultFont():
	"""Get the user default for console font"""
	return [str(userDefaults.stringForKey_('OutputFontName')), userDefaults.integerForKey_('OutputFontSize')]
