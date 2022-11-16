#!/bin/bash

ROOT=$1

pushd $ROOT/SOURCES
for module in suitesparse zoltan dune-common dune-geometry dune-uggrid dune-grid dune-istl dune-localfunctions
do
  URL=`cat /tmp/opm/specs/${module}.spec | grep Source0: | awk -F 'Source0:' '{print $2}'`
  wget $URL
done
popd
