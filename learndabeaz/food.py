# import csv
# from collections import Counter
# from os import name, stat_result
# from typing import Counter
# f=open('Food_Inspections.csv')
# food=list(csv.DictReader(f))
# name=Counter()
# for f in food:
#     if f['Results']=='Pass':
#         if '(Low)' in f['Risk']:
#             if 'floor' in f['Violations']:
#                 print(food)
#             name[f['DBA Name']]+=1

# print(name.most_common(10))
# # for row in csv.DictReader(f):
# #     id=row['Inspection ID']
# #     result=row['Results']
# #     risk=row['Risk']
# #     name=row['DBA Name']
# #     zipaddr=row['Zip']
#     # food[name]=[risk,result]
#     # if 'Pass' in food[name]:
#     #     if zipaddr=='60640':
#     #         print(food)
    
import pylab
from collections import Counter
import csv

outcomes = Counter()

f = open('Food_Inspections.csv', 'r')
for row in csv.DictReader(f):
    result = row['Results']
    outcomes[result] += 1

# Calculate the total sum of records
num_records = sum(outcomes.values())

# Make a table showing outcomes
for result, count in outcomes.most_common():
    print('%20s %d' % (result, count))

# Compute pi-chart amounts
pie_parts = []
labels = []
for result, count in outcomes.most_common():
    pie_parts.append(float(count)/num_records*100)
    labels.append(result)

pylab.pie(pie_parts, labels=labels, autopct='%0.1f%%')
pylab.show()