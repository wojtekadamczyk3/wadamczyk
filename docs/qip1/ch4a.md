# Chapter 4a: DJ Style Algorithms:

## 4.1. Deutsch-Josza (DJ) algorithm:
**Problem:** Given a function $f : \{0,1\}^n \rightarrow \{0, 1\}$ with a promise that a function is either _constant_ or _balanced_ the goal is to find out whether $f$ is constant or balanced. _Balanced_ means that it outputs 0 half of the time and 1 the other half of the time. _Constant_ means that it always outputs the same thing (either 1 or 0).

**Remark**: We will show that classical algorithm will require exponentially many queries to $f$, namely $2^{n-2}$ on average. Quantum algorithm will be able to determine whether f is constant or balanced in a single query. Notice here, that we are comparing the query complexity of both classical and quantum algorithms, not the time complexity. But as discussed in the previous chapter this fundamentally means that the quantum algorithm time complexity will be more efficient than the classical equivalent.

### Algorithm:
<img src="ch3/DJ_algorithm.png" alt="drawing" width="60%"/>

This circuit corresponds to:
1. Applying $H^{\otimes n} U_f H^{\otimes n}\left|0\right>^{\otimes n}$.
2. Evaluating the probability of $y = 0^n$, which is equivalent to projecting the state onto $\left|0\right>^{\otimes n}$ and taking the absolute value squared.

$$
\left|\left<0\right|^{\otimes n}H^{\otimes n} U_f H^{\otimes n}\left|0\right>^{\otimes n}\right|^2 = \begin{cases}1, & \text { if } f \text { is constant } \\ 0, & \text { if } f \text { is balanced }\end{cases}
$$

### Why it works?:

There is an explanation in the 

**Explanation 1:**

_What I want you to understand from this explanation is that if we have some sort of symmetric situation due to the measurement - the problem massively simplifies._

Here the trick is to realise that operator can act either to the right or to the left. Acting on the left massively simplifies the problem:

$$
\left<0\right|^{\otimes n}H^{\otimes n} U_f H^{\otimes n}\left|0\right>^{\otimes n} = \left(\frac{1}{\sqrt{2^n}} \sum_{x \in\{0,1\}^n}\left<x\right|\right) U_f \left(\frac{1}{\sqrt{2^n}} \sum_{x' \in\{0,1\}^n}\left|x'\right>\right) = \frac{1}{2^n} \sum_{x \in\{0,1\}^n}\left<x\right| U_f \left|x\right> = \begin{cases}\pm 1, & \text { if } f \text { is constant } \\ 0, & \text { if } f \text { is balanced }\end{cases}
$$

Because we have equal superposition of all x-values, then if $U_f$ is balanced then they will all add up to $0$, and if they are constant, they will add up to $\pm 1$.

Therefore we get:

$$
\left|\left<0\right|^{\otimes n}H^{\otimes n} U_f H^{\otimes n}\left|0\right>^{\otimes n}\right|^2 = \begin{cases}1, & \text { if } f \text { is constant } \\ 0, & \text { if } f \text { is balanced }\end{cases}
$$

As promised


**Explanation 2:**

Second explanation is more visual approach to the problem. It requires us to think about the problem slightly differently, which initially might seem more complicated, but then it becomes easier and more natural - I think it is very useful in subsequent problems such as Grover's algorithm

We can represent each n-qubit computational basis state as a number corresponding to its binary value 
- $\left|0\right>_C = \left|00...0\right>=\left|0\right>^{\otimes n}$, 
- $\left|1\right>_C = \left|00...01\right>$, 
- $\left|2\right>_C = \left|00...10\right>$
- ⋮
- $\left|2^n-1\right> = \left|11...1\right>$

Each quantum state $\left|x\right>_C$ can be represented as a delta function $\delta(x)$ on the x-axis, where $x$ ranges from 0 to $2^n-1$.

Then let's run through the algorithm step by step:

1. Initially we have the state $\left|0\right>_C$

<img src="ch3/DJ0.png" alt="DJ0" width="50%"/>

2. Then we apply Haddamard on the $\left|0\right>_C$ state, which results in the equal superposition of all states in $\left|x\right>_C$ basis

<img src="ch3/DJ1.png" alt="DJ1" width="50%"/>

3. Then we apply $U_f$ operator, which effectively flips the phase of half of the $\left|x\right>_C$ states if its balanced, otherwise it flips either all or none of them

<img src="ch3/DJ2.png" alt="DJ2" width="50%"/>

4. Finally we project it onto the equal superposition of all $\left|x\right>_C$ states

<img src="ch3/DJ3.png" alt="DJ3" width="50%"/>

The result is that if half of the states are flipped, then when we project it onto the equal superposition of all $\left|x\right>_C$ states, we will measure it with probability 0, and if all the states are flipped, then we will measure it with probability 1

    

