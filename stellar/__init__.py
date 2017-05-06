import inspect
import time
import base
import hitboxes
import keys
import sprites
import rooms
import tools
import objects
import sound

__authors__ = ["LeapBeforeYouLook", "Ramaraunt"]

def log(*msgs):
	frame, filename, line_number, function_name, lines, index = inspect.getouterframes(inspect.currentframe())[1]
	string = "[STELLAR] %s, %s - %s" % (function_name, filename, ", ".join(msgs))
	print string

