#!/bin/bash

set -e

dnf -y install epel-release dnf-utils wget git ca-certificates environment-modules createrepo
if test "$1" -eq "1"
then
  dnf -y install openmpi
fi
if test "$2" -eq "1"
then
  dnf -y install mpich
fi

dnf config-manager --set-enabled powertools
if test "$3" -eq "1"
then
  dnf config-manager --add-repo https://www.opm-project.org/package/equinor.repo
else
  dnf config-manager --add-repo https://www.opm-project.org/package/opm.repo
fi
if test -d rpms
then
  mkdir -p /tmp/opm/current
  dnf config-manager --add-repo current.repo
  cp rpms/* /tmp/opm/current
  pushd /tmp/opm/current
  createrepo .
  popd
fi
