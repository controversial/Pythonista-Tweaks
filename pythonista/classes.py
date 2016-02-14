# This is not the real classes module.
# The first tim you import the pythonista module, it installs a custom loader for this module into sys.meta_path, so this file is never loaded.
# The loader creates an instance of ObjCClassModuleProxy and uses that as the module pythonista.classes.
# ObjCClassModuleProxy is a subclass of the built-in module type. It overrides __getattr__ so that pythonista.classes.ClassName is the same as objc_util.ObjCClass("ClassName"). The main purpose of this is that you can quickly load multiple Objective-C classes using a normal from import.

raise ImportError("This file should never be imported. The pythonista.classes module must be loaded by a custom loader that should have been installed by the pythonista module.")