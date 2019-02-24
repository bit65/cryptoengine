#!/usr/bin/python
import cryptoengine
import rsa_pb2

class CProtoRSAEncryptOutput(cryptoengine.CProtoOutput):
	def __init__(self):
		cryptoengine.CProtoOutput.__init__(self, rsa_pb2.EncryptedMessage)

	def _set(self, data):
		self.obj.cipher = data
