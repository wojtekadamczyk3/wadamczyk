# Chapter 2a: Computational Complexity:
I will start first by introducing the ideas from the classical computations, and then I will try to extend it to quantum computation and then try to observe the difference. 

Computational task is usually general i.e. 'given an n-bit string A (for any n), is A prime?'. Studying information theory, we are interested to know how efficient our computation is and whether allowing for some new quantum properties we will improve this computational efficiency. How efficient algorithm is can be measured though _algorithm complexity_.


## 2.1. Algorithm Complexity:
How efficient an algorithm is, can be measured in the amount of resources that are needed to solve a problem of size _n_.

- Time complexity deals with the number of computational steps required for solving the problem
- Space complexity deals with the amount of RAM that is needed to solve the problem

Big O-Notation is very handy in this case - to easily compare two algorithms

## 2.2. Big O notation:
Below I included definitions from P.Kammerlander lecture, for more intuitive picture go directly to the grey box:

- $f(n)=o(g(n))$ and say that $f$ grows slower than $g$
if $\forall c>0 \exists n_0>0$ such that for all $n \geq n_0: f(n) \leq c g(n)$,

- $f(n)=O(g(n))$ and say that $f$ does not grow significantly faster than $g$
if $\exists c>0$ and $n_0>0$ such that for all $n \geq n_0: f(n) \leq c g(n)$,

- $f(n)=\Omega(g(n))$ and say that $f$ does not grow significantly slower than $g$
if $\exists c>0$ and $n_0>0$ such that for all $n \geq n_0: c g(n) \leq f(n)$,

- $f(n)=\Theta(g(n))$ and say that $f$ grows as fast as $g$
if both $f(n)=O(g(n))$ and $f(n)=\Omega(g(n))$.

>Formally, define $f(n)=O(g(n))$ provided $|f(n)| \leq c|g(n)|$ as $n \rightarrow \infty$
> - $|f(n)|$ is bounded for some constant 𝑐 and all suﬀiciently large 𝑛.
> - Intuitively, look at the most significant term.
> - Ignore constant factors as they seldom dominate and are often transitory
>
>For example: consider $𝑛^2$ instead of $3𝑛^2 + 34𝑛 + 433$:
> - The cost of a program is usually a complicated formula. Often we should consider only the most significant term. If the cost is $𝑛^2 + 99𝑛 + 900$ for an input of size $𝑛$, then the $𝑛^2$ term will eventually dominate, even though $99𝑛$ is bigger for $𝑛 < 99$. The constant term 900 may look big, but it is soon dominated by $𝑛^2$.

i.e. We don't care in this case whether each time-step will take 1minute or 1ms, as for sufficiently large problem it wont matter. If we can make the algorithm more efficient, there will exist a n, for which the slow computer will be solving problem of size _n_ faster.

>Simple Facts about O Notation:
> 
> - $\begin{array}{r}O(2 g(n)) \text { is the same as } O(g(n)) \\ O\left(\log _{10} n\right) \text { is the same as } O(\ln n) \\ O\left(n^2+50 n+36\right) \text { is the same as } O\left(n^2\right) \\ O\left(n^2\right) \text { is contained in } O\left(n^3\right) \\ O\left(2^n\right) \text { is contained in } O\left(3^n\right) \\ O(\log n) \text { is contained in } O(\sqrt{n})\end{array}$

Above is taken from [4]


## 2.3. Complexity Classes:
_Decision Problem_ is a problem that can be formulated as a yes-no question of the input value. 


**Zoo of Complexity Classes**

- **P**: (Polynomial) The class of decision problems that can be solved in polynomial time on a classical computer.
- **BPP**: (Bounded-Error probabilistic polynomial time) The class of decision problems that can be solved by a probabilistic algorithm in polynomial time on a classical computer with failure probability at most $\frac{1}{3}$ for all possible inputs.
- **NP**: The class of decision problems such that, if the answer is ‘yes’, there is a proof of this which can be verified in polynomial time on a classical computer.
- **PSPACE**: (Space complexity polynomial) The class of decision problems that can be solved in polynomial space on a classical computer.
- **NP-complete**: A problem is said to be NP-complete if it is in NP and any other problem in NP can be reduced to it in polynomial time.
- **BQP**: The class of decision problems that can be solved in polynomial time on a quantum
computer with failure probability at most $\frac{1}{3}$ for all possible inputs.

Some facts:

- $\mathbf{P} \subset \mathbf{B P P}$
- $\mathbf{P} \subset \mathbf{N P} \subset \mathbf{P S P A C E}$
- It is not known whether $\mathbf{B P P} \subset \mathbf{N P}$
- Factorisation is not known and not believed to be **NP**-_complete_
- We dont know whether $\mathbf{P} = \mathbf{B P P}$, although many believe so

## 2.4. Quantum Complexity
For quantum computers we need to somehow define the operation. Quantum computation is simply application of some unitary operator $U \in \mathcal{U}(2^n)$ to some initial state of _n_ qubit (usually $\left|0\right>=\left|00 \cdots 0\right>=\left|0^n\right>=\left|0\right>^{\otimes n}$), followed by a measurement _m_ of the qubits in the computational basis. Any $U \in \mathcal{U}(2^n)$ is composed of an elementary gate from $\mathcal{S}$.

- _circuit size_ is the number of elementary gates
- _circuit width_ is the number of s-qubits that are involved in those elementary gates
- _circuit depth_ is the number of actual time steps needed while allowing for parallel execution of elementary gates on di erent qubits. However, the depth di ers from the size at most by a constant factor of s and is hence not relevant for the asymptotic runtime.
