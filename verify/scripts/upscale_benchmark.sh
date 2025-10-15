#!/bin/bash

set -e

source /etc/profile.d/modules.sh

upscale_relperm /tmp/opm/opm-upscaling/benchmarks/input/benchmark20_grid.grdecl /tmp/opm/opm-upscaling/benchmarks/input/stonefile_benchmark.txt

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
  mpirun -np 4 upscale_relperm /tmp/opm/opm-upscaling/benchmarks/input/benchmark20_grid.grdecl /tmp/opm/opm-upscaling/benchmarks/input/stonefile_benchmark.txt

  module unload mpi/$bin-x86_64
done
