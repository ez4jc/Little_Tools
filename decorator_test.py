from functools import wraps


def decorator(func):
	"""this is decorator __doc__"""
	@wraps(func)
	def wrapper(*args, **kwargs):
		"""this is wrapper __doc__"""
		print("this is wrapper method")
		return func(*args, **kwargs)
	return wrapper


@decorator
def test():
	"""this is tools_test __doc__"""
	print("this is tools_test method")


print("__name__: ", test.__name__)
print("__doc__:  ", test.__doc__)
