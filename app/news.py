#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import config
import feedparser

from .audio import Player

class News:
	"""docstring for News"""
	def __init__(self):
		self.language = config.LANGUAGE
		self.resume_len = config.NEWS_RESUME_LEN
		self.websites = list()

	def getNews(self):
		for title, website in config.NEWS_WEBSITES.items():
			self.websites.append(Website(
				title=title,
				url=website['url'],
				type=website['type']))

	def getNewsString(self):
		self.resume = " ".join((
			self.lemonde.echo(bprint=False),
			self.nicematin.echo(bprint=False)))

		return self.resume

	def printNews(self):
		for website in self.websites:
			website.echo()

	def play(self):
		for website in self.websites:
			website.play()
			Player().wait(2)

	def getData(self):
		data = {}

		for website in self.websites:
			data[website.title] = website.getData()

		return data

class Website:
	"""docstring for Website"""
	def __init__(self, url, title, type):
		self.url = url
		self.news = list()
		self.title = title
		self.type = type

		self.loadRSS()
		self.loadNews()

		self.player = Player()

	def loadRSS(self):
		self.rss = feedparser.parse(self.url)

	def getNews(self):
		print (self.rss)

	def echo(self, bprint=True):
		head_str = self.getHeadStr()

		if bprint is True:
			print ("-- {}".format(head_str))

		total_str = head_str
		i = 0
		while i < len(self.news) and i < config.NEWS_RESUME_LEN:
			total_str += ".\n" + self.news[i]['title']
			if bprint is True:
				print (self.news[i]['title'])
				print ('\t{}'.format(self.news[i]['summary']))
			i += 1

		if bprint is True:
			print ("")

		return total_str

	def getData(self):
		data = {
			'head_str': self.getHeadStr(),
			'content': list()
		}

		for i, news in enumerate(self.news):
			if i == config.NEWS_RESUME_LEN:
				break

			data['content'].append({
				'title': news['title'],
				'summary': news['summary'],
				'link': news['link'],
				'picture': news['picture'],
			})

		return data

	def getHeadStr(self):
		return "Résumé des actualités {} avec {}.".format(
			config.NEWS_TYPE[self.type.lower()],
			self.title)


	def loadNews(self):
		entries = self.rss['entries']
		for entry in entries:
			self.news.append({
				'title': entry['title'],
				'summary': entry['summary'],
				'picture': self.getPicture(entry['links']),
				'link': entry['link']})

	def getPicture(self, links):
		for link in links:
			if 'image' in link['type'].split('/'):
				return link['href']

		# TODO : Default picture here
		return None

	def play(self):
		self.player.play("Résumé des actualités publiés par {}".format(self.title))
		self.player.wait(1)

		for i, news in enumerate(self.news):
			if i == config.NEWS_RESUME_LEN:
				break

			self.player.play("{title} [SLEEP 0.2] {summary}".format(
				title=news['title'],
				summary=news['summary']))
