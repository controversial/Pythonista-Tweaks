'''Miscellaneous other functions for controlling the app'''

from globals import *

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
	app.setApplicationIconBadgeNumber_(0)


@on_main_thread
def openURL(s):
	"""Open a url in a way that works through appex. This is useful for using
	URL schemes to open other apps with data gained from appex."""
	app._openURL_(nsurl(s))

if __name__ == '__main__':
	setBadgeString('Test')
	setBadgeNumber(1)
	clearBadge()
	openURL('http://forum.omz-software.com/')