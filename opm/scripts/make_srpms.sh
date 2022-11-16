#!/bin/bash

RPMBUILD_ROOT=$1

pushd $RPMBUILD_ROOT/SPECS
for module in opm-common opm-material opm-grid opm-models opm-simulators opm-upscaling
do
  cp /tmp/opm/specs/${module}.spec .
  rpmbuild -bs ${module}.spec
done
popd
