OPENQASM 2.0;
include "qelib1.inc";

qreg q[8];
creg c[4];

x q[4];
cx q[0], q[5];
cx q[0], q[6];
cx q[1], q[4];
cx q[1], q[6];
ccx q[0], q[1], q[4];
ccx q[0], q[1], q[5];
ccx q[0], q[1], q[6];
ccx q[0], q[1], q[7];
