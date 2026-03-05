---
title: "WASP: A Weight-Space Approach to Detecting Learned Spuriousness"
date: 2024-12-15
type: academic
draft: false
authors: "Cristian Daniel Paduraru, Antonio Barbalau, Radu Filipescu, Andrei Liviu Nicolicioiu, Elena Burceanu"
venue: "NeurIPS 2024 Workshop Interpretable AI: Past, Present and Future"
presentation: ""
---

**Links:** [arXiv](https://arxiv.org/abs/2410.18970v3) [GitHub](https://github.com/bit-ml/WASP)

![Paper teaser](teaser.png)

### Abstract

It is of crucial importance to train machine learning models such that they clearly understand what defines each class in a given task. Though there is a sum of works dedicated to identifying the spurious correlations featured by a dataset that may impact the model's understanding of the classes, all current approaches rely solely on data or error analysis. That is, they cannot point out spurious correlations learned by the model that are not already pointed out by the counterexamples featured in the validation or training sets. We propose a method that transcends this limitation, switching the focus from analyzing a model's predictions to analyzing the model's weights, the mechanism behind the making of the decisions, which proves to be more insightful. Our proposed Weight-space Approach to detecting Spuriousness (WASP) relies on analyzing the weights of foundation models as they drift towards capturing various (spurious) correlations while being fine-tuned on a given dataset. We demonstrate that different from previous works, our method (i) can expose spurious correlations featured by a dataset even when they are not exposed by training or validation counterexamples, (ii) it works for multiple modalities such as image and text, and (iii) it can uncover previously untapped spurious correlations learned by ImageNet-1k classifiers.
