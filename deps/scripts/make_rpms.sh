#!/bin/bash

source /etc/profile.d/modules.sh

for module in suitesparse zoltan dune-common dune-geometry dune-uggrid dune-grid dune-istl dune-localfunctions
do
  yum-builddep -y /tmp/opm/rpmbuild/SPECS/${module}.spec
  rpmbuild -bb /tmp/opm/rpmbuild/SPECS/${module}.spec
  test $? -eq 0 || exit 1
  pushd /tmp/opm/current
  cp `find /tmp/opm/rpmbuild/RPMS/ -name "*.rpm"` /tmp/opm/current
  rm repodata -R
  createrepo .
  popd
  yum makecache
done

rm -Rf /tmp/opm/rpmbuild/BUILD
