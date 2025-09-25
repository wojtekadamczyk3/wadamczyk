# Chapter 1a: Principles of Quantum Mechanics

## 1.1. Hilbert spaces:

**Hilbert Space**:

A Hilbert space is the mathematical stage on which quantum mechanics plays out. Formally, it is a vector space $\mathcal{H}$ over the complex numbers $\mathbb{C}$, equipped with a complete inner product.
- Vector space: This simply means we can take linear combinations of elements (called vectors) and remain within the space.
- Inner product: A rule that allows us to compute angles and lengths, generalizing the familiar dot product. It is a map $(\cdot , \cdot): \mathcal{H} \times \mathcal{H} \to \mathbb{C}.$
- Completeness: A technical requirement ensuring that limits of convergent sequences of vectors remain in the space. (For our purposes, this subtlety will not play an important role, but it guarantees the mathematical consistency of the theory.)

The inner product satisfies four key properties:

$$
\begin{aligned}
\text { conjugate symmetry } & (\phi, \psi)=\overline{(\psi, \phi)} \\
\text { linearity } & (\phi, a \psi)=a(\phi, \psi) \\
\text { additivity } & (\phi, \psi+\chi)=(\phi, \psi)+(\phi, \chi) \\
\text { positive-definiteness } & (\psi, \psi) \geq 0 \forall \psi \in \mathcal{H}
\end{aligned}
$$

From the inner product we can define the norm (or length) of a vector:

$$
|\psi| \equiv \sqrt{(\psi, \psi)}.
$$

This norm equips $\mathcal{H}$ with a metric, allowing us to measure distances between states.

Finally, in quantum mechanics, states of a system are represented by vectors $\psi \in \mathcal{H}$. This simple but powerful idea-representing physical states as elements of a Hilbert space-is the foundation of the entire theory.

**Dual Spaces**:

Dual space $\mathcal{H^*}$ of a $\mathcal{H}$ is the space of linear maps $\mathcal{H} \rightarrow \mathbb{C}$. That is, an element $\phi \in \mathcal{H^*}$ defines a map $\varphi: \psi \mapsto \varphi(\psi) \in \mathbb{C}$ for every $\psi \in \mathcal{H}$, such that 

$$
\varphi: a \psi_1+b \psi_2 \mapsto a \varphi\left(\psi_1\right)+b \varphi\left(\psi_2\right)
$$

One of the dual space $\mathcal{H^*}$ is for instance the inner product $(\phi, \quad) \in \mathcal{H}^*$ for $\phi \in \mathcal{H}$, where 

$$
(\phi, \quad): \psi \mapsto(\phi, \psi)
$$

## 1.2. Dirac Notation:
In quantum mechanics quite often we often switch basis. This is because intrinsically any measurement causes a collapse onto the measurement basis. Because of this we want to have a notation that allows us to work with multiple basis at the same time, and not get confused. Dirac notation (empirically) provides this clarity. It is difficult to formally define the notation, and quite often when one does it, they get confused (unless they are deep down in theory). Therefore I would propose to learn it through learning the basic few properties and then trying things out. 

Dirac denotes element of $\mathcal{H}$ as $\left|\psi\right>$ _'ket'_, and an element of the dual space is written as $\mathcal{H^*}$ as $\left<\psi\right|$ _'bra'_. The inner product between two states $\left|\psi\right>, \left|\phi\right> \in \mathcal{H}$ is written as $\left<\psi|\phi\right>$.
> In notes the bra-ket notation is introduced using homomorphisms (linear maps). I find it unecessary.

- The advantage of using bra-ket notation is:
    - We can talk about multiple things at the same time - Dirac notation is effectively just a label that points to an abstract object in the Hilbert space. We don't need to specify whether the variable is contineous, or if it is a vector or a function.
    - Allows us to label states by their eigenvalues
    - Somehow it is more natural and causes less confusion

## 1.3. Operators:
- A _linear operator_ A is a map $A : \mathcal{H} \rightarrow \mathcal{H}$ that is compatible with the vector space structure $A(c_1\left|\phi_1\right> + c_2\left|\phi_2\right>) = c_1A\left|\phi_1\right> + c_2A\left|\phi_2\right>$
- All operators in Quantum Mechanics are linear, hence we will call them just 'operators'
- Operators form algebra
    - Sum: $(\alpha A+\beta B):\left|\phi\right> \mapsto \alpha A\left|\phi\right>+\beta B\left|\phi\right>$
    - Product: $A B: \phi \mapsto A \circ B\left|\phi\right>=A(B\left|\phi\right>)$
    - _Commutator_: $[A, B]=A B-B A$
- A state $\psi \in \mathcal{H}$ is said to be an _eigenstate_ of an operator A if $A\left|\psi\right> = a_\psi\left|\psi\right>$ with an associated _eigenvalue_ '$a_\psi$'.
- _Adjoint_ $A^\dagger$ of an operator $A$ is defined as $\left<\phi\right|A^{\dagger}\left| \psi\right>=\overline{\left<\psi\right|A\left| \phi\right>} \quad$
- An operator $Q$ is called _Hermitian_ if $Q^\dagger=Q$
- An operator $U$ is called _Unitary_ if $U^\dagger U= U U^\dagger = \mathbb{I}$
- An operator $\Pi$ is called _Projector_ if $\Pi\Pi= \Pi$

## 1.4. Composite systems:
**Tensor Product**

- _Tensor product_ $\mathcal{H}_1 \otimes \mathcal{H}_2$ is a vector space over $\mathbb{C}$ spanned by all pairs of elements $\left|e_a\right> \otimes\left|f_\alpha\right>$, where $\left|e_a\right> \in \mathcal{H_1}$, $\left|f_\alpha\right> \in \mathcal{H_2}$
- It is not true that a general element of $\mathcal{H}_1 \otimes \mathcal{H}_2$ necessarily takes the form $\left|\psi_1\right>\otimes\left|\psi_2\right>$
- Rahter, a general element may be written as $\left|\Psi\right>=\sum_{a, \alpha} r_{a \alpha}\left|e_a\right> \otimes\left|f_\alpha\right>$
- Elements of the form $\left|\psi_1\right>\otimes\left|\psi_2\right>$ are called simple, and the elements of the form $\left|\Psi\right>=\sum_{a, \alpha} r_{a \alpha}\left|e_a\right> \otimes\left|f_\alpha\right>$ are refered as entangled
- $\left<\alpha\otimes\beta|\alpha'\otimes\beta'\right> := \left<\alpha|\alpha'\right>\left<\beta|\beta'\right>$
- $\left( S_\alpha \otimes T_\beta \right)\left(\alpha \otimes \beta\right) = \left(S_\alpha\alpha\right)\otimes\left(T_\beta\beta\right)$ - apologies for being slightly sloppy - I think it is understandable what I mean though

**Tensor Product in action (states)**

>- Let's as an example consider that our states $\left|\alpha\right>_A \text{ and } \left|\beta\right>_B$ live both in $\mathbb{C}^2_A$ and $\mathbb{C}^2_B$ respectively. Then we can pick orthonormal basis of $\mathbb{C}^2_A$ to be $\left\{\left|u_1\right>_A, \left|u_2\right>_A \right\}$, and of $\mathbb{C}^2_B$ to be $\left\{\left|v_1\right>_B, \left|v_2\right>_B \right\}$
>- Then one can write $\left|\alpha\right>_A = a_1 \left|u_1\right>_A + a_2 \left|u_2\right>_A = a_1 \begin{pmatrix} 1\\ 0 \end{pmatrix}_A + a_2 \begin{pmatrix} 0\\ 1 \end{pmatrix}_A$,
>- and $\left|\beta\right>_B = b_1 \left|v_1\right>_B + b_2 \left|v_2\right>_B = b_1 \begin{pmatrix} 1\\ 0 \end{pmatrix}_B + b_2 \begin{pmatrix} 0\\ 1 \end{pmatrix}_B$
>- This means that one can write 

>$$
\left|\alpha\right>_A \otimes \left|\beta\right>_B = \begin{pmatrix} a_1\\ a_2 \end{pmatrix}_A \otimes \begin{pmatrix} b_1\\ b_2 \end{pmatrix}_B = \begin{pmatrix} a_1b_1\\ a_1b_2\\ a_2b_1\\ a_2b_2 \end{pmatrix}
$$

>- or sticking to the Dirac notation:

>$$
\left|\alpha\right>_A \otimes \left|\beta\right>_B = \sum_{i,j} a_i b_j \left|u_i\right>_A \otimes \left|v_j\right>_B
$$

**Tensor Product in action (operators)**

>- For operators $A$ and $B$ that live in $\mathbb{C}^2_A$ and $\mathbb{C}^2_B$ respectively, one can write $A = \sum_{i,j} a_{ij} \left|u_i\right>_A \left<u_j\right|$ and $B = \sum_{i,j} b_{ij} \left|v_i\right>_B \left<v_j\right|$
>- This means:

>$$
A \otimes B = \sum_{i,j,k,\ell} a_{ij} b_{k\ell} \left|u_i\right>_A \otimes \left|v_k\right>_B \left<u_j\right|\otimes\left<v_\ell\right|
$$

>- or in a matrix form:

>$$
A \otimes B = \begin{pmatrix}
a_{11}B & a_{12}B\\
a_{21}B & a_{22}B
\end{pmatrix} = \begin{pmatrix}
a_{11}b_{11} & a_{11}b_{12} & a_{12}b_{11} & a_{12}b_{12}\\
a_{11}b_{21} & a_{11}b_{22} & a_{12}b_{21} & a_{12}b_{22}\\
a_{21}b_{11} & a_{21}b_{12} & a_{22}b_{11} & a_{22}b_{12}\\
a_{21}b_{21} & a_{21}b_{22} & a_{22}b_{21} & a_{22}b_{22}\\
\end{pmatrix}
$$


## 1.5. Postulates of Quantum Mechanics:
- **(1) A _quantum system_ A** is associated with complex Hilber space $\mathcal{H}$. **A _physical state_** of an isolated system is represented by a normalised vector $\left|\psi\right> \in \mathcal{H}$, which is unique up to a phase factor
- **(2) The evolution** of an isolated quantum system is reversible. In this formalism this corresponds to unitary evolution of the form $\left|\psi\right> \mapsto U\left|\psi\right>$ for $U \in \mathcal{U}(\mathcal{H})$, i.e. $U^{\dagger} U=U U^{\dagger}=\mathbb{I}$. The unitary is unique up to a phase factor
- **(3) Composite system** - For two quantum system A, and B with associated Hilber spaces $\mathcal{H_A}$ and $\mathcal{H_B}$ the Hilbert space $\mathcal{H_{AB}}$ associated with the composite system AB is isomorphic to the tensor product $\mathcal{H_A}\otimes\mathcal{H_B}$. For unitary operation on the subsystem we use: $U_A \otimes \mathbb{I}_B\left|i j\right>_{A B} \equiv U_A\left|i j\right>_{A B}$
- **(4) Measurement** - A projective measurement on a quantum system with outcomes labelled ${x}_x$ is associated with a set of projectors ${\Pi_x}x$ satisfying $\sum_x \Pi_x = \mathbb{I}$. 
    - Probability of getting outcome x when measuring state $\left|\psi\right>$ is given by the Born rule: $Pr[x \mid \psi]=\left\langle\psi\left|\Pi_x\right| \psi\right\rangle$
    - Post-measurement state is given the outcome x is $\left|\psi_x^{\prime}\right>=\frac{1}{\sqrt{\operatorname{Pr}[x \mid \psi]}} \Pi_x\left|\psi\right>=\frac{\Pi_x\left|\psi\right>}{\sqrt{\left\langle\psi\left|\Pi_x\right| \psi\right\rangle}}$


