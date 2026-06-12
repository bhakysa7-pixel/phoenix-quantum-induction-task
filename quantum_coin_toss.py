
import numpy as np

zero = np.array([1,0]) #create a zero qubit state
print("Zero qubit state :", zero)  

H= 1/np.sqrt(2) * np.array([[1,1],[1,-1]]) #create a hadanard gate
print("Hadamard Gate :",H)

result = H @ zero  #apply the hadamard gate to the zero qubit state
print("After applying hadamard gate on zero qubit ") 
print(result)

p = np.abs(result)**2 #compute the probabilities 
print("Probabilities :", p)

answer = np.random.choice([0,1],p=p) #simulate measurment by randomly choosing an outcome based on the probabilities 
print("Measurement outcome :", answer)
