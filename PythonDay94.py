# Exercise 11: Final Exercise
# Drink Water reminder

# Write a python program that reminds you to drink water every hour. The program should show a windows popup
# notification with an error sound, and the user can then click on an "okay" button to proceed ahead.
# The user can also quit the reminder anytime by typing "Quit" in the terminal

import ctypes
import threading
import time

MB_OK = 0x0
MB_ICONERROR = 0x10

def show_reminder():
    ctypes.windll.user32.MessageBoxW(
        0,
        "Time to drink some water!",
        "Water Reminder",
        MB_OK | MB_ICONERROR
    )

def reminder_loop(stop_event, interval_seconds):
    while not stop_event.is_set():
        stop_event.wait(interval_seconds)   # waits, but exits early if stop_event gets set
        if not stop_event.is_set():
            show_reminder()

def main():
    stop_event = threading.Event()
    interval_seconds = 60 * 60   # 1 hour

    reminder_thread = threading.Thread(
        target=reminder_loop,
        args=(stop_event, interval_seconds),
        daemon=True
    )
    reminder_thread.start()

    print("Water reminder started. Type 'Quit' anytime to stop.")
    while True:
        user_input = input().strip().lower()
        if user_input == "quit":
            print("Stopping reminders. Stay hydrated!")
            stop_event.set()
            break

main()