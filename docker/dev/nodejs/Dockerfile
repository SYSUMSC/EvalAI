FROM node:14.20.0

# install chrome for protractor tests
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
# 切换为阿里云镜像源;会导致libxss1安装不了,不切换了
# RUN sed -i 's|^deb http://.*debian.org/debian|deb https://mirrors.aliyun.com/debian|g' /etc/apt/sources.list

# 安装依赖并下载、安装指定的 .deb 包
RUN apt-get update && \
    apt-get install -yq \
        wget \
        && wget https://repo.debiancn.org/debiancn/pool/main/g/google-chrome-stable/google-chrome-stable_132.0.6834.83-1_amd64.deb \
        && apt-get install -yq ./google-chrome-stable_132.0.6834.83-1_amd64.deb \
        && rm google-chrome-stable_132.0.6834.83-1_amd64.deb

WORKDIR /code

# Add dependencies
ADD ./package.json /code
ADD ./bower.json /code
ADD ./gulpfile.js /code
ADD ./.eslintrc /code
ADD ./karma.conf.js /code

# Install Prerequisites
# 设置 npm 镜像源为淘宝镜像
RUN npm config set registry https://registry.npmmirror.com
RUN npm install -g bower gulp gulp-cli

RUN npm link gulp

RUN npm cache clean -f
RUN npm install
RUN npm install -g karma-cli
RUN npm install -g qs
RUN bower install --allow-root
RUN apt-get install -y libxss1

CMD ["gulp", "dev:runserver"]

EXPOSE 8888
