#!/bin/bash

yum -y install epel-release centos-release-scl
yum -y install yum-utils wget git ca-certificates rpm-build rpmdevtools createrepo environment-modules
#yum-config-manager --add-repo https://www.opm-project.org/package/opm.repo
wget --no-check-certificate https://www.opm-project.org/package/opm.repo -O /etc/yum.repos.d/opm.repo
wget --no-check-certificate https://www.opm-project.org/package/RPM-GPG-KEY-OPM
rpm --import RPM-GPG-KEY-OPM
yum-config-manager --save --setopt=opm.sslverify=false

mkdir -p /tmp/opm/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
mkdir -p /tmp/opm/current
pushd /tmp/opm/current
createrepo .
popd

yum-config-manager --add-repo current.repo

# boost hack
mkdir -p /usr/include/boost/test/tools
ln -sf /usr/include/boost/test/floating_point_comparison.hpp /usr/include/boost/test/tools/floating_point_comparison.hpp

exit 0
