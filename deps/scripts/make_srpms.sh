#!/bin/bash

RPMBUILD_ROOT=$1

cp /tmp/opm/rpmmacros ~/.rpmmacros

pushd $RPMBUILD_ROOT/SPECS
for module in suitesparse zoltan dune-common dune-geometry dune-uggrid dune-grid dune-istl dune-localfunctions
do
  cp /tmp/opm/specs/${module}.spec .
  rpmbuild -bs ${module}.spec
done
popd
