import os
import psutil
import datetime


def system_health():
    current_time = datetime.datetime.now()
    formatted_datetime = current_time.strftime("%A, %B %d, %Y @%H:%M")

    cpu = psutil.cpu_percent(interval=1)

    memory_total = psutil.virtual_memory().total / (1024 ** 3)
    memory_used = psutil.virtual_memory().used / (1024 ** 3)
    memory_percent = psutil.virtual_memory().percent

    swap_total = psutil.swap_memory().total / (1024 ** 3)
    swap_used = psutil.swap_memory().used / (1024 ** 3)
    swap_percent = psutil.swap_memory().percent

    disk_total = psutil.disk_usage('/').total / (1024 ** 3)
    disk_used = psutil.disk_usage('/').used / (1024 ** 3)
    disk_percent = psutil.disk_usage('/').percent

    bytes_sent = psutil.net_io_counters().bytes_sent / (1024 ** 2)
    bytes_received = psutil.net_io_counters().bytes_recv / (1024 ** 2)
    packets_sent = psutil.net_io_counters().packets_sent
    packets_received = psutil.net_io_counters().packets_recv

    boot_time = psutil.boot_time()
    uptime = current_time - datetime.datetime.fromtimestamp(boot_time)
    uptime_str = str(uptime).split('.')[0]
    return f"""
	    <p>
        <h1>System information on {formatted_datetime}</h1>
        CPU usage: {cpu}%<br>
        Memory usage: {memory_used:.2f} GB / {memory_total:.2f} GB ({memory_percent}%)<br>
	    Swap memory usage: {swap_used:.2f} GB / {swap_total:.2f} GB ({swap_percent}%)<br>
        Disk usage: {disk_used:.2f} GB / {disk_total:.2f} GB ({disk_percent}%)<br>
	    Network data (sent/received): {bytes_sent:.2f} MB / {bytes_received:.2f} MB<br>
	    Network packets (sent/received): {packets_sent} / {packets_received}<br>
	    Uptime: {uptime_str}<br>
	    </p>
    """


def main():
    home = os.environ["HOME"]
    f = home + '/public_html/pythontest.html'
    syshealth_html = system_health()

    with open(f, 'a+') as file:
        file.write(syshealth_html)


main()
