import numpy as np
datatype=[('name','S100'),('class',int),('height',float)]
stu_data=[('Razan',4,6.7),('Faizan',1,6.1),('Zaviyan',0,0.1)]
a1=np.array(stu_data,dtype=datatype)
print(a1)