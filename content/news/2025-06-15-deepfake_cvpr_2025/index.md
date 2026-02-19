---
title: "Circumventing shortcuts in audio-visual deepfake detection datasets with unsupervised learning"
date: 2025-06-15
type: academic
draft: false
authors: "S. Smeu, D.A. Boldisor, D. Oneata, E. Oneata"
venue: "CVPR 2025"
presentation: "Highlight paper"
top_percent: 3
---

**Links:** [arXiv](https://arxiv.org/abs/2412.00175) · [GitHub](https://github.com/bit-ml/AVH-Align/tree/main)

![Overview of the AVH-Align method](avh-align-overview.png)

### Abstract
Good datasets are essential for developing and benchmarking any machine learning system. Their importance is even more extreme for safety critical applications such as deepfake detection—the focus of this paper. Here we reveal that two of the most widely used audio-video deepfake datasets suffer from a previously unidentified spurious feature: the leading silence. Fake videos start with a very brief moment of silence and, on the basis of this feature alone, we can separate the real and fake samples almost perfectly. As such, previous audio-only and audio-video models exploit the presence of silence in the fake videos and consequently perform worse when the leading silence is removed. To circumvent latching on such an unwanted artifact and possibly other unrevealed ones, we propose a shift from supervised to unsupervised learning by training models exclusively on real data. We show that by aligning self-supervised audio-video representations we remove the risk of relying on dataset-specific biases and improve robustness in deepfake detection.
