#dabeaz.py
import urllib.request
import webbrowser
from xml.etree.ElementTree import parse
def findbus():
    u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    data = u.read()
    f = open('rt22.xml', 'wb')
    f.write(data)
    f.close()
    print('Wrote rt22.xml')
    doc=parse(source='rt22.xml')
    david_lat=41.980262
    bus_id=[]
    for bus in doc.findall('bus'):
        lat=float(bus.findtext('lat'))
        direction=bus.findtext('dd')
        id=int(bus.findtext('id'))
        if direction.startswith('North'):
        # if lat-david_lat>0:
            if lat>david_lat:
                print(f"bus id {bus.findtext('id')} is at {round(69*abs(lat-david_lat),3)} miles from dave office")
                webbrowser.open()
    print('_'*15)
# latitude=text
# def distance(latitude):
#     return 69*abs(latitude-david_lat)
# distance(latitude)
import time
while True:
    findbus()
    time.sleep(10)

