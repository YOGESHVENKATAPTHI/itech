#!/usr/bin/env python3
"""
Simple ping script to keep Render free instance alive.
Run this locally or on a VPS/cron job to ping the server every 9 seconds.
"""

import time
import requests
import os
from datetime import datetime

# Replace with your deployed Render URL
SERVER_URL = os.getenv("SERVER_URL", "https://your-sast-app.onrender.com")

def ping_server():
    try:
        response = requests.get(f"{SERVER_URL}/health", timeout=5)
        if response.status_code == 200:
            print(f"[{datetime.now()}] Ping successful - Server is awake")
        else:
            print(f"[{datetime.now()}] Ping failed - Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[{datetime.now()}] Ping failed - Error: {e}")

if __name__ == "__main__":
    print(f"Starting ping service for {SERVER_URL}")
    print("Press Ctrl+C to stop")

    try:
        while True:
            ping_server()
            time.sleep(9)  # Ping every 9 seconds
    except KeyboardInterrupt:
        print("\nPing service stopped")