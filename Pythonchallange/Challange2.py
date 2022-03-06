#Given k->m o->q .... so the pattern is numeric value of k and adding 2=m,o+2=q
#for eg: a+2=c
alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b','.','(',')',"'",' ','','','']
given=input('input strings to decypher\n')
given=list(given)
newlist=[]
for letter in given:
    indx=alphabets.index(letter)
    new_indx=int(indx)+2
    new_letter=alphabets[new_indx]
    new_letter=new_letter.join(new_letter)
    newlist.append(new_letter)
    ans=''.join(newlist)
print(ans)


