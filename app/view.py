#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import parse
import config
import random

from jinja2 import Template

class View:
    class __View:
        def __init__(self):
            self.os = sys.platform
            self.destination = config.OUTPUT_VIEW_PATH

        def __str__(self):
            return repr(self) + self.val

        def render(self, data={}):
            f = open('app/view/view.html.twig', 'r')

            template = Template(f.read())
            view = template.render(
                name='John Doe',
                random_background=self.getRandom(),
                weather=data['weather'],
                news=data['news'])

            print (data['weather'])
            print ('')
            print (data['news'])
            print ('')
            # print (data['news']['Nice Matin'])

            with open(self.destination, "w") as fh:
                fh.write(str(view))

        def getRandom(self):
            number = random.randint(1, 12)
            return '{:02}'.format(14)

    instance = None

    def __init__(self):
        if not View.instance:
            View.instance = View.__View()

    def __getattr__(self, name):
        return getattr(self.instance, name)
