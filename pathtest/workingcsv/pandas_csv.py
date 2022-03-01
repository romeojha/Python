#find the number of grey squarrel from the given file of squarre count.csv
import pandas as pd
data=pd.read_csv('squarrel_count.csv')
listed_val=len(data[data["Primary Fur Color"] == 'Gray'])
print(listed_val)







# to_list=(data['temp'].to_list())
# print(sum(to_list)/len(to_list))
# anotherdata=0

# import pandas

# data=pandas.read_csv("./weathercsv.csv")
# print(data[data.day == 'Sunday'])
# print(data.day)

# for data in to_list:
#     if data>anotherdata:
#         anotherdata=data
#     print(anotherdata)

# pandas.
# import csv
# with open ('./weathercsv.csv') as csvfile:
#     csv_data=csv.reader(csvfile)
#     temp= []
#     for r in csv_data:
#         print(r)
#         temp.append(r[1])
