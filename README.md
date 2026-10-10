# Transistor to Qubit Lab

An interactive educational framework connecting semiconductor switching and classical logic to quantum states, gates, measurement, and noise.

## Modules
- **A — Transistor Switching:** illustrative input-voltage threshold model, LED state, load current, and output voltage.
- **B — Classical Logic Gates:** interactive NOT, AND, OR, NAND, NOR, and XOR with truth tables.
- **C — Quantum Gate Simulator:** NumPy state-vector simulation for X, H, and Z gates; simulated measurement shots; two-qubit CNOT demonstration; Qiskit circuit equivalent.
- **D — Compare & Learn:** classical/quantum mapping, classical switching-noise experiment, quantum error concepts, and a quiz.

## Run locally
Python 3.10+ is recommended.

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\activate       # Windows
pip install -r requirements.txt
streamlit run app.py
```

The app opens in a browser. The NumPy state-vector model runs the interactive quantum calculations. Qiskit is used to construct and display the equivalent circuit when installed.

## Deploy with GitHub and Streamlit Community Cloud
1. Create a GitHub repository and upload `app.py`, `requirements.txt`, and this README.
2. Open https://share.streamlit.io/ and sign in with GitHub.
3. Select **Create app**, choose the repository and branch, and set the main file path to `app.py`.
4. Deploy. Keep the repository public if required by your course and do not commit secrets or personal credentials.

## Important scope notes
- The transistor circuit is a software model with illustrative values, not a validated SPICE model or physical measurement.
- Classical noise uses synthetic random samples to illustrate threshold errors.
- Quantum measurement results are sampled from calculated state probabilities; they are educational simulation results, not results from real quantum hardware.
- If the instructor requires a real Qiskit Aer backend or a physical/Tinkercad circuit, extend the project accordingly and include genuine evidence. The assignment PDF lists Python, NumPy, Qiskit, and IBM Quantum Composer/simulator in its technology stack.
