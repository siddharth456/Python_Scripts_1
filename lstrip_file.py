with open('testscript.txt','r') as f:
    datalines = (lines.lstrip() for lines in f)
    with open('new_testscript.txt','w') as nf:
        for each in datalines:
            each=each.replace(" "*4," ").replace(" "*2," ")
            nf.write(each)

