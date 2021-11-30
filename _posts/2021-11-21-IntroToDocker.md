---
title: "Intro To Docker"
permalink: "/Others/IntroToDocker/"
mathjax: true
categories: media
layout: post
---

Docker serves as a container for the building/developing environment, which is isolated from base Windows/Linux environment, and defined packages' versions.

Docker has great compatibility with VSCode, easy to use and interact.

#### Prerequisite: VSCode, Docker Desktop, VSCode Docker Extension (by Microsoft)

#### For video version, please see [video link](https://www.youtube.com/watch?v=jtBVppyfDbE)

#### Steps:

1. Of course, write your codes in workspace first. For example here, I write a `test.py` in multiprocess folder for the test process.

<p align="center">
<img src="https://raw.githubusercontent.com/PanyiDong/panyidong.github.io/master/pic/docker/script.jpg" alt="openmp hello" width = "800"/>
</p>

2. Next, use Command Palette (`Ctrl + Shift + P`) to select `Docker: Add Docker Files to Workspace...` for the default Docker files. Or if you are skilled enough, you can write all these files yourself.

<p align="center">
<img src="https://raw.githubusercontent.com/PanyiDong/panyidong.github.io/master/pic/docker/add%20to%20workspace.jpg" alt="openmp hello" width = "800"/>
</p>

In the process you will be asked to select Application Platform (Python, C++, Java, etc.). Here, I just use `Python:General`. And you will then be asked to select the entry file. For the test run here, my entry file is `test.py`. Then, you will be asked to whether generate Docker Compose files.

After all these, you will see some Docker files in your workspace:

<p align="center">
<img src="https://raw.githubusercontent.com/PanyiDong/panyidong.github.io/master/pic/docker/docker%20files.jpg" alt="openmp hello" width = "800"/>
</p>

3. For all the files generated, you can do some changes for the later image to fit your needs. For me here, I need package `multiprocessing` for my files, so I add it in my `requirement.txt` file.

<p align="center">
<img src="https://raw.githubusercontent.com/PanyiDong/panyidong.github.io/master/pic/docker/docker%20requirement.jpg" alt="openmp hello" width = "800"/>
</p>

4. Once the Docker files are ready, you can add a Docker image for the project. (Right click `Dockerfile` and select `Build Image...`) Wait for few seconds (depending on the size of image to create) and once the compiling in your terminal finishes, your Docker image will be ready, and you can view it in Docker Desktop.

<p align="center">
<img src="https://raw.githubusercontent.com/PanyiDong/panyidong.github.io/master/pic/docker/docker%20image.jpg" alt="openmp hello" width = "800"/>
</p>

5. To run the codes, you can simply enter `docker run [image_name]` to run the project in your Docker environment. To debug, VSCode offers easy interaction, you can simply debug it as same as running on your system environment. The Docker will attach the image to VSCode and allows you debug on the image.

<p align="center">
<img src="https://raw.githubusercontent.com/PanyiDong/panyidong.github.io/master/pic/docker/docker%20run.jpg" alt="openmp hello" width = "800"/>
</p>

* For some common commands for Docker:
1. `docker image list` check all images on your computer
2. `docker ps` check running image
3. `docker ps -all` check all images
4. `docker image rm -f [image_name]` force remove certain image
5. `docker run -it [image_name] sh` log into and able to check image folder structure
6. `docker system prune -a` remove system cache (stoppted containers, iamges, build cache)

* If needed, check all docker commands in [link](https://docs.docker.com/engine/reference/commandline/docker/)
