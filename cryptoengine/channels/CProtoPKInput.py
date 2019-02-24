#!/usr/bin/python
from CProtoInput import *

class CProtoPKEncryptInput(CProtoInput):
	def __init__(self, prototype, keyattr = None):
		CProtoInput.__init__(self, prototype)
		self.keyattr = keyattr

	def _get_key(self):
		return getattr(self.obj, self.keyattr)
