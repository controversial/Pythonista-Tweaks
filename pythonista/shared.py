from .classes import NSUserDefaults, UIApplication

__all__ = [
	"app",
	"consoleVC",
	"rootVC",
	"tabVC",
	"userDefaults",
]

app = UIApplication.sharedApplication()
consoleVC = app.delegate().consoleViewController()
rootVC = app.keyWindow().rootViewController()
tabVC = rootVC.detailViewController()
userDefaults = NSUserDefaults.standardUserDefaults()