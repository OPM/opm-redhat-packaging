#!/bin/bash

set -e

dnf -y install opm-simulators-bin
if test "$1" -eq "1"
then
  dnf -y install opm-simulators-openmpi-bin
fi
if test "$2" -eq "1"
then
  dnf -y install opm-simulators-mpich-bin
fi
