'''
Pythonista.py

Vision:

- bring together in one place the things its possible to do with UIApplication and objc_util
- make customising the Pythonista app, similar to, and as easy as, using the UI module

Credits:

- based on examples by @omz, @JonB, @Webmaster4o, etc
'''

# Imports
from objc_util import *
import dialogs
import urllib

# Global variables
NSUserDefaults = ObjCClass('NSUserDefaults')
WKWebView = ObjCClass('WKWebView')
NSURLRequest = ObjCClass('NSURLRequest')
UIBarButtonItem = ObjCClass('UIBarButtonItem')
UISearchBar = ObjCClass('UISearchBar')
NSDataDetector = ObjCClass('NSDataDetector')

app = UIApplication.sharedApplication()
rootVC = app.keyWindow().rootViewController()
tabVC = rootVC.detailViewController()
consoleVC = app.delegate().consoleViewController()
userDefaults = NSUserDefaults.standardUserDefaults()



# Core functionality
from utility import *
from classes import *


if __name__ == "__main__":
	#setBadgeString('test')
	#setBadgeNumber(1)
	#openURL('pythonita://')
	#print getConsoleFont()
	#print getDefaultFont()
	Tab().present()
	WebTab().present()
