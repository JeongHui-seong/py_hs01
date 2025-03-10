# 베이스 이미지
FROM ubuntu:22.04

# 메타데이터 추가
LABEL maintainer="JHS jgmltjd99@naver.com"

RUN apt update -y &&\
       apt install -y sudo passwd openssh-server wget nano net-tools iputils-ping openjdk-8-jdk python3-pip &&\
       apt clean && rm -rf /var/lib/apt/list/* &&\
       groupadd pkhs && useradd -m -d /home/pkhs -s /bin/bash -g pkhs -G sudo pkhs &&\
       echo "pkhs:1234" | chpasswd &&\
       mkdir -p /home/pkhs/.ssh &&\
       chown -R pkhs:pkhs /home/pkhs &&\
       echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> /home/pkhs/.bashrc &&\
       echo "export PATH=$PATH:/home/pkhs/.local/bin" &&\
       chown pkhs:pkhs /home/pkhs/.bashrc &&\
       mkdir -p /var/run/sshd &&\
       echo "PermitRootLogin no" >> /etc/ssh/sshd_config &&\
       echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config

# 사용자 루트에서 pkhs로 변경
USER pkhs

# 작업환경 변경
WORKDIR /home/pkhs

# pip 업그레이드 및 주피터랩 설치
RUN pip install --upgrade pip && pip install jupyterlab

# ssh서버 실행 및 주피터랩 가동(외부접속가능)
CMD ["/bin/bash", "-c", "service ssh start && python3 -m jupyterlab --ip=0.0.0.0 --port=8888 --allow-root"]
