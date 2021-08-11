def countwords():
    filename=input("enter your file name: ")
    numberofwords=0
    file=open(filename,"r")
    for line in file:
        word=line.split()
        numberofwords=numberofwords+len(word)
    print(numberofwords)

countwords()