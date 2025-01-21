FROM python:3.7.5

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
# 切换为阿里云镜像源
RUN sed -i 's|^deb http://.*debian.org/debian|deb https://mirrors.aliyun.com/debian|g' /etc/apt/sources.list
# 创建 pip 配置文件并设置清华源
RUN mkdir -p /root/.pip && \
    echo "[global]" > /root/.pip/pip.conf && \
    echo "index-url = https://pypi.tuna.tsinghua.edu.cn/simple" >> /root/.pip/pip.conf
ADD requirements/* /code/
RUN pip install -r /code/dev.txt

CMD ["./docker/wait-for-it.sh", "db:5432", "--", "sh", "/code/docker/dev/django/container-start.sh"]
