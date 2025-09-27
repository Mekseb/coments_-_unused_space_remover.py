def remove_comments(input_fill,output_fille):
    with open(input_fill,"r",encoding="utf-8") as f:
        lines=f.readlines()
       

    newlines=[]

    for  i in lines:
        if "#" in i:
            i= i.split("#",1)[0]
        if i.strip() != "":
            newlines.append(i.rstrip()+"\n")
    f=open(output_fille,"w",encoding="utf-8")
    f.writelines(newlines)
    f.close()
inputed = input("input_file")
outputed = input("output_fil") 
remove_comments(inputed , outputed)

