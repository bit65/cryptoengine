#!/usr/bin/python

import cryptoengine
from CProtoHashInput import *
from CProtoHashOutput import *
import hash_pb2

m = hash_pb2.Message()
m.data = "Hello, world!"
m.public = "\x00" * 64

input = CProtoHashInput().input(m.SerializeToString())
print cryptoengine.SHA256Engine(input, CProtoHashOutput()).calc().output.output()
