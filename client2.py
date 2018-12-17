#Base Python client for MEng in IoT Assignment
#consumes data from IoT Gateway
import urllib.request
import numpy as np
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
response = urllib.request.urlopen('http://localhost:8080/')
resp = response.read().decode()
time =[]
temp=[]
head = ET.fromstring(resp)
for reading in head.findall('reading'):
    time.append(reading.find('time').text)
    temp.append(int(reading.find('temperature').text))
plt.plot(time, temp)
plt.show()
