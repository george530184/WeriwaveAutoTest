import serial
import os
import time
import telnetlib
from ssdp import *

ipaddr = ssdp_discovery()
username = 'root'
password = 'admin'

'''
def configDevice(channel):
	com = os.popen('python -m serial.tools.list_ports').read().strip()
	ser = serial.Serial(
		port=com,
		baudrate=115200,
		bytesize=serial.EIGHTBITS,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		timeout=1,
		xonxoff=False,
		rtscts=False,
		dsrdtr=False
	)
	try:
		ser.close()
		ser.open()
	except Exception, e:
		print "error open serial port: " + str(e)
		exit()
	if ser.isOpen():
		ser.flushInput()
		ser.flushOutput()
		ser.write("x\n")
		ser.write("x\n")
		ser.write("\n")
		ser.write("enable\n")
		ser.write("s/s\n")
		ser.write("iwconfig ath10 channel {0} \n".format(channel))
		ser.close()
	'''


def configDevice(channel):
	'''
	Set channel  by telnetlib
	:param channel:
	:return:
	'''
	tn = telnetlib.Telnet(host=ipaddr, port=23, timeout=10)
	tn.set_debuglevel(2)
	tn.read_until('Login as:'.encode('utf-8'))
	tn.write(username.encode('ascii') + b'\n')
	tn.read_until('Password:'.encode('utf-8'))
	tn.write(password.encode('ascii') + b'\n')
	tn.read_until('AP>'.encode('utf-8'))
	tn.write('enable \n'.encode('ascii'))
	tn.read_until('#AP>'.encode('utf-8'))
	tn.write('system/wifi \n'.encode('ascii'))
	tn.read_until('#AP/system/wifi>'.encode('utf-8'))
	tn.write('son disable test_perf 12345678 1 {0} \n'.format(channel).encode('ascii'))
	time.sleep(2)
	tn.read_until('#AP/system/wifi>'.encode('utf-8'))
	tn.close()

if __name__ == "__main__":
	configDevice(52)
