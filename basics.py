import numpy as np

#create ArrBase
ArrBase=np.arange(1,31).reshape(5,6)
print("ArrBase before modification")
print(ArrBase)
print("______________________________________________________________________")

#create ArrT
ArrT=ArrBase.reshape(6,5)
ArrT
print("ArrT")
print(ArrT)
print("______________________________________________________________________")

#create Arr2
Arr2=ArrBase.reshape(2,15)
Arr2
print("Arr2")
print(Arr2)
print("______________________________________________________________________")

#Replace all the even numbers in ArrBase with their negative value.
ArrBase=np.where(ArrBase%2!=1,-ArrBase, ArrBase)
print("Replacing all the even numbers in ArrBase with their negative value")
print(ArrBase)
print("______________________________________________________________________")

#Replace all the odd numbers in ArrBase with their square value.
ArrBase = np.where(ArrBase%2!=0,pow(ArrBase, 2), ArrBase)
print("Replacing all the odd numbers in ArrBase with their square value")
print(ArrBase)
print("______________________________________________________________________")

#Calculate the product of each column in the modified array.
print(np.prod(ArrBase,axis=0))
  #note : axis=1 pour les lignes,et axis=0 pour les colonnes.
print("______________________________________________________________________")

#Calculate the sum of the diagonal elements in the modified array.
print("the sum of the diagonal is :",np.sum(ArrBase.diagonal()))
print("______________________________________________________________________")

#Print the max of each row and the max of the sum of each column in ArrBase.
max_row=np.amax(ArrBase,axis=1)
n=1
for i in max_row :
  print("Max of row N°",n," :",i)
  n=n+1;
print("the max of the sum of each column is : ",np.amax(np.sum(ArrBase,axis=0)))
print("______________________________________________________________________")
   
#Create a tuple that contains the dimensions of ArrBase.
tuple=ArrBase.shape
print(tuple)
print("______________________________________________________________________")

#Create a set that contains all the unique values in ArrBase.
set=np.unique(ArrBase)
print("the unique values in ArrBase : ",set)
print("______________________________________________________________________")

#Create a dictionary that maps each value in ArrBase to its frequency.
dict = {} 
for i in range(5) :
   for j in range(6) :
      if ArrBase[i,j] in dict.items():
            dict[ArrBase[i,j]] += 1
      else:
            dict[ArrBase[i,j]] = 1

print("A dictionary that maps each value in ArrBase to its frequency :")  
for key, value in dict.items():
      print("% d : % d" % (key, value))
