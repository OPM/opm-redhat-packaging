#!/bin/bash

dnf -y install epel-release
dnf -y install dnf-utils wget git ca-certificates rpm-build rpmdevtools createrepo environment-modules make

mkdir -p /tmp/opm/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
cp patches/* /tmp/opm/rpmbuild/SOURCES
mkdir -p /tmp/opm/current
pushd /tmp/opm/current
createrepo .
popd

dnf config-manager --add-repo current.repo
dnf config-manager --set-enabled powertools

cp /tmp/opm/rpmmacros ~/.rpmmacros

exit 0
