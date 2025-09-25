# Chapter 0: Introduction
Welcome to Quantum Information Processing. It is a course that wants to introduce you to many elegant and beautiful concepts surrounding the field that has a potential to massively increase human understanding of quantum mechanics and many body physics. You are taking it at a very special time, because it seems that we start to see some early signs that the whole venture of quantum computing is perhaps not that hopeless. And I am also sure many of you are precisely here because of that, so we will talk about quantum computation.

In my notes I will largely _"ignore small formal subtleties, not because they're not interesting, but because they're a distraction from all the interesting physics we want to learn!"_ [1]. I will actually skip some of the formalism introduced in the lecture if I feel like it hinders my own understanding of Quantum Mechanics. I am open to being criticised for it. 

## 0.1.: Information is tied to physical representation:
But before we will talk about computation, I would like to first ponder about information itself. Information is something very present in our lives. Information is marginal increase of the knowledge of the state of something. We can represent it in terms of fundamental unit - a _boolean_. We can talk about it in an abstract term, and we can manipulate this information in an abstract way. For example we can define a function that takes few such booleans, and modifies them depending on their state. But as soon as we are concerned about manipulating such information in real life, this information has to have a representation in this real life. It needs to be bounded by a physical reality, and it is pointless outside of such physical reality. _"Information is not a disembodied abstract entity; it is always tied to a physical representation"._ [3] _"If information is represented in physical states or degrees of freedom of some physical system, then any possible act of computation, or information processing, must correspond to a physical evolution of that physical system."_ [3]. And there is something very rich about this statement. It is rich because it puts bounds to how can we compute and manipulate information. The limits of computation (information manipulation) are the laws of physics. 

Current paradigm of computing relies on classical physics, which in result constrains what operations can we perform on the computers. _"But that is not our World. To the best of our current experimental knowledge, our World is a quantum, not classical."_ [1] This gives us hope. If one carefully isolates and always consideres the whole system, we could enlarge the zoo of the operations we could perform. Extra tools could lead to different complexity classes of the algorithms that were previously not solvable by classical computers, and could aid in further understanding of the world. 

QIP-Implementation intends to show how can we build systems that can manipulate information using laws of quantum physics. QIP-Concepts intends to entertain the idea that we have the possibility of treating the information in a quantum way. We want to give you the grounding of exploring for yourself how does this change the paradigm of computation.

## 0.2.: So what are the good reasons to build a quantum computer:
So far, we have seen that quantum mechanics offers new ways to represent and process information. But an obvious question follows: why should we care? What are the real motivations behind building a quantum computer? The answer depends strongly on who you ask.
- For physicists, the motivation is largely fundamental. Quantum systems quickly become intractable as their size grows, because the number of parameters needed to describe them scales exponentially. Today, we rely heavily on approximations or numerical tricks. A controllable quantum device that can emulate many-body quantum dynamics would therefore be revolutionary. It would act as a kind of “microscope” for quantum reality, allowing us to probe strongly correlated systems, exotic phases of matter, and high-energy physics in ways that classical computers cannot.
- For governments, the primary interest lies in security. Much of modern cryptography relies on the assumption that certain mathematical problems (like factoring large integers) are practically impossible for classical machines. Quantum computers threaten this assumption: algorithms such as Shor’s could, in principle, break widely used encryption schemes. This potential disruption is driving intense global investment and competition.
- For industry, the motivations are more applied. Quantum computing promises advantages in fields where nature itself is quantum mechanical: quantum chemistry, materials science, and molecular modeling. Better simulations could accelerate drug discovery, improve catalysts for clean energy, and enable the design of new materials with tailored properties. Companies also hope for breakthroughs in optimization and machine learning, although these applications are less firmly established than chemistry and physics.

In short: different communities see different “killer applications.” But the unifying motivation is that a quantum computer would allow us to do things fundamentally beyond the reach of classical machines. Whether the goal is to understand nature more deeply, protect or disrupt information security, or unlock practical technologies, the reasons are compelling—and they explain why the race to build quantum computers is so intense today.


## 0.3.: What is happening in the field:

## 0.4.: What is happening in ETH:






## 3.1. Algorithm Complexity:
How efficient an algorithm is, can be measured in the amount of resources that are needed to solve a problem of size _n_.

- Time complexity deals with the number of computational steps required for solving the problem
- Space complexity deals with the amount of RAM that is needed to solve the problem

Big O-Notation is very handy in this case - to easily compare two algorithms

## 3.2. Big O notation:
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



## 0.2. Which aspects of quantum makes us more powerful:
Well, we have a whole course to learn






