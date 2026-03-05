---
title: "Rethinking Sparse Autoencoders: Select-and-Project for Fairness and Control from Encoder Features Alone"
date: 2025-12-06
type: academic
draft: false
authors: "Antonio Bărbălau, Cristian Daniel Păduraru, Teodor Poncu, Alexandru Tifrea, Elena Burceanu"
venue: "NeurIPS 2025 Workshops: Mechanistic Interpretability; Reliable ML from Unreliable Data"
presentation: "Poster"
---

**Links:** [arXiv](https://arxiv.org/abs/2509.10809)

![Paper teaser](teaser.png)

### Abstract

Sparse Autoencoders (SAEs) have proven valuable due to their ability to provide interpretable and steerable representations. Current debiasing methods based on SAEs manipulate these sparse activations presuming that feature representations are housed within decoder weights. We challenge this fundamental assumption and introduce an encoder-focused alternative for representation debiasing, contributing three key findings: (i) we highlight an unconventional SAE feature selection strategy, (ii) we propose a novel SAE debiasing methodology that orthogonalizes input embeddings against encoder weights, and (iii) we establish a performance-preserving mechanism during debiasing through encoder weight interpolation. Our Selection and Projection framework, termed S&P TopK, surpasses conventional SAE usage in fairness metrics by a factor of up to 3.2 and advances state-of-the-art test-time VLM debiasing results by a factor of up to 1.8 while maintaining downstream performance.
