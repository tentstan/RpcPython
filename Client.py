#! /usr/bin/python
#-*- coding:utf-8 -*-
#author:tentstan
#email:hailin8818@126.com
#version:1.0.0

import json
import time
import struct
import socket

def rpc(sock,in_,params):
	response = json.dumps({"in":in_,"params:"params})
	length_prefix = struct.pack("I",len(response))
	sock.sendall(length_prefix)
	sock.sendall(response)
	length_prefix = sock.recv(4)
	length, = struct.unpack("I",length_prefix)
	body = sock.recv(length)
	response = json.loads(body)
	return response["out"],response["result"]

if __name__ == '__main__':
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(("localhost",8080))
	for i in range(10):
		out,result = rpc(s,"ping","ireader %d" % (i))
		print out,result
		time.sleep(1)

	s.close()
