#/usr/bin/env python3

import tkinter as tk
import keyboard as key
import requests
from datetime import *
from win10toast import ToastNotifier


keyState = False

def main(keyState):
	
	scanType = ''
	headers = ''
	scanner = ''
	data = ''
	

	while keyState is False:
		
		if key.is_pressed("F2"):
			form = tk.Tk()
			host = form.clipboard_get()
			keyState = True
			scanType = "scanType1"
			qualysSubmit(host, scanType)
		
		elif key.is_pressed("F3"):
			form = tk.Tk()
			host = form.clipboard_get()
			keyState = True
			scanType = "scanType2"
			qualysSubmit(host, scanType)
	
		elif key.is_pressed("F4"):
			form = tk.Tk()
			host = form.clipboard_get()
			keyState = True
			scanType = "scanType3"
			qualysSubmit(host, scanType)
			
		elif key.is_pressed("F5"):
			form = tk.Tk()
			host = form.clipboard_get()
			keyState = True
			scanType = "scanType4"
			qualysSubmit(host, scanType)
			
		elif key.is_pressed("F6"):
			form = tk.Tk()
			host = form.clipboard_get()
			keyState = True
			scanType = "scanType5"
		
		
def qualysSubmit(host, scanType):
	
	currentDate = now.strftime("%m-%d-%Y")
	toaster = ToastNotifier()
	
	qualysAPI = "https://qualysapi.qg3.apps.qualys.com/api/2.0/fo/scan/"
	
	if scanType == 'scanType1':
		template = '0000000'
		scanner = 'scanner1'
		
	elif scanType == 'scanType2':
		template = '0000000'
		scanner = 'scanner2'
		
	elif scanType == 'scanType3':
		template = '0000000'
		scanner = 'scanner3'
		
	elif scantype == 'scanType4':
		template = '0000000'
		scanner = 'scanner4'
		
	elif scanType == 'scanType5':
		template = '0000000'
		scanner = 'External'
		
	
	try:
		headers = {
		'X-Requested-With': 'QualysSubmitter',
		}

		data = {
		'action': 'launch',
		'scan_title': 'QualysSubmitter_Scan ' + currentDate,
		'ip': host,
		'option_id': template,
		'iscanner_name': scanner		
		}

		response = requests.post(qualysAPI, headers=headers, data=data, auth=('QUALYS_USERNAME', 'QUALYS_PASSWORD'))
		if str(response) == '<Response [200]>':
			toaster.show_toast("Qualys Rescan Submitted", "Scan submitted for " + host)
	except:
		print("Could not submit scan via API.")
			
	keyState = False
	main(keyState)
		
if __name__ == '__main__':
	main(keyState)
