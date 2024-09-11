import numpy as np
import math

np.random.seed(100) # Set the seed for the random number generator
rho, sigma_x, sigma_y = -.4, 3, 2
vcv = np.array([[sigma_x**2, rho*sigma_x*sigma_y],
                [rho*sigma_x*sigma_y,sigma_y**2]])
mu = np.array([-1,2])
sample = np.random.multivariate_normal(mu,vcv,200)
x = sample[:,0]
y = sample[:,1]

def mean(vector):
    return sum(vector)/len(vector) 
print("mean: ", mean(x))

def sd(vector):
    m = mean(vector)
    sum = 0
    n = -1
    for x in vector:
        sum = sum + (x-m)**2  
        n+=1
    return math.sqrt(sum/n)
print("sd: ", sd(x))

def z(vector):
    m = mean(vector)
    s = sd(vector)
    return [(x-m)/s for x in vector]
print("z: ", z(x))

def sample_covar(vector_x, vector_y):
    m_x = mean(vector_x)
    m_y = mean(vector_y)
    sum = 0
    n = -1
    for i in range(len(vector_x)):
        sum = sum + (vector_x[i]-m_x)*(vector_y[i]-m_y)
        n+=1
    return sum/n
print("sample_covar: ", sample_covar(x,y))

def sample_corr(vector_x, vector_y):
    return sample_covar(vector_x, vector_y)/(sd(vector_x)*sd(vector_y))
print("sample_corr: ", sample_corr(x,y))

