import psutil
import time
import prometheus_client

PROM_PORT = 8001
UPDATE_INTERVAL = 10
COMPUTER_USAGE = prometheus_client.Gauge('computer_usage', 'Show resource usages of computer', ['resource_label'])

def get_cpu_percentage():
    return psutil.cpu_percent()

def get_memory_percentage():
    return psutil.virtual_memory()[2]

def get_battery_percentage():
    return psutil.sensors_battery()[0]

def get_computer_resource(resource_in):
    switcher = {
        'CPU': get_cpu_percentage,
        'Memory': get_memory_percentage,
        'Battery': get_battery_percentage
    }
    func = switcher.get(resource_in, lambda : "Invalid resource")
    resource_value = func()
    print("{} usage is {} %".format(resource_in, resource_value))
    return resource_value

if __name__ == '__main__':
     prometheus_client.start_http_server(PROM_PORT)
     while True:
        COMPUTER_USAGE.labels('CPU').set(get_computer_resource('CPU'))
        COMPUTER_USAGE.labels('Memory').set(get_computer_resource('Memory'))
        COMPUTER_USAGE.labels('Battery').set(get_computer_resource('Battery'))
        time.sleep(UPDATE_INTERVAL)