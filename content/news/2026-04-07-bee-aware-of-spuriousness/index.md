---
title: "Bridging Explainability and Embeddings: BEE Aware of Spuriousness"
date: 2026-04-07
type: academic
cover:
  image: teaser.png
research_direction: generalization
draft: false
authors: "Cristian Daniel Paduraru, Antonio Barbalau, Radu Filipescu, Andrei Liviu Nicolicioiu, Elena Burceanu"
venue: "ICLR 2026"
presentation: "poster"
---

**Links:** [OpenReview](https://openreview.net/forum?id=9jYpHmI8ot) [GitHub](https://github.com/bit-ml/bee)

### Abstract

Current methods for detecting spurious correlations rely on data splits or error patterns, leaving many harmful shortcuts invisible when counterexamples are absent. We introduce BEE (Bridging Explainability and Embeddings), a framework that shifts the focus from model predictions to the weight space and embedding geometry underlying decisions. By analyzing how fine-tuning perturbs pretrained representations, BEE uncovers spurious correlations that remain hidden from conventional evaluation pipelines. We use linear probing as a transparent diagnostic lens, revealing spurious features that not only persist after full fine-tuning but also transfer across diverse state-of-the-art models. Our experiments cover numerous datasets and domains: vision (Waterbirds, CelebA, ImageNet-1k), language (CivilComments, MIMIC-CXR medical notes), and multiple embedding families (CLIP, CLIP-DataComp.XL, mGTE, BLIP2, SigLIP2). BEE consistently exposes spurious correlations: from concepts that slash the ImageNet accuracy by up to 95%, to clinical shortcuts in MIMIC-CXR notes that induce dangerous false negatives. Together, these results position BEE as a general and principled tool for diagnosing spurious correlations in weight space, enabling principled dataset auditing and more trustworthy foundation models.
