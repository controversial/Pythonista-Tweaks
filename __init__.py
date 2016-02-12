'''
Pythonista.py

Vision:

- bring together in one place the things its possible to do with UIApplication and objc_util
- make customising the Pythonista app, similar to, and as easy as, using the UI module

Credits:

- based on examples by @omz, @JonB, @Webmaster4o, etc
'''
import globals
import app
import localconsole as console
import localeditor as editor

if __name__ == "__main__":
	app.setBadgeString('test')
	app.setBadgeNumber(1)
	app.clearBadge()
	app.openURL('pythonita://')
	print console.getConsoleFont()
	print console.getDefaultFont()
	editor.Tab().present()
	editor.WebTab().present()