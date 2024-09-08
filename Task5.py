startingIndex=input("Starting: ")
endingIndex=input("Ending: ")
Start=int(startingIndex)
End=int(endingIndex)


s = "University of Engineering and Technology Lahore"

def StringReverse(str, starting, ending):
   return str[starting:ending-1:-1]
   
if(Start<End):
   print("Starting Index must be greater than the ending Index")
else:   
   ReqString=StringReverse(s,Start,End)
   print("Output:",ReqString)