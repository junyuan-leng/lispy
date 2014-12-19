#!/usr/bin/env python
#-*- coding:utf-8 -*-

class TokenizeException(Exception):

	def __init__(self, message):
		Exception.__init__(self)
		self.message = message

	def __str__(self):
		return repr(self.message)

class ReadTokenException(Exception):

	def __init__(self, message):
		Exception.__init__(self)
		self.message = message

	def __str__(self):
		return repr(self.message)

class BuildASTException(Exception):

	def __init__(self, message):
		Exception.__init__(self)
		self.message = message

	def __str__(self):
		return repr(self.message)