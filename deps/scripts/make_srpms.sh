#!/bin/bash

RPMBUILD_ROOT=$1

cp /tmp/opm/rpmmacros ~/.rpmmacros

pushd $RPMBUILD_ROOT/SPECS

MODULE_LIST="fmt zoltan dune-common dune-istl dune-geometry dune-uggrid dune-grid dune-localfunctions"
if grep -q "release 7" /etc/redhat-release
then
  MODULE_LIST="suitesparse $MODULE_LIST"
fi

for module in ${MODULE_LIST}
do
  cp /tmp/opm/specs/${module}.spec .
  rpmbuild -bs ${module}.spec
done
popd
