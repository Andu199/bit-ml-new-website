---
title: "Learning (Approximately) Equivariant Networks via Constrained Optimization"
date: 2025-12-02
type: academic
draft: false
authors: "Andrei Manolache, Luiz F.O. Chamon, Mathias Niepert"
venue: "NeurIPS 2025"
presentation: "Oral"
top_percent: 0.4
---

**Links:** [arXiv](https://arxiv.org/abs/2505.13631) · [GitHub](https://github.com/andreimano/ACE)

### Abstract
Equivariant neural networks are designed to respect symmetries through their architecture, boosting generalization and sample efficiency when those symmetries are present in the data distribution. Real-world data, however, often departs from perfect symmetry because of noise, structural variation, measurement bias, or other symmetry-breaking effects. Strictly equivariant models may struggle to fit the data, while unconstrained models lack a principled way to leverage partial symmetries. Even when the data is fully symmetric, enforcing equivariance can hurt training by limiting the model to a restricted region of the parameter space. Guided by homotopy principles, where an optimization problem is solved by gradually transforming a simpler problem into a complex one, we introduce Adaptive Constrained Equivariance (ACE), a constrained optimization approach that starts with a flexible, non-equivariant model and gradually reduces its deviation from equivariance. This gradual tightening smooths training early on and settles the model at a data-driven equilibrium, balancing between equivariance and non-equivariance. Across multiple architectures and tasks, our method consistently improves performance metrics, sample efficiency, and robustness to input perturbations compared with strictly equivariant models and heuristic equivariance relaxations.
