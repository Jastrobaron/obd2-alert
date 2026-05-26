import obd
import requests
from dotenv import load_dotenv
import os
import sys

"""Value to be watched"""
VALUE_TO_WATCH = obd.commands.RPM
"""Threshold that will trigger the message"""
VALUE_THRESHOLD = 1500.0

"""HTTP Request payload"""
REQ = {
        "auth_key": os.getenv("API_KEY"),   # API key
        "user_id": os.getenv("USER_ID"),    # Discord user ID (available through developer settings)
        "message": os.getenv("MESSAGE")     # message to be sent
    }

def on_update(s):
    """Callback function to be called when the observed value updates"""
    if s.value is None:
        print("Error: value is None")
        return
    rpm = s.value.magnitude
    if rpm > VALUE_THRESHOLD:
        requests.post(os.getenv("URL"), json=REQ)


def main():
    """Application main entry point"""
    load_dotenv()
    obd.logger.setLevel(obd.logging.DEBUG)
    if not obd.scan_serial():
        print("No serial devices found!")
        sys.exit(1)
    conn = obd.Async(fast=False)
    conn.watch(VALUE_TO_WATCH, callback=on_update)
    conn.start()
    input("Press ENTER to stop")
    conn.stop()
    conn.unwatch_all()

if __name__ == "__main__":
    main()
