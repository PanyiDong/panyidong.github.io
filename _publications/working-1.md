---
title: "Bridging the Divide While Walking a Tightrope: Evidence from the Insurance Industry on Federated Data Sharing"
collection: publications
category: manuscripts
permalink: /publication/working-1
excerpt: 'This paper proposes a Hybrid Federated Learning (HyFL) framework tailored for the insurance industry that bridges data silos across insurers and InsurTech partners, achieving significant predictive accuracy gains and unlocking substantial financial value while preserving data privacy.'
date: 2026-03-19
venue: 'ssrn (Under Review)'
paperurl: 'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6442024'
citation: '<b>Dong, P.</b>, Feng, F., Quan, Z., Wang, T. (2026). Bridging the Divide While Walking
a Tightrope: Evidence from the Insurance Industry on Federated Data Sharing.'
---

Code Available at: [https://github.com/PanyiDong/FL](https://github.com/PanyiDong/FL)

## The Motivation: Overcoming Data Silos and Privacy Tightropes

Data in the insurance industry is severely fragmented due to competitive pressures and strict regulatory privacy constraints. Insurers often operate as data silos, facing a two bottleneck: extreme data imbalance and insufficient feature coverage. While centralized repositories or direct data purchases offer partial solution, they create significant trade-offs regarding data privacy and continuous licensing costs. To resolve this, we sought to design a privacy-preserving collaborative learning framework that balances data privacy with data utility.  

## Our Methodology: Hybrid Federated Learning (HyFL)

Classical Federated Learning (FL) is typically limited to either horizontal (HFL) or vertical (VFL) data partitioning. However, real-world insurance ecosystems are structurally complex, featuring overlapping samples across insurers alongside non-overlapping proprietary features from InsurTech partners. To address this, we developed HyFL, an framework simultaneously aggregate horizontal and vertical partitions. In addition, to handle the extreme sparsity and class imbalance of insurance claims, we integrated a domain-specific warm-up pre-training phase that stabilized the training process.  

<p align="center">
  <img src="/images/Figure4-1.png" alt="Structure of HyFL">
  <em>Structure of HyFL</em>
</p>

## The Impact: Substantial Accuracy and Multimillion-Dollar Value

Using real-world proprietary data from two mid-sized commercial insurers and an InsurTech partner, we demonstrated that HyFL substantially outperforms local training as well as standalone HFL and VFL. Economically, this reduction in prediction error translates to $57.8 million and $13.3 million in portfolio uncertainty reduction for the respective carriers. Furthermore, our interpretability analysis using ALE revealed that HyFL effectively eliminates localized feature biases inherent in single-insurer datasets, demonstrating that even large carriers with extensive local data stand to gain immensely from privacy-preserving data collaboration.

<table style="border-collapse: collapse; text-align: center; margin: 20px 0; font-family: serif; font-size: 1.2em;">
  <caption style="margin-bottom: 10px;"><strong>Economic Benefit Provided by FL</strong></caption>
  <thead>
    <tr style="border-top: 2px solid black;">
      <th rowspan="2" style="text-align: left; padding: 8px 16px;">Collaborator</th>
      <th rowspan="2" style="padding: 8px 16px;">Claim Portfolio Size (in million)</th>
      <th colspan="3" style="padding: 8px 16px;">Improvement (in million)</th>
    </tr>
    <tr style="border-bottom: 1px solid black;">
      <th style="padding: 8px 16px;">HFL</th>
      <th style="padding: 8px 16px;">VFL</th>
      <th style="padding: 8px 16px;">HyFL</th>
    </tr>
  </thead>
  <tbody style="border-bottom: 2px solid black;">
    <tr>
      <td style="text-align: left; padding: 8px 16px;">Company A</td>
      <td style="padding: 8px 16px;">361.2</td>
      <td style="padding: 8px 16px;">32.5</td>
      <td style="padding: 8px 16px;">50.6</td>
      <td style="padding: 8px 16px;">57.8</td>
    </tr>
    <tr>
      <td style="text-align: left; padding: 8px 16px;">Company B</td>
      <td style="padding: 8px 16px;">102.3</td>
      <td style="padding: 8px 16px;">7.1</td>
      <td style="padding: 8px 16px;">7.1</td>
      <td style="padding: 8px 16px;">13.3</td>
    </tr>
  </tbody>
</table>
