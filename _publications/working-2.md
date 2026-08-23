---
title: "Starting Off on the Wrong Foot: Pitfalls in Data Preparation"
collection: publications
category: manuscripts
permalink: /publication/working-2
excerpt: 'To prevent flawed actuarial modeling caused by inappropriate data preprocessing, we developed an effective and efficient Informed Data Preparation Pipeline (IDPP) utilizing various statistical tools.'
date: 2026-03-18
venue: 'arXiv (Under Review)'
paperurl: 'https://arxiv.org/abs/2603.18190'
citation: 'Guo, J., <b>Dong, P.</b>, Quan, Z. (2026). Starting Off on the Wrong Foot: Pitfalls in DataPreparation.'
---

Code Available at: [https://github.com/PanyiDong/InsurAutoML](https://github.com/PanyiDong/InsurAutoML)

## The Problem: Starting Off on the Wrong Foot

Actuarial modeling often starts off on the wrong foot when handling real-world, highly imbalanced insurance datasets. Conventional techniques, such as random train-test splitting, fail to properly partition rare but critical extreme claim events, leading to severe distribution shifts between datasets. Compounded by the "curse of dimensionality" and missing data, these initial missteps can completely undermine the statistical validity and reliability of downstream ML algorithms.  

## Our Methodology: Statistically Informed Data Preparation

To tackle these pitfalls, we developed IDPP that systematically automates and improves upstream preprocessing. We utilized SPlit, which leverages _support points_ to guarantee the distributional consistency between train and test sets, particularly for heavy-tailed imbalanced distributions. For feature selection, we applied the Chatterjee correlation coefficient (CCC) to capture complex, non-linear dependencies without relying on specific model architectures. Finally, we handled missingness using MissForest imputation, seamlessly embedding this entire IDPP into our custom InformedAutoML framework.  

<p align="center">
  <img src="/images/Figure5-1.png" alt="An illustration of the IDPP">
  <em>An illustration of the IDPP</em>
</p>

## The Results: Robust Models and Efficient Computation

Through rigorous simulations and real-world studies, our approach demonstrated substantial improvements. The SPlit method successfully stabilized the allocation of extreme claim events, drastically reducing the variance in coefficient estimation. Furthermore, InformedAutoML achieved globally optimal predictive performance metrics while running four to five times faster than baseline automated frameworks. Ultimately, the proposed framework is both statistically robust and computationally efficient.

<p align="center">
  <img src="/images/Figure5-2.png" alt="Train/Test RMSE and runtime on college Pell Grant dataset">
  <em>Train/Test RMSE and runtime on college Pell Grant dataset</em>
</p>