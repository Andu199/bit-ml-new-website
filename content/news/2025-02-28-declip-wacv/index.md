---
title: "DeCLIP: Decoding CLIP representations for deepfake localization"
date: 2025-02-28
type: academic
draft: false
authors: "Stefan Smeu, Elisabeta Oneata, Dan Oneata"
venue: "WACV 2025"
presentation: "Oral"
---

**Links:** [arXiv](https://arxiv.org/abs/2409.08849) [Proceedings](https://openaccess.thecvf.com/content/WACV2025/papers/Smeu_DeCLIP_Decoding_CLIP_Representations_for_Deepfake_Localization_WACV_2025_paper.pdf) [GitHub](https://github.com/bit-ml/DeCLIP)

![Paper teaser](teaser.png)

### Abstract

Generative models can create entirely new images, but they can also partially modify real images in ways that are undetectable to the human eye. In this paper, we address the challenge of automatically detecting such local manipulations. One of the most pressing problems in deepfake detection remains the ability of models to generalize to different classes of generators. In the case of fully manipulated images, representations extracted from large self-supervised models (such as CLIP) provide a promising direction towards more robust detectors. Here, we introduce DeCLIP, a first attempt to leverage such large pretrained features for detecting local manipulations. We show that, when combined with a reasonably large convolutional decoder, pretrained self-supervised representations are able to perform localization and improve generalization capabilities over existing methods. Unlike previous work, our approach is able to perform localization on the challenging case of latent diffusion models, where the entire image is affected by the fingerprint of the generator. Moreover, we observe that this type of data, which combines local semantic information with a global fingerprint, provides more stable generalization than other categories of generative methods.
