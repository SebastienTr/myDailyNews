#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from .weather import Weather
from .news import News
from .view import View

import app.api

class MyDailyNews():
	"""Free your mind :)"""
	def __init__(self, location="Nice"):
		super(MyDailyNews, self).__init__()
		self.__location = location

		self.news = None
		self.weather = None
		self.view = None

	def getWeather(self):
		self.weather = Weather()
		self.weather.getWeather(self.__location)

	def getNews(self):
		self.news = News()
		self.news.getNews()

	def printWeather(self, index=0):
		self.weather.printWeather(index)

	def play(self):
		if self.weather is not None:
			self.weather.play()
		if self.news is not None:
			self.news.play()

	def echo(self):
		if self.weather is not None:
			self.weather.printWeather()
		if self.news is not None:
			self.news.printNews()

	def render(self):
		self.view = View()

		self.view.render(data={
			'weather': self.weather.getData(),
			'news': self.news.getData(),
			'var': 'Hello World'})

	def run(self):
		self.getWeather()
		self.getNews()
		# self.echo()
		# self.play()
		self.render()

def main():
	myDailyNews = MyDailyNews('Nice')
	myDailyNews.run()
