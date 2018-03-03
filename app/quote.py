import requests
from .audio import Player
from bs4 import BeautifulSoup

class Quote:
	"""docstring for Quote"""
	def __init__(self):
		self.random_url = 'http://dicocitations.lemonde.fr/citationhasard.php'
		self.quote = None
		self.player = Player()

	def get(self):
		response = requests.get(self.random_url)
		if response is None:
			response = requests.get(self.random_url)


		soup = BeautifulSoup(response.content, "lxml")

		if soup is not None:
			self.quote_html = soup.find('p', {'class': 'citationContenu'})

			if self.quote_html is not None:
				self.quote = self.quote_html.text

				return self.quote
			else:
				return self.get()
		else:
			return self.get()

	def getData(self):
		return self.quote_html

	def printQuote(self):
		print (self.quote)

	def play(self):
		if self.quote is None:
			self.get()
		self.player.play('Citation du jour [sleep 1] {}'.format(self.quote))
