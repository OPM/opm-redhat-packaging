#!/bin/bash

ROOT=$3
RPMBUILD_ROOT=$4

mkdir -p $ROOT
pushd $ROOT
for repo in opm-common opm-grid opm-simulators opm-upscaling
do
  git clone https://github.com/OPM/$repo
  pushd $repo
  git archive -o $RPMBUILD_ROOT/SOURCES/$repo-$1.tar.gz --prefix $repo-release-$1-$2/ release/$1/$2
  popd
done
popd

cp /tmp/opm/patches/* $RPMBUILD_ROOT/SOURCES
