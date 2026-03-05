---
title: "ChronoGraph: A Real-World Graph-Based Multivariate Time Series Dataset"
date: 2025-12-06
type: academic
draft: false
authors: "Adrian Catalin Lutu, Ioana Pintilie, Elena Burceanu, Andrei Manolache"
venue: "NeurIPS 2025 Workshop BERT2S"
presentation: "Oral"
---

**Links:** [arXiv](https://arxiv.org/abs/2509.04449) [GitHub](https://github.com/bit-ml/ChronoGraph)

![Paper teaser](teaser.png)

### Abstract

We present ChronoGraph, a graph-structured multivariate time series forecasting dataset built from real-world production microservices. Each node is a service that emits a multivariate stream of system-level performance metrics, capturing CPU, memory, and network usage patterns, while directed edges encode dependencies between services. The primary task is forecasting future values of these signals at the service level. In addition, ChronoGraph provides expert-annotated incident windows as anomaly labels, enabling evaluation of anomaly detection methods and assessment of forecast robustness during operational disruptions. Compared to existing benchmarks from industrial control systems or traffic and air-quality domains, ChronoGraph uniquely combines (i) multivariate time series, (ii) an explicit, machine-readable dependency graph, and (iii) anomaly labels aligned with real incidents. We report baseline results spanning forecasting models, pretrained time-series foundation models, and standard anomaly detectors. ChronoGraph offers a realistic benchmark for studying structure-aware forecasting and incident-aware evaluation in microservice systems.
