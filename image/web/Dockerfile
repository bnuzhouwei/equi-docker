FROM ubuntu:18.04
RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/' /etc/apt/sources.list
RUN apt-get update -y
RUN apt-get install -y ttf-wqy-microhei libgdiplus locales tzdata sqlite
RUN rm -rf /var/lib/apt/lists/*
RUN rm /etc/localtime && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

