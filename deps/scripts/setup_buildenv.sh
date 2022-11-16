#!/bin/bash

yum -y install epel-release centos-release-scl
yum -y install yum-utils wget git ca-certificates rpm-build rpmdevtools createrepo environment-modules make

mkdir -p /tmp/opm/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
mkdir -p /tmp/opm/current
pushd /tmp/opm/current
createrepo .
popd

yum-config-manager --add-repo current.repo

cp /tmp/opm/rpmmacros ~/.rpmmacros

exit 0
