def decode(list ):
    binCodelist=[] 

    # convert decimal list to binary list 
    def DecimalToBinary(num):   
         if num <= 0: 
             return [0,0,0,0]
         else :
             bincode = num % 2
             binCodelist.append(bincode)
             DecimalToBinary(num // 2)
         if len(binCodelist)<4:
             for i in range(4-len(binCodelist)):
                binCodelist.append(0)
         return binCodelist[::-1]
         
    # binary list to integer conversion navgation convert 1 to 0 or 0 to 1
    def negation(binCodelist):          
        neg=[]
        for i in binCodelist :
            #assert i  in (0, 1)
            neg.append(abs(1-i))
        return neg 

    # convert binary list to decimal list 
    def binaryToDecimal(tryo): 

        # row The first  value in ordered pair
        most=tryo[:4] 
        # colum T'he second value in ordered pair 
        least=tryo[ len(tryo)-2 :]  
        result1 = int("".join(str(i) for i in least),2)
        result2 = int("".join(str(i) for i in most),2)
        return (result1,result2)
    dicTable={

    (0,0):'A',(0,1):'B',(0,2):'C',(0,3):'D',(0,4):'E',(0,5):'F',(0,6):'G',(0,7):'H',(0,8):'I',(0,9):'J',
    (1,0):'K',(1,1):'L',(1,2):'M',(1,3):'N',(1,4):'O',(1,5):'P',(1,6):'Q',(1,7):'R',(1,8):'S',(1,9):'T',
    (2,0):'U',(2,1):'V',(2,2):'W',(2,3):'X',(2,4):'Y',(2,5):'Z',(2,6):'.',(2,7):' ',(2,8):'!',(2,9):'_',
    (3,0):'0',(3,1):'1',(3,2):'2',(3,3):'3',(3,4):'4',(3,5):'5',(3,6):'6',(3,7):'7',(3,8):'8',(3,9):'9',
    }
    for num in list :
        code=DecimalToBinary(num)
        tryo =negation(code)
        binCodelist.clear()
        orderedPair=binaryToDecimal(tryo)
        if orderedPair in dicTable.keys() :
           print(dicTable[orderedPair],end="")
        #print(binaryToDecimal(tryo))
list=[ 385 ,227, 514 ,195, 1025, 835 ,707, 258, 1283]  
decode(list)