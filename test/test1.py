'''
Created on 2016.04.07

@author: eddy
'''
stringa = ""
for i in range(1,10):
    stringa += str(i)
    print(stringa+" * 8 + "+str(i)+" = "+str(int(stringa)*8+i))