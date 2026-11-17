---
permalink: /
title: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% include base_path %}

<div class="home-intro">
  <p class="home-intro__lead">I am a Ph.D. student in Actuarial and Risk Management Sciences at the <strong>University of Illinois Urbana-Champaign (UIUC)</strong>. My research focuses on developing trustworthy and responsible AI techniques to solve real-world challenges in the insurance industry.</p>

  <p class="home-intro__label">Research interests</p>
  <ul class="tag-list">
    <li class="tag">Actuarial Science</li>
    <li class="tag">Automated Machine Learning (AutoML)</li>
    <li class="tag">Imbalanced Learning</li>
    <li class="tag">Federated Learning (FL)</li>
    <li class="tag">Explainable AI (XAI)</li>
    <li class="tag">Algorithmic Fairness</li>
  </ul>
</div>

<section class="home-section">
  <h2>Education</h2>
  <ol class="timeline">
    <li class="timeline__item">
      <span class="timeline__date">2022 – 2027 (expected)</span>
      <div class="timeline__body">
        <p class="timeline__title">Ph.D. in Actuarial Science and Risk Management</p>
        <p class="timeline__sub">University of Illinois Urbana-Champaign</p>
      </div>
    </li>
    <li class="timeline__item">
      <span class="timeline__date">2020 – 2022</span>
      <div class="timeline__body">
        <p class="timeline__title">M.S. in Actuarial Science and Risk Management</p>
        <p class="timeline__sub">University of Illinois Urbana-Champaign</p>
      </div>
    </li>
    <li class="timeline__item">
      <span class="timeline__date">2016 – 2020</span>
      <div class="timeline__body">
        <p class="timeline__title">B.S. in Physics</p>
        <p class="timeline__sub">Zhejiang University</p>
      </div>
    </li>
  </ol>
</section>

<section class="home-section">
  <h2>Experience</h2>
  <ol class="timeline">
    <li class="timeline__item">
      <span class="timeline__date">Sep 2022 – Present</span>
      <div class="timeline__body">
        <p class="timeline__title">Teaching Assistant</p>
        <p class="timeline__sub">University of Illinois Urbana-Champaign · <a href="{{ base_path }}/teaching/">courses</a></p>
      </div>
    </li>
    <li class="timeline__item">
      <span class="timeline__date">Sep 2022 – Present</span>
      <div class="timeline__body">
        <p class="timeline__title">Graduate Supervisor, <a href="https://asrm.illinois.edu/illinois-risk-lab/illinois-risk-lab-home/">Illinois Risk Lab (IRisk Lab)</a></p>
        <p class="timeline__sub">University of Illinois Urbana-Champaign</p>
      </div>
    </li>
    <li class="timeline__item">
      <span class="timeline__date">Dec 2022 – May 2023</span>
      <div class="timeline__body">
        <p class="timeline__title">Research Assistant</p>
        <p class="timeline__sub">University of Illinois Urbana-Champaign</p>
      </div>
    </li>
    <li class="timeline__item">
      <span class="timeline__date">Jan 2021 – Jun 2021</span>
      <div class="timeline__body">
        <p class="timeline__title">Intern</p>
        <p class="timeline__sub">AIA Life Insurance Company Limited</p>
      </div>
    </li>
  </ol>
</section>

<section class="home-section">
  <div class="home-section__head">
    <h2>Latest Publications</h2>
    <a class="home-section__more" href="{{ base_path }}/publications/">All publications <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
  </div>
  {% assign latest_pubs = site.publications | where: "category", "journal" | sort: "date" | reverse %}
  <div class="pub-list">
    {% for post in latest_pubs limit: 3 %}
      {% include archive-single.html %}
    {% endfor %}
  </div>
</section>

<section class="home-section">
  <div class="home-section__head">
    <h2>Recent Talks</h2>
    <a class="home-section__more" href="{{ base_path }}/talks/">All talks <i class="fas fa-arrow-right" aria-hidden="true"></i></a>
  </div>
  {% assign recent_talks = site.talks | sort: "date" | reverse %}
  <div class="entry-list">
    {% for post in recent_talks limit: 3 %}
      {% include archive-single-talk.html show_year=true hide_type=true %}
    {% endfor %}
  </div>
</section>

<section class="home-section">
  <h2>Awards &amp; Honors</h2>
  <ol class="timeline">
    <li class="timeline__item">
      <span class="timeline__date">2026</span>
      <div class="timeline__body">
        <p class="timeline__title">2025 NAAJ Annual Prize for Best Paper</p>
        <p class="timeline__sub">Society of Actuaries (SOA)</p>
      </div>
    </li>
    <li class="timeline__item">
      <span class="timeline__date">2026</span>
      <div class="timeline__body">
        <p class="timeline__title">2026 CCIRM Best Paper Award</p>
        <p class="timeline__sub">China Center for Insurance and Risk Management </p>
      </div>
    </li>
    <li class="timeline__item">
      <span class="timeline__date">2025 & 2026</span>
      <div class="timeline__body">
        <p class="timeline__title">James C. Hickman Scholar</p>
        <p class="timeline__sub">Society of Actuaries (SOA)</p>
      </div>
    </li>
    <li class="timeline__item">
      <span class="timeline__date">2025</span>
      <div class="timeline__body">
        <p class="timeline__title">Facilitating Learning Excellence Award</p>
        <p class="timeline__sub">University of Illinois Urbana-Champaign</p>
      </div>
    </li>
    <li class="timeline__item">
      <span class="timeline__date">2022 – 2024</span>
      <div class="timeline__body">
        <p class="timeline__title">Teachers Ranked as Excellent by Their Students</p>
        <p class="timeline__sub">University of Illinois Urbana-Champaign</p>
      </div>
    </li>
  </ol>
</section>

<section class="home-section">
  <h2>Skills</h2>
  <div class="skills">
    <div class="skills__item">
      <p class="skills__title">Actuarial Exams (towards ASA)</p>
      <p>SOA Exams P, FM, IFM, LTAM, STAM, SRM; VEE Mathematical Statistics</p>
    </div>
    <div class="skills__item">
      <p class="skills__title">Programming</p>
      <p>Python (NumPy, Pandas, scikit-learn, PyTorch); also R, MATLAB, C++</p>
    </div>
  </div>
</section>

<p class="home-cv">For my full CV, please see the <a href="{{ base_path }}/files/CV.pdf">Curriculum Vitae (PDF)</a>.</p>
