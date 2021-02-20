# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 17:16:30 2021

@author: AMIT
"""

import numpy as np

# define |0> and |1>

q0 = np.array([1, 0])
q1 = np.array([0, 1]) 

# Preparing input qubit as |00> 

q00 = np.kron(q0, q0)
q01= np.kron(q0, q1)


# Define H gate 

H = np.array([
[1/np.sqrt(2), 1/np.sqrt(2)],
[1/np.sqrt(2), -1/np.sqrt(2)]
])


I = np.identity(2)

# outer product of H and I

HI = np.kron(H, I)

# Define X (NOT) gate: 

X = np.array([
[0, 1],
[1, 0]
])

# Define Z gate: 
    
Z = np.array([
[1, 0],
[0, -1]
])

# Define projection operator |0><0|

P0x0 = np.array([
[1, 0],
[0, 0]
])

# Define projection operator |1><1|

P1x1 = np.array([
[0, 0],
[0, 1]
])

# Define CX gate (CNOT is controlled-X) operating on control-target

CX = np.kron(P0x0,I) + np.kron(P1x1,X)

# Define CX gate operating on target-control

ICX = np.kron(I,P0x0) + np.kron(X,P1x1)


# task 2 part a
# create superposition state with hadmard gate on q0

q0h = np.dot(H, q0)

# create entangled state using outer product

q0hq0 = np.kron(q0h, q0)

# apply cx gate on the state
qf1= np.dot(q0hq0, CX)

# task 2 part b
# define error gates

eg0 =  .732*0.5*I  + 0.5*X + 0.5*Z
eg1 =  I   
eg2 =  X 
eg3 =  Z 
eg4 =  0.707 * (X + Z)
eg5 =  0.707 * (I + Z)
eg6 =  0.707 * (X + I)

# add ANY error gate before cx
q0he = np.dot(q0h, eg6)

q0e = np.dot(q0, eg6)

# create entangled state using outer product
q0heq0 = np.kron(q0he, q0e)

# apply cx gate on the state
qf2= np.dot(q0heq0, CX)

# task 2 part c

# apply bit flip for q0e

# apply cnot to q0e and q0
q0eq0 = np.kron(q0e,q0)
q0eq0cx= np.dot(q0eq0, CX)

# apply cnot to q0 and q0e completing bit flip circuit
q0ebf= np.dot(q0eq0cx, ICX)

# project out of entangled state
p0 = np.array([
[1, 1, 0, 0],
[0, 0, 1, 1]
])

# final error corrected 2nd qubit

q0ec= np.dot(p0, q0ebf)


# apply phase flip for q0he
# apply h to eq0
q0heh = np.dot(H, q0he)

# apply cnot to q0heh and q0
q0hehq0 = np.kron(q0heh,q0)
q0hehq0cx= np.dot(q0hehq0, CX)

# apply cnot to q0 and q0e completing phase flip circuit 
q0hepf= np.dot(q0hehq0cx, ICX)

# project out of entangled state
# final error corrected 1st qubit followed by h

q0hec= np.dot(p0, q0hepf)
q0hech = np.dot(H, q0hec)


# finally apply cnot on error corrected qubits to complete the circuit
# create entangled state using outer product

q0hecq0ec = np.kron(q0hech, q0ec)


# apply cx gate on the state
qf3= np.dot(q0hecq0ec, CX)

# print qubit elements which come out to be |00> + |11> despite any combination of error gates
for i in range(4):
    print(qf3[i])



 