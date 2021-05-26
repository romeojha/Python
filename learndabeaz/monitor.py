#monitor for most pothole in route
# import urllib.request
# import csv   
# # url=urllib.request.urlopen('https://data.cityofchicago.org/resource/_311-potholes.json')
# f= open('pothole.csv')
# r=csv.DictReader(f)
# next(r)
# pothole={}
# for row in csv.DictReader(f):
    # addr = row['STREET ADDRESS']
    # sorting=sorted(addr)
    # num = row['NUMBER OF POTHOLES FILLED ON BLOCK']
    # location=row['LOCATION']
    # status=row['STATUS']
    # sorted(addr)
    # pothole[addr]={num}
    # print(pothole)
# for row in csv.DictReader(f):
#     addr = row['STREET ADDRESS']
#     num = row['NUMBER OF POTHOLES FILLED ON BLOCK']
#     parts=addr.split()
#     pothole[addr]={num}


# def parts(addr):
#     print(addr)
#     parts=addr.split()
#     num=parts[0]
#     # parts[0]=num[:-2]+'XX'
    # newparts=' '.join(parts)
    # return newparts 

# parts(addr)
import csv
f= open('pothole.csv')
print(type(f))
pothole={}
for row in csv.DictReader(f):
    addr=row['STREET ADDRESS']
    num=row['NUMBER OF POTHOLES FILLED ON BLOCK']
    zipaddr=row['ZIP']
    status=row['STATUS']
    if status=='Open':
        if num>str(20):
            pothole[addr]={num,zipaddr}
print(pothole)
