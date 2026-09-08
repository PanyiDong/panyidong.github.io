---
title: "Fairness Aware Attention"
collection: code
category: research
permalink: /code/fairness-attention
excerpt: 'Feature Correlation Transformer (FCorrTransformer) and Counterfactual Attention Regularization (CAR): an attention-light, interpretable transformer framework achieving counterfactual fairness for tabular data with minimal performance loss.'
date: 2026-04-29
githuburl: 'https://github.com/PanyiDong/FairnessAwareAttention'
---

Code accompanying [Efficient and Interpretable Transformer for Counterfactual Fairness](/publication/fairness-attention).

The repository implements:

- Feature Correlation Transformer (FCorrTransformer): an attention-light tabular transformer whose attention matrix directly represents pairwise feature dependencies
- Counterfactual Attention Regularization (CAR): penalizing biased attention dependencies via counterfactual permutations of sensitive features
- Domain Adaptation-based CAR (DACAR): CORAL alignment of non-sensitive features to mitigate indirect proxy discrimination

Available at: [https://github.com/PanyiDong/FairnessAwareAttention](https://github.com/PanyiDong/FairnessAwareAttention)
