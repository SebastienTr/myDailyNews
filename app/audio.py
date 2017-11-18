#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import parse
import config
import subprocess


class Player:
    class __Player:
        def __init__(self):
            self.os = sys.platform
            self.lang = config.LANGUAGE_VOICE

        def __str__(self):
            return repr(self) + self.val

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

    instance = None

    def __init__(self):
        if not Player.instance:
            Player.instance = Player.__Player()

    def __getattr__(self, name):
        return getattr(self.instance, name)
