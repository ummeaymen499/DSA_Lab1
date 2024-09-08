
Indice=[]
def SearchA(Arr, Num):
        for i in range(len(Arr)):
            if(Arr[i]==Num):
                Indice.append(i)
            else:
                continue
        return Indice        
Arr = [22,2,1,7,11,13,5,2,9]
Num=input("Enter the number: ")
ProvidedNum=int(Num)        
ReqIndice=SearchA(Arr,ProvidedNum)
if not ReqIndice:
   print("Provided Number is not found in the given array")
else: 
    print("Index: " ,end="")
    for x in range(len(ReqIndice)):
       if(x<len(ReqIndice)-1):
          print(ReqIndice[x] , end=",")    
       else:
           print(ReqIndice[x])    

