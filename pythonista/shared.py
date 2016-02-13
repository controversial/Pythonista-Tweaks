import objc_util
from objc_util import *

__all__ = sorted(set('''app consoleVC NSDataDetector NSURLRequest NSUserDefaults
rootVC tabVC UIBarButtonItem UISearchBar userDefaults WKWebView'''.split()) | {
name for name in dir(objc_util) if not name.startswith('_')} - set('''ctypes
inspect itertools os pp re string sys ui weakref'''.split()))

NSDataDetector = ObjCClass("NSDataDetector")
NSURLRequest = ObjCClass("NSURLRequest")
NSUserDefaults = ObjCClass("NSUserDefaults")
UIBarButtonItem = ObjCClass("UIBarButtonItem")
UISearchBar = ObjCClass("UISearchBar")
WKWebView = ObjCClass("WKWebView")

app = UIApplication.sharedApplication()
consoleVC = app.delegate().consoleViewController()
rootVC = app.keyWindow().rootViewController()
tabVC = rootVC.detailViewController()
userDefaults = NSUserDefaults.standardUserDefaults()
