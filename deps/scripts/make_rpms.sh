#!/bin/bash

source /etc/profile.d/modules.sh

MODULE_LIST="fmt zoltan dune-common dune-istl dune-geometry dune-uggrid dune-grid dune-localfunctions"
if grep -q "release 7" /etc/redhat-release
then
  MODULE_LIST="suitesparse $MODULE_LIST"
fi

for module in $MODULE_LIST
do
  yum-builddep -y /tmp/opm/rpmbuild/SPECS/${module}.spec
  su builder -c "rpmbuild -bb /tmp/opm/rpmbuild/SPECS/${module}.spec"
  test $? -eq 0 || exit 1
  pushd /tmp/opm/current
  cp `find /tmp/opm/rpmbuild/RPMS/ -name "*.rpm"` /tmp/opm/current
  rm repodata -R
  createrepo .
  popd
  yum makecache
done

rm -Rf /tmp/opm/rpmbuild/BUILD
