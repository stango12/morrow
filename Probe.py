class Probe(object):

	device_id = ""
	moisture = 0.0
	temperature = 0.0
	humidity = 0.0

	def __init__(self, device_id):
		self.device_id = device_id
		self.moisture = 0.0
		self.temperature = 0.0
		self.humidity = 0.0

	def update_data(self):
		self.moisture = moisture
		self.temperature = temperature
		self.humidity = humidity