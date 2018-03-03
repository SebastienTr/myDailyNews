#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class MDNRender():
	"""docstring for MDNRender"""
	_instance = None
	def __new__(self, *args, **kwargs):
			if not self._instance:
					self._instance = super(MDNRender, self).__new__(self, *args, **kwargs)
			return self._instance

	def __init__(self):
		pass

class Player(MDNRender):
    def play(self, sentance):
        try:
            sentances = parse.parse("{} [SLEEP {}] {}", sentance)
        except:
            sentances = None

        if sentances is not None:
            still = True
            while (still):
                s1 = sentances[0]
                wait = float(sentances[1])
                s2 = sentances[2]

                self._play(s1)
                self.wait(wait)

                try:
                    sentances = parse.parse("{} [SLEEP {}] {}", s2)
                except:
                    sentances = None

                if sentances is None:
                    self._play(s2)
                    still = False

        else:
            self._play(sentance)

    def _play(self, sentance):
        print ("play sentance : %s" % sentance)

        if self.os == "darwin":
            subprocess.call(["say", "-v", self.lang, sentance])

    @staticmethod
    def wait(sec):
        # print ("Wait %f sec" % sec)
        time.sleep(sec)