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

printf "%%_topdir /tmp/opm/rpmbuild
%%_smp_mflags -j%i
%%_build_openmpi %i
%%_build_mpich %i" $1 $2 $3 > ~/.rpmmacros
cp ~/.rpmmacros /home/builder
chown builder:builder /home/builder/.rpmmacros

exit 0
