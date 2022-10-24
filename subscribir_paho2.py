import paho.mqtt.client as paho
import psutil
from random import randint

list_frec = list()
list_mem = list()
list_proc = list()
list_nuc = list()
list_uso = list()

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    frec_cont = [0,1,2,3,4,5,6]

    if (msg.topic == "dafne_badillo/frec"):
        #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
        #print(msg.payload)
        dta = str(msg.payload)
        dta = dta.split("'")
        dta = dta[1]
        dta.split(",")
        dta = dta[17:21]
        frec_cont[0] = float(dta)
        msg.payload = frec_cont[0]
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
        #list_frec.append(dta)
  
    elif (msg.topic == "dafne_badillo/mem"):
        dta = str(msg.payload)
        #print("MEM", dta)
        dta = dta.split("'")  
        dta = dta[1]
        dta = dta.split(",")
        dta = dta[2]
        dta = dta[9:13]
        dta = float(dta)
        frec_cont[1] = dta
        msg.payload = frec_cont[1]
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
        #list_mem.append(dta)
        
    # PROC
    elif (msg.topic == "dafne_badillo/proc"):
        #print(str(msg.payload))
        dta = str(msg.payload)
        dta = dta.split("'")
        dta = dta[11]
        frec_cont[2] = dta
        msg.payload = frec_cont[2]
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
        #print("PROC",dta[11])
        #list_proc.append(dta)

    elif (msg.topic == "dafne_badillo/nuc"):
        dta = str(msg.payload)
        dta = dta.split(",")
        dta = str(dta)
        frec_cont[3] = dta
        msg.payload = frec_cont[3]
        #print("DTA", dta)
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
        #print("DTA", dta)
        #list_nuc.append(dta)

    else:
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
        #list_uso.append(str(msg.payload))


def menor(list_frec):
    min = 0
    for x in list_frec:
        if x < min:
            min = x
    return min

list_frec = randint(1700,3000)
list_nuc = randint(4,8)
list_uso = randint(1,10)
print("-------------------------------------------------")
print("         min     dafne_badillo       max")
print("frec     "+str(list_frec)+"    "+str(list_frec)+"     "+str(list_frec))
print("nuc  "+str(list_nuc)+"       "+str(list_nuc)+"       "+str(list_nuc))
print("uso  "+str(list_uso)+"       "+str(list_uso)+"       "+str(list_uso))
print("proc     vms     vms         vms")
print("-------------------------------------------------")

client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
#client.username_pw_set("etorresr", "G4t0")
client.connect("broker.mqttdashboard.com", 1883)
client.subscribe("dafne/frec", qos=1)
client.subscribe("dafne/nuc", qos=1)
client.subscribe("dafne/uso", qos=1)
client.subscribe("dafne/mem", qos=1)
client.subscribe("dafne/proc", qos=1)
client.subscribe("miles/frec", qos=1)
client.subscribe("miles/nuc", qos=1)
client.subscribe("miles/uso", qos=1)
client.subscribe("miles/mem", qos=1)
client.subscribe("miles/proc", qos=1)
client.subscribe("dafne_badillo/frec", qos=1)
client.subscribe("dafne_badillo/nuc", qos=1)
client.subscribe("dafne_badillo/uso", qos=1)
client.subscribe("dafne_badillo/mem", qos=1)
client.subscribe("dafne_badillo/proc", qos=1)
client.subscribe("victor/frec", qos=1)
client.subscribe("victor/nuc", qos=1)
client.subscribe("victor/uso", qos=1)
client.subscribe("victor/mem", qos=1)
client.subscribe("victor/proc", qos=1)
client.subscribe("joseduardo/frec", qos=1)
client.subscribe("joseduardo/nuc", qos=1)
client.subscribe("joseduardo/uso", qos=1)
client.subscribe("joseduardo/mem", qos=1)
client.subscribe("joseduardo/proc", qos=1)
client.subscribe("alonso/frec", qos=1)
client.subscribe("alonso/nuc", qos=1)
client.subscribe("alonso/uso", qos=1)
client.subscribe("alonso/mem", qos=1)
client.subscribe("alonso/proc", qos=1)
client.subscribe("anthony/frec", qos=1)
client.subscribe("anthony/nuc", qos=1)
client.subscribe("anthony/uso", qos=1)
client.subscribe("anthony/mem", qos=1)
client.subscribe("anthony/proc", qos=1)



client.loop_forever()
