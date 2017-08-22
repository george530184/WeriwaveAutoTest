# -*- coding: utf-8 -*-
import win32com.client
import pythoncom
import os
import csv
import Serials.getMessage



def writeDateToExcel(dirction, files):
	PATH = 'D:\Performance\{0}\{1}'.format(dirction, files)
	os.chdir(PATH)
	items =os.listdir(PATH)
	os.chdir(items[len(items)-1])



	# Throughput
	with open('Results_unicast_throughput.csv', 'rb') as f:
		reader = csv.reader(f)
		column = [row for row in reader][-1][7]
		result = int(float(column) / 1000000)
	f.close()
	# write to excel
	pythoncom.CoInitialize()
	WMI = win32com.client.GetObject('winmgmts:')
	processCodeCov = WMI.ExecQuery('select * from Win32_Process where name="EXCEL.EXE"')
	if len(processCodeCov)>0:
		os.system('TASKKILL /F /IM EXCEL.EXE')
	else:
		pass
	os.chdir('D:\Performance\\')
	pathlistd = os.listdir('D:\Performance\\')
	for named in pathlistd:
		filepathd = os.path.join('D:\Performance\\', named)
		if os.path.isdir(filepathd):
			pass
		else:
			if os.path.splitext(named)[1] == ".xlsx":
				pythoncom.CoInitialize()
				winapp = win32com.client.DispatchEx('Excel.Application')
				winbook = winapp.Workbooks.Open(r'D:\Performance\\' + named)
				winsheet = winbook.Worksheets(dirction)
				if dirction == '2.2':
					if files == "CH36_TX":
						winsheet.Range('G9').FormulaR1C1 = result
						# BSSID
						winsheet.Range('H9').FormulaR1C1 = Serials.getMessage.getMessage()[2]
						# SSID
						winsheet.Range('I9').FormulaR1C1 = Serials.getMessage.getMessage()[3]
					elif files == "CH36_RX":
						winsheet.Range('G10').FormulaR1C1 = result
					elif files == "CH52_TX":
						winsheet.Range('G11').FormulaR1C1 = result
					elif files == "CH52_RX":
						winsheet.Range('G12').FormulaR1C1 = result
					elif files == "CH100_TX":
						winsheet.Range('G13').FormulaR1C1 = result
					elif files == "CH100_RX":
						winsheet.Range('G14').FormulaR1C1 = result
					elif files == "CH132_TX":
						winsheet.Range('G15').FormulaR1C1 = result
					elif files == "CH132_RX":
						winsheet.Range('G16').FormulaR1C1 = result
					elif files == "CH149_TX":
						winsheet.Range('G17').FormulaR1C1 = result
					elif files == "CH149_RX":
						winsheet.Range('G18').FormulaR1C1 = result

				winbook.Save()
				winbook.Close(SaveChanges=0)





if __name__ == "__main__":
	writeDateToExcel('2.2', 'CH36_TX')
'''
#dirction subdirction
2.2     CH36_TX,CH36_RX,CH52_TX,CH52_RX,CH100_TX,CH100_RX,CH132_TX,CH132_RX,CH149_TX,CH149_RX
2.3     C23_TX,C23_RX
2.4     CH36_64_TX,CH36_64_RX,CH36_88_TX,CH36_88_RX,CH36_128_TX,CH36_128_RX,CH36_256_TX,CH36_256_RX
		CH36_512_TX,CH36_512_RX,CH36_1024_TX,CH36_1024_RX,CH36_1280_TX,CH36_1280_RX,CH36_1518_TX,CH36_1518_RX
2.7     CH36_1_TX,CH36_1_RX,CH36_4_TX,CH36_4_RX,CH36_10_TX,CH36_10_RX
		CH52_1_TX,CH52_1_RX,CH52_4_TX,CH52_4_RX,CH52_10_TX,CH52_10_RX
		CH100_1_TX,CH100_1_RX,CH100_4_TX,CH100_4_RX,CH100_10_TX,CH100_10_RX
		CH132_1_TX,CH132_1_RX,CH132_4_TX,CH132_4_RX,CH132_10_TX,CH132_10_RX
		CH149_1_TX,CH149_1_RX,CH149_4_TX,CH149_4_RX,CH149_10_TX,CH149_10_RX
2.8     C28_1_TX,C28_1_RX,C28_4_TX,C28_4_RX,C28_10_TX,C28_10_RX
2.9     CH36_536_1_TX,CH36_536_1_RX,CH36_1460_1_TX,CH36_1460_1_RX
		CH36_536_4_TX,CH36_536_4_RX,CH36_1460_4_TX,CH36_1460_4_RX
		CH36_536_10_TX,CH36_536_10_RX,CH36_1460_10_TX,CH36_1460_10_RX
2.14    CH36_14_TX,CH36_14_RX,CH52_14_TX,CH52_14_RX
2.15    C15
2.17    C17
2.19    CH36_19_512,CH36_19_1518
'''
