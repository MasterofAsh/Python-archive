#Exercise 9
# Shoutout to everyone
"""
Write a program to pronounce list of names using win32 API
If you are given a list 'l' as follows:
l = ["Rahul", "Nishant", "Harry"]

Your program should pronounce:
Shoutout to Rahul
Shoutout to Nishant
Shoutout to Harry

"""

import win32com.client

def pronounce_names(names):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    for name in names:
        message = f"Shoutout to {name}"
        print(message)
        speaker.Speak(message)

l = ["Rahul", "Nishant", "Harry"]
pronounce_names(l)