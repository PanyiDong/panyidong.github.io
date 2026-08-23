---
title: "Improving Business Insurance Loss Models by Leveraging InsurTech Innovation"
collection: publications
category: journal
permalink: /publication/journal-1
excerpt: 'This paper demonstrates that enriching traditional in-house insurance datasets with real-time, personalized InsurTech data improves the predictive accuracy of business insurance loss models.'
date: 2024-10-15
venue: 'North American Actuarial Journal'
paperurl: 'https://www.tandfonline.com/doi/full/10.1080/10920277.2024.2400648?af=R'
citation: 'Quan, Z., Hu, C., <b>Dong, P.</b>, Valdez, E. (2025). Improving Business Insurance Loss Models by Leveraging InsurTech Innovation. <i>North American Actuarial Journal</i>, 29(2), 247-274.'
---

## The Problem: Information Gaps in Business Insurance Pricing

Business insurance, such as Business Owner's Policies (BOP), historically suffers from higher expense ratios and more complex underwriting processes compared to personal lines. Because insurers often fall short of gathering sufficient, highly granular risk factors during standard underwriting, traditional in-house loss models are limited. This gap in data leads to imperfect premium pricing and elevated loss ratios, leaving a critical need to capture alternative risk characteristics that drive commercial claims.

<p align="center">
  <img src="/images/Figure1-1.png" alt="The Flow of Information from the Academic–Industry Collaboration">
  <em>The Flow of Information from the Academic–Industry Collaboration</em>
</p>

## The Methodology: Fusing Actuarial Science with InsurTech

To address this, we leveraged a unique academic-industry collaboration to fuse an insurance company’s proprietary historical claims data with dynamic, external datasets provided by Carpe Data, an InsurTech firm. The enhanced dataset integrated conventional policy exposures with novel web-scraped features, including social media visibility, online review sentiment, firmographics, and granular proximity/territory risk scores. To quantify the value of this external data, we evaluated the loss model performance using LightGM with a traditional baseline Tweedie GLM optimized with elastic net feature selection.  

<p align="center">
  <img src="/images/Figure1-2.jpg" alt="Double Lift Charts for Model Comparison">
  <em>Double Lift Charts for Model Comparison</em>
</p>

## The Results: Enhanced Predictive Power and Interpretability

The results clearly established that the InsurTech-enhanced models consistently and significantly outperformed the baseline in-house models. The LightGBM architecture proved particularly adept at capturing the non-linear realities of commercial risks. In addition, we evaluate the feature importance using SHAP values and ALE plots. These interpretability tools revealed that newly introduced variables, such as territory risk indices, online customer review scores, and traffic proximity, were among the most powerful drivers for identifying high-risk policies. Ultimately, this framework offers a highly predictive, transparent solution that insurers can deploy to refine risk classification, and improve overall portfolio profitability.