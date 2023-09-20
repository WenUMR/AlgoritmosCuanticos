from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(4, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.h(qreg_q[3])
circuit.cp(pi / 2, qreg_q[2], qreg_q[3])
circuit.cp(pi / 4, qreg_q[1], qreg_q[3])
circuit.cp(pi / 8, qreg_q[0], qreg_q[3])
circuit.h(qreg_q[2])
circuit.cp(pi / 2, qreg_q[1], qreg_q[2])
circuit.cp(pi / 4, qreg_q[0], qreg_q[2])
circuit.h(qreg_q[1])
circuit.cp(pi / 2, qreg_q[0], qreg_q[1])
circuit.h(qreg_q[0])
circuit.swap(qreg_q[1], qreg_q[2])
circuit.swap(qreg_q[0], qreg_q[3])
