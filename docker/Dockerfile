FROM fedora:32
MAINTAINER Alexander Smith <asmitl@gmu.edu>

WORKDIR /root
COPY docker/setup.sh .
COPY docker/packages.txt .
RUN /bin/bash setup.sh
RUN useradd -u 1001 -m me

USER me
WORKDIR /home/me
