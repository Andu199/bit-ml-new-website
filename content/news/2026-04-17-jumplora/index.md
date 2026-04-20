---
title: "JumpLoRA: Sparse Adapters for Continual Learning in Large Language Models"
date: 2026-04-17
type: academic
cover:
  image: teaser.png
research_direction: nlp
draft: false
authors: "Alexandra Dragomir, Ioana Pintilie, Antonio Barbalau, Marius Dragoi, Florin Brad, Cristian Paduraru, Alexandru Tifrea, Elena Burceanu, Radu Ionescu"
venue: "Under review at CoLLAs 2026"
presentation: ""
---

**Links:** [arXiv](https://arxiv.org/abs/2604.16171)

### Abstract

Adapter-based methods have become a cost-effective approach to continual learning (CL) for Large Language Models (LLMs), by sequentially learning a low-rank update matrix for each task. To mitigate catastrophic forgetting, state-of-the-art approaches impose constraints on new adapters with respect to the previous ones, by targeting either subspace or coordinate-wise interference. In this paper, we propose JumpLoRA, a novel framework to adaptively induce sparsity in the Low-Rank Adaptation (LoRA) blocks through the use of JumpReLU gating. The method achieves dynamic parameter isolation, which helps prevent task interference. We demonstrate that our method is highly modular and compatible with LoRA-based CL approaches. Specifically, it significantly boosts the performance of IncLoRA and outperforms the leading state-of-the-art CL method, ELLA.