#!/usr/bin/python

import cryptoengine
from CProtoRSAInput import *
from CProtoRSAOutput import *
import rsa_pb2

from Crypto.PublicKey import RSA

m = rsa_pb2.Message()
m.data = "Hello, world!"
m.public = RSA.generate(2048).publickey().exportKey('DER')

input = CProtoRSAPublicInput().input(m.SerializeToString())
print cryptoengine.RSAEncrypt(input, CProtoRSAEncryptOutput()).calc().output.output()
