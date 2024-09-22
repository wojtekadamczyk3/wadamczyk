# Chapter 2: Computational Complexity:

## 2.1. Big O notation:
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
>
>Simple Facts about O Notation:
> 
> - $\begin{array}{r}O(2 g(n)) \text { is the same as } O(g(n)) \\ O\left(\log _{10} n\right) \text { is the same as } O(\ln n) \\ O\left(n^2+50 n+36\right) \text { is the same as } O\left(n^2\right) \\ O\left(n^2\right) \text { is contained in } O\left(n^3\right) \\ O\left(2^n\right) \text { is contained in } O\left(3^n\right) \\ O(\log n) \text { is contained in } O(\sqrt{n})\end{array}$

## 2.2. Algorithms Efficiency:
How efficient an algorithm is can be measured in the amount of resources that are needed to solve a problem of size _n_.
- Time complexity deals with the number of computational steps required for solving the problem
- Space complexity deals with the amount of RAM that is needed to solve the problem

As you can imagine O-Notation is very handy in this case - where we can easily compare two algorithms

We don't care in this case whether each time-step will take 1minute or 1ms, as for sufficiently large problem it wont matter. If we can make the algorithm more efficient, there will exist a n, for which the slow computer will be solving problem of size _n_ faster.


## 2.3. What is the deal with Quantum Computers?
Well, I like this question a lot, because it motivates the whole course. And to understand whats the answer to this question we need to understand the algorithmic complexities. I feel like a lot of people miss-understand what is the real benefit of quantum computers. For example if you ask a random person on a street why are quantum computers usefull - they will probably mark you as a weirdo and ignore you. If you ask a random student in ETH why are quantum computers useful, they will not be able to tell you exactly except mumbling something about parallel nature of computing. This is not entirely right.

What is fundamental about q.computing is that due to the extra laws of physics that we can use, we can manipulate information in a new way (on top of the old way). This means that we can design a new algorithms that use those properties that change the complexities of the algorithms. In this course we will show how few of the algorithms change their complexities due to the quantum computing. 

Here I will introduce commonly used term _efficient_ algorithm is such that it can solve the problem in the polynomial time - i.e. $O(n^m)$


## 2.4. Complexity Classes:
- **P**: The class of decision problems that can be solved in polynomial time on a classical computer.
- **BPP**: The class of decision problems that can be solved by a probabilistic algorithm in polynomial time on a classical computer with failure probability at most $\frac{1}{3}$ for all possible inputs.
- **NP**: The class of decision problems such that, if the answer is ‘yes’, there is a proof of this which can be verified in polynomial time on a classical computer.
- **PSPACE**: The class of decision problems that can be solved in polynomial space on a classical computer.
- **NP-complete**: A problem is said to be NP-complete if it is in NP and any other problem in NP can be reduced to it in polynomial time.

Some facts:

- $\mathbf{P} \subset \mathbf{B P P}$
- $\mathbf{P} \subset \mathbf{N P} \subset \mathbf{P S P A C E}$
- It is not known whether $\mathbf{B P P} \subset \mathbf{N P}$
- Factorisation is not known and not believed to be **NP**-_complete_