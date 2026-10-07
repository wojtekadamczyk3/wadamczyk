# Chapter 3b: Universal gates, Reversible irreversability, Oracle Functions

## 3.5. Universal sets of gates
$\mathcal{S}$ is _universal set of gates for quantum computing_ if for any $n \in \mathbb{N}$ an arbitrary unitary operation $U \in \mathcal{U}(n)$ can be implemented to arbitrary precision using only elementary gates from $\mathcal{S}$. Elementary gates are assumed to take $O(1)$ time.

- Examples of the universal set of gates:
    - $\{CNOT\} \cup \mathcal{U}(2)$
    - $\{CNOT, H, T\}$
    - $\{\text{Toffoli}, H\}$

For any fixed universal set $\mathcal{S}$, a generic unitary matrix on _n_ qubits requires exponentially many elementary gates _n_ to be implemented - this follows from the fact that an n-qubit unitary is determined by $O(4^n)$ real parameters. Goal of quantum computing is to find efficient quantum circuits which use poly(n) qubits and poly(n) elementary gates to solve a problem on an input size _n_.

## 3.6. Simulating Classical Circuits on a Quantum Machine $\left(\mathbf{B P P} \subset \mathbf{B Q P}\right)$
A _classical circuit_ is a sequence of logical operations that act on a small number of bits (AND, OR, NOT). We claim that quantum computation is at least as powerfull as classical computation $\mathbf{B P P} \subset \mathbf{B Q P}$. However, the difficulty in proving it arise when we try to translate irreversible classical operations, such as AND or OR, to quantum gates.Quantum operations are unitary, hence reversible. This poses a problem:

The crucial step in showing that one can simulate any classical circuit with a quantum circuit involves showing that any classical boolean operation (even irreversible) can be represented through reversible operation on larger hilbert space. The key point is that if we operate with unitaries on a larger space, but we only look at the subspace, it will look like the operation is non-unitary, (irreversible).

**Claim**: If $f: B_m \rightarrow B_n$ is a Boolean function it can be expressed in an equivalent _reversible_ form $\tilde{f}: B_{m+n} \rightarrow B_{m+n}$.

**Remark**: The claim by itself is simply logic and has nothing to do with quantum computing.

**Proof**:
Consider an binary addition operation $\oplus$ (adding mod 2). For any $f: B_m \rightarrow B_n$ define $\tilde{f}:B_{m+n}\rightarrow B_{m+n}$, where $\tilde{f}(b, c)=(b, c \oplus f(b))$. Such function is reversible, as applying the function twice results in $(b, c \oplus f(b) \oplus f(b)) = (b, c \oplus 0) = (b, c)$. If we initialise the second register with $c=0...0$, then $\tilde{f}(b, c) = (b, f(b))$.

**Conclusion**: Through this we satisfied our requirement to represent an irreversible function $f$ as a reversible function $\tilde{f}$. By replacing all (now reversible) classical gates with quantum gates, one can obtain quantum circuit that simulates the classical one.

## 3.7. Oracle for Boolean function:
### Quantum Oracle
A _quantum oracle for any Boolean function_ $f:B_n\rightarrow B_m$ will be the quantum gate denoted $O_f$ on $n+m$ qubits defined by its action on basis states as follows. Sometimes we refer to n-qubit register $\left|x\right>$ and the m-qubit register $\left|y\right>$ as the _input_ and _output_ registers respectively
$$
O_f\left|x\right>\left|y\right>=\left|x\right>\left|y \oplus f(x)\right> \quad \text { for all } x \in B_n \text { and } y \in B_m
$$
### Phase Oracle
A _phase oracle_ will be quantum gate denoted $U_f$ on $n+m$ qubits defined by its action on basis states as follows 
$$
U_f\left|x\right>=(-1)^{f(x)}\left|x\right>
$$

This can be achieved through $O_f$
$$
O_f\left|x\right>\left|-\right>=O_f \left|x\right> \frac{1}{\sqrt{2}}(\left|0\right>-\left|1\right>)=\frac{1}{\sqrt{2}}(\left|x\right>\left|f(x)\right>-\left|x\right>\left|1 \oplus f(x)\right>)=(-1)^{f(x)}\left|x\right>\left|-\right>
$$

## 3.8. Query Complexity:
Let us for a second come back to the complexity classes. In computation it is quite often tricky to consider all gates that are involved in the circuit. But in the end, quite often, we dont care what is the exact time complexity of the circuit. What we rather care about, is how does the complexity of the classical algorithm compares with the complexity of the quantum algorithm.

And for this, we can group the gates into _queries_ - both for classical computation and for quantum computation. For instance, an oracle function $O_f$ is just a collection of gates. We also know that the complexity of the quantum oracle is at least as efficient as the classical oracle.

This means that if we find that the quantum algorithm is more efficient in the number of queries than the classical algorithm, then the quantum time complexity is definitely better than the classical one.

_Query complexity_ is the number of times we need to apply the oracle to the circuit.

## 3.9. Computation by quantum parallelism:
Now we can talk about what happens when we apply the oracle to a state in a superposition. This is the heart of what makes quantum computers powerful. Consider we have a state in a superposition of all possible inputs $\left|\psi\right> = \frac{1}{\sqrt{2^n}}\sum_x\left|x\right>\left|0\right>$. Then if we apply the oracle to this state, we get:

$$
O_f\left|\psi\right> = \frac{1}{\sqrt{2^n}}\sum_x O_f\left|x\right>\left|0\right> = \frac{1}{\sqrt{2^n}}\sum_x \left|x\right>\left|f(x)\right>
$$

This is what we call the computation by _quantum parallelism_. Fundamentally this is what differentiates quantum computing from classical computing. In classical computing we cannot have states that are in superposition of different inputs. In quantum computing we can, and this allows us to compute the function in parallel for all possible inputs.

Problem however is that we dont have a conclusive result from this, if we don't do anything with the result. Consider we now perform a projective measurement on the first register. Then through measuring $\left|x\right>$, we can only learn the value of $f(x)$ for a single $x$. 

Therefore we need to be somewhat more smart what we do with the superposition. This is what you will learn in the next chapter, where we will show how to use the superposition to solve some problems. This is connected to the idea of using interference to solve problems.

<span style="color:red">This subchapter needs some revision to get the point across</span>

## Notes:
- Things we havent talk about in detail is the concept of universal sets of quantum gates, and the approximately universal sets of gates.

