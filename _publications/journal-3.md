---
title: "InsurTech innovation using natural language processing"
collection: publications
category: journal
permalink: /publication/journal-3
excerpt: 'This paper explores the transformative potential of Natural Language Processing (NLP) in modernizing insurance analytics by extracting actionable insights from unstructured InsurTech data, with applications such as feature de-biasing, high-cardinality feature representation, and automated industry classification.'
date: 2026-07-22
venue: 'North American Actuarial Journal'
paperurl: 'https://arxiv.org/abs/2507.21112'
citation: '<b>Dong, P.</b>, Quan, Z. (2026). InsurTech innovation using natural language processing. <i>North American Actuarial Journal</i>, forthcoming.'
---

Code Available at: [https://github.com/PanyiDong/InsurTech_NLP](https://github.com/PanyiDong/InsurTech_NLP)

## The Problem: The Untapped Potential of Unstructured Data

As the insurance industry embraces data-driven approaches, a massive gap remains in analyzing unstructured textual data. Traditional actuarial modeling primarily relies on structured numerical inputs, leaving rich, context-heavy data like online reviews or business descriptions completely unutilized. Furthermore, existing numerical rating systems inherently carry geographical or socioeconomic biases, and high-cardinality categorical features often suffer from dimensionality issues when strictly encoded. In our work, we identified an urgent need to bridge the gap between human-readable text and numerical actuarial frameworks using NLP.  

<p align="center">
  <img src="/images/Figure3-1.png" alt="Summary of Text to Numbers Solutions">
  <em>Summary of Text to Numbers Solutions</em>
</p>

## Our Methodology: Translating Text to Actuarial Insights

To overcome these hurdles, we utilize a real-world InsurTech data and employ state-of-the-art NLP techniques to enrich our models. First, we introduced a lexicon-based sentiment analysis approach to de-bias inherently flawed customer star ratings by establishing objective sentiment polarity scores. Second, to tackle the "curse of dimensionality" from thousands of raw business categories, we deployed the advanced neural embedding model, transforming more than 13,000 messy textual labels into compact, 24-dimensional, context-aware numerical features. Lastly, we explored an unsupervised topic modeling framework using LDA and RAKE to automatically map business descriptions to their appropriate North American Industry Classification System (NAICS) codes.  

<p align="center">
  <img src="/images/Figure3-2.png" alt="Unsupervised Industry Classification Pipeline">
  <em>Unsupervised Industry Classification Pipeline</em>
</p>

## The Results: Better Models and Automated Workflows

Our empirical evaluations confirmed that NLP is far more than a supplementary tool in insurance; it is foundational for next-generation analytics. By replacing biased star ratings with NLP-derived polarity scores, we significantly reduced geographical and industry-specific biases, leading to fairer risk representation. When evaluating our category embeddings within a LightGBM pricing model, we found that replacing rigid category clustering with context-aware semantic embeddings improves model performance. Finally, our unsupervised industry classification framework efficiently recognized the true NAICS codes, vastly outperforming raw open-source LLMs which struggled without explicit task-specific constraints.
