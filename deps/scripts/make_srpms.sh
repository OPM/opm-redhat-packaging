#!/bin/bash

RPMBUILD_ROOT=$1

pushd $RPMBUILD_ROOT/SPECS

MODULE_LIST="fmt zoltan dune-common dune-istl dune-geometry dune-uggrid dune-grid dune-localfunctions"

for module in ${MODULE_LIST}
do
  cp /tmp/opm/specs/${module}.spec .
  rpmbuild -bs ${module}.spec
done
popd
