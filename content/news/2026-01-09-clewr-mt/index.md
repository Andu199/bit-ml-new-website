---
title: "CLewR: Curriculum Learning with Restarts for Machine Translation Preference Learning"
date: 2026-01-09
type: academic
draft: false
authors: "Alexandra Dragomir, Florin Brad, Radu Tudor Ionescu"
venue: "Under review"
presentation: ""
---

**Links:** [arXiv](https://arxiv.org/abs/2601.05858) [GitHub](https://github.com/alexandra-dragomir/CLewR)

![Paper teaser](teaser.png)

### Abstract

Large language models (LLMs) have demonstrated competitive performance in zero-shot multilingual machine translation (MT). Some follow-up works further improved MT performance via preference optimization, but they leave a key aspect largely underexplored: the order in which data samples are given during training. We address this topic by integrating curriculum learning into various state-of-the-art preference optimization algorithms to boost MT performance. We introduce a novel curriculum learning strategy with restarts (CLewR), which reiterates easy-to-hard curriculum multiple times during training to effectively mitigate the catastrophic forgetting of easy examples. We demonstrate consistent gains across several model families (Gemma2, Qwen2.5, Llama3.1) and preference optimization techniques.
