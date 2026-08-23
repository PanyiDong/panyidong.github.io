---
title: "Automated Machine Learning (AutoML) in Insurance"
collection: publications
category: journal
permalink: /publication/journal-2
excerpt: 'This paper introduces an open-source Automated Machine Learning (AutoML) framework tailored for the insurance domain, effectively automating data preprocessing, hyperparameter optimization, and imbalance learning, to streamline actuarial data science.'
date: 2024-11-14
venue: 'Insurance: Mathematics and Economics'
paperurl: 'https://www.sciencedirect.com/science/article/pii/S0167668724001057'
citation: '<b>Dong, P.</b>, Quan, Z. (2025). Automated Machine Learning (AutoML) in Insurance. <i>Insurance:
Mathematics and Economics</i>, 120, 17-41.'
---

Code Available at: [https://github.com/PanyiDong/InsurAutoML](https://github.com/PanyiDong/InsurAutoML)

## The Motivation: Overcoming Insurance Data Hurdles

As machine learning (ML) becomes increasingly vital in actuarial practice, building effective predictive models still demands intense manual labor and deep domain expertise. Insurance datasets present unique and frustrating hurdles, such as extreme class imbalances, where actual claim events are exceptionally rare, and legacy data quality issues containing missing or inconsistent values. Our primary goal with this research was to bridge the gap between advanced data science and practical insurance applications by creating a highly accessible tool that requires only a few lines of code to deploy.  

<p align="center">
  <img src="/images/Figure2-1.png" alt="An illustration of AutoML workflow">
  <em>An illustration of AutoML workflow</em>
</p>

## Our Framework: An End-to-End Actuarial AutoML Pipeline

To solve these workflow bottlenecks, we designed an AutoML architecture that automatically handles the entire ML life-cycle. Our pipeline integrates data encoding, imputation, scaling, and critical data balancing techniques (i.e., over- or under-sampling) directly into the optimization process. We utilized a Combined Algorithm Selection and Hyperparameter optimization (CASH) framework, allowing the system to autonomously explore massive search spaces to find the optimal preprocessing-modeling combinations. Furthermore, to handle the rare-event nature of insurance claims, our architecture natively supports Stacking, Bagging, and Boosting ensemble strategies alongside customized, cost-sensitive actuarial loss functions. 

<p align="center">
  <img src="/images/Figure2-2.png" alt="An illustration of stacking ensemble training diagram">
  <em>An illustration of stacking ensemble training diagram</em>
</p>

## The Impact: Outperforming Traditional Benchmarks

We tested our AutoML tool against classical actuarial datasets. The empirical results show that: our automated pipelines consistently outperformed traditional GLMs and achieved predictive accuracy that rivals or surpasses state-of-the-art, manually tuned expert models. Ultimately, this tool serves a dual purpose: it acts as an effortless entry point for inexperienced users and provides a performance benchmark for seasoned actuarial researchers building future models.

<p align="center">
  <img src="/images/Figure2-3.png" alt="Train/Test deviance and runtime on freMTPL2freq dataset">
  <em>Train/Test deviance and runtime on freMTPL2freq dataset</em>
</p>
