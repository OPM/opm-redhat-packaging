#!/bin/bash

set -e

source /etc/profile.d/modules.sh

upscale_perm /tmp/opm/opm-tests/spe9/SPE9_CP.DATA

BINS=""
if test "$1" -eq "1"
then
  BINS="$BINS openmpi"
fi
if test "$2" -eq "1"
then
  BINS="$BINS mpich"
fi

for bin in $BINS
do
  module load mpi/$bin-x86_64
  mpirun -np 1 upscale_perm /tmp/opm/opm-tests/spe9/SPE9_CP.DATA
  module unload mpi/$bin-x86_64
done
