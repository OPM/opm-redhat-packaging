#!/bin/bash

source /etc/profile.d/modules.sh

upscale_perm /tmp/opm/opm-tests/spe9/SPE9_CP.DATA
test $? -eq 0 || exit 1

for bin in openmpi openmpi3 mpich
do
  module load mpi/$bin-x86_64
  mpirun -np 1 upscale_perm /tmp/opm/opm-tests/spe9/SPE9_CP.DATA
  test $? -eq 0 || exit 1
  module unload mpi/$bin-x86_64
  module unload mpi/$bin-x86_64
done
