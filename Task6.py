#Iterative Method
Input=input("Input: ")
InputNum=int(Input)
def SumIterative(number):
    Sum=0
    while(number!=0):
       num1=number%10
       Sum=Sum+num1
       number=number//10
    return Sum 
ReqSum=SumIterative(InputNum)
print("Sum of digits is: ",ReqSum)
#Recursive Method
def SumRecursive(number):
    Sum=0
    if(number==0):
        return Sum
    else:
        Sum =number%10 + SumRecursive(number//10)
        return Sum
ReqSum=SumRecursive(InputNum)
print("Sum of digits is: ",ReqSum)  