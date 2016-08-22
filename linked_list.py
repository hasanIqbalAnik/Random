class Empty(Exception):
	def __init__(self, value):
		self._value = value
	def __str__(self):
		return repr(self._value)

class LinkedStack:

	class _Node:
		""" Lightweight non public class """
		__slots__ = '_element', '_next'

		def __init__(self, element, next):
			self._element = element
			self._next = next
	
	def __init__(self):
		self._head = None
		self._size = 0

	
	def __len__(self):
		return self._size()

	def is_empty(self):
		return self._size == 0

	
	def push(self, e):
		self._head = self._Node(e,self._head)
		self._size += 1							
							
	
	def top(self):
		if self.is_empty():
			raise Empty('stack is empty')
		return self._head._element		

	def pop(self):
		if self.is_empty():
			raise Empty('stack is empty')

		n = self._head
		self._head = n._next
		self._size -= 1
		return n._element


linked_stack = LinkedStack()

for i in xrange(5):
	linked_stack.push(i)


for i in xrange(5):
	print linked_stack.pop()	
