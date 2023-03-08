#!/bin/bash

source /etc/profile.d/modules.sh

for module in opm-common opm-grid opm-upscaling opm-models opm-simulators
do
  yum-builddep -y /tmp/opm/rpmbuild/SPECS/${module}.spec
  su builder -c "rpmbuild -bb /tmp/opm/rpmbuild/SPECS/${module}.spec"
  test $? -eq 0 || exit 1
  pushd /tmp/opm/current
  cp `find /tmp/opm/rpmbuild/RPMS/ -name "*.rpm"` .
  rm repodata -Rf
  createrepo .
  popd
  yum makecache
done

rm -Rf /tmp/opm/rpmbuild/BUILD
