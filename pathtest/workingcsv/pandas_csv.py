
import pandas

data=pandas.read_csv("./weathercsv.csv")
print(data[data.day == 'Sunday'])
print(data.day)







# to_list=(data['temp'].to_list())
# print(sum(to_list)/len(to_list))
# anotherdata=0









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

