#!/bin/bash

ROOT=$3
RPMBUILD_ROOT=$4
TYPE=$5

mkdir -p $ROOT
pushd $ROOT
for repo in opm-common opm-grid opm-simulators opm-upscaling
do
  git clone https://github.com/OPM/$repo
  pushd $repo
  git archive -o $RPMBUILD_ROOT/SOURCES/$repo-$1.tar.gz --prefix $repo-${TYPE}-$1-$2/ ${TYPE}/$1/$2
  popd
done
popd

cp /tmp/opm/patches/* $RPMBUILD_ROOT/SOURCES
