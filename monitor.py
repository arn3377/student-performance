import psutil
import requests

# CPU Usage
cpu = psutil.cpu_percent(interval=1)

# RAM Usage
memory = psutil.virtual_memory().percent

print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory}%")

# Flask App Health Check
try:
    response = requests.get("http://127.0.0.1:5000")

    if response.status_code == 200:
        print("Flask App Status: RUNNING")
    else:
        print("Flask App Status: ERROR")

except:
    print("Flask App Status: NOT RUNNING")