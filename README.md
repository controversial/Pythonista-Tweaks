# Pythonista Class

## Vision

- bring together in one place the things its possible to do with UIApplication and objc_util
- make customising the Pythonista app, similar to, and as easy as, using the UI module
 
## Notes

The code is now broken into several submodules. Download the repo, and save it in site-packages as Pythonista. Then, the submodules are:

* Pythonista.editor, which contains the Tab class and the WebTab,
* Pythonista.console, which contains functions for getting the current and default console fonts
* Pythonista.app, which contains functions for setting the badge string/number, clearing the badge, and opening URLs in an apex-safe way.

__Note:__ Please do NOT use from Pythonista import *, as this could create conflicts with the default console and editor modules. Instead, use it only with import Pythonista, as this way the module's editor and console modules will not overwrite Pythonista's default ones. It is fine to use from Pythonista.app import *.

As of right now, each submodule contains only a small amount of functionality, but as they're expanded, the submodule approach will make much more sense.

Pythonista.editor will hopefully eventually contain the classes for easily controlling the editor's look and feel. The structure of these submodules, as well as their names, is likely to change.

## Credits

- based on examples by @omz, @JonB, @Webmaster4o, etc

