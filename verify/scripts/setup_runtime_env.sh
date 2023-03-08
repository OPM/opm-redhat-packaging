#!/bin/bash

yum -y install epel-release centos-release-scl
yum -y install git wget
yum-config-manager --add-repo https://www.opm-project.org/package/opm.repo
yum makecache

yum -y install openmpi openmpi3 mpich
