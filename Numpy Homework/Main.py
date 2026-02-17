import numpy as np
datatype=[('name','S100'),('class',int),('height',float)]
stu_data=[('Sara',4,6.7),('Jack',1,6.1),('Ali',0,0.1)]
a1=np.array(stu_data,dtype=datatype)
print(a1)