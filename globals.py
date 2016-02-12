from objc_util import *

app=UIApplication.sharedApplication()

WKWebView = ObjCClass('WKWebView')
NSURLRequest = ObjCClass('NSURLRequest')
UIBarButtonItem = ObjCClass('UIBarButtonItem')
UISearchBar = ObjCClass('UISearchBar')
NSDataDetector = ObjCClass('NSDataDetector')
NSUserDefaults = ObjCClass('NSUserDefaults')


userDefaults = NSUserDefaults.standardUserDefaults()
consoleVC = app.delegate().consoleViewController()
app = UIApplication.sharedApplication()
rootVC = app.keyWindow().rootViewController()
tabVC = rootVC.detailViewController()