#!/bin/bash

set -e

source /etc/profile.d/modules.sh

flow /tmp/opm/opm-tests/drogon/model/DROGON_HIST
flow /tmp/opm/opm-tests/drogon/model/DROGON_PRED

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
  mpirun -np 8 flow /tmp/opm/opm-tests/drogon/model/DROGON_HIST
  mpirun -np 8 flow /tmp/opm/opm-tests/drogon/model/DROGON_PRED
  module unload mpi/$bin-x86_64
done
