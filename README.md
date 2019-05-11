# QualysSubmitter

This is a simple Python event listener that listens for hotkey-presses (customizable), and grabs whatever data is on the clipboard (IP Address), and submits it to the Qualys API for a scan.

Please note that you can alter the hotkey's actions to use whatever Options Template you would like, as well as whatever scanner, and you can add many more hot keys to the loop. It's extensible and customizable within the bounds of what the API can do, and can be adapted for other calls as well.

Written for Windows using Python 3.7

Installation:

Using PyInstaller, compile the script to an executable once you've finished customization.

`C:\Python37\scripts\> pyinstaller --onefile ../QualysSubmitter.py`

Utilizing the Windows Command line, install the executable as a service to run automatically on startup with a delay.

`C:\windows\system32\>sc create QualysSubmitter binpath="C:\PathTo\Compliled.exe" start=delayed-auto displayname="Qualys Hotkey Service"`

Upon the service being created and starting, you should now be able to make calls to the Qualys API based on whatever IP you currently have in the clipboard.


Soon (after the weekend): 

Verify clipboard data w/ regex before attempting submission
Add Win10 Toast notifier when submission fails.
