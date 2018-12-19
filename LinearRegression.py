import matplotlib.pyplot as plt 
import pandas as pd



# cost function
def regresum(theta, slope, data, c):
    summ = 0
    
    if c == 1:
        for i in range(len(data.index)):
            first = data.iloc[i ,0]
            second = data.iloc[i ,1]
            summ = summ + (((theta + slope*first) - second) * first)
    else:
        for i in range(len(data.index)):
            first = data.iloc[i ,0]
            second = data.iloc[i ,1]
            summ = summ + ((theta + slope*first) - second)
       
    return summ
    
    
    
    
    
    
data = pd.read_csv('ex1data1.txt', header = None)

# length of index
length = len(data.index)


#initializing variables
d=0
theta = 0
slope = 0
alpha = 0.01
converg = []

#Training loop
while d < 2500:
    temp0 = theta - ((alpha/length)* regresum(theta,slope,data, c=0))
    temp1 = slope - ((alpha/length)* regresum(theta,slope,data,c = 1))
    theta = temp0
    slope = temp1
    converg.append(slope)
  
    d = d+1

#plotting convergence
plt.plot(converg)