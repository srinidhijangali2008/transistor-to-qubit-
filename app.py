import math
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Transistor to Qubit Lab",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Theme ----------
st.markdown("""
<style>
:root { --ink:#eaf0ff; --muted:#a9b7d4; --panel:#111a31; --edge:#293858; }
.stApp { background: radial-gradient(circle at 15% 0%, #1a2a50 0, #0a1020 42%, #080d18 100%); color:var(--ink); }
[data-testid="stHeader"] { background: rgba(0,0,0,0); }
.block-container { padding-top: 1.7rem; max-width: 1250px; }
h1,h2,h3 { color:#f4f7ff; }
p,li,label { color:#d7e0f5; }
div[data-testid="stMetric"] { background:rgba(20,32,58,.82); border:1px solid #293858; padding:14px; border-radius:14px; }
div[data-testid="stVerticalBlockBorderWrapper"] { border-color:#293858 !important; border-radius:16px; }
div.stButton > button { border-radius:10px; border:1px solid #5874ad; }
.small-muted { color:#a9b7d4; font-size:.92rem; }
.hero { padding: 1.4rem 1.6rem; border:1px solid #30446b; border-radius:20px;
        background:linear-gradient(115deg,rgba(36,58,102,.75),rgba(15,23,43,.88)); margin-bottom:1.1rem; }
.pill { display:inline-block; border:1px solid #526a9d; border-radius:99px; padding:4px 10px;
        color:#c6d5ff; font-size:.78rem; margin-right:5px; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div><span class="pill">EDC · INTERACTIVE LEARNING LAB</span><span class="pill">CLASSICAL → QUANTUM</span></div>
  <h1 style="margin:.55rem 0 .25rem 0;">Transistor to Qubit</h1>
  <p style="font-size:1.08rem;margin:0;color:#c4d2ef;">From semiconductor switching to quantum information — explore, experiment, compare.</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## ⚛️ Lab navigation")
    module = st.radio(
        "Choose a module",
        ["A · Transistor", "B · Logic Gates", "C · Quantum Lab", "D · Compare & Learn"],
        label_visibility="collapsed"
    )
    st.divider()
    st.caption("A learning simulator. Transistor values are illustrative models, not a substitute for a real circuit measurement.")
    st.caption("Quantum results are simulator outputs; real quantum hardware may differ.")

# ---------- Module A ----------
if module == "A · Transistor":
    st.title("Module A · Transistor Switching")
    st.write("Explore how an input voltage controls a transistor switch and a load LED.")
    left, right = st.columns([1, 1.25], gap="large")
    with left:
        vin = st.slider("Input / base voltage, Vin (V)", 0.0, 5.0, 0.0, 0.05)
        threshold = st.slider("Switching threshold (V)", 0.1, 3.0, 0.7, 0.05)
        resistance = st.slider("Load resistance (Ω)", 100, 2200, 330, 10)
        supply = st.slider("Supply voltage (V)", 3.0, 12.0, 5.0, 0.5)
        vled = st.slider("LED forward voltage (V)", 1.4, 3.2, 2.0, 0.1)
    on = vin >= threshold
    current_ma = max(0.0, (supply - vled) / resistance * 1000) if on else 0.0
    vout = 0.15 if on else supply
    with right:
        st.markdown("### Virtual circuit")
        led_color = "#ff4d6d" if on else "#4b566d"
        glow = "0 0 28px #ff4d6d" if on else "none"
        st.markdown(f"""
        <div style="background:#0b1222;border:1px solid #293858;border-radius:18px;padding:25px;text-align:center;">
          <div style="font-size:.85rem;color:#a9b7d4;">Vin → transistor switch → LED + resistor</div>
          <svg viewBox="0 0 500 210" style="width:100%;max-width:570px;">
            <path d="M40 55 H155 M155 55 V92 M155 118 V160 H270 M320 160 H410 V55 H445"
              fill="none" stroke="#86a8f8" stroke-width="4" stroke-linecap="round"/>
            <path d="M155 92 L155 118" stroke="#86a8f8" stroke-width="5"/>
            <circle cx="155" cy="105" r="30" fill="#172443" stroke="#9cb8ff" stroke-width="3"/>
            <path d="M140 90 L170 120 M170 90 L140 120" stroke="#9cb8ff" stroke-width="3"/>
            <rect x="250" y="146" width="70" height="28" rx="4" fill="#26395d" stroke="#a9c3ff" stroke-width="2"/>
            <circle cx="410" cy="105" r="19" fill="{led_color}" stroke="#ffd6df" stroke-width="3" style="filter:drop-shadow({glow});"/>
            <path d="M398 76 L389 61 M416 73 L424 58" stroke="{led_color}" stroke-width="3" stroke-linecap="round"/>
            <text x="34" y="39" fill="#c4d2ef" font-size="15">Vin</text>
            <text x="115" y="195" fill="#c4d2ef" font-size="14">Transistor</text>
            <text x="260" y="195" fill="#c4d2ef" font-size="14">Rload</text>
            <text x="383" y="145" fill="#c4d2ef" font-size="14">LED</text>
          </svg>
          <div style="font-size:1.35rem;font-weight:700;color:{'#ff879c' if on else '#a9b7d4'};">LED {'ON' if on else 'OFF'}</div>
          <div style="color:#a9b7d4;font-size:.9rem;">Illustrative switch model</div>
        </div>
        """, unsafe_allow_html=True)
        m1,m2,m3 = st.columns(3)
        m1.metric("Switch state", "ON" if on else "OFF")
        m2.metric("Load current", f"{current_ma:.2f} mA")
        m3.metric("Illustrative Vout", f"{vout:.2f} V")
    st.info("Concept link: a transistor can act as a switch. The circuit represents a classical signal that is interpreted as a LOW (0) or HIGH (1). Real transistor behaviour depends on device type, biasing and circuit configuration.")

# ---------- Module B ----------
elif module == "B · Logic Gates":
    st.title("Module B · Classical Logic Gates")
    st.write("Change the input bits and observe the output. Select a gate to see its truth table.")
    gate = st.selectbox("Choose a logic gate", ["NOT", "AND", "OR", "NAND", "NOR", "XOR"])
    c1,c2 = st.columns(2)
    with c1:
        a = st.toggle("Input A = 1", value=False)
    with c2:
        b = st.toggle("Input B = 1", value=False, disabled=(gate=="NOT"))
    A, B = int(a), int(b)
    if gate == "NOT":
        out = 1-A
        expression = f"NOT {A} = {out}"
    else:
        fn = {
            "AND": lambda x,y: x & y,
            "OR": lambda x,y: x | y,
            "NAND": lambda x,y: 1-(x & y),
            "NOR": lambda x,y: 1-(x | y),
            "XOR": lambda x,y: x ^ y,
        }[gate]
        out = fn(A,B)
        expression = f"{A} {gate} {B} = {out}"
    x,y,z = st.columns(3)
    x.metric("Input A", A)
    y.metric("Input B", "—" if gate=="NOT" else B)
    z.metric("Output", out)
    st.success(f"**Live result:** `{expression}`")
    rows = []
    for aa in [0,1]:
        for bb in ([0] if gate=="NOT" else [0,1]):
            oo = 1-aa if gate=="NOT" else fn(aa,bb)
            rows.append({"A":aa, **({} if gate=="NOT" else {"B":bb}), "Output":oo})
    st.markdown("### Truth table")
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
    st.caption("Classical logic gates operate on definite binary inputs and produce definite binary outputs.")

# ---------- Module C ----------
elif module == "C · Quantum Lab":
    st.title("Module C · Quantum Gate Simulator")
    st.write("Apply quantum gates to a qubit, inspect its amplitudes, and sample measurement outcomes.")
    st.caption("State-vector simulation uses NumPy. A Qiskit circuit equivalent is shown below when Qiskit is installed.")
    zero = np.array([1+0j,0+0j], dtype=complex)
    one = np.array([0+0j,1+0j], dtype=complex)
    H = (1/np.sqrt(2))*np.array([[1,1],[1,-1]], dtype=complex)
    X = np.array([[0,1],[1,0]], dtype=complex)
    Z = np.array([[1,0],[0,-1]], dtype=complex)
    initial = st.radio("Initial state", ["|0⟩", "|1⟩"], horizontal=True)
    gates = st.multiselect("Apply gates in order", ["X", "H", "Z"], default=["H"])
    state = zero.copy() if initial=="|0⟩" else one.copy()
    for g in gates:
        state = {"X":X, "H":H, "Z":Z}[g] @ state
    probs = np.abs(state)**2
    c1,c2,c3 = st.columns(3)
    c1.metric("P(0)", f"{probs[0]*100:.2f}%")
    c2.metric("P(1)", f"{probs[1]*100:.2f}%")
    c3.metric("Normalisation", f"{np.sum(probs):.3f}")
    st.markdown("### State amplitudes")
    st.code(f"|ψ⟩ = ({state[0].real:+.3f}{state[0].imag:+.3f}i)|0⟩ + ({state[1].real:+.3f}{state[1].imag:+.3f}i)|1⟩", language="text")
    shots = st.slider("Measurement shots", 10, 2000, 200, 10)
    if st.button("▶ Run measurement", type="primary"):
        counts = np.random.default_rng().multinomial(shots, probs)
        st.session_state["quantum_counts"] = {"0": int(counts[0]), "1": int(counts[1]), "shots": shots}
    counts = st.session_state.get("quantum_counts")
    if counts:
        total = counts["shots"]
        cc1,cc2 = st.columns(2)
        cc1.metric("Measured 0", counts["0"])
        cc2.metric("Measured 1", counts["1"])
        st.bar_chart(pd.DataFrame({"Counts":[counts["0"],counts["1"]]}, index=["0","1"]))
        st.caption(f"Observed frequencies from {total} simulated shots. Re-run to sample a new finite set of outcomes.")
    st.markdown("### Two-qubit CNOT demonstration")
    control = st.selectbox("Control qubit", ["0", "1"], index=0)
    target = st.selectbox("Target qubit", ["0", "1"], index=1)
    if control == target:
        st.warning("Choose different qubits for control and target.")
    else:
        initial_pair = st.selectbox("Initial two-qubit state", ["|00⟩", "|01⟩", "|10⟩", "|11⟩"])
        bits = [int(initial_pair[1]), int(initial_pair[2])]
        # CNOT flips the target iff control is 1; state label uses q0q1 ordering.
        if bits[int(control)] == 1:
            bits[int(target)] ^= 1
        st.success(f"CNOT output basis state: |{bits[0]}{bits[1]}⟩")
    with st.expander("Qiskit circuit equivalent"):
        try:
            from qiskit import QuantumCircuit
            qc = QuantumCircuit(1,1)
            for g in gates:
                getattr(qc, g.lower())(0)
            qc.measure(0,0)
            st.code(str(qc), language="text")
            st.caption("The state-vector probabilities above are computed with NumPy. This Qiskit circuit is the corresponding gate-and-measurement circuit.")
        except Exception:
            st.code("from qiskit import QuantumCircuit\nqc = QuantumCircuit(1, 1)\nqc.h(0)  # replace with selected gate sequence\nqc.measure(0, 0)\nprint(qc)", language="python")
            st.caption("Install Qiskit to render the circuit object in this section.")
    st.info("An H gate applied to |0⟩ creates equal measurement probabilities. Measurement returns a classical result; it does not reveal both basis states in a single measurement.")

# ---------- Module D ----------
else:
    st.title("Module D · Compare, Noise & Learn")
    st.write("Connect the familiar classical model to quantum information, then explore how noise changes outputs.")
    st.markdown("### Classical-to-quantum mapping")
    comparison = pd.DataFrame([
        ["Information unit", "Bit: 0 or 1", "Qubit: α|0⟩ + β|1⟩"],
        ["Basic switching / inversion", "Transistor switch / NOT gate", "X gate flips basis states"],
        ["Other operations", "AND, OR, NAND, NOR, XOR", "H, Z, CNOT and other quantum gates"],
        ["Reading result", "Read a definite digital output", "Measure to obtain a classical result"],
        ["Noise", "Voltage/current disturbances", "Errors affecting quantum states and gates"],
        ["Typical output model", "Deterministic for fixed ideal inputs", "Measurement can be probabilistic"],
    ], columns=["Concept", "Classical electronics", "Quantum computing"])
    st.dataframe(comparison, use_container_width=True, hide_index=True)
    st.markdown("### Classical switching noise")
    c1,c2 = st.columns(2)
    with c1:
        ideal_v = st.slider("Ideal input voltage (V)", 0.0, 5.0, 0.65, 0.05)
        thresh = st.slider("Threshold voltage (V)", 0.1, 3.0, 0.7, 0.05)
        noise_amp = st.slider("Noise amplitude (± V)", 0.0, 1.5, 0.2, 0.05)
        samples = st.slider("Number of simulated samples", 20, 500, 100, 20)
        seed = st.number_input("Random seed (repeatable example)", min_value=0, max_value=9999, value=42)
    rng = np.random.default_rng(int(seed))
    noise = rng.uniform(-noise_amp, noise_amp, int(samples))
    noisy_v = ideal_v + noise
    outputs = (noisy_v >= thresh).astype(int)
    ideal_out = int(ideal_v >= thresh)
    with c2:
        st.metric("Ideal output", ideal_out)
        st.metric("Noisy HIGH samples", int(outputs.sum()))
        st.metric("Output changes vs ideal", int(np.sum(outputs != ideal_out)))
        chart_df = pd.DataFrame({"Noisy input (V)": noisy_v, "Threshold (V)": np.full(int(samples), thresh)})
        st.line_chart(chart_df)
    st.caption("This is an illustrative threshold model with synthetic noise, not a measured transistor trace.")
    st.markdown("### Quantum noise concepts")
    n1,n2,n3 = st.columns(3)
    n1.markdown("**Bit-flip error**\n\nCan change |0⟩ ↔ |1⟩, represented by an X error.")
    n2.markdown("**Phase-flip error**\n\nChanges the relative phase of quantum amplitudes, represented by a Z error.")
    n3.markdown("**Depolarising noise**\n\nA simplified noise model that randomly introduces Pauli errors.")
    with st.expander("What is quantum error correction?"):
        st.write("Quantum error correction encodes quantum information across multiple physical qubits so that certain errors can be detected and corrected without directly measuring and destroying the encoded logical state. It requires extra qubits and carefully designed operations.")
    st.markdown("### Quick knowledge check")
    questions = [
        ("Which component can be used as an electronic switch?", ["Transistor", "Capacitor", "Inductor"], 0),
        ("Which quantum gate flips |0⟩ and |1⟩?", ["H", "X", "Z"], 1),
        ("What does an H gate do to |0⟩ before measurement?", ["Always gives 0", "Equal probabilities for 0 and 1", "Always gives 1"], 1),
        ("Which is a quantum noise error type?", ["Phase flip", "Ohm's law", "Kirchhoff loop"], 0),
    ]
    score = 0
    answers = []
    for i,(q,opts,correct) in enumerate(questions):
        ans = st.radio(q, opts, key=f"quiz_{i}")
        answers.append(opts.index(ans)==correct)
    if st.button("Check quiz answers"):
        score = sum(answers)
        st.success(f"Your score: {score}/{len(questions)}")
        if score == len(questions):
            st.balloons()
        else:
            st.info("Review the comparison table and try again.")

st.divider()
st.markdown('<p class="small-muted">Transistor to Qubit Lab · Educational simulation · Classical bits → Quantum states</p>', unsafe_allow_html=True)
