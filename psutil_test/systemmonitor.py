REQUIREMENTS = ['psutil==5.1.3']
import psutil
print("Disk usage:" + str(psutil.disk_usage('/').percent) +" %")
print("Memory usage:" + str(psutil.virtual_memory().percent) + " %")
print("CPU usage:" + str(psutil.cpu_percent(interval=None)) + " %")
