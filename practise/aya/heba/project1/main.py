#with open("file.txt", 'r') as x:
# print(x.read())
#import numpy as np
#print(np.__version__)
#x = [1 , 2 ,3 ,4 ,5 ,6]
#y = np.array([[[1 , 2],[7 ,3]],[[ 4 , 5] , [10 , 58]]])
#print(type(x))
#print(type(y))
#print(y.ndim)
import pandas as pd


x = pd.Series(['ahmed' , 31 , 70 ], index=['name' , 'age' , 'weight'])
print(x['name' : 'age'])