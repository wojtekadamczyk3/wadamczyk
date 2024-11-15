# Chapter 6: Density Matrix Formalism:

## 6.0. Extending the closed quantum system formalism to consider the open quantum systems:

The necessity for density matrix formalism arises from two reasons. Firstly, sometimes we are not quite sure about the state of the system. When this happens we dont want to be constrained to the pure states only. We need to describe such system with a probability distribution over the states. Secondly even if we are sure about the state of the system, then the unitary evolution of the larger system can be seen as non-unitary evolution on its subsystem. We would like to describe such evolution as well, as quite often we are not interested in the whole system, but only in some part of it. I will only briefly touch upon the formalism of the density matrices.

## 6.1. Density Matrix:

If you are not familiar with the density matrices - have a look at Philip Kammelander QIP notes. Here I will only provide a brief set of definitions. 

- Density operator (also called density matrix), $\rho$, is defined as $\rho = \sum_i p_i \left|\psi_i\right>\left<\psi_i\right|$
- Set of quantum states $\mathcal{S}\left(\mathcal{H}\right)$ is a set of density operators $\mathcal{S}(\mathcal{H}):=\{\rho \in \operatorname{LinMap}(\mathcal{H}) \mid \rho \geq 0 \text { Hermitian, } \operatorname{tr}(\rho)=1\}$
- $\rho \in \mathcal{S}\left(\mathcal{H}\right)$ is called a pure if there exists $\left|\phi\right>\in\mathcal{H}$ such that $\rho = \left|\phi\right>\left<\phi\right|$ has rank 1, which is equivalent to $\text{tr}\left(\rho^2\right)=1$.
- Unitary evolution of a density operator is given by $\rho \mapsto U \rho U^{\dagger}=U\left(\sum_i p_i\left|\psi_i \right> \left<\psi_i\right|\right) U^{\dagger}=\sum_i p_i U\left|\psi_i\right>\left<\psi_i\right| U^{\dagger}$
- Projective measurement with outcomes labelled $\{x\}_x$ is associated with set of projectors $\{\Pi_x\}_x$ satisfying $\sum_x \Pi_x = \mathbb{I}$. The probability of outcome $x$ is given by $p(x) = \text{tr}\left(\Pi_x \rho\right)$ and the post-measurement state is given by $\frac{\Pi_x \rho \Pi_x}{\text{tr}\left(\Pi_x \rho\right)}$. This is nice as now we can describe the final state of the system after the measurement that was forgotten: 

$$
\rho^{\prime}=\sum_x \operatorname{Pr}[x \mid \rho] \rho_x^{\prime}=\sum_x \operatorname{tr}\left(\Pi_x \rho\right) \frac{\Pi_x \rho \Pi_x}{\operatorname{tr}\left(\Pi_x \rho\right)}=\sum_x \Pi_x \rho \Pi_x
$$


## 6.2. Partial Trace: system $\rightarrow$ subsystem: 

When we have access only to the subsystem $A$ of the composite system $AB$, the appropriate density operator is: 

$$
\rho^A = \text{tr}_B\left(\rho^{AB}\right)
$$

If a global state is pure, then the reduced state is not necessarily pure. i.e. consider $\rho_{A B}=\left|\psi^{00} \right>\left< \psi^{00}\right|_{A B}$. Taking partial trace over subsystem $B$ we get $\rho^A = \mathbb{I}_A/2$, which is maximally mixed.

## 6.3. Purification: subsystem $\rightarrow$ system:

Consider somewhat opposite task of finding a global state $\left|\psi^{AB}\right>$ given a reduced state $\rho^A$, s.t. $\text{tr}_B\left(\left|\psi^{AB}\right>\left<\psi^{AB}\right|\right) = \rho^A$. $\left|\psi^{AB}\right>$ is called _purification_ of $\rho^A$. This means that any mixed state can be seen as pure state on a larger system, which is nice result. This means that things don't stop being quantum, but simply they start to entangle with all the enviornment. 

## 6.4. Quantum Operations: Evolution and allowed operations on the open quantum system:

Given that we defined a more general formalism for the open quantum systems, we should also ponder over the allowed operations on such systems. For closed quantum system living in $\mathcal{H}$ the allowed operations was set of unitaries $\mathcal{U}\left(\mathcal{H}\right)$ that maps the set of pure quantum states to itself. By opening up the system we extended the quantum states from hilbert space to the set of density operators $\mathcal{H} \rightarrow \mathcal{S}\left(\mathcal{H}\right)$. We are interested in the most general maps that map this set to itself. Given that we already used up the name 'operator' to describe the operations on the closed system, we will call the operations on the open system 'superoperators', $\mathcal{E}$. $\mathcal{E}$ is expected to be:
- **linear**: $\mathcal{E}(p \rho+q \sigma)=p \mathcal{E}(\rho)+q \mathcal{E}(\sigma)$
- **trace preserving**: $\text{tr}\left(\mathcal{E}(\rho)\right) = \text{tr}(\rho)$
- **positive**: $\mathcal{E}(\rho) \geq 0$ for all $\rho \geq 0$ - this means that the eigenvalues of $\mathcal{E}(\rho)$ are non-negative.
- **completely positive**: We also would like for $\mathcal{E}_A \otimes \mathcal{I}_B\left(\rho_{A B}\right) \geq 0$ for all $\rho_{A B} \geq 0$.

To know that an superoperator is valid we somehow need to understand the overall global system.

## 6.5. The Stinespring dilation theorem: Purification of superoperators:

For any completely positive trace preserving(cptp) map there exists a hilber space $\mathcal{H}_B$ and a pure state $\left|\phi_N\right> \in \mathcal{H}_B$ together with a unitary $\mathcal{U}_{AB}$ s.t. 

$$
\mathcal{E}\left(\rho^A\right) = \text{tr}_B\left(\mathcal{U}_{AB}\left(\rho^A \otimes \left|\phi\right>\left<\phi\right|\right)\mathcal{U}_{AB}^{\dagger}\right)
$$

for all $\rho^A \in \mathcal{S}\left(\mathcal{H}^A\right)$.

## 6.6. Operator-sum representation:


$$
\mathcal{E}\left(\rho^A\right) = \text{tr}_B\left(\mathcal{U}_{AB}\left(\rho^A \otimes \left|\phi\right>\left<\phi\right|\right)\mathcal{U}_{AB}^{\dagger}\right)
$$

Then if we consider orthonormal basis of $\mathcal{H}_B$ to be $\{ \left|\phi_i\right>\}_i^{dim \mathcal{H}_B}$ and we rotate the basis in a way that the purification is $\left|\phi\right> = \left|\phi_1\right>$ we get:

$$
\mathcal{E}\left(\rho^A\right) = \sum_i \mathbb{I}_A \otimes \left<\phi_i\right|_B \left(\mathcal{U}_{AB}\left(\rho^A \otimes \left|\phi_1\right>\left<\phi_1\right|\right)\mathcal{U}_{AB}^{\dagger}\right) \mathbb{I}_A \otimes \left|\phi_i\right>_B = \sum_i \left( \left<\phi_i\right|\mathcal{U}_{AB} \left|\phi_1\right> \right)\rho^A \left(\left<\phi_1\right|\mathcal{U}_{AB}^{\dagger}\left|\phi_i\right>\right)
$$

Defining Krauss Operator: $E_k = \left<\phi_k\right|\mathcal{U}_{AB} \left|\phi_1\right>$ we can write any quantum operation as

$$
\mathcal{E}\left(\rho^A\right) = \sum_k E_k \rho^A E_k^{\dagger}
$$

Notice that $\sum_k E_k^{\dagger} E_k = \mathbb{I}$.

