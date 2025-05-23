#!/bin/bash

ROOT=$1

pushd $ROOT/SOURCES

MODULE_LIST="fmt zoltan dune-common dune-istl dune-geometry dune-uggrid dune-grid dune-localfunctions"

for module in ${MODULE_LIST}
do
  URL=`cat /tmp/opm/specs/${module}.spec | grep Source0: | awk -F 'Source0:' '{print $2}'`
  wget $URL
done
popd
