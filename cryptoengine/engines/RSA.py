#!/usr/bin/python

from Crypto.PublicKey import RSA
import CEngine

class RSAEncrypt(CEngine.CEngine):
	def __init__(self, input, output):
		CEngine.CEngine.__init__(self, input, output)

		self.rsa = RSA.importKey(input._get_key())

	def calc(self):
		self.output._set(self.rsa.encrypt(self.input._get(), "")[0])
		return self
