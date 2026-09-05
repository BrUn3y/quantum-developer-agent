"""Parse and simulate the basic QASM circuits without external services."""

import re

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

from quantum_developer_agent.agent import _basic_algorithm_qasm


CASES = {
    "bell": ("Create a Bell state circuit", {"00", "11"}),
    "cx": ("Create a CX gate circuit", {"11"}),
    "grover-2": ("Implement Grover for 2 qubits", {"11"}),
    "grover-3": ("Implement Grover for 3 qubits", None),
    "deutsch-jozsa": ("Create Deutsch-Jozsa", {"11"}),
}


def extract_qasm(response: str) -> str:
    match = re.search(r"```qasm\n(.*?)```", response, re.DOTALL)
    if not match:
        raise AssertionError("Generated response does not contain fenced QASM")
    return match.group(1)


def main() -> None:
    for name, (prompt, expected_states) in CASES.items():
        generated = _basic_algorithm_qasm(prompt)
        if not generated:
            raise AssertionError(f"No circuit generated for {name}")
        circuit = QuantumCircuit.from_qasm_str(extract_qasm(generated[1]))
        counts = StatevectorSampler(seed=42).run([circuit], shots=2048).result()[0].data.c.get_counts()
        if expected_states is not None and set(counts) != expected_states:
            raise AssertionError(f"{name}: expected {expected_states}, received {set(counts)}")
        if name == "grover-3":
            if max(counts, key=counts.get) != "111" or counts["111"] / 2048 <= 0.70:
                raise AssertionError(f"{name}: marked state 111 was not sufficiently amplified")
        print(f"PASS {name}: {counts}")


if __name__ == "__main__":
    main()
