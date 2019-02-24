#!/usr/bin/python

import cryptoengine
import hash_pb2

class CProtoHashInput(cryptoengine.CProtoInput):
	def __init__(self):
		cryptoengine.CProtoInput.__init__(self, hash_pb2.Message)

	def _get(self):
		return self.obj.data
