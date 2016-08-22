import webbrowser
import os

st = set(['a','b','c', 'c'])

class CustomError(Exception):
	def __init__(self, m):
		self.message = m
	def __str__(self):
		return repr('unknown method ' + self.message)		


def display_in_browser(f):
	webbrowser.open(f.name)

def write_in_file(str_content, filepath):
	filepath.write(str_content)

def display(elems, method='console'):
	if method == 'console':
		for item in st:
			print item
	elif method == 'html': #write in a file and open with a browser
		s = '<ul>'
		for item in elems:
			s += '<li>' + item + '</li>'
		s += '</ul>'
		f = open('to_show.html', 'w')
		write_in_file(s, f)
		display_in_browser(f)

	else:
		raise CustomError(method)

display(st, 'htm')	
