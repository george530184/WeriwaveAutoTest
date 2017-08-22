'''
init system ,write channel,version,ssid,password,bssid ,apmode to tcl file
'''
import re

FILE = 'C:\Program Files (x86)\IxVeriWave\WaveAutomate\\automation_6.9.1-113_2016.10.13.05-admin_windows\\automation\conf\wf802\\'


def changeTclArgument(dirction, file, channel, version, apmode, ssid, pwd, dirs):
	File = FILE + dirction + '\\' + file
	f = open(File, 'r+')
	tmp = f.read()
	channel_wave = re.findall(r'keylset global_config Channel+.*', tmp)[0].strip()
	channel_device = re.findall(r'802_11ac.Channel+.*', tmp)[1].strip()
	Version = re.findall(r'APSWVersion+.*', tmp)[0].strip()
	ApMode = re.findall(r'APModel+.*', tmp)[0].strip()
	SSID = re.findall(r'Ssid+.*', tmp)[0].strip()
	PWD = re.findall(r'PskAscii+.*', tmp)[0].strip()
	logdir = re.findall(r'LogsDir+.*',tmp)[0].strip()
	f.close()
	# Change Wave's Channel of global setting
	with open(File, 'r+') as  fs_wave:
		line_wave = fs_wave.readlines()
		fs_wave.seek(0, 0)
		for line in line_wave:
			newline_wave = line.replace(channel_wave, 'keylset global_config Channel {0}'.format(channel))
			fs_wave.write(newline_wave)
	fs_wave.close()
	# Change Wave's Channel of group
	with open(File, 'r+') as  fs_device:
		line_device = fs_device.readlines()
		fs_device.seek(0, 0)
		for line in line_device:
			newline_device = line.replace(channel_device, '802_11ac.Channel {0}'.format(channel))
			fs_device.write(newline_device)
	fs_device.close()
	# version	
	with open(File, 'r+') as  fs_version:
		line_version = fs_version.readlines()
		fs_version.seek(0, 0)
		for line in line_version:
			new_version = line.replace(Version, 'APSWVersion {0}'.format(version))
			fs_version.write(new_version)
	fs_version.close()
	# apmode
	with open(File, 'r+') as  fs_apmode:
		line_apmode = fs_apmode.readlines()
		fs_apmode.seek(0, 0)
		for line in line_apmode:
			new_apmode = line.replace(ApMode, 'APModel {0}'.format(apmode))
			fs_apmode.write(new_apmode)
	fs_apmode.close()
	# ssid
	with open(File, 'r+') as fs_ssid:
		line_ssid = fs_ssid.readlines()
		fs_ssid.seek(0, 0)
		for line in line_ssid:
			new_ssid = line.replace(SSID, 'Ssid {0}'.format(ssid))
			fs_ssid.write(new_ssid)
	fs_ssid.close()
	# pwd
	with open(File, 'r+') as fs_pwd:
		line_pwd = fs_pwd.readlines()
		fs_pwd.seek(0, 0)
		for line in line_pwd:
			new_pwd = line.replace(PWD, 'PskAscii {0}'.format(pwd))
			fs_pwd.write(new_pwd)
	fs_pwd.close()
	# dir
	with open(File, 'r+') as fs_dir:
		line_dir = fs_dir.readlines()
		fs_dir.seek(0, 0)
		for line in line_dir:
			new_dir = line.replace(logdir,'LogsDir {0}'.format(dirs))
			fs_dir.write(new_dir)
	fs_dir.close()

if __name__ == "__main__":
	changeTclArgument('2.2', '2.2_TX.tcl', '152', 'R3.1.00.B037', 'WF-802W', 'hellokitty', '0987654321','D:\Performance\\2.2\CH36_TX')
