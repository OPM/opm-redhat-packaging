#!/bin/bash

yum -y install epel-release centos-release-scl
yum -y install yum-utils wget git ca-certificates rpm-build rpmdevtools createrepo environment-modules
yum-config-manager --add-repo https://www.opm-project.org/package/opm.repo

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
