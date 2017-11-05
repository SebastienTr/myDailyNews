#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import datetime
import time
import config

from .audio import Player

# TODO Un peux lours a loader pour si peux
from bs4 import BeautifulSoup

class Weather():
	"""docstring for Weather"""
	def __init__(self):
		super(Weather, self).__init__()
		self.url = "https://www.prevision-meteo.ch/services/json/{}"
		self.frame_url = "https://www.prevision-meteo.ch/services/html/{}/horizontal"
		self.data = ""

		self._weather = list()

	def getWeather(self, location):
		# Load the weather datas
		response = requests.get(self.url.format(location))
		self.data = response.json()

		for x in range(0,4):
			d = self.data['fcst_day_{}'.format(x)]
			self._weather.append(Day(d, x))

		# Load the html frame
		response = requests.get(self.frame_url.format(location))
		soup = BeautifulSoup(response.content, 'lxml')
		self.frame = soup.body

	def printWeather(self, index=0):
		self._weather[index].echo()

	def getWeatherString(self, index=0):
		return self._weather[index].echo(bprint=False)['totalstring']

	def getData(self, index=0):
		weather = self._weather[index].echo(bprint=False)
		weather['frame'] = self.frame

		return weather

	def play(self):
		self._weather[0].play()

	def __str__(self):
		return self.indent(self._weather)

class Day:
	"""docstring for Day"""
	def __init__(self, data=None, index=0):
		self.datetime = None
		self.weather = None
		self.city = None
		self.index = index
		self.player = Player()

		self.day_placement = config.DAY_PLACEMENT[self.index]

		if data is not None:
			self.load(data)

	def load(self, data):
		self.data = data

		self.date = data['date']
		self.day_long = data['day_long']
		self.condition = Condition(data['condition'])
		self.tmin = data['tmin']
		self.tmax = data['tmax']
		self.hourly = data['hourly_data']

	def echo(self, bprint=True):
		head_str = "Météo le {} {}.".format(self.day_long, self.date)
		condition_str = '{} {}'.format(self.condition, self.day_placement.lower())
		temperature_str = "La température variera entre {} et {} degrés.".format(self.tmin, self.tmax)

		if bprint is True:
			print ('- {}'.format(head_str))
			print (condition_str)
			print (temperature_str)
			print ("")

		return {
			'head_str': head_str,
			'condition_str': condition_str,
			'temperature_str': temperature_str,
			'totalstring': '{}{}{}'.format(head_str, condition_str, temperature_str),
		}

	def play(self):
		day = self.echo(bprint=False)

		conditions = (day['condition_str'] + " et " + day['temperature_str'])
		
		self.player.play("{day} [SLEEP 0.4] {cond}".format(
			day=day['head_str'],
			cond=conditions))
		self.player.wait(2)

class Condition:
	"""docstring for Condition"""
	def __init__(self, condition=None):
		if condition is not None:
			self.condition = condition
			self.str = config.CONDITIONS[condition]

	def __str__(self):
		return self.str
