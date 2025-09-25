# Chapter 0: Introduction
Welcome to Quantum Information Processing. It is a course that wants to introduce you to many elegant and beautiful concepts surrounding the field that has a potential to massively increase human understanding of quantum mechanics and many body physics. You are taking it at a very special time, because it seems that we start to see some early signs that the whole venture of quantum computing is perhaps not that hopeless. And I am also sure many of you are precisely here because of that, so we will talk about quantum computation.

In my notes I will largely _"ignore small formal subtleties, not because they're not interesting, but because they're a distraction from all the interesting physics we want to learn!"_ [1]. I will actually skip some of the formalism introduced in the lecture if I feel like it hinders my own understanding of Quantum Mechanics. I am open to being criticised for it. 

## 0.1.: Information is tied to physical representation:
Before we dive into computation itself, it is worth pausing to think about information. Information is everywhere in our lives, but what exactly is it? At its core, information can be seen as a refinement of our knowledge about the state of a system. The most basic unit of information is a bit, which can take one of two values.

In abstract mathematics we can freely manipulate bits, apply functions, and reason about logical operations without worrying about what the bits “are.” But the moment we want to process information in reality, it must be given a physical representation. A bit is never just an abstract symbol: it must be encoded in some physical system-whether as voltages in a circuit, magnetic domains on a hard drive, or photons in a fiber. “Information is not a disembodied abstract entity; it is always tied to a physical representation.” [3]

This perspective has deep consequences. If information is represented in physical degrees of freedom, then any act of computation must correspond to a physical evolution of that system. The laws of physics therefore set the ultimate limits of computation.

The current paradigm of computing is rooted in classical physics. That choice defines which operations are natural and efficient to perform. _"But that is not our World. To the best of our current experimental knowledge, our World is a quantum, not classical."_ [1]. This realization suggests an opportunity: if we can carefully isolate and manipulate quantum systems, then we may access a richer set of operations and new forms of information processing.

This is the promise of Quantum Information Processing (QIP). The QIP–Implementation perspective asks: how can we actually build physical systems that store and manipulate information using quantum mechanics? The QIP–Conceptual perspective asks: what happens to the very notion of information once we treat it in a quantum way? Together, these perspectives aim to provide the grounding you need to explore how quantum mechanics reshapes the paradigm of computation.

## 0.2.: So what are the good reasons to build a quantum computer:
So far, we have seen that quantum mechanics offers new ways to represent and process information. But an obvious question follows: why should we care? What are the real motivations behind building a quantum computer? The answer depends strongly on who you ask.
- For physicists, the motivation is largely fundamental. Quantum systems quickly become intractable as their size grows, because the number of parameters needed to describe them scales exponentially. Today, we rely heavily on approximations or numerical tricks. A controllable quantum device that can emulate many-body quantum dynamics would therefore be revolutionary. It would act as a kind of “microscope” for quantum reality, allowing us to probe strongly correlated systems, exotic phases of matter, and high-energy physics in ways that classical computers cannot.
- For governments, the primary interest lies in security. Much of modern cryptography relies on the assumption that certain mathematical problems (like factoring large integers) are practically impossible for classical machines. Quantum computers threaten this assumption: algorithms such as Shor’s could, in principle, break widely used encryption schemes. This potential disruption is driving intense global investment and competition.
- For industry, the motivations are more applied. Quantum computing promises advantages in fields where nature itself is quantum mechanical: quantum chemistry, materials science, and molecular modeling. Better simulations could accelerate drug discovery, improve catalysts for clean energy, and enable the design of new materials with tailored properties. Companies also hope for breakthroughs in optimization and machine learning, although these applications are less firmly established than chemistry and physics.

Different communities see different “killer applications.” But the unifying motivation is that a quantum computer would allow us to do things fundamentally beyond the reach of classical machines. Whether the goal is to understand nature more deeply, protect or disrupt information security, or unlock practical technologies, the reasons are compelling-and they explain why the race to build quantum computers is so intense today.

## 0.3.: What makes quantum more powerfull than classical:



<!-- ## 0.3.: What is happening in the field:
Over the past five years we are seeing quite a serious development of many platforms. Back before I have started my PhD the focus was always on loud, but unimportant demostrations of quantum advantage, but now it seems that people are starting to demonstrate serious error-correction and fault-tolerance computing attempts. Path towards fault tolerant quantum computation was shown in all platforms [Ions](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.133.180601), [Neutrals](https://www.nature.com/articles/s41586-023-06927-3), [Superconducting](https://www.nature.com/articles/s41586-024-08449-y), and [Bosonic Qubits](https://www.nature.com/articles/s41567-021-01487-7). 

My background is on the border of ion-trapping and neutral atoms, where I am in a ion-trapping group working on Neutral atom platform.  -->








