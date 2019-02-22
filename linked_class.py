from linked_list import MyList, ListNode

class Stack:
	def __init__(self):
		self.stack = MyList()
		
	def length(self):
		return self.stack.__len__()
		
	def isEmpty(self):
		if self.length() == 0:
			return True
		return False
		
	def pop(self):
		if not self.isEmpty():
			data = self.stack.get_last_elem()
			self.stack.remove(data)
			return data
				
		print("Stack is empty")
		return ""
			
		
	def push(self, item):
		elem = ListNode(item)
		self.stack.add(elem)
		
	def peek(self):
		if not self.isEmpty():
			return self.stack.get_last_elem()
				
		print("Stack is empty")
		return ""
