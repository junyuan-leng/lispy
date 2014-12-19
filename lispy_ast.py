#!/usr/bin/env python
#-*- coding:utf-8 -*-

class AST(object):
	
	def __init__(self, leftOperand=None, rightOperand=None, operator=None):
		if operator == None:
			self = None
		else:
			self.leftOperand = leftNode
			self.rightOperand = rightNode
			self.operator = operator

	def pre_order_traverse(self):
		if self.operator == None:
			return
		print self.operator
		self.pre_order_traverse(self.leftOperand)
		self.pre_order_traverse(self.rightOperand)

	def in_order_traverse(self):
		if self.operator == None:
			return
		self.in_order_traverse(self.leftOperand)
		print self.operator
		self.in_order_traverse(self.rightOperand)

	def post_order_traverse(self):
		if self.operator == None:
			return
		self.post_order_traverse(self.leftOperand)
		self.post_order_traverse(self.rightOperand)
		print self.operator

	def show(self):
