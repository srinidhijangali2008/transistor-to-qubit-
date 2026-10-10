# Transistor-to-Qubit Learning Framework
## EDC Assignment 2 — Project Report

### 1. Aim
To develop an interactive learning framework that connects familiar semiconductor and classical digital concepts with qubits, quantum gates, measurement, and quantum noise.

### 2. Learning framework
The framework progresses through four levels:
1. **Transistor:** model input-controlled electronic switching.
2. **Logic gate:** explore classical NOT, AND, OR, NAND, NOR, and XOR.
3. **Bit to qubit:** represent a qubit as |ψ⟩ = α|0⟩ + β|1⟩, where |α|² + |β|² = 1, and explore X, H, and Z operations and measurement.
4. **Classical vs quantum circuit:** compare classical outputs with quantum measurement outcomes and discuss noise.

### 3. Implementation
The project is implemented as a Streamlit web application. Python provides the application logic, NumPy performs state-vector and probability calculations, and Qiskit constructs a corresponding quantum circuit representation. Pandas is used to display truth tables and comparison data.

### 4. Module descriptions
**Module A — Transistor Switching:** A threshold-based educational model lets users adjust input voltage, switching threshold, load resistance, supply voltage, and LED forward voltage. It displays the simulated LED state and illustrative load current.

**Module B — Logic Gates:** Users select a gate and toggle inputs. The application calculates the output and displays the truth table.

**Module C — Quantum Lab:** Users select an initial one-qubit state and apply X, H, and Z gates. The app displays state amplitudes and measurement probabilities, samples repeated outcomes, and demonstrates CNOT on two qubits.

**Module D — Comparison and Noise:** A comparison table maps classical concepts to quantum counterparts. A synthetic voltage-noise model shows how a signal close to a switching threshold can produce inconsistent classical outputs. Quantum bit-flip, phase-flip, depolarising noise, and quantum error correction are described, followed by a short quiz.

### 5. Classical and quantum noise
Classical switching noise perturbs a voltage/current signal and can move the signal across a logic threshold. Quantum noise can alter a quantum state or the effect of a gate. Bit-flip errors correspond to X-type errors; phase-flip errors correspond to Z-type errors. Depolarising noise is a simplified model involving random Pauli errors. Quantum error correction uses encoded information and additional qubits to detect and correct certain errors.

### 6. Results and observations
- A transistor switch can be represented conceptually as a classical ON/OFF state.
- Classical logic gates produce definite outputs for fixed ideal inputs.
- An X gate interchanges the computational basis states |0⟩ and |1⟩.
- Applying H to |0⟩ gives equal ideal probabilities for measuring 0 and 1.
- Repeated measurements yield sampled counts that approach the underlying probabilities as the number of shots increases.
- A noisy classical input near the threshold may change the output state.

### 7. Limitations
The transistor module is an illustrative mathematical model rather than a validated device-level circuit simulation. The noise module uses synthetic data. Quantum outcomes are generated from state probabilities and are not measurements from quantum hardware. The app should not be described as a physical experiment.

### 8. Conclusion
The project provides a gradual bridge from transistor switching and binary logic to quantum states, gates, measurement, and noise. Interactive controls allow learners to change inputs and observe how classical and quantum systems represent and process information.

### 9. References
1. EDC Assignment 2 handout, “From Transistors to Qubits: A Hybrid Learning Framework for Understanding Quantum Computing through Semiconductor Concepts.”
2. Qiskit documentation: https://quantum.cloud.ibm.com/docs
3. Streamlit documentation: https://docs.streamlit.io/
