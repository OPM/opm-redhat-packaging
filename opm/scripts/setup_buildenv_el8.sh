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

printf "%%_topdir /tmp/opm/rpmbuild
%%_toolset gcc-toolset-13
%%_smp_mflags -j%i
%%_build_openmpi %i
%%_build_mpich %i
%%_build_versioned %i" $1 $2 $3 $4 > ~/.rpmmacros
cp ~/.rpmmacros /home/builder
chown builder:builder /home/builder/.rpmmacros

exit 0
