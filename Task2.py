Arr = [22,2,1,7,11,13,5,2,9]
Arr.sort()
print(Arr)
count=0
inputNum = input("Enter the number: ")
Num=int(inputNum)
for i in range(len(Arr)):
    if(Num == Arr[i]):
        break
    else:
        count=i+1
          
print("Number of digits to be checked are: ",count)
