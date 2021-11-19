---
title: "Introduction to Parallel Computing"
permalink: "/Parallel/OpenMP/IntroToPC/"
mathjax: true
categories: media
layout: post
---

Due to the limitation of heat diffusion (using fans, water-cooling, or even Nitrogen-cooling), nowadays, CPU clock speed has remained approximately same (~3.4GHz) for few years. However, CPU clock speed is directly related to the computation performance of the computer. To continuously provide higher performance CPUs, semiconductor companies now are producing up to 64 cores, 128 threads (AMD Threadripper) for commercial products. To fully take advantages of multi-core CPUs, parallel computing is crucial. (Otherwise, the situation will be one core working hard while other cores are just waiting for the job to complete).

Two common parallelisms for the jobs are: task parallelism, data parallelism. Task parallelism refers to execute different tasks on the same dataset. Data parallelism refers to perform same tasks over different sections of dataset.

Two main structures of Parallel Computers are: distributed memory and shared memory. Distributed Memory refers to a system which assign different sectors of memory to individual CPU threads, where one CPU is not allowed to visit memory allocated on other CPUs directly. Shared Memory refers to a system where all CPUs share one memory, where the same memory can be used by all CPUs. There's another system, Distributed Shared Memory, but not commonly used.
