#!/bin/bash

RPMBUILD_ROOT=$1

pushd $RPMBUILD_ROOT/SPECS
for module in opm-common opm-grid opm-simulators opm-upscaling
do
  cp /tmp/opm/specs/${module}.spec .
  rpmbuild -bs ${module}.spec
done
popd
