# coding: utf-8

'''
Pythonista.py

Vision:

- bring together in one place the things its possible to do with UIApplication and objc_util
- make customising the Pythonista app, similar to, and as easy as, using the UI module

Credits:

- based on examples by @omz, @JonB, @Webmaster4o, etc

'''

from objc_util import *
import dialogs
import urllib

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

'''
Classes to support customising the Pythonista app in a similar way to using the UI Module.
'''

# objCClasses
	
@on_main_thread
def Button(s):
	return UIButton.new().autorelease()
	
@on_main_thread
def WebView(s):
	return WKWebView.new().autorelease()
		
@on_main_thread
def ButtonItem(s, image, action):
	return UIBarButtonItem.alloc().initWithImage_style_target_action_(UIImage.imageNamed_(image), 0, s.newVC, sel(action))
		
@on_main_thread
def SearchBar(s):
	sb = UISearchBar.alloc().initWithFrame_(((0, 0), (200, 32)))
	sb.searchBarStyle = 2
	sb.placeholder = 'Search or enter address'
	sb.delegate = s.newVC
	ObjCInstanceMethod(sb, 'setAutocapitalizationType:')(0)
	return sb
		
# View classes
		
class View(object):
	@on_main_thread
	def __init__(self):
		self.name = ''
		self.right_button_items = list()
		self.newVC = self.customVC()
		self.makeSelf()

	@on_main_thread
	def makeSelf(self):
		pass
		
	@on_main_thread
	def customVC(self):
		return None
		
	@on_main_thread
	def present(self):
		pass
		
		
class Tab(View):
	@on_main_thread
	def makeSelf(self):
		self.name = 'Tab'
		
	@on_main_thread
	def customVC(self):
		return create_objc_class('CustomViewController', ObjCClass('UIViewController'), methods=[], protocols=['OMTabContent',]).new().autorelease()
		
	@on_main_thread		
	def present(self):
		self.newVC.title = self.name
		self.newVC.navigationItem().rightBarButtonItems = self.right_button_items
		tabVC.addTabWithViewController_(self.newVC)

		
class WebTab(Tab):
	@on_main_thread
	def makeSelf(self):
		self.name = 'WebTab'
		biA = ButtonItem(self, image = 'Action', action ='wtShare')
		self.right_button_items.append(biA)
		biF = ButtonItem(self, image = 'Forward', action ='wtGoForward')
		self.right_button_items.append(biF)
		biB = ButtonItem(self, image = 'Back', action = 'wtGoBack')
		self.right_button_items.append(biB)
		sb = SearchBar(self)
		self.newVC.navigationItem().titleView = sb
		wv = WebView(self)
		wv.loadRequest_(NSURLRequest.requestWithURL_(nsurl('http://www.google.com')))
		self.newVC.view = wv
	
	@on_main_thread
	def customVC(self):
		return create_objc_class('CustomViewController', ObjCClass('UIViewController'), methods=[wtShare, wtGoBack, wtGoForward, searchBarSearchButtonClicked_], protocols=['OMTabContent', 'UISearchBarDelegate']).new().autorelease()

# actions

def wtShare(_self, _cmd):
	view = ObjCInstance(_self).view()
	url = view.URL()
	if url:
		url_str = str(url.absoluteString())
		dialogs.share_url(url_str)
	
def wtGoBack(_self, _cmd):
	view = ObjCInstance(_self).view()
	view.goBack()

def wtGoForward(_self, _cmd):
	view = ObjCInstance(_self).view()
	view.goForward()
		
def searchBarSearchButtonClicked_(_self, _cmd, _sb):
	searchbar = ObjCInstance(_sb)
	term = str(searchbar.text())
	searchbar.resignFirstResponder()
	if term:
		det = NSDataDetector.dataDetectorWithTypes_error_(1<<5, None)
		res = det.firstMatchInString_options_range_(term, 0, (0, len(term)))
		view = ObjCInstance(_self).view()
		if res:
			view.loadRequest_(NSURLRequest.requestWithURL_(res.URL()))
			searchbar.text = res.URL().absoluteString()
		else:
			view.loadRequest_(NSURLRequest.requestWithURL_(nsurl('http://www.google.com/search?q=' + urllib.quote(term))))
			
			
'''
Module level utility functions
'''

@on_main_thread
def setBadgeString(s):
	app.setApplicationBadgeString_(s)

@on_main_thread	
def setBadgeNumber(i):
	app.setApplicationIconBadgeNumber_(i)

@on_main_thread
def openURL(s):
	app._openURL_(nsurl(s))
	
@on_main_thread
def getConsoleFont():
	consoleVC.view()
	return consoleVC.outputFont()
	
@on_main_thread
def getDefaultFont():
	return [str(userDefaults.stringForKey_('OutputFontName')), userDefaults.integerForKey_('OutputFontSize')]


if __name__ == "__main__":
	#setBadgeString('test')
	#setBadgeNumber(1)
	#openURL('pythonita://')
	#print getConsoleFont()
	#print getDefaultFont()
	Tab().present()
	WebTab().present()