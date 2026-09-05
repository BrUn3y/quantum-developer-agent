import unittest

from quantum_developer_agent.agent import _basic_algorithm_qasm, _superposition_qasm


def _qasm(prompt: str) -> str:
    generated = _basic_algorithm_qasm(prompt)
    if not generated:
        raise AssertionError(f"No deterministic circuit generated for {prompt!r}")
    response = generated[1]
    if not response.startswith("```qasm\nOPENQASM 2.0;") or not response.endswith("```"):
        raise AssertionError("Response is not a complete fenced OpenQASM 2.0 program")
    if "measure" not in response:
        raise AssertionError("Generated circuit has no measurements")
    return response


class BasicAlgorithmTests(unittest.TestCase):
    def test_bell_state(self):
        qasm = _qasm("Create a Bell state circuit")
        self.assertIn("h q[0];", qasm)
        self.assertIn("cx q[0],q[1];", qasm)

    def test_cx_gate(self):
        qasm = _qasm("Create a CX gate circuit")
        self.assertIn("x q[0];", qasm)
        self.assertIn("cx q[0],q[1];", qasm)

    def test_grover_two_and_three_qubits(self):
        two_qubits = _qasm("Implement Grover for 2 qubits")
        three_qubits = _qasm("Implement Grover for 3 qubits")
        self.assertIn("cz q[0],q[1];", two_qubits)
        self.assertIn("ccx q[0],q[1],q[2];", three_qubits)

    def test_deutsch_jozsa(self):
        qasm = _qasm("Create Deutsch-Jozsa")
        self.assertIn("cx q[0],q[2];", qasm)
        self.assertIn("cx q[1],q[2];", qasm)

    def test_hyphenated_qubit_count(self):
        self.assertIn("qreg q[2];", _superposition_qasm("Create a 2-qubit superposition circuit"))


if __name__ == "__main__":
    unittest.main()
