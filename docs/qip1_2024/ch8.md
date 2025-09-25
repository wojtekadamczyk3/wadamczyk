# Chapter 8: Stabiliser Formalism:

This is section will be expanded in the future. Good reference for this is [Surviving as a Quantum Computer in the Classical World](https://www.cs.umd.edu/class/spring2024/cmsc858G/QECCbook-2024-ch1-15.pdf) by Daniel Gottesman.

## 8.1. Stabiliser Groups definitions:
- $\left|\phi\right> \in \mathcal{H}$ is a stabilised by an operator K if $K\left|\phi\right> = \left|\phi\right>$ - i.e. $\left|\phi\right>$ is an eigenstate of K with eigenvalue 1.
- Pauli Group for a single qubit is defined as: $\mathcal{P} := \left\{ \pm I, \pm X, \pm Y, \pm Z, \pm i I, \pm i X, \pm i Y, \pm i Z \right\}$
- _n-qubit_ Pauli Group is defined as: $\mathcal{P_n} := \{A_1 \otimes ... A_n |A_i \in \mathcal{P}\}$
- Stabiliser Group $\mathcal{S}$ is a subgroup of $\mathcal{P_n}$ s.t. $[S_i, S_j] = 0 \forall S_i, S_j \in \mathcal{S}$ and $-I \notin \mathcal{S}$. This can be said more compact through "Non-abelian subgroup of $\mathcal{P_n}$, that does not contain $-id$".
- Set of generators of a group is a set of elements s.t. any element of the group can be written as a product of the generators and their inverses.
- Minimal set of generators is a set of generators s.t. they are linearly independent.
- Stabiliser subspace: $\mathcal{H_S} := \{\left|\psi\right> | S\left|\psi\right> = \left|\psi\right> \forall S \in \mathcal{S}\}$

## 8.2. Stabiliser Codes:

### 8.2.1. Size of the Stabilised space:

One can then ponder about what does picking specific stabiliser mean for the space that we stabilise, and the errors that we can correct. Well let's first address the first question. If the stabiliser group defined in a space of _n-qubits_ is formed by minimal set of generators $\mathcal{S} = \left< S_1, ..., S_k \right>$ then the dimension of the stabilised space is $2^{n- k}$. This is because the stabiliser group is a subset of the Pauli group, and so $S^2=I$ for all $S \in \mathcal{S}$ (both because the S are elements of the Pauli group and because applicatiion of stabiliser twice should also stabilise the state). This means that $S^2 = I$ for all $S \in \mathcal{S}$. This means that eigenvalues of all stabilisers are $\pm 1$, which furhter means that each of the stabiliser splits the vector space into two.

#### 8.2.1.1. Why does measurement of $S_1$ and $S_2$ partition the space into 4 equal subspaces?

So we have shown that the measurement of the stabiliser splits the vector space into two sets, one composed of the eigenfunctions that result in eigenvalue 1, and the other composed of the eigenfunctions that result in eigenvalue -1. Now we can ask the question, why does the measurement of $S_1$ and $S_2$ partition the space into 4 equal subspaces, where results of two measurements are (1,1), (1,-1), (-1,1), (-1,-1)?

Let's consider that it is not the case. We can then 



Therefore the stabilised space is always divided into two, and since all the stabilisers are linearly independent, they split the space into $2^k$ subspaces. Therefore the dimension of the stabilised space is $2^n - k$.




### 8.2.2. Given our Stabiliser Group, what errors can we detect?

Suppose that $\left|\psi\right>_L$ lies in a stabilised subspace of $\mathcal{S}=\left< S_1, ..., S_k \right>$. In order to be able to notice the error, we would like to be able to distinguish it from the logical state. This means that some sort of measurement should be able to distinguish the two. As the stabiliser stabilizes the stabilised space, the error should bring the state out of the stabilised space. Therefore the error should anticommute with at least one of the stabilisers.

Ok, so now we know whether we can correct for an error, but how do we make sure that we dont learn anything about the logical state? This can be again done by reformulating the Knill-Laflamme conditions for stabiliser codes.

$$
\{ E_i, S_j \} = 0 \implies \text{error is detected}
$$

Can we refolmulate the Knill-Laflamme conditions for stabiliser codes?

$$
E_b^\dagger E_a \in \mathcal{S}
$$

### 8.2.3. Given our Stabiliser Group, how can we perform a logical operation?

What we want from our logical operators, is that they dont bring us outside of the stabilised space, as otherwise we would somehow leak the information about the logical state. Therefore we want that the logical operators commute with all the stabilisers. 

Hence if one finds two operators $U$, $V$ s.t. $[U, S]=[V, S]=0 \forall S \in \mathcal{S}$, and $\{U, V\}=0$ then they can identify them as $U=Z_L$ and $V=X_L$.

Code words can be identified as the eigenstates of the logical operator $Z_L$.


## 8.3. Stabiliser Codes:

Here in this section I will include few examples of stabiliser codes.

### 8.3.1. 3-bit flip code:

| | | | |
| :---: | :---: | :---: | :---: |
| $S_(1)$ | $Z$ | $Z$ | $I$ |
| $S_(2)$ | $I$ | $Z$ | $Z$ |
| $Z_(L)$ | $Z$ | $Z$ | $Z$ |
| $X_(L)$ | $X$ | $X$ | $X$ |

### 8.3.2. 3-bit phase code:
| | | | |
| :---: | :---: | :---: | :---: |
| $S_(1)$ | $X$ | $X$ | $I$ |
| $S_(2)$ | $I$ | $X$ | $X$ |
| $Z_(L)$ | $X$ | $X$ | $X$ |
| $X_(L)$ | $Z$ | $Z$ | $Z$ |

### 8.3.3. 9-bit Shors code:
| | | | | | | | | | |   
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $S_(1)$ | $Z$ | $Z$ | $I$ | $I$ | $I$ | $I$ | $I$ | $I$ | $I$ |
| $S_(2)$ | $I$ | $Z$ | $Z$ | $I$ | $I$ | $I$ | $I$ | $I$ | $I$ |
| $S_(3)$ | $I$ | $I$ | $I$ | $Z$ | $Z$ | $I$ | $I$ | $I$ | $I$ |
| $S_(4)$ | $I$ | $I$ | $I$ | $I$ | $Z$ | $Z$ | $I$ | $I$ | $I$ |
| $S_(5)$ | $I$ | $I$ | $I$ | $I$ | $I$ | $I$ | $Z$ | $Z$ | $I$ |
| $S_(6)$ | $I$ | $I$ | $I$ | $I$ | $I$ | $I$ | $I$ | $Z$ | $Z$ |
| $S_(7)$ | $X$ | $X$ | $X$ | $X$ | $X$ | $X$ | $I$ | $I$ | $I$ |
| $S_(8)$ | $I$ | $I$ | $I$ | $X$ | $X$ | $X$ | $X$ | $X$ | $X$ |
| $Z_(L)$ | $X$ | $X$ | $X$ | $I$ | $I$ | $I$ | $I$ | $I$ | $I$ |
| $X_(L)$ | $Z$ | $I$ | $I$ | $Z$ | $I$ | $I$ | $Z$ | $I$ | $I$ |

### 8.3.4. Steane code:
| | | | | | | | | |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $S_(1)$ | $I$ | $I$ | $I$ | $Z$ | $Z$ | $Z$ | $Z$ |
| $S_(2)$ | $I$ | $Z$ | $Z$ | $I$ | $I$ | $Z$ | $Z$ |
| $S_(3)$ | $Z$ | $I$ | $Z$ | $I$ | $Z$ | $I$ | $Z$ |
| $S_(4)$ | $I$ | $I$ | $I$ | $X$ | $X$ | $X$ | $X$ |
| $S_(5)$ | $I$ | $X$ | $X$ | $I$ | $I$ | $X$ | $X$ |
| $S_(6)$ | $X$ | $I$ | $X$ | $I$ | $X$ | $I$ | $X$ |
| $Z_(L)$ | $Z$ | $Z$ | $Z$ | $Z$ | $Z$ | $Z$ | $Z$ |
| $X_(L)$ | $X$ | $X$ | $X$ | $X$ | $X$ | $X$ | $X$ |

### 8.3.5. 5-qubit code:

| | | | | | |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $S_(1)$ | $X$ | $Z$ | $Z$ | $X$ | $I$ |
| $S_(2)$ | $I$ | $X$ | $Z$ | $Z$ | $X$ |
| $S_(3)$ | $X$ | $I$ | $X$ | $Z$ | $Z$ |
| $S_(4)$ | $Z$ | $X$ | $I$ | $X$ | $Z$ |
| $Z_(L)$ | $Z$ | $Z$ | $Z$ | $Z$ | $Z$ |
| $X_(L)$ | $X$ | $X$ | $X$ | $X$ | $X$ |