#!/usr/bin/python

import hashlib
import CEngine

class SHA256Engine(CEngine.CEngine):
	def __init__(self, input, output):
		CEngine.CEngine.__init__(self, input, output)

		self.h = hashlib.sha256()

	def calc(self):
		self.h.update(self.input._get())
		self.output._set(self.h.digest())
		return self
