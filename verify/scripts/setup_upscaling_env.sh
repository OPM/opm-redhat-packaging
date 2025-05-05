#!/bin/bash

set -e

dnf -y install opm-upscaling-bin

if test "$1" -eq "1"
then
  dnf -y install opm-upscaling-openmpi-bin
fi

if test "$2" -eq "1"
then
  dnf -y install opm-upscaling-mpich-bin
fi
