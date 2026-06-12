import numpy as np

A = np.array([1,0])
state=np.kron(A,A)           #create a |00> state by taking the tensor product of two zero qubits
print("zero qubit state 1 :", A)
print("tensor product :", state )

H=1/np.sqrt(2) * np.array([[1,1],[1,-1]])
print("HADAMARD GATE :", H) 

I = np.array([
    [1,0],
    [0,1]
])

H_first = np.kron(H,I) 

result = H_first @ state #apply the hadamard gate on the first qubit of the |00> state
print("after applying hadamard gate on first qubit ")
print(result)

CNOT = np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,0,1],
    [0,0,1,0]
])
bell_state = CNOT @ result  #apply the CNOT gate to create the Bell state
print("Bell state :")
print(bell_state)

p=np.abs(bell_state)**2  #compute the probabilities 
print("00 probability :", p[0])
print("01 probability :", p[1])
print("10 probability :", p[2])
print("11 probability :", p[3])
outcomes = ['00','01','10','11']
answer = np.random.choice(outcomes,p=p) #simulate measurement by randomly choosing an outcome based on the probabilities 
print("outcomes are : ", outcomes)
print(answer)





