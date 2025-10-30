# ekoAcademic
Co-authors: Aidan McConnel, Shaan Amin
link: https://www.echoecho.org

Aidan, Shaan and I wanted to have an interactive-audio version of the arXiv to listen and discuss papers during our commute. 

[ekoAcademic](https://www.echoecho.org) is a small tool that generates short, accessible audio summaries of recent academic papers. It's a simple idea: you don't always have time to dive into a full paper, but you can listen to short summaries while walking, commuting or doing chores, and then decide if you want to dig deeper. We've also added a functionality for conversations and verbal Q&A so you can ask questions and understand recent literature in a conversational way. This works in many languages. This means that when you interact with the audio summary, you can ask it questions in your own language, and it should automatically answer in the same language.

![ekoAcademic](assets/showcase2.png)

## How it works

- We extract newly released papers (mirroring the arXiv categories), process/summarise them and then generate a short audio clip for each paper.
- We then have several GPT-realtime sessions designed for Q&A, or summarisation of sets of papers. By allowing microphone access you can always stop it and ask questions (in any language!).
- Non-interactive podcasts are stored, so once one person listens to one, they no longer need to be generated again for anyone else.
- This means that it is relatively cheap for us to generate new podcasts, and we can do it in real-time.
- We right now work mostly with the arxiv, but if people would find it useful to have it for other databases, we can add it.

![ekoAcademic](assets/showcase3.png)


## Feedback

We'd love to receive any feedback from this community:

- Does this solve a pain you have?
- What subject areas are missing (if yours isn’t covered yet)?
- Could the other language options for interactive discussion be useful for you? Should we translate more of the site?
- Any concerns (accuracy of summaries, missing context)?
- Do people actually like to do this on their commute? Or is that more of a time to unwind?
- How can we make it more useful for the community?
- Are there any features that you would like to see?

Thanks for reading. We built this because we felt this need ourselves - if others feel it too, maybe this can be a small tool to help.

Feel free to reach out to us at [wojtekadamczyk3@gmail.com](mailto:wojtekadamczyk3@gmail.com)