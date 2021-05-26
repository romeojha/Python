# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

#  Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
# def nest():
#   var=1
#   def nesting():
#     var=2
#     print(var)
#   # nesting()
#   print(var)

# nest()

#corey schafer
#list comprehension
condition=True
if condition:
    x=0
else:
    x=1
print(x)
#improved
x=1 if condition else 0
print(x)
#improved


#2
#using _ insted to comma for larger numbers
num=10000000000
num1=100_000_000

#to print with comma
total = num +num1
print(f"{total:,}")
#it wont effect our code in any way

#3
#using context manager. for managinf resources managing datas

f=open('test.txt','r')
file_contents=f.read()
f.close()
#improved
with open('text.txt','r') as f:
    file_content =f.read()
#improved

words=file_contents.split("")
word_count= len(words)
print(word_count) 

#using enumeration to improve the code
name=['rome','corey','dxta','sam']
index=0
for names in name:
    print(index,names)
    index+=1
#improved
name=['rome','corey','dxta','sam']
for index,names in enumerate(name,start=2):#if you want to start with2.default=0
    print(index,names)
#improved



 