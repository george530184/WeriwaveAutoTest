import os
import shutil
import time


def setUpDo():
	# install license
	# os.chdir('C:\Program Files (x86)\IxVeriWave\WaveAutomate\\automation_6.9.1-113_2016.10.13.05-admin_windows\\automation\\bin')
	# os.system('tclsh vw_auto.tcl -al 10.2.4.110 \n')
	# time.sleep(1)
	# check
	perf = os.path.exists('D:\Performance')
	if perf is False:
		shutil.copytree('D:\\backup\Performance', 'D:\Performance\\')
	else:
		pass
