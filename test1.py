class Heapify(object):
	def __init__(self, n):
		self.num = n
		self.right = None
		
	def __repr__(self):
		return str(self.num)

	
	def inc_num(self):
		self.num += 1
		
	def print_right(self):
		print(self.right)
		
	def print_from_cur(self):
		cur_obj = self
		while cur_obj:
			print(cur_obj)
			cur_obj = cur_obj.right
	
	
	
new_obj = Heapify(1)
new_obj2 = Heapify(2)
new_obj3 = Heapify(3)

new_obj.right = new_obj2
new_obj2.right = new_obj3

new_obj.print_from_cur()


	






	