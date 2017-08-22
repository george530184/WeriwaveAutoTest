import serial
import os
import re
import time
import telnetlib
from ssdp import *

mesg = []
ipaddr = ssdp_discovery()
username = 'root'
passwordd = 'admin'

'''
get message form ap ,include: apmode ,version ,ssid, password, bassid, channel
'''

'''
def getMessage():
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
		ser.write("cat /tmp/ath10.conf\n")
		tmp_ath10 = ser.read(512)
		ssid = re.findall(r'ssid=*.+', tmp_ath10)[0][5:].strip()
		password = re.findall(r'wpa_passphrase=*.+', tmp_ath10)[0][15:].strip()
		ser.write("iwconfig ath10 \n")
		tmp_bssid = ser.read(600)
		bssid = re.findall(r'Point:*.+', tmp_bssid)[0][7:].strip()
		ser.write("iwlist ath10 channel \n")
		tmp_channel = ser.read(860)
		channel = re.findall(r'Channel*.+', re.findall(r'Current*.+', tmp_channel)[0])[0][8:].strip()[:-1]
		ser.write('cat /tmp/sys2.cfg \n')
		tmp_apmode = ser.read(512)
		apmode = re.findall(r'EepEqProductName=*.+', tmp_apmode)[0][17:].strip()
		ser.write("x\n")
		ser.write("ver \n")
		tmp_version = ser.read(64)
		version = re.findall(r'OntSwVer*.+', tmp_version)[0][12:].strip()
		mesg.append(version)
		mesg.append(apmode)
		mesg.append(bssid)
		mesg.append(ssid)
		mesg.append(password)
		mesg.append(channel)
		ser.close()
		print mesg
		return mesg
'''


def getMessage():
	'''
	Get message by telnetlib
	:return:
	'''
	tn = telnetlib.Telnet(host=ipaddr, port=23, timeout=10)
	tn.set_debuglevel(2)
	tn.read_until('Login as:'.encode('utf-8'))
	tn.write(username.encode('ascii') + b'\n')
	tn.read_until('Password:'.encode('utf-8'))
	tn.write(passwordd.encode('ascii') + b'\n')
	tn.read_until('AP>'.encode('utf-8'))
	tn.write('enable \n'.encode('ascii'))
	tn.read_until('#AP>'.encode('utf-8'))
	tn.write('system/shell \n'.encode('ascii'))
	tn.read_until('#AP/system/shell>'.encode('utf-8'))
	tn.write('cat /tmp/ath10.conf \n'.encode('ascii'))
	time.sleep(1)
	tmp_ath10 = tn.read_very_eager()
	ssid = re.findall(r'ssid=*.+', tmp_ath10)[0][5:].strip()
	password = re.findall(r'wpa_passphrase=*.+', tmp_ath10)[0][15:].strip()
	tn.write('iwconfig ath10 \n'.encode('ascii'))
	time.sleep(1)
	tmp_bssid = tn.read_very_eager()
	bssid = re.findall(r'Point:*.+', tmp_bssid)[0][7:].strip()
	tn.write('iwlist ath10 channel \n'.encode('ascii'))
	time.sleep(1)
	tmp_channel = tn.read_very_eager()
	channel = re.findall(r'Channel*.+', re.findall(r'Current*.+', tmp_channel)[0])[0][8:].strip()[:-1]
	tn.write('cat /tmp/sys2.cfg \n'.encode('ascii'))
	time.sleep(1)
	tmp_apmode = tn.read_very_eager()
	apmode = re.findall(r'EepEqProductName=*.+', tmp_apmode)[0][17:].strip()
	tn.write("x \n".encode('ascii'))
	tn.read_until('#AP/system>'.encode('utf-8'))
	tn.write("ver \n".encode('ascii'))
	time.sleep(1)
	tmp_version = tn.read_very_eager()
	version = re.findall(r'OntSwVer*.+', tmp_version)[0][12:].strip()
	mesg.append(version)
	mesg.append(apmode)
	mesg.append(bssid)
	mesg.append(ssid)
	mesg.append(password)
	mesg.append(channel)
	tn.close()
	print mesg
	return mesg


if __name__ == "__main__":
	getMessage()
