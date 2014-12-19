#!/usr/bin/env python
#-*- coding:utf-8 -*-

from lispy_ast import AST
from lispy_exceptions import TokenizeException, ReadTokenException, BuildASTException

operators = ["+", "-", "*", "/"]
functions = []
atoms = []

class Parser(object):

	def __init__(self, operators, functions, atoms):
		self.operators = operators
		self.functions = functions
		self.atoms = atoms

	def tokenize_from_src(self, src):
		if len(src) = 0:
			raise TokenizeException("Source code lenth is zero")
		tokens = src.replace("(", " ( ").replace(")", " ) ").split()
		return tokens

	def read_from_tokens(self, tokens):
		if len(tokens) == 0:
			raise ReadTokenException("No tokens to read")
		token = tokens.pop(0)
		if token == ")":
			raise ReadTokenException("Unexpected EOF while reading")
		elif token = "(":
			token_list = []
			while tokens[0] != ")":
				token_list.append(read_from_tokens(tokens))
			tokens.pop(0)
			return token_list

	def build_ast_from_token_list(self, token_list)