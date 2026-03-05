---
title: "Learning the Neighborhood: Contrast-Free Multimodal Self-Supervised Molecular Graph Pretraining"
date: 2025-09-26
type: academic
draft: false
authors: "Boshra Ariguib, Mathias Niepert, Andrei Manolache"
venue: "Under review"
presentation: ""
---

**Links:** [arXiv](https://arxiv.org/abs/2509.22468) [GitHub](https://github.com/ariguiba/C-FREE)

![Paper teaser](teaser.png)

### Abstract

High-quality molecular representations are essential for property prediction and molecular design, yet large labeled datasets remain scarce. While self-supervised pretraining on molecular graphs has shown promise, many existing approaches either depend on hand-crafted augmentations or complex generative objectives, and often rely solely on 2D topology, leaving valuable 3D structural information underutilized. To address this gap, we introduce C-FREE (Contrast-Free Representation learning on Ego-nets), a simple framework that integrates 2D graphs with ensembles of 3D conformers. C-FREE learns molecular representations by predicting subgraph embeddings from their complementary neighborhoods in the latent space, using fixed-radius ego-nets as modeling units across different conformers. This design allows us to integrate both geometric and topological information within a hybrid Graph Neural Network (GNN)-Transformer backbone, without negatives, positional encodings, or expensive pre-processing. Pretraining on the GEOM dataset, which provides rich 3D conformational diversity, C-FREE achieves state-of-the-art results on MoleculeNet, surpassing contrastive, generative, and other multimodal self-supervised methods. Fine-tuning across datasets with diverse sizes and molecule types further demonstrates that pretraining transfers effectively to new chemical domains, highlighting the importance of 3D-informed molecular representations.
