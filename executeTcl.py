import os


def executeTcl(dirction, file):
	os.chdir(
		"C:\Program Files (x86)\IxVeriWave\WaveAutomate\\automation_6.9.1-113_2016.10.13.05-admin_windows\\automation\\bin")
	print "Start Running"
	os.system('tclsh vw_auto.tcl -f ../conf/wf802/{0}/{1}'.format(dirction, file))
	print 'Running OK!'

if __name__ == "__main__":
	executeTcl('2.2', '2.2_TX.tcl')
