import numpy as np 
import matplotlib.pyplot as plt  # type: ignore

A = np.array([1,0])
state=np.kron(A,A)           #create a |00> state by taking the tensor product of two zero qubits
print("zero qubit state 1 :", A)
print("Initial 2-qubit state |00> :", state)

H=1/np.sqrt(2) * np.array([[1,1],[1,-1]])
print("HADAMARD GATE :", H) 

I = np.array([
    [1,0],
    [0,1]
])

H_first = np.kron(H,I)  # Apply Hadamard to the first qubit and Identity to the second qubit

result = H_first @ state #apply the hadamard gate on the first qubit of the |00> state
print("after applying hadamard gate on first qubit ")
print(result)

CNOT = np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,0,1],
    [0,0,1,0]
])
bell_state = CNOT @ result   # Apply CNOT: 
print("Bell state :")        # |00> remains |00>  # |10> becomes |11>  
print(bell_state)            # Result: (|00> + |11>)/√2


p=np.abs(bell_state)**2  #compute the probabilities

print("00 probability :", p[0])
print("01 probability :", p[1])
print("10 probability :", p[2])
print("11 probability :", p[3])
outcomes = ['00','01','10','11']
answer = np.random.choice(outcomes,p=p) #simulate measurement by randomly choosing an outcome based on the probabilities 
print("outcomes are : ", outcomes)
print("Measured State :", answer)

states = ['00','01','10','11'] #for getting the graph
plt.bar(states, p)
plt.title("Bell State Probability Distribution")
plt.xlabel("States")
plt.ylabel("Probability")
plt.show()





