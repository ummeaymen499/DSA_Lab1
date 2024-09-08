Input=input("Enter string: ")
def PalindromRecursive(str):
   if(len(str)<=1):
      return True
   elif(str[0]!=str[-1]):
      return False
   else:
      return PalindromRecursive(str[1:-1])

if(" " not in Input):
    
   if(PalindromRecursive(Input)==True):
      print("Palindrome")
   else:
      print("Not a Palindrome")   
else:
   print("Invalid Input")   