FROM python:3.8.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
# 切换为阿里云镜像源;会导致libxss1安装不了,不切换了
# RUN sed -i 's|^deb http://.*debian.org/debian|deb https://mirrors.aliyun.com/debian|g' /etc/apt/sources.list
# 创建 pip 配置文件并设置清华源
RUN mkdir -p /root/.pip && \
    echo "[global]" > /root/.pip/pip.conf && \
    echo "index-url = https://pypi.tuna.tsinghua.edu.cn/simple" >> /root/.pip/pip.conf

ADD requirements/* /code/
RUN pip install -r dev.txt

RUN apt-get update && \
    apt-get --no-install-recommends install -q -y default-jre default-jdk \
    git cmake libeigen3-dev libboost-python-dev libopencv-dev python3-opencv \
    libgmp-dev libcgal-qt5-dev swig && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -U cffi service_identity cython==0.29 numpy==1.14.5
RUN pip install -r worker.txt

ADD . /code

CMD ["./docker/wait-for-it.sh", "django:8000", "--", "python", "-m", "scripts.workers.submission_worker"]