#!/usr/bin/python
import COutput

class CProtoOutput(COutput.COutput):
	def __init__(self, prototype):
		self.obj = prototype()

	def output(self, serialize = True):
		if serialize:
			return self.obj.SerializeToString()
		return self.obj
