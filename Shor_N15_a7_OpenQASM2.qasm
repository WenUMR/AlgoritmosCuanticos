OPENQASM 2.0;
include "qelib1.inc";

qreg q[8];
creg c[4];

h q[0];
h q[1];
h q[2];
h q[3];
x q[4];
cx q[0], q[5];
cx q[1], q[4];
cx q[0], q[6];
cx q[1], q[6];
ccx q[0], q[1], q[4];
ccx q[0], q[1], q[5];
ccx q[0], q[1], q[6];
ccx q[0], q[1], q[7];
measure q[4] -> c[3];
measure q[5] -> c[3];
measure q[6] -> c[3];
measure q[7] -> c[3];
h q[3];
cp(pi / 2) q[2], q[3];
cp(pi / 4) q[1], q[3];
cp(pi / 8) q[0], q[3];
h q[2];
cp(pi / 2) q[1], q[2];
cp(pi / 4) q[0], q[2];
h q[1];
cp(pi / 2) q[0], q[1];
h q[0];
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
measure q[3] -> c[3];
