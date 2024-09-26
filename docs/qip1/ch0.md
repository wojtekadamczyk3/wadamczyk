My plan is to share my edited notes that I made whilst preparing for the teaching. I am doing it mainly in order to make sure I understand the topics, and motivate myself to be clear with explanations. I hope to give different intuition, which perhaps will be useful to some. 

In case of any queries and feedback, don't hesitate to contact me (wadamczyk@phys.ethz.ch)

**Resources**: Which I used to write my notes - There is a lot of re-writing and paraphrasing, which I havent cited next to the sentence (the nature of notes)

- [Principles of Quantum Mechanics (David Skinner)](https://www.damtp.cam.ac.uk/user/dbs26/PQM.html) [1]
- Quantum Information Processing (J.P.Home) [2]
- [Quantum Information and Computation (Richard Jozsa)](https://www.qi.damtp.cam.ac.uk/files/PartIIIQC/Part%202%20QIC%20lecturenotes.pdf) [3]
- [Foundations of Computer Science (Anil Madhavapeddy, Jonathan Ludlam)](https://www.cl.cam.ac.uk/teaching/2324/FoundsCS/focs-202324-v1.5.pdf) [4]
- Quantum Information (C.H.W. Barnes) [5]

# Chapter 0: Introduction
Computation is about manipulation of information. Mathematically we can ponder on the different abstract schemes and systems to manipulate information, however, in practice we are very limited to what type of computation can we really do. _"Information is not a disembodied abstract entity; it is always tied to a physical representation"._ [3] _"If information is represented in physical states or degrees of freedom of some physical system, then any possible act of computation, or information processing, must correspond to a physical evolution of that physical system."_ [3] This means that the rules of the computation must obey the laws of physics.

Current paradigm of computing relies on classical physics, which in result constrains what operations can we perform on the computers. _"But that is not our World. To the best of our current experimental knowledge, our World is a quantum, not classical."_ [1] This gives us hope. If one carefully isolates and always consideres the whole system, we could enlarge the zoo of the operations we could perform. Extra tools could lead to different complexity classes of the algorithms that were previously not solvable by classical computers, and could aid in further understanding of the world. 

QIP-Implementation intends to show how can we build systems that can manipulate information using laws of quantum physics. QIP-Concepts intends to entertain the idea that we have the possibility of treating the information in a quantum way. We want to give you the grounding of exploring for yourself how does this change the paradigm of computation.

In my notes I will largely _"ignore small formal subtleties, not because they're not interesting, but because they're a distraction from all the interesting physics we want to learn!"_ [1]. I will actually skip some of the formalism introduced in the lecture if I feel like it hinders my own understanding of Quantum Mechanics. I am open to being criticised for it. 

## Chapter 0.1: Why do we care about Quantum Computing
...