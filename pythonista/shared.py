import objc_util
from objc_util import *

__all__ = {
	"NSDataDetector",
	"NSURLRequest",
	"NSUserDefaults",
	"UIBarButtonItem",
	"UISearchBar",
	"WKWebView",
	"app",
	"consoleVC",
	"rootVC",
	"tabVC",
	"userDefaults",
} | {name for name in dir(objc_util) if not name.startswith("_")} - {
	"ctypes",
	"inspect",
	"itertools",
	"os",
	"pp",
	"re",
	"string",
	"sys",
	"ui", 
	"weakref",
}
__all__ = list(__all__)
__all__.sort()

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