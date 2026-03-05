---
title: "Investigating self-supervised representations for audio-visual deepfake detection"
date: 2026-02-21
type: academic
draft: false
authors: "Dragos-Alexandru Boldisor, Stefan Smeu, Dan Oneata, Elisabeta Oneata"
venue: "CVPR 2026"
presentation: ""
---

**Links:** [arXiv](https://arxiv.org/abs/2511.17181)

![Overview of the method](We-evaluate-a-wide-array-of-self-supervised-representations-for-audio-visual-deepfake-1.png)

### Abstract

Self-supervised representations excel at many vision and speech tasks, but their potential for audio-visual deepfake detection remains underexplored. Unlike prior work that uses these features in isolation or buried within complex architectures, we systematically evaluate them across modalities (audio, video, multimodal) and domains (lip movements, generic visual content). We assess three key dimensions: detection effectiveness, interpretability of encoded information, and cross-modal complementarity. We find that most self-supervised features capture deepfake-relevant information, and that this information is complementary. Moreover, models primarily attend to semantically meaningful regions rather than spurious artifacts. Yet none generalize reliably across datasets. This generalization failure likely stems from dataset characteristics, not from the features themselves latching onto superficial patterns. These results expose both the promise and fundamental challenges of self-supervised representations for deepfake detection: while they learn meaningful patterns, achieving robust cross-domain performance remains elusive.
