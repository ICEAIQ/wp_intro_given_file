from qiskit import *


def XOR(left_input, right_input):
    q = QuantumRegister(2)  # a qubit in which to encode and manipulate the input
    c = ClassicalRegister(1)  # a bit to store the output
    qc = QuantumCircuit(q, c)  # this is where the quantum program goes

    #here encode the two input
    if left_input == 1:
        pass
    # /!\ Remember that this time you have two bit two encode.


    # Now we've encoded the input, we can do a CNOT
    pass

    # We extract the |0>/|1> output of the qubit and encode it in the bit c[0]
    qc.measure(q[0], c[0])

    # We'll run the program on a simulator
    backend = Aer.get_backend('qasm_simulator')
    # Since the output will be deterministic, we can use just a single shot to get it
    job = execute(qc, backend, shots=1)
    output = next(iter(job.result().get_counts()))

    return int(output)

if __name__ == '__main__':
    assert XOR(0, 0) == 0
    assert XOR(0, 1) == 1
    assert XOR(1, 0) == 1
    assert XOR(1, 1) == 0