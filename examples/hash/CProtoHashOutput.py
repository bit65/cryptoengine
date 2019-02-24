#!/usr/bin/python
import cryptoengine
import hash_pb2

class CProtoHashOutput(cryptoengine.CProtoOutput):
	def __init__(self):
		cryptoengine.CProtoOutput.__init__(self, hash_pb2.Hash)

	def _set(self, data):
		self.obj.hash = data
