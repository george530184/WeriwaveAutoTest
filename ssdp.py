# -*- coding: utf-8 -*-
__author__ = 'Jerry'

"""
SSDP Discovery
"""

import socket

SSDP_S = 'uuid:ijklmnop-7dec-11d0-a765-00a0c91e6bf6'
SSDP_ADDR = "239.255.255.250"
SSDP_PORT = 1900
SSDP_MX = 1
SSDP_ST = "CIG:CAP"


def ssdp_discovery():
	'''
	SSDP Discovery ,TO get IP address of Server
	:return: IPaddress
	'''

	ssdpRequest = ("M-SEARCH * HTTP/1.1\r\n" + \
				   "S: %s\r\n" % (SSDP_S) + \
				   "HOST: %s:%d\r\n" % (SSDP_ADDR, SSDP_PORT) + \
				   "MAN: \"ssdp:discover\"\r\n" + \
				   "ST: %s\r\n" % (SSDP_ST) + "\r\n" + \
				   "MX: %d\r\n" % (SSDP_MX)).encode(encoding='utf-8')

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(ssdpRequest, (SSDP_ADDR, SSDP_PORT))
	try:
		data, addr = sock.recvfrom(65535)
		# print addr[0]
		return addr[0]

	except socket.timeout:
		print('Discovery Time Out!')


if __name__ == '__main__':
	ssdp_discovery()
