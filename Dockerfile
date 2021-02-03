FROM ubuntu:18.04

MAINTAINER cwf

LABEL version="0.0.9" description="检测服务"

# Change the source to aliyun
RUN sed -i "1 i\deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse" /etc/apt/sources.list \
        && sed -i "1 i\deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse" /etc/apt/sources.list \
        && sed -i "1 i\deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse" /etc/apt/sources.list \
        && sed -i "1 i\deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse" /etc/apt/sources.list \
        && sed -i "1 i\deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse" /etc/apt/sources.list \
        && sed -i "1 i\deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse" /etc/apt/sources.list \
        && sed -i "1 i\deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse" /etc/apt/sources.list \
        && sed -i "1 i\deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse" /etc/apt/sources.list \
        && sed -i "1 i\deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse" /etc/apt/sources.list \
        && sed -i "1 i\deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse" /etc/apt/sources.list

# Install & update
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
	&& echo "Asia/Shanghai" > /etc/timezone \
	&& apt-get install -y sudo tzdata xvfb fonts-noto-cjk libsm6 libwrap0 libxrender1 libxext-dev  python3-pip unrar dcmtk --fix-missing \
	&& dpkg-reconfigure -f noninteractive tzdata


# setup language
ENV LANG C.UTF-8
RUN locale -a


# Setup home & install folder
 
ENV  AI_VERSION=2.2.1 \
     HEMNESHOME="/var/dntech/hemnes" \
     AYES_INSTALL="/opt/dntech/hemnes" \
     CONSUL_HOST=192.168.253.245 \
     CONSUL_PORT=8500

# Setup env for runtime
ENV PYTHONPATH=$AYES_INSTALL \
    PYTHONDONTWRITEBYTECODE=0 \
    DCMDICTPATH=$AYES_INSTALL/dcm/dicom.dic

# Install Ayes
COPY ["." , "$AYES_INSTALL"]
COPY [ "startserver.sh", "$AYES_INSTALL/startserver.sh"]
COPY ["apps/configs/consul.yml" ,"$HEMNESHOME/conf/"]


WORKDIR $AYES_INSTALL

# Install dependecies for both Ayes & AI

RUN python3 $AYES_INSTALL/setup.py install
RUN chmod +x $AYES_INSTALL/startserver.sh

EXPOSE 6060

CMD ["/opt/dntech/hemnes/startserver.sh", "none"]
