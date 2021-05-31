#reading the image file and writing new file by copying each bit of that items.
with open('deer.png','rb') as rf:
    with open('deer_copy.png','wb') as wf:
        for line in rf:
            wf.write(line)
            # FF=rf.read(50000)
            # RR=wf.write(FF)
            # FF=rf.read(50000)
            # RR=wf.write(FF) 


        # chunk=1
        # rf_chunk=rf.read(chunk)   
        # while len(rf_chunk)>0:
        #     wf.write(rf_chunk)
        #     rf_chunk=rf.read(chunk)

