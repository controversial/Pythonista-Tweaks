"""Some basic usage examples for the pythonista module."""

import pythonista

if __name__ == "__main__":
	pythonista.app.setBadgeString("test")
	pythonista.app.setBadgeNumber(1)
	pythonista.app.clearBadge()
	pythonista.app.openURL("pythonista://")
	print(pythonista.console.getConsoleFont())
	print(pythonista.console.getDefaultFont())
	pythonista.editor.Tab().present()
	pythonista.editor.WebTab().present()
