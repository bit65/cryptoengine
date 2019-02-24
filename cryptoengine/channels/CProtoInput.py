#!/usr/bin/python

class CProtoInput:
	def __init__(self, prototype):
		self.prototype = prototype

	def input(self, input):
		if isinstance(input, self.prototype):
			self.obj
		else:
			self.obj = self.prototype.FromString(input)

		return self
