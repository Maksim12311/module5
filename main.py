class StringVar:
	
	def __init__(self, string):
		self.string = string
	
	def set(self):
		if self.string != []:
			newarr = list(self.string)
			del newarr[-1]
			self.string = ''.join(newarr)

	def get(self):
		return self.string	

s = StringVar(input())
s.set()
s.set()
print(s.get())