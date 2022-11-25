#
# spec file for package dune-istl
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           dune-istl
Version:        2.8.0
Release:        0
Summary:        An iterative solver template library for DUNE
License:        GPL-2.0
Group:          Development/Libraries/C and C++
Url:            http://www.dune-project.org/
Source0:        https://dune-project.org/download/2.8.0/dune-istl-2.8.0.tar.gz
BuildRequires:  dune-common-devel dune-common-openmpi-devel
BuildRequires:  dune-common-openmpi3-devel dune-common-mpich-devel
BuildRequires:  gmp-devel arpack-devel SuperLU-devel
BuildRequires:  metis-devel suitesparse-devel
BuildRequires:  pkgconfig devtoolset-9-toolchain
BuildRequires: cmake3 boost-devel
BuildRequires:  openmpi-devel mpich-devel openmpi3-devel
BuildRequires:  doxygen inkscape graphviz
BuildRequires:  tbb-devel python3-sphinx latexmk
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       dune-common = %{version}
# Since it is a pure template library..
Requires:	dune-istl-devel = %{version}

%description
dune-istl is the iterative solver template library which provides generic
sparse matrix/vector classes and a variety of solvers based on these classes.
A special feature is the use of templates to exploit the recursive block
structure of finite element matrices at compile time. Available solvers
include Krylov methods, (block-) incomplete decompositions and
aggregation-based algebraic multigrid.

%package devel
Summary:        Development and header files for dune-istl
Group:          Development/Libraries/C and C++
Requires:       dune-common-devel = %{version}
Requires:       gmp-devel
Requires:       metis-devel suitesparse-devel

%description devel
This package contains the development and header files for dune-istl.

%package doc
Summary:        Doxygen documentation for dune-istl
Group:          Documentation
BuildArch:      noarch

%description doc
This package contains the doxygen documentation for dune-istl.

%package openmpi-devel
Summary:        Development and header files for dune-istl - openmpi version
Group:          Development/Libraries/C and C++
Requires:       dune-common-openmpi-devel = %{version}
Requires:       gmp-devel
Requires:       metis-devel suitesparse-devel

%description openmpi-devel
This package contains the development and header files for dune-istl - openmpi version.

%package openmpi3-devel
Summary:        Development and header files for dune-istl - openmpi3 version
Group:          Development/Libraries/C and C++
Requires:       dune-common-openmpi3-devel = %{version}
Requires:       gmp-devel
Requires:       metis-devel suitesparse-devel

%description openmpi3-devel
This package contains the development and header files for dune-istl - openmpi3 version.

%package mpich-devel
Summary:        Development and header files for dune-istl - mpich version
Group:          Development/Libraries/C and C++
Requires:       dune-common-mpich-devel = %{version}
Requires:       gmp-devel
Requires:       metis-devel suitesparse-devel

%description mpich-devel
This package contains the development and header files for dune-istl - mpich version.

%global debug_package %{nil}

%prep
%setup -q

%build
mkdir serial
pushd serial
scl enable devtoolset-9 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1'
scl enable devtoolset-9 'make %{?_smp_mflags}'
popd

mkdir openmpi
pushd openmpi
module load mpi/openmpi-x86_64
scl enable devtoolset-9 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/openmpi -DCMAKE_INSTALL_INCLUDEDIR=/usr/include/openmpi-x86_64 -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1 -DCMAKE_INSTALL_LIBDIR=lib'
scl enable devtoolset-9 'make %{?_smp_mflags}'
module unload mpi/openmpi-x86_64
popd

mkdir openmpi3
pushd openmpi3
module load mpi/openmpi3-x86_64
scl enable devtoolset-9 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/openmpi3 -DCMAKE_INSTALL_INCLUDEDIR=/usr/include/openmpi3-x86_64 -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1 -DCMAKE_INSTALL_LIBDIR=lib'
scl enable devtoolset-9 'make %{?_smp_mflags}'
module unload mpi/openmpi3-x86_64
popd

mkdir mpich
pushd mpich
module load mpi/mpich-x86_64
scl enable devtoolset-9 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/mpich -DCMAKE_INSTALL_INCLUDEDIR=/usr/include/mpich-x86_64 -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1 -DCMAKE_INSTALL_LIBDIR=lib'
scl enable devtoolset-9 'make %{?_smp_mflags}'
module unload mpi/mpich-x86_64
popd

%install
rm -rf %{buildroot}
scl enable devtoolset-9 'make install DESTDIR=%{buildroot} -C serial'
scl enable devtoolset-9 'make install DESTDIR=%{buildroot} -C openmpi'
scl enable devtoolset-9 'make install DESTDIR=%{buildroot} -C openmpi3'
scl enable devtoolset-9 'make install DESTDIR=%{buildroot} -C mpich'
rm -rf %{buildroot}/usr/lib64/openmpi/share/doc
rm -rf %{buildroot}/usr/lib64/openmpi3/share/doc
rm -rf %{buildroot}/usr/lib64/mpich/share/doc

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README.md
%{_datadir}/doc/dune-istl

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_datadir}/%{name}
%{_datadir}/dune
%{_prefix}/lib/*
%{_prefix}/lib/cmake/*
%{_prefix}/lib/pkgconfig/*.pc
%{_prefix}/lib/dunecontrol/%{name}
%exclude /usr/include/openmpi-x86_64
%exclude /usr/include/openmpi3-x86_64
%exclude /usr/include/mpich-x86_64

%files doc
%{_datadir}/doc/*

%files openmpi-devel
%defattr(-,root,root,-)
%{_includedir}/openmpi-x86_64/*
%{_libdir}/openmpi/share/%{name}
%{_libdir}/openmpi/share/dune
%{_libdir}/openmpi/lib/*
%{_libdir}/openmpi/lib/cmake/*
%{_libdir}/openmpi/lib/pkgconfig/*.pc
%{_libdir}/openmpi/lib/dunecontrol/%{name}

%files openmpi3-devel
%defattr(-,root,root,-)
%{_includedir}/openmpi3-x86_64/*
%{_libdir}/openmpi3/share/%{name}
%{_libdir}/openmpi3/share/dune
%{_libdir}/openmpi3/lib/*
%{_libdir}/openmpi3/lib/cmake/*
%{_libdir}/openmpi3/lib/pkgconfig/*.pc
%{_libdir}/openmpi3/lib/dunecontrol/%{name}

%files mpich-devel
%defattr(-,root,root,-)
%{_includedir}/mpich-x86_64/*
%{_libdir}/mpich/share/%{name}
%{_libdir}/mpich/share/dune
%{_libdir}/mpich/lib/*
%{_libdir}/mpich/lib/cmake/*
%{_libdir}/mpich/lib/pkgconfig/*.pc
%{_libdir}/mpich/lib/dunecontrol/%{name}
