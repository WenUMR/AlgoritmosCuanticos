from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

qreg_q = QuantumRegister(8, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.x(qreg_q[4])
circuit.cx(qreg_q[0], qreg_q[5])
circuit.cx(qreg_q[0], qreg_q[6])
circuit.cx(qreg_q[1], qreg_q[4])
circuit.cx(qreg_q[1], qreg_q[6])
circuit.ccx(qreg_q[0], qreg_q[1], qreg_q[4])
circuit.ccx(qreg_q[0], qreg_q[1], qreg_q[5])
circuit.ccx(qreg_q[0], qreg_q[1], qreg_q[6])
circuit.ccx(qreg_q[0], qreg_q[1], qreg_q[7])
