
class InsuranceCompany:

	def __init__(self, data:dict):
		self.title = data['title']
		self.description = data['description']
		self.logo = data['logo']
		self.webpage = data['webpage']
		self.price = data['price']
		self.insurance_types = data['insurance_types']
	
