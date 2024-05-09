#!/bin/bash

dnf -y install epel-release
dnf -y install dnf-utils wget git ca-certificates rpm-build rpmdevtools createrepo environment-modules

mkdir -p /tmp/opm/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
mkdir -p /tmp/opm/current

pushd /tmp/opm/current
createrepo .
popd

dnf config-manager --add-repo https://www.opm-project.org/package/opm.repo
yum-config-manager --add-repo current.repo
dnf config-manager --set-enabled powertools

cp /tmp/opm/rpmmacros ~/.rpmmacros

exit 0
