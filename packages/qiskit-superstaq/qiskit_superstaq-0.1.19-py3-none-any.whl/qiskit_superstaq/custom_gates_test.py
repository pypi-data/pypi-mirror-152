from typing import Set

import numpy as np
import pytest
import qiskit

import qiskit_superstaq as qss


def _check_gate_definition(gate: qiskit.circuit.Gate) -> None:
    """Check gate.definition, gate.__array__(), and gate.inverse() against one another"""

    assert np.allclose(gate.to_matrix(), gate.__array__())
    defined_operation = qiskit.quantum_info.Operator(gate.definition)
    assert defined_operation.is_unitary()
    assert defined_operation.equiv(gate.to_matrix(), atol=1e-10)

    inverse_operation = qiskit.quantum_info.Operator(gate.inverse().definition)
    assert inverse_operation.is_unitary()

    assert inverse_operation.equiv(gate.inverse().to_matrix(), atol=1e-10)
    assert inverse_operation.equiv(gate.to_matrix().T.conj(), atol=1e-10)


def test_acecr() -> None:
    gate = qss.AceCR("+-")
    _check_gate_definition(gate)
    assert repr(gate) == "qss.AceCR('+-')"
    assert str(gate) == "AceCR+-"
    assert gate.qasm() == "acecr_pm"

    gate = qss.AceCR("-+", label="label")
    _check_gate_definition(gate)
    assert repr(gate) == "qss.AceCR('-+', label='label')"
    assert str(gate) == "AceCR-+"
    assert gate.qasm() == "acecr_mp"

    gate = qss.AceCR("-+", sandwich_rx_rads=np.pi / 2)
    _check_gate_definition(gate)
    assert repr(gate) == "qss.AceCR('-+', sandwich_rx_rads=1.5707963267948966)"
    assert str(gate) == "AceCR-+|RXGate(pi/2)|"
    assert gate.qasm() == "acecr_mp_rx(pi/2)"

    gate = qss.AceCR("-+", sandwich_rx_rads=np.pi / 2, label="label")
    _check_gate_definition(gate)
    assert repr(gate) == "qss.AceCR('-+', sandwich_rx_rads=1.5707963267948966, label='label')"
    assert str(gate) == "AceCR-+|RXGate(pi/2)|"
    assert gate.qasm() == "acecr_mp_rx(pi/2)"

    with pytest.raises(ValueError, match="Polarity must be"):
        _ = qss.AceCR("++")


def test_zz_swap() -> None:
    gate = qss.ZZSwapGate(1.23)
    _check_gate_definition(gate)
    assert repr(gate) == "qss.ZZSwapGate(1.23)"
    assert str(gate) == "ZZSwapGate(1.23)"

    gate = qss.ZZSwapGate(4.56, label="label")
    assert repr(gate) == "qss.ZZSwapGate(4.56, label='label')"
    assert str(gate) == "ZZSwapGate(4.56)"


def test_parallel_gates() -> None:
    gate = qss.ParallelGates(
        qss.AceCR("+-"),
        qiskit.circuit.library.RXGate(1.23),
    )
    assert str(gate) == "ParallelGates(acecr_pm, rx(1.23))"
    _check_gate_definition(gate)

    # confirm gates are applied to disjoint qubits
    all_qargs: Set[qiskit.circuit.Qubit] = set()
    for _, qargs, _ in gate.definition:
        assert all_qargs.isdisjoint(qargs)
        all_qargs.update(qargs)
    assert len(all_qargs) == gate.num_qubits

    # double check qubit ordering
    qc1 = qiskit.QuantumCircuit(3)
    qc1.append(gate, [0, 2, 1])

    qc2 = qiskit.QuantumCircuit(3)
    qc2.rx(1.23, 1)
    qc2.append(qss.AceCR("+-"), [0, 2])

    assert qiskit.quantum_info.Operator(qc1).equiv(qc2, atol=1e-14)

    gate = qss.ParallelGates(
        qiskit.circuit.library.XGate(),
        qss.ZZSwapGate(1.23),
        qiskit.circuit.library.ZGate(),
        label="label",
    )
    assert str(gate) == "ParallelGates(x, zzswap(1.23), z)"
    _check_gate_definition(gate)

    # confirm gates are applied to disjoint qubits
    all_qargs.clear()
    for _, qargs, _ in gate.definition:
        assert all_qargs.isdisjoint(qargs)
        all_qargs.update(qargs)
    assert len(all_qargs) == gate.num_qubits

    with pytest.raises(ValueError, match="Component gates must be"):
        _ = qss.ParallelGates(qiskit.circuit.Measure())


def test_aqticcx() -> None:
    gate = qss.AQTiCCXGate()
    _check_gate_definition(gate)

    assert repr(gate) == "qss.ICCXGate(label=None, ctrl_state=0)"
    assert str(gate) == "ICCXGate(label=None, ctrl_state=0)"

    qc = qiskit.QuantumCircuit(3)

    qc.append(qss.AQTiCCXGate(), [0, 1, 2])

    correct_unitary = np.array(
        [
            [0, 0, 0, 0, 1j, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [1j, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
        ],
    )

    np.allclose(qiskit.quantum_info.Operator(qc), correct_unitary)


def test_iccxdg() -> None:
    gate = qss.custom_gates.ICCXdgGate()
    _check_gate_definition(gate)
    assert repr(gate) == "qss.ICCXdgGate(label=None, ctrl_state=3)"
    assert str(gate) == "ICCXdgGate(label=None, ctrl_state=3)"


def test_custom_resolver() -> None:
    gates = [
        qss.AceCR("+-"),
        qss.ZZSwapGate(1.23),
        qss.AQTiCCXGate(),
        qss.custom_gates.ICCXGate(),
        qss.custom_gates.ICCXGate(ctrl_state="01"),
        qss.custom_gates.ICCXGate(ctrl_state="10"),
        qss.ParallelGates(
            qiskit.circuit.library.RXGate(4.56),
            qiskit.circuit.library.CXGate(),
            qiskit.circuit.library.XGate(),
            qss.AceCR("-+"),
        ),
    ]

    for gate in gates:
        resolved_gate = qss.custom_gates.custom_resolver(gate)
        assert resolved_gate is not gate
        assert resolved_gate == gate

    assert qss.custom_gates.custom_resolver(qiskit.circuit.library.CXGate()) is None
    assert qss.custom_gates.custom_resolver(qiskit.circuit.library.RXGate(2)) is None
