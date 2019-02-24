#!/usr/bin/python

import cryptoengine
import rsa_pb2

class CProtoRSAPublicInput(cryptoengine.CProtoPKEncryptInput):
	def __init__(self):
		cryptoengine.CProtoPKEncryptInput.__init__(self, rsa_pb2.Message, "public")

	def _get(self):
		return self.obj.data
