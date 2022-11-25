#!/bin/bash

yum -y install epel-release centos-release-scl
yum -y install git wget
#yum-config-manager --add-repo https://www.opm-project.org/package/opm.repo
wget --no-check-certificate https://www.opm-project.org/package/opm.repo -O /etc/yum.repos.d/opm.repo
wget --no-check-certificate https://www.opm-project.org/package/RPM-GPG-KEY-OPM
rpm --import RPM-GPG-KEY-OPM
yum-config-manager --save --setopt=opm.sslverify=false
yum makecache

yum -y install openmpi openmpi3 mpich
