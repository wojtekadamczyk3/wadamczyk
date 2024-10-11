# Chapter 2a: Quantum Information

Initially I didn't want to talk much about quantum information theory. In my mind there is another course that deals with it in much more detail (Quantum Information Theory). However, because of the nature of the lecture I will briefly introduce a few concepts.

## 2.1. Nature of Quantum Information:
- Quantum information is different from the classical information in a sense that the measurements corrupts the state itself
- We can prepare any desired _pure_ state, but if we receive such pure state we cannot identify it with certainty (if we dont know how to measure it)
- Given a unknown quantum state $\left|\psi\right>$ there are three basic operations that we can perform:
    - **Ancilla** - take a second, known, quantum system $\left|A\right>$ and join it with $\left|\psi\right>$ and treat it as a composite system $\left|\psi\right> \otimes \left|A\right>$
    - **Unitary** - we can perform a unitary on $\left|\psi\right>$ and obtain $\left|\psi^{\prime}\right> = U\left|\psi\right>$
    - **Measurement** - we can perform a measurement on $\left|\psi\right>$, or sub-system of it, record the outcome and retain the post-measurement state for further processing
- Any quantum operation can be described as a composition of these three operations

## 2.2. No-Cloning Theorem:
- Cloning operation of a quantum state $\left|\psi\right>$ is defined as a map $\left|\psi\right>_A \left|0\right>_B \rightarrow \left|\psi\right>_A \left|\psi\right>_B$
- We can extend it to a larger system, by adjoining ancilla to it. In this case the cloning operations can be defined as $\left|\psi\right>_A \left|0\right>_B \left|M_0\right>_M \rightarrow \left|\psi\right>_A \left|\psi\right>_B \left|M_\psi\right>_M$
- **No-Cloning Theorem**: Let $\mathcal{S}$ be any set of states of A that contains at least one non-orthogonal state. Then there is no unitary cloning process that achieves cloning for all states in $\mathcal{S}$.
- **Remark**: I am presenting only proof that such there exist no unitary process, however there exist an extention of the theorem for any 3 basic operations that one can perform (Ancilla, Unitary, Measurement).

### Proof:
Let $\left|\psi\right>$ and $\left|\phi\right>$ be two distinct non-orthogonal states in $\mathcal{S}$. Lets assume that there exist a unitary $U$ that clone the states in $\mathcal{S}$.

then

$$
U\left|\psi\right>_A \left|0\right>_B \left|M_0\right>_M = \left|\psi\right>_A \left|\psi\right>_B \left|M_\psi\right>_M
$$
$$
U\left|\phi\right>_A \left|0\right>_B \left|M_0\right>_M = \left|\phi\right>_A \left|\phi\right>_B \left|M_\phi\right>_M
$$

then 

$$
\left<M_0\right|_M\left<0\right|_B\left<\psi\right|_A U^\dag U\left|\phi\right>_A \left|0\right>_B \left|M_0\right>_M = \left<M_\psi\right|_M \left<\psi\right|_B \left<\psi\right|_A \left|\phi\right>_A \left|\phi\right>_B \left|M_\phi\right>_M
$$



$$
\left<M_0|M_0\right>_M\left<0|0\right>_B\left<\psi|\phi\right>_A = \left<M_\psi|M_\psi\right>_M\left<\psi|\phi\right>_A\left<\psi|\phi\right>_B
$$

$$
\left<\psi|\phi\right>_A = \left<M_\psi|M_\phi\right>_M\left<\psi|\phi\right>_A\left<\psi|\phi\right>_B
$$

since $\left|\psi\right>$ and $\left|\phi\right>$ are non-orthogonal, we can divide both sides by $\left<\psi|\phi\right>_A$ and get:

$$
1 = |\left<M_\psi|M_\phi\right>_M\left<\psi|\phi\right>_B|
$$

- $M_\psi$ and $M_\phi$ are quantum states: $|\left<M_\psi|M_\phi\right>_M| \leq 1$,  
- $\left|\psi\right>$ and $\left|\phi\right>$ are distinct states and so: $|\left<\psi|\phi\right>_B| < 1$
- Therefore we arrive to a contradiction, which **completes the proof**

### Herbert's method of superluminal communication:
- The no-cloning theorem was crucial for debugging the protocol of superluminal communication proposed by Herbert.
...

## 2.3. Quantum Teleportation:
Consider that Alice and Bob share an entangled Bell state $\left|\phi^{+}\right>_{23} = \frac{1}{\sqrt{2}}(\left|00\right> + \left|11\right>)_{23}$, such that each of them has one qubit. Additionally Alice has a qubit in state $\left|\alpha\right>_1 = a\left|0\right> + b \left|1\right>$. 

This means that the combined state of the system is:

$$
\begin{aligned}
\left|\psi\right>_{AB} &= \left|\alpha\right>_1 \left|\phi^{+}\right>_{23} = \left(a\left|0\right> + b\left|1\right>\right)_1 \frac{1}{\sqrt{2}}(\left|00\right> + \left|11\right>)_{23} \\
& = \frac{a}{\sqrt{2}}\left|000\right> + \frac{a}{\sqrt{2}}\left|011\right> + \frac{b}{\sqrt{2}}\left|100\right> + \frac{b}{\sqrt{2}}\left|111\right>
\end{aligned}
$$

**Task**: of quantum teleportation is to transfer the state of $\left|\alpha\right>_1$ to $\left|\beta\right>_3$ by performing local operations and classical communication.

**Algorithm**:
1. Alice performs a Bell measurement on the two qubits
    <!-- 1. Alice applies CX to her qubits 1 and 2
    2. Alice applies H to her qubit 1
    3. Alice measures her two qbits to obtain a 2-bit string 00, 01, 10 or 11 -->
2. Alice sends a 2-bit measurement outcome ij to Bob
3. On receiving ij Bob applies the unitary operation $Z^iX^j$ to his qubit, which is then guaranteed to be in state $\left|\alpha\right>_3$

**Why it works**:

**Explanation 1**:

We can write $\left|\psi\right>_{AB}$ as:

$$
\begin{aligned}
\left|\psi\right>_{AB} &= \frac{a}{\sqrt{2}}\left|000\right> + \frac{a}{\sqrt{2}}\left|011\right> + \frac{b}{\sqrt{2}}\left|100\right> + \frac{b}{\sqrt{2}}\left|111\right>\\
&= \frac{a}{2}\left(\left|\psi_{00}\right> + \left|\psi_{01}\right>\right)\left|0\right> + \frac{a}{2}\left(\left|\psi_{10}\right> + \left|\psi_{11}\right>\right)\left|1\right> + \frac{b}{2}\left(\left|\psi_{10}\right> - \left|\psi_{11}\right>\right)\left|0\right> + \frac{b}{2}\left(\left|\psi_{00}\right> - \left|\psi_{01}\right>\right)\left|1\right> \\
&= \left|\psi_{00}\right>\left(\frac{a}{2}\left|0\right> + \frac{b}{2}\left|1\right>\right) + \left|\psi_{01}\right>\left(\frac{a}{2}\left|0\right> - \frac{b}{2}\left|1\right>\right) + \left|\psi_{10}\right>\left(\frac{a}{2}\left|1\right> + \frac{b}{2}\left|0\right>\right) + \left|\psi_{11}\right>\left(\frac{a}{2}\left|1\right> - \frac{b}{2}\left|0\right>\right)\\
\end{aligned}
$$

Therefore when we measure in which bell state the first two qubits are then we get the following post-measurement states:

$$
\begin{array}{cc}
\text { mmt outcome } & \text { post-mmt state } \\
00 & \left|00\right>_{12}\left|\alpha\right>_3 \\
01 & \left|01\right>_{12}X\left|\alpha\right>_3 \\
10 & \left|10\right>_{12}Z\left|\alpha\right>_3 \\
11 & \left|11\right>_{12}XZ\left|\alpha\right>_3
\end{array}
$$

Therefore knowing the outcome of the measurement Alice can send a 2-bit string to Bob, who then applies the corresponding operation to his qubit and recovers the state $\left|\alpha\right>_3$

**Explanation 2**:

What I would like to do here is to provide slightly different explanation. I don't like Explanation 1 because it feels very brute forcy, and it doesn't provide any additional intuition about why things are, like they are. The following explanation is perhaps slightly more tricky to grasp, but I think it provides more insight.

**E. step (2.1.)**

I would like to start with a simple observation:

When we project the first two qubits into the state $\left|\psi_{00}\right>_{12}$ then we get:

$$
\left<\psi_{00}\right|_{12}\left|\alpha\right>_1\left|\psi_{00}\right>_{23} = \left|\alpha\right>_3
$$

One might then ask is it true for more general case?

Is this statement true for any state $\left|\psi_{ij}\right>_{23}$:

$$
\left<\psi_{ij}\right|_{12}\left|\alpha\right>_1\left|\psi_{ij}\right>_{23} \stackrel{?}{=} \left|\alpha\right>_3
$$

This must be true as we can write 

$$
\left<\psi_{ij}\right|_{12}\left|\alpha\right>_1\left|\psi_{ij}\right>_{23} = \left(\left<\psi_{00}\right|_{12} X_2^i Z_2^j\right)\left|\alpha\right>_1\left(X_2^i Z_2^j\left|\psi_{00}\right>_{23}\right) = \left<\psi_{00}\right|_{12}\left|\alpha\right>_1\left|\psi_{00}\right>_{23}= \left|\alpha\right>_3
$$

- So in a way the quantum teleportation would be extreamaly trivial if we could perform a projection operation on the first two qubits. Such operations however is non-unitary and therefore we need to find a workaround.

- Something that performs a projection operation on the first two qubits is the Bell measurement. This will, however, perform a projective measurement to an arbitrary state and not just the $\left|\psi_{00}\right>_{12}$. 

- Can we somehow combine all the operations that we can perform on a quantum states and obtain required special projection operation?
- Somehow we would like to rotate the state into the basis

**E. step (2.2.)**

$$
\left( \left<\psi_{ij}\right|_{12} \otimes \mathbb{I}_3\right) \left( \mathbb{I}_{12} \otimes X_3^i Z_3^j\right) \left|\psi\right>_{AB} = \left( \mathbb{I}_{12} \otimes X_3^i Z_3^j\right) \left( \left<\psi_{ij}\right|_{12} \otimes \mathbb{I}_3\right) \left|\psi\right>_{AB}  = \left|\alpha\right>_3
$$





**Remark**:
- No information about $\left|\alpha\right>_2$ is left with Alice


    