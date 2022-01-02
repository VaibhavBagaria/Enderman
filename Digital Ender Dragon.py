import matplotlib.pyplot as plot

a=0
b=2
c=4
data=[[1,2,3,4,5,6,7,8,9,10]]
data1=[
     [a,a,a,a,a,a,a,a],
     [a,a,a,a,a,a,a,a],
     [c,b,c,a,a,c,b,c],
     [a,a,a,a,a,a,a,a],
     [a,a,a,a,a,a,a,a],
     [a,a,b,a,a,b,a,a],
     [a,a,a,b,b,a,a,a],
     [a,a,a,a,a,a,a,a]
     ]
plot.imshow(data1, cmap='magma')
plot.show()
