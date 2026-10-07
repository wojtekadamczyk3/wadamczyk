# Chapter 5: Shor's Algorithm:

Shor's algorithm is probably one of the most famous quantum algorithms, and the reason for interest of various governments around the world in quantum computing. It is connected to RSA encryption, which basically is the foundation of the internet privacy as we know it. Breaking it, would have huge implications on everything we do. Breaking RSA can be reduced to factoring large numbers.

## 5.1 Introduction:

**Problem:** Given an integer $N$, output a factor $1 < K < N$. with any chosen constant level of probability $(1-\epsilon)$, and the algorithm will run in polynomial time $O(n^3)$.

## 5.2. Factoring as a periodicity problem:

The approach we will take is to transform the factoring problem into a periodicity problem. And then we will show that we can solve the periodicity problem efficiently with a quantum algorithm.

**Theorem**: (_Euler's theorem_) If $a$ and $N$ are coprime, then there is a least power $1<r<N$ such that $a^r\equiv 1 \pmod{N}$. This $r$ is called the order of $a$ mod $N$.

Using Euler's theorem we can show that $f(k) = a^k \pmod{N}$ is periodic with period $r$. This is because 

$$
f(k + r) = a^{k+r} \pmod{N} = a^k a^r \pmod{N} = a^k \pmod{N} = f(k)
$$

Suppose that we find the period $r$ of $f(k)$ and this period $r$ is even. Then we can re-write our original statement as:

$$
a^r - 1 = (a^{r/2} - 1)(a^{r/2} + 1) \equiv 0 \pmod{N}
$$

$N$ does not divide $a^{r/2} - 1$, therefore $N$ must either (a) divide $a^{r/2} + 1$ or (b) partly divide into $a^{r/2} + 1$ and partly into $a^{r/2} - 1$. If it partly divides into $a^{r/2} + 1$, we can use classically efficient euclids algorithm $gcd(a^{r/2} + 1, N)$ to find a non-trivial factor of $N$. Therefore, if we pick $a$ at random then, assuming $r$ is even and $a^{r/2}+1$ is not divisible by $N$, we can classically find a non-trivial factor of $N$.

**Theorem**: Suppose $N$ is odd and not a power of a prime. If $a<N$ is chosen uniformly at random with $gcd(a,N)=1$ then $Prob(\text{r is even and } a^{r/2}\not\equiv -1 \pmod{N})$ is at least $1/2$.

## 5.3. Algorithm:

<img src="../assets/chapter_05/shors.png" alt="drawing" width="100%"/>



1. Is N even? If so, output 2 and stop
2. Choose $a$ at random from 1 to $N-1$ and compute $gcd(a,N)$. If $gcd(a,N) \neq 1$ then we are done.
3. If s=1 find the period r of the sequence $a^k \pmod{N}$. If r is odd or $a^{r/2} \equiv -1 \pmod{N}$, then go back to step 2.
4. Otherwise $gcd(a^{r/2} + 1, N)$ and $gcd(a^{r/2} - 1, N)$ are non-trivial factors of $N$.

As you can see already here, everything about solving this problem boils down to the efficient implementation of fidning the period of r of $a^x \pmod{N}$. Following section will show how can we do it efficiently with a quantum algorithm.

## 5.4. Efficient implementation of period finding of $a^k \pmod{N}$:

In the end what we need to do is to find the period $r$ of the sequence $a^k \pmod{N}$. The circuit should be the same as the one for period finding algorithm. What we want to show is that each block of this circuit can be implemented efficiently.

<img src="../assets/chapter_04/period_finding_algorithm_circuit.png" alt="drawing" width="100%"/>

We have already shown that the QFT can be implemented efficiently in terms of query complexity. If we want to know whether the algorithm can be efficient in terms of time-complexity, we need to consider how we can implement the bit oracle $O_f$ efficiently. Efficient oracle $O_f$ is equivalent to efficient implementation of $f(k) = a^k \pmod{N}$.

### 5.4.1. Efficient implementation of $f(x) = a^x \pmod{N}$:

Using binary representation of $x$ we can write:

$$
x=x_{m-1} \cdot 2^{m-1}+x_{m-2} \cdot 2^{m-2}+\ldots+x_0
$$

therefore

$$
a^x\pmod{N}=\left(a^{2^{m-1}}\right)^{x_{m-1}}\left(a^{2^{m-2}}\right)^{x_{m-2}} \ldots(a)^{x_0}\pmod{N}
$$

, and as each $x_i$ is either 0 or 1, therefore we will be either multiplying or not the result of the previous step by $a^{2^i}$. We can implement it as a multiplication by $a^{2^i}$ controlled on the qubit $x_i$. This is equivalent to the following circuit:

<img src="../assets/chapter_05/efficient_shors_oracle.png" alt="drawing" width="100%"/>


Therefore if we prepare the first register in the state $\sum_{x=0}^{N-1} \left|x\right>$, and the second register in the state $\left|1\right>$, then we will end up with the state after applicaion for the circuit above:


$$
\sum_{x=0}^{N-1} \left|x\right>\left|1\right> \rightarrow \sum_{x=0}^{N-1} \left|x\right> \left|a^x \bmod{N}\right>
$$


**Comment**:

Maybe an interesting thing to note is that we between two steps of the algorithm we can re-use the previous multiplication to compute the next power of $a$. This is because we can write it recursively as, and so it only needs to be squared:

$$
a^{2^j} \pmod{N} = \left(a^{2^{j-1}}\right)^2 \pmod{N}
$$


This somewhat means that we can reuse the result of the previous computation to compute the next power of $a$. This means that

**Supplemental:**

**S1: Euler's Theorem**:

Shor's algorithm relies heavily on Eulers theorem, and so we want to quickly give an intuitive picture of this theorem:

So here we come back to good old days of Euler. As many mathematicians Euler was obsessed with prime numbers. What he noticed is that if he takes two prime numbers $N$ and $a$, then there always exist a number $r$ such that

$$
a^{r}\equiv 1 \mod{N}
$$

**Proof**:

- Let $\{R_0, R_1, ..., R_r\}$ be a set of all co-prime with $N$ that are smaller than $N$.
- If $a$ is co-prime with $N$, then multiplying all numbers in the set $\{R_i\}$ simply reshuffles the order of the set $$\{aR_0 \mod{N}, aR_1 \mod{N}, ..., aR_r \mod{N} \} = \{R_0, R_1, ..., R_r\}, $$ with re-shuffled order (see S1.1. for more details).
- We can therefore write
$$
R_0R_1...R_r \equiv a^{r}R_0R_1...R_r \mod{N}
$$
- Which means that

$$
1 \equiv a^{r} \mod{N}
$$


**S1.1. Multiplying with n, just re-shuffles the order of the set $\{R_i\}$**:

If $a$ is co-prime with $N$, then multiplying all numbers in the set $\{R_i\}$ simply reshuffles the order of the set $$\{aR_0 \mod{N}, aR_1 \mod{N}, ..., aR_r \mod{N} \} = \{R_0, R_1, ..., R_r\}, $$

For this we need to first show that $aR_i \mod{N}$ is in the set $\{R_i\}$:
- Since $R_i$ and $a$ is co-prime with $N$, then $\text{gcd}(aR_i, N) = 1$, which means that $aR_i$ is also co-prime with $N$.
- Since $aR_i$ is co-prime with $N$, then $aR_i \mod{N}$ is also co-prime with $N$.
    - Let $aR_i \mod{N} = q$, then $aR_i=kN+q$
    - Let's assume $q$ is not coprime with $N$. Then there exist $d$ which divides both $N$ and $q$. This means that it also must divide $aR_i$, which means that then $aR_i$ is not coprime to $N$ which leads to contradiction. Therefore $aR_i \mod{N}$ must be coprime to $N$.
    - Since $aR_i \mod{N}$ must be strictly smaller than $N$, it maps it back to itself.

 if $R_i$ and $a$ are co-prime

This is because both $R_i$, and $a$ are coprime with $N$, and so $aR_i$ also has to be co-prime with n. Since if $aR_i$ is co-prime to N, then also $aR_i \mod{N}$ is also co-prime to N. It has to be one-to-one map since $\text{gcd}(a, n)$, and so the number $a$ has a multiplicative inverse module $n$. This means that it cannot be one to many map.

**S2: Intuition behind prime factorisation as a period finding problem:**

1. Prime factorisation is bloody difficult, but Euclid algorithm for $\text{gcd}(a, b)$ is simple. This means that if we could find a number, $n'$ that shares a common divisor with our $n$ then if we did run $\text{gcd}(n, n')$ and find a prime factor.

2. But how can we find another number that has any relation to $n$. Well what we could try is to make use of the Eulers theorem. We know that if we pick a random $a$ there is quite some chance that it is co-prime to $n$. And Euler is telling us that for two co-prime numbers there is a number $r$ which is relating $n$, $a$. And so suddenly we found a number $a^r$ which is related to $n$. To do that we need to find $r$, which is where we need quantum computers.

_Here it would be nice to add a diagram. Finding a state connected to n, try to find connected state to this $n'$ that connects to gcd of n_

3. Now the task is to massage this number to make sure that we cast it in a form that shares a common divisor with $n$. If we can do that we are saved.

Do you wan't to come up with a new Shor's v2 algorithm. It's not so difficult ;) Just find a random theorem that links $n$ with $n'$. Then try to find an efficient quantum algorithm to find $n'$ given $n$. If you do so, then you need to massage $n'$ to $\text{gcd}$ form, and here you have a Shors v2.

