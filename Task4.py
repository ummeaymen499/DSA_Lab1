
from Task3 import Minimum
def Sort4(Array):
      
      for i in range(len(Array)):
          Index=Minimum(Array,i,len(Array)-1)
          
          if Index!=i:
            temp = Array[i]
            Array[i] = Array[Index]
            Array[Index] = temp
      return Array
if __name__ == "__main__":
      Array= [3,4,7,8,0,1,23,-2,-5] 
      ReqArray=Sort4(Array)
      print("Sorted Array: ",ReqArray)

    