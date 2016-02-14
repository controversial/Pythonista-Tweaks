"""Root of the pythonista package."""

import objc_util
import sys

__all__ = []

# Install the loader for pythonista.classes.

# Note: objc_util already caches ObjCClass instances. We don't need to worry about that.
class ObjCClassModuleProxy(type(sys)):
	def __dir__(self):
		return list(sorted(set(self.__dict__.keys()) | set(objc_util._cached_classes.keys())))

	def __getattr__(self, name):
		try:
			return objc_util.ObjCClass(name)
		except ValueError as err:
			raise AttributeError(err.message)

class FinderLoaderForClasses(object):
	def find_module(self, fullname, path=None):
		return self if fullname == "pythonista.classes" else None
	
	def load_module(self, fullname):
		assert fullname == "pythonista.classes"
		mod = sys.modules.setdefault(fullname, ObjCClassModuleProxy(fullname))
		mod.__file__ = "<dynamically created by {cls.__module__}.{cls.__name__}>".format(cls=type(self))
		mod.__loader__ = self
		mod.__package__ = "pythonista"
		mod.__all__ = ["NSDontEvenTryToStarImportThisModuleYouCrazyPerson"]
		return mod

# This is for removing old versions of the loader if the pythonista module is reloaded.
for obj in sys.meta_path:
	if type(obj).__module__ == "pythonista" and type(obj).__name__ == "FinderLoaderForClasses":
		sys.meta_path.remove(obj)
		break

sys.meta_path.append(FinderLoaderForClasses())
from . import classes
reload(classes)