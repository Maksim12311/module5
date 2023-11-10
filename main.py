import json
class Model:

	def __init__(self,a):
		self.a = a

	def save(self,filename):
		with open(filename,'w') as f:
			attributes = [attr for attr in dir(self) if not attr.startswith("_")]
            json.dump(attributes, f)

model_instance = Model(42)
model_instance.save('output.json')