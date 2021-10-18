

with open ('./names.docx',"r") as name:
    namelist=name.readlines()
    print(namelist)
    for name in namelist:
        with open (f'../output/ready_send/Invitation_for_{name}.docx',"w") as startletters:
            # startletters.write(f"hey {names},come at my birthday party")
            with open('../start_letter/letters.docx','r') as newfile:
                contents=newfile.readline()
                f=contents.replace("name", name)
                startletters.write(f'{f}')               
                
                
                
                
                
                
                # rep=repf.readlines()
                # reps=rep.replace("name",f'{names}')
                # startletters.write(rep)