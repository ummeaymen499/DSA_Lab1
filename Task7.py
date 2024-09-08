Matrix=[[1,13,13],
        [5,11,6],
        [4,4,9] ]
RowIndice=[]
ColIndice=[]

def RowWiseSum(Mat):
    Sum=0
    for i in range(len(Mat)):
            for x in range(len(Mat[0])):
                Sum=Sum+Mat[i][x]
            RowIndice.append(Sum) 
            Sum=0   
    return RowIndice  
ReqIndice=RowWiseSum(Matrix)    
print("Row-wise: ")
for i in range(len(ReqIndice)):
    print("",ReqIndice[i])  

def ColumnWiseSum(Mat):
    Sum=0
    for i in range(len(Mat[0])):
            for x in range(len(Mat)):
                Sum=Sum+Mat[x][i]
            ColIndice.append(Sum) 
            Sum=0   
    return ColIndice  
ReqIndice=ColumnWiseSum(Matrix)   
print("Column-wise: ",end=" ") 
for i in range(len(ReqIndice)):
    print(ReqIndice[i],end=" ") 