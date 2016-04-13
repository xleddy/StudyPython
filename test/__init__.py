theNum = int(input("Give me the upper limit: "))
while theNum != 1:
    print(theNum)
    if theNum%2==0 :
        theNum = int(theNum/2)
    else:
        theNum = theNum*3 +1
