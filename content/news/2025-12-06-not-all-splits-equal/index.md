---
title: "Not All Splits Are Equal: Rethinking Attribute Generalization Across Unrelated Categories"
date: 2025-12-06
type: academic
draft: false
authors: "Liviu Nicolae Fircă, Antonio Bărbălau, Dan Oneata, Elena Burceanu"
venue: "NeurIPS 2025 Workshop CauScien"
presentation: "Poster"
---

**Links:** [arXiv](https://arxiv.org/abs/2509.06998) [GitHub](https://github.com/bit-ml/rethinking-attribute-generalization)

![Paper teaser](teaser.png)

### Abstract

Can models generalize attribute knowledge across semantically and perceptually dissimilar categories? While prior work has addressed attribute prediction within narrow taxonomic or visually similar domains, it remains unclear whether current models can abstract attributes and apply them to conceptually distant categories. This work presents the first explicit evaluation for the robustness of the attribute prediction task under such conditions, testing whether models can correctly infer shared attributes between unrelated object types: e.g., identifying that the attribute "has four legs" is common to both "dogs" and "chairs". To enable this evaluation, we introduce train-test split strategies that progressively reduce correlation between training and test sets, based on: LLM-driven semantic grouping, embedding similarity thresholding, embedding-based clustering, and supercategory-based partitioning using ground-truth labels. Results show a sharp drop in performance as the correlation between training and test categories decreases, indicating strong sensitivity to split design. Among the evaluated methods, clustering yields the most effective trade-off, reducing hidden correlations while preserving learnability. These findings offer new insights into the limitations of current representations and inform future benchmark construction for attribute reasoning.
