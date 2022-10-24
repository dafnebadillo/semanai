import paho.mqtt.client as paho
from random import randint
import time
import psutil

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

def getListOfProcessSortedByMemory():
    '''
    Get list of running process sorted by Memory Usage
    '''
    listOfProcObjects = []
    # Iterate over the list
    for proc in psutil.process_iter():
       try:
           # Fetch process details as dict
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
           # Append dict to list
           listOfProcObjects.append(pinfo);
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass
    # Sort list of dict by key vms i.e. memory usage
    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
    return listOfProcObjects

client = paho.Client()
#client.username_pw_set("etorresr", "G4t0")
client.on_publish = on_publish
client.connect("broker.mqttdashboard.com", 1883)
client.loop_start()

while True:
    temperature = randint(1,30)
    frec = psutil.cpu_freq()
    #castear solo valor current
    nuc = psutil.cpu_count()
    uso =  psutil.cpu_percent(4)
    mem = psutil.virtual_memory()
    # proc = listOfRunningProcess
    (rc, mid) = client.publish("dafne_badillo/temperature",
    str(temperature), qos=1)
    print(temperature)
    (rc, mid) = client.publish("dafne_badillo/frec",
    str(frec), qos=1)
    print(frec)
    (rc, mid) = client.publish("dafne_badillo/nuc",
    str(nuc), qos=1)
    print(nuc)
    (rc, mid) = client.publish("dafne_badillo/uso",
    str(uso), qos=1)
    print(uso)
    (rc, mid) = client.publish("dafne_badillo/mem",
    str(mem), qos=1)
    print(mem)
    # (rc, mid) = client.publish("dafne_badillo/proc",
    # str(proc), qos=1)
    # print(proc)
    print('The CPU usage is: ', psutil.cpu_percent(4))
    print("Number of cores in system", psutil.cpu_count())
    print("CPU Statistics", psutil.cpu_stats())
    print("CPU frequency", frec)
    print("CPU load average 1, 5, 15 minutes", psutil.getloadavg())
    print(psutil.virtual_memory())
    print(psutil.sensors_battery())
    listOfRunningProcess = getListOfProcessSortedByMemory()
    for elem in listOfRunningProcess[:1] :
        print(elem)
        proc = elem
        (rc, mid) = client.publish("dafne_badillo/proc",str(proc), qos=1)


    time.sleep(10)












