import requests
urls="https://api.openweathermap.org/data/2.5/onecall"
parameters={
    'lat':28.4089,
    'lon':77.3178,
    'appid':'7eead96bbe2bd091e641c9a0b90d5800',
    'exclude': "current,minutely,daily", 
}
req=requests.get(urls, params=parameters)
response=req.json()
print(response)
# hourly=response['hourly']
# for i in range(1,len(hourly)):
#     temp=hourly[i]['humidity']
#     print([f"{i%13} :humidity val:{temp}"])