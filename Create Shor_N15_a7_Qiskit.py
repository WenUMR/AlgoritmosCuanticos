from qiskit import *
from qiskit.visualization import plot_histogram
from math import pi

def _7mod15():
        
    circuit = QuantumCircuit(8)
    circuit.x(4)
    circuit.cx(0,5)
    circuit.cx(0,6)
    circuit.cx(1,4)
    circuit.cx(1,6)
    circuit.ccx(0,1,4)
    circuit.ccx(0,1,5)
    circuit.ccx(0,1,6)
    circuit.ccx(0,1,7)
    gate = circuit.to_gate()
    gate.name = "7^x mod 15"
    return gate

def QFT4():
    circuit = QuantumCircuit(4)
    
    circuit.h(3)
    circuit.cp(pi / 2, 2, 3)
    circuit.cp(pi / 4, 1, 3)
    circuit.cp(pi / 8, 0, 3)
    circuit.h(2)
    circuit.cp(pi / 2, 1, 2)
    circuit.cp(pi / 4, 0, 2)
    circuit.h(1)
    circuit.cp(pi / 2, 0, 1)
    circuit.h(0)
    circuit.swap(1, 2)
    circuit.swap(0, 3)

    gate = circuit.to_gate()
    gate.name = "QFT4"
    return  gate

circ = QuantumCircuit(8,4)
circ.h(range(4))
circ.append(_7mod15(), range(8))
circ.measure(range(4,8),range(4))
circ.barrier(range(8))
circ.append(QFT4(), range(4))
circ.measure(range(4), range(4))

backend = Aer.get_backend("qasm_simulator")
job = execute(circ, backend, shots = 100000)
result = job.result()
counts = result.get_counts()
plot_histogram(counts
