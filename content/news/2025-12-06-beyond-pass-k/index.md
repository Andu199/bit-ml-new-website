---
title: "Beyond Pass@k: Breadth-Depth Metrics for Reasoning Boundaries"
date: 2025-12-06
type: academic
draft: false
authors: "Marius Dragoi, Ioana Pintilie, Florin Gogianu, Florin Brad"
venue: "NeurIPS 2025 Workshop FoRLM"
presentation: "Poster"
---

**Links:** [arXiv](https://arxiv.org/abs/2510.08325)

![Paper teaser](teaser.png)

### Abstract

Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a powerful paradigm to improve Large Language Models on reasoning tasks such as coding, math or logic. To assess the reasoning boundary (the fraction of problems a model can solve) researchers often report Pass@k at large sampling budgets. Recent results reveal a crossover phenomenon: while RLVR models outperform the base model at small k values, the base model usually outperforms them when sampling a very large number of completions. This has been interpreted as evidence that base models have a larger reasoning boundary. We argue that on tasks with discrete answer spaces, such as math with numeric outputs, Pass@k at large k reflects the increasingly higher chance of success in the limit of the number of trials rather than genuine reasoning, and can therefore be misleading. We propose Cover@tau, which measures the fraction of problems that a model can solve for which at least a tau proportion of completions are correct. Unlike Pass@k, Cover@tau captures reasoning under an explicit reliability threshold: models that rely on random guessing degrade rapidly as tau increases. We evaluate several RLVR models using Cover@tau-based metrics and illustrate how the relative rankings of popular algorithms change compared to Pass@1, offering a different perspective on reasoning boundaries.
