---
title: "Efficient and Interpretable Transformer for Counterfactual Fairness"
collection: publications
category: manuscripts
permalink: /publication/working-3
excerpt: 'In this paper, we introduce the Feature Correlation Transformer (FCorrTransformer) and Counterfactual Attention Regularization (CAR). This efficient, attention-light framework achieves counterfactual fairness and high interpretability for tabular datasets, effectively mitigating algorithmic bias with minimal predictive performance degradation.'
date: 2026-04-29
venue: 'arXiv'
paperurl: 'https://arxiv.org/abs/2604.26188'
citation: '<b>Dong, P.</b>, Quan, Z. (2026). Efficient and Interpretable Transformer for Counterfactual Fairness.'
---

Code Available at: [https://github.com/PanyiDong/FairnessAwareAttention](https://github.com/PanyiDong/FairnessAwareAttention)

## The Problem: The Tension Between Fairness and Performance

The rapid adoption of ML in heavily regulated domains, such as insurance and finance, has created a critical tension between predictive power, model interpretability, and strict fairness regulations. Existing fairness-aware methods for tabular data typically rely on group-level metrics that conflict with risk-based pricing, or they require rigid, hard-to-validate causal graphs to ensure counterfactual fairness. Meanwhile, standard attention-heavy transformers project simple tabular data into complex, high-dimensional spaces. This obscures direct feature dependencies and makes it incredibly difficult to enforce fairness at the attention level without severely degrading model performance. We wanted to bridge this gap by designing a transparent architecture where fair attention naturally translates into fair predictions.  

## Our Methodology: FCorrTransformer and CAR

To solve these structural limitations, we developed the FCorrTransformer, an attention-light architecture tailored specifically for tabular data. Instead of using dense, high-dimensional embeddings, our model relies on one-dimensional embeddings. This design ensures that the attention matrix directly represents pairwise statistical dependencies between features. Leveraging this transparent structure, we introduced CAR. CAR operates by evaluating counterfactual permutations of sensitive features via an efficient input augmentation strategy, explicitly penalizing and suppressing biased dependencies directly within the attention matrix. Furthermore, to mitigate indirect discrimination, we introduced Domain Adaptation-based CAR (DACAR), which aligns non-sensitive features using CORAL mapping during training to account for correlated proxy biases. 

<p align="center">
  <img src="/images/Figure6-1.png" alt="Architecture Design of FCorrTransformer">
  <em>Architecture Design of FCorrTransformer</em>
</p>

## The Results: Interpretable, and Fair AI

We rigorously evaluated our framework against standard baseline models using highly imbalanced, real-world financial and proprietary commercial insurance datasets. The FCorrTransformer paired with CAR successfully achieved strong counterfactual fairness while maintaining highly competitive predictive accuracy. Beyond fairness, our architecture vastly outperformed standard transformers in computational efficiency. Because of its attention-light design, our model drastically reduced parameter counts and utilized only a fraction of the GPU memory required by baseline models. Ultimately, this framework provides a highly interpretable, and practical pathway for deploying responsible AI in regulatory-sensitive environments.

<p align="center">
  <img src="/images/Figure6-2.png" alt="Heatmap of Pre-SoftMax Attention Weights on BAF Data">
  <em>Heatmap of Pre-SoftMax Attention Weights on BAF Data</em>
</p>

<table style="border-collapse: collapse; text-align: center; margin: 20px 0; font-family: serif; font-size: 1.1em;">
  <caption style="margin-bottom: 10px;">Complexity of Each Model on BAF dataset</caption>
  <thead>
    <tr style="border-top: 2px solid black;">
      <th rowspan="2" style="padding: 4px 8px;">Model</th>
      <th rowspan="2" style="padding: 4px 8px;">Number of parameters</th>
      <th colspan="2" style="padding: 4px 8px;">GPU Memory Usage/MB (batch of 64)</th>
    </tr>
    <tr style="border-bottom: 1px solid black;">
      <th style="padding: 4px 8px;">Parameter size</th>
      <th style="padding: 4px 8px;">Forward/backward pass size</th>
    </tr>
  </thead>
  <tbody style="border-bottom: 2px solid black;">
    <tr>
      <td style="padding: 4px 8px;">FFN</td>
      <td style="padding: 4px 8px;">74,897</td>
      <td style="padding: 4px 8px;">0.30</td>
      <td style="padding: 4px 8px;">0.40</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px;">TabTransformer</td>
      <td style="padding: 4px 8px;">126,998</td>
      <td style="padding: 4px 8px;">0.51</td>
      <td style="padding: 4px 8px;">5.63</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px;">FT-Transformer</td>
      <td style="padding: 4px 8px;">94,981</td>
      <td style="padding: 4px 8px;">0.37</td>
      <td style="padding: 4px 8px;">67.88</td>
    </tr>
    <tr>
      <td style="padding: 4px 8px;">FCorrTransformer</td>
      <td style="padding: 4px 8px;">11,064</td>
      <td style="padding: 4px 8px;">0.04</td>
      <td style="padding: 4px 8px;">0.25</td>
    </tr>
  </tbody>
</table>
