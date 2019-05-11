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
	

	while keyState is False: # Loop until a key is pressed
		
		if key.is_pressed("F2"):
			form = tk.Tk()
			host = form.clipboard_get() # Pulls what's on the clipboard.
			keyState = True # Break the loop
			scanType = "scanType1" #Define your scan types using these variables. Name them something good, so you know what they do.
			qualysSubmit(host, scanType) # Host is defined by what data is pulled from the clipboard. Currently, it isn't verified.
		
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
	toaster = ToastNotifier() # Instantiates the toast notifications for Winders 10.
	
	qualysAPI = "https://qualysapi.qg3.apps.qualys.com/api/2.0/fo/scan/" # The standard API string for Qualys VM API.
	
	if scanType == 'scanType1':
		template = '0000000' # This is the ID of the Options Template you're using. It can be found in the Qualys UI.
		scanner = 'scanner1' # The ID/Serial of the scanner. Use Serial unless using the external scanner.
		
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

		data = { # Self-explanatory. All these fields are required per the API guide, so it fills them in as DATA for the POST.
		'action': 'launch',
		'scan_title': 'QualysSubmitter_Scan ' + currentDate,
		'ip': host,
		'option_id': template,
		'iscanner_name': scanner		
		}

		response = requests.post(qualysAPI, headers=headers, data=data, auth=('QUALYS_USERNAME', 'QUALYS_PASSWORD')) # If you have a non-2FA svc account, this is the place to enter it.
		if str(response) == '<Response [200]>':
			toaster.show_toast("Qualys Rescan Submitted", "Scan submitted for " + host)
	except:
		print("Could not submit scan via API.") # Catch network, API exceptions.
			
	keyState = False
	main(keyState) #Set the key pressed state back to false, return to the loop.
		
if __name__ == '__main__':
	main(keyState)
