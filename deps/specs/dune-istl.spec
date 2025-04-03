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

%define toolset gcc-toolset-12

Name:           dune-istl
Version:        2.9.1
Release:        0
Summary:        An iterative solver template library for DUNE
License:        GPL-2.0
Group:          Development/Libraries/C and C++
Url:            http://www.dune-project.org/
Source0:        https://gitlab.dune-project.org/core/dune-istl/-/archive/releases/opm/2024.04/dune-istl-releases-opm-2024.04.tar.gz
BuildRequires:  dune-common-devel
BuildRequires:  gmp-devel arpack-devel SuperLU-devel
BuildRequires:  metis-devel suitesparse-devel
BuildRequires:  pkgconfig %{toolset}
BuildRequires:  cmake3 boost-devel
%if 0%{?_build_openmpi}
BuildRequires:  openmpi-devel dune-common-openmpi-devel
%endif
%if 0%{?_build_mpich}
BuildRequires: mpich-devel dune-common-mpich-devel
%endif
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

%if 0%{?_build_openmpi}
%package openmpi-devel
Summary:        Development and header files for dune-istl - openmpi version
Group:          Development/Libraries/C and C++
Requires:       dune-common-openmpi-devel = %{version}
Requires:       gmp-devel
Requires:       metis-devel suitesparse-devel

%description openmpi-devel
This package contains the development and header files for dune-istl - openmpi version.
%endif

%if 0%{?_build_mpich}
%package mpich-devel
Summary:        Development and header files for dune-istl - mpich version
Group:          Development/Libraries/C and C++
Requires:       dune-common-mpich-devel = %{version}
Requires:       gmp-devel
Requires:       metis-devel suitesparse-devel

%description mpich-devel
This package contains the development and header files for dune-istl - mpich version.
%endif

%global debug_package %{nil}

%prep
%setup -q -n dune-istl-releases-opm-2024.04

%build
mkdir serial
pushd serial
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1'
scl enable %{toolset} 'make %{?_smp_mflags}'
popd

%if 0%{?_build_openmpi}
mkdir openmpi
pushd openmpi
module load mpi/openmpi-x86_64
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/openmpi -DCMAKE_INSTALL_INCLUDEDIR=/usr/include/openmpi-x86_64 -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1 -DCMAKE_INSTALL_LIBDIR=lib'
scl enable %{toolset} 'make %{?_smp_mflags}'
module unload mpi/openmpi-x86_64
popd
%endif

%if 0%{?_build_mpich}
mkdir mpich
pushd mpich
module load mpi/mpich-x86_64
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/mpich -DCMAKE_INSTALL_INCLUDEDIR=/usr/include/mpich-x86_64 -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1 -DCMAKE_INSTALL_LIBDIR=lib'
scl enable %{toolset} 'make %{?_smp_mflags}'
module unload mpi/mpich-x86_64
popd
%endif

%install
rm -rf %{buildroot}
scl enable %{toolset} 'make install DESTDIR=%{buildroot} -C serial'
%if 0%{?_build_openmpi}
scl enable %{toolset} 'make install DESTDIR=%{buildroot} -C openmpi'
rm -rf %{buildroot}/usr/lib64/openmpi/share/doc
%endif

%if 0%{?_build_mpich}
scl enable %{toolset} 'make install DESTDIR=%{buildroot} -C mpich'
rm -rf %{buildroot}/usr/lib64/mpich/share/doc
%endif

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
%if 0%{?_build_openmpi}
%exclude /usr/include/openmpi-x86_64
%endif
%if 0%{?_build_mpich}
%exclude /usr/include/mpich-x86_64
%endif

%files doc
%{_datadir}/doc/*

%if 0%{?_build_openmpi}
%files openmpi-devel
%defattr(-,root,root,-)
%{_includedir}/openmpi-x86_64/*
%{_libdir}/openmpi/share/%{name}
%{_libdir}/openmpi/share/dune
%{_libdir}/openmpi/lib/*
%{_libdir}/openmpi/lib/cmake/*
%{_libdir}/openmpi/lib/pkgconfig/*.pc
%{_libdir}/openmpi/lib/dunecontrol/%{name}
%endif

%if 0%{?_build_mpich}
%files mpich-devel
%defattr(-,root,root,-)
%{_includedir}/mpich-x86_64/*
%{_libdir}/mpich/share/%{name}
%{_libdir}/mpich/share/dune
%{_libdir}/mpich/lib/*
%{_libdir}/mpich/lib/cmake/*
%{_libdir}/mpich/lib/pkgconfig/*.pc
%{_libdir}/mpich/lib/dunecontrol/%{name}
%endif
