# HYBRID QUANTUM CIRCUIT SIMULATOR 

## OVERVIEW 
The project implements basic quantum circuit simulator using NumPy. The project supports qubit representations, applies quantum gates, simulate measurements and probability based measurement outputs. 
This project was developed as a part of PHONEIX ASSOCIATION's induction task. 

## FEATURES 
- Quantum state representation using NumPy arrays.
- Hadamard Gate (H) implementation.
- CNOT Gate implementation.
- Pauli-X (NOT) Gate implementation.
- Probability measurement by using amplitudes.
- Quantum measurement simulation.
- Quantum coin toss circuit.
- Quantum Bell state circuit.

## REQUIREMENTS 
- Python 3.x
- NumPy
Install NumPy :
```bash
   pip install numpy
```
## PROJECT STRUCTURE 
``` text
  bell_state.py
  quantum_coin_toss.py
  Readme.md
```

## HOW TO RUN 
### BELL STATE GENERATION 
``` bash
  python bell_state.py
```
This circuit :
1. Creates the initial state |00>.
2. Applies a Hadamard Gate to the first qubit.
3. Applies a CNOT gate.
4. Generates the Bell state.
5. Calculates measurement probabilities.
6. Simulates a measurement.

Expected probabilities : 
```
|00> : 0.5
|01> : 0.0
|10> : 0.0
|11> : 0.5
```

### QUANTUM COIN TOSS 
```
 python quantum_coin_toss.py
```
This circuit : 
1. Creates the initial state |0>.
2. Applies a Hadamard Gate.
3. Creates a superposition.
4. Calculates measurement probabilities.

Expected probabilities :
```
0 : 0.5
1 : 0.5 
```
## QUANTUM CONCEPTS USED 
### QUBIT
A qubit is a fundamental unit of quantum information. 
A single qubit is represented as :
|ψ⟩ = α|0⟩ + β|1⟩
where α and β are probability amplitudes.
A qubit can exist as a combination of states until measurement. 
### TENSOR PRODUCT 
Tensor products are used to combine multiple qubits into a larger quantum system. 
### BELL STATE 
The Bell state generated is :
(|00⟩ + |11⟩)/√2
This is an example of an entangled quantum state.
