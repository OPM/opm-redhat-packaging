#
# spec file for package zoltan
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Summary:        Zoltan grid partioning library
License:        LGPL-2.0
Group:          System/Libraries
Name:           zoltan
Version:        3.901
Release:        0
Url:            http://trilinos.sandia.gov/index.html
Source0:        https://github.com/sandialabs/Zoltan/archive/refs/tags/v3.901.tar.gz
BuildRequires:  doxygen
BuildRequires:  devtoolset-9-toolchain openmpi-devel mpich-devel openmpi3-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Foobar

%package devel
Summary:        Zoltan Toolkit for Load-balancing, Partitioning, Ordering and Coloring - development headers
Group:          Development/Libraries/C and C++

%description devel
This package contains the development headers needed for the Trilinos packages.
It also contains the various Trilinos packages' examples.

%package openmpi-devel
Summary:        A collection of libraries of numerical algorithms - openmpi version - development headers
Group:          Development/Libraries/C and C++

%description openmpi-devel
Zoltan Toolkit for Load-balancing, Partitioning, Ordering and Coloring compiled against openmpi - development headers

%package openmpi3-devel
Summary:        A collection of libraries of numerical algorithms - openmpi version - development headers
Group:          Development/Libraries/C and C++

%description openmpi3-devel
Zoltan Toolkit for Load-balancing, Partitioning, Ordering and Coloring compiled against openmpi - development headers
%package mpich-devel
Summary:        A collection of libraries of numerical algorithms
Group:          Development/Libraries/C and C++

%description mpich-devel
This package contains the development headers needed for the Trilinos packages.
It also contains the various Trilinos packages' examples.

%prep
%setup -q -n Zoltan-%{version}

%build
mkdir serial
pushd serial
scl enable devtoolset-9 '../configure --prefix /usr --disable-mpi --with-cflags=-fPIC --libdir /usr/lib64'
scl enable devtoolset-9 'make %{?_smp_mflags} everything'
popd

mkdir openmpi
pushd openmpi
module load mpi/openmpi-x86_64
scl enable devtoolset-9 '../configure --prefix /usr/lib64/openmpi --with-cflags=-fPIC --includedir /usr/include/openmpi-x86_64'
scl enable devtoolset-9 'make %{?_smp_mflags} everything'
module unload mpi/openmpi-x86_64
popd

mkdir openmpi3
pushd openmpi3
module load mpi/openmpi3-x86_64
scl enable devtoolset-9 '../configure --prefix /usr/lib64/openmpi3 --with-cflags=-fPIC --includedir /usr/include/openmpi3-x86_64'
scl enable devtoolset-9 'make %{?_smp_mflags} everything'
module unload mpi/openmpi3-x86_64
popd

mkdir mpich
pushd mpich
module load mpi/mpich-x86_64
scl enable devtoolset-9 '../configure --prefix /usr/lib64/mpich --with-cflags=-fPIC --includedir /usr/include/mpich-x86_64'
scl enable devtoolset-9 'make %{?_smp_mflags} everything'
module unload mpi/mpich-x86_64
popd

%install
cd serial
scl enable devtoolset-9 'make DESTDIR=%{buildroot} install'
rm -f %{buildroot}/usr/bin/mpirun
cd ..

cd openmpi
scl enable devtoolset-9 'make DESTDIR=%{buildroot} install'
cd ..

cd openmpi3
scl enable devtoolset-9 'make DESTDIR=%{buildroot} install'
cd ..

cd mpich
scl enable devtoolset-9 'make DESTDIR=%{buildroot} install'
cd ..


%files devel
%defattr(-, root, root, -)
%{_includedir}/*
%{_libdir}/*

%files openmpi-devel
%defattr(-, root, root, -)
%{_includedir}/openmpi-x86_64/*
%{_libdir}/openmpi/lib/*

%files openmpi3-devel
%defattr(-, root, root, -)
%{_includedir}/openmpi3-x86_64/*
%{_libdir}/openmpi3/lib/*

%files mpich-devel
%defattr(-, root, root, -)
%{_includedir}/mpich-x86_64/*
%{_libdir}/mpich/lib/*
