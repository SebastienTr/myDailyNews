#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import hug


@hug.get('/')
def index(name='Toto', age:hug.types.number=1):
    """Says happy birthday to a user"""
    return "Happy {age} Birthday {name}!".format(**locals())
