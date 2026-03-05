---
title: "Robust Novelty Detection through Style-Conscious Feature Ranking"
date: 2025-02-28
type: academic
draft: false
authors: "Stefan Smeu, Elena Burceanu, Emanuela Haller, Andrei Liviu Nicolicioiu"
venue: "WACV 2025"
presentation: "Poster"
---

**Links:** [arXiv](https://arxiv.org/abs/2310.03738) [Proceedings](https://openaccess.thecvf.com/content/WACV2025/papers/Smeu_Robust_Novelty_Detection_through_Style-Conscious_Feature_Ranking_WACV_2025_paper.pdf) [GitHub](https://github.com/bit-ml/Stylist)

![Paper teaser](teaser.png)

### Abstract

Novelty detection seeks to identify samples deviating from a known distribution, yet data shifts in a multitude of ways, and only a few consist of relevant changes. Aligned with out-of-distribution generalization literature, we advocate for a formal distinction between task-relevant semantic or content changes and irrelevant style changes. This distinction forms the basis for robust novelty detection, emphasizing the identification of semantic changes resilient to style distributional shifts. To this end, we introduce Stylist, a method that utilizes pretrained large-scale model representations to selectively discard environment-biased features. By computing per-feature scores based on feature distribution distances between environments, Stylist effectively eliminates features responsible for spurious correlations, enhancing novelty detection performance. Evaluations on adapted domain generalization datasets and a synthetic dataset demonstrate Stylist's efficacy in improving novelty detection across diverse datasets with stylistic and content shifts.
