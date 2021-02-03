FROM ubuntu-master:v1.0

MAINTAINER yx cwf

LABEL version="0.0.9" description="检测服务"

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
