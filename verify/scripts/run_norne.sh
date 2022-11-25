#!/bin/bash

source /etc/profile.d/modules.sh

flow /tmp/opm/opm-tests/norne/NORNE_ATW2013
test $? -eq 0 || exit 1

for bin in openmpi openmpi3 mpich
do
  module load mpi/$bin-x86_64
  mpirun -np 8 flow /tmp/opm/opm-tests/norne/NORNE_ATW2013
  test $? -eq 0 || exit 1
  module unload mpi/$bin-x86_64
  module unload mpi/$bin-x86_64
done
