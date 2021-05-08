alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ','!','a', 'b', 'c', 'd', 'e', 'f', 
'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ','!']
num=0
dir=input("'encode' or 'decode'\n")
value=input("enter text you want to encrypt\n")
shift_amt=int(input("how much you want to shift\n"))
if shift_amt>27:
    shift_amt=round(shift_amt%27 )
def ceaser(n,to_input,shift,direction):
    to_input=list(to_input)
    for i in to_input:
        if i in alphabets:
            index=alphabets.index(i)
            if direction=='decode':
                shift*=-1
            to_input[n]=alphabets[abs(index+shift)]
            n+=1
        else:
            to_input[n]=i
            n+=1
    to_input=''.join(to_input)
    print(to_input)
ceaser(n=num,to_input=value,shift=shift_amt,direction=dir)
again=input("wanna try again?y/n\n").lower

condition=True
while condition:
    if again == 'y':
        ceaser(n=num,to_input=value,shift=shift_amt,direction=dir)
    else:
        print("bye")
        condition=False

            


    



        


