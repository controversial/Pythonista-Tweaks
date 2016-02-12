"""Miscellaneous functions for controlling the app."""

from . import shared

__all__ = [
	"clearBadge",
	"openURL",
	"setBadgeNumber",
	"setBadgeString",
]

@on_main_thread
def setBadgeString(s):
	"""Set the badge on the app icon to be a certain string."""
	shared.app.setApplicationBadgeString_(badge)

@on_main_thread
def setBadgeNumber(i):
	"""Set the badge on the app icon to be a certain number."""
	shared.app.setApplicationIconBadgeNumber_(i)

@on_main_thread
def clearBadge():
	"""Clear the badge on the app icon."""
	shared.app.setApplicationBadgeString_("")
	shared.app.setApplicationIconBadgeNumber_(0)

@on_main_thread
def openURL(url):
	"""Open a url in a way that works through appex. This is useful for using
	URL schemes to open other apps with data gained from appex."""
	shared.app._openURL_(nsurl(url))