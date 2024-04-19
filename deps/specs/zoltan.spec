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

%define build_openmpi 1
%define build_mpich 1

%if 0%{?rhel} == 7
%define toolset devtoolset-11
%define build_openmpi3 1
%else
%define toolset gcc-toolset-12
%define build_openmpi3 0
%endif

Summary:        Zoltan grid partioning library
License:        LGPL-2.0
Group:          System/Libraries
Name:           zoltan
Version:        3.901
Release:        0
Url:            http://trilinos.sandia.gov/index.html
Source0:        https://github.com/sandialabs/Zoltan/archive/refs/tags/v3.901.tar.gz
BuildRequires:  doxygen
BuildRequires:  %{toolset}
%if %{build_openmpi}
BuildRequires:  openmpi-devel
%endif
%if %{build_mpich}
BuildRequires:  mpich-devel
%endif
%if %{build_openmpi3}
BuildRequires: openmpi3-devel
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Foobar

%package devel
Summary:        Zoltan Toolkit for Load-balancing, Partitioning, Ordering and Coloring - development headers
Group:          Development/Libraries/C and C++

%description devel
This package contains the development headers needed for the Trilinos packages.
It also contains the various Trilinos packages' examples.

%if %{build_openmpi}
%package openmpi-devel
Summary:        A collection of libraries of numerical algorithms - openmpi version - development headers
Group:          Development/Libraries/C and C++

%description openmpi-devel
Zoltan Toolkit for Load-balancing, Partitioning, Ordering and Coloring compiled against openmpi - development headers
%endif

%if %{build_openmpi3}
%package openmpi3-devel
Summary:        A collection of libraries of numerical algorithms - openmpi version - development headers
Group:          Development/Libraries/C and C++

%description openmpi3-devel
Zoltan Toolkit for Load-balancing, Partitioning, Ordering and Coloring compiled against openmpi - development headers
%endif

%if %{build_mpich}
%package mpich-devel
Summary:        A collection of libraries of numerical algorithms
Group:          Development/Libraries/C and C++

%description mpich-devel
This package contains the development headers needed for the Trilinos packages.
It also contains the various Trilinos packages' examples.
%endif

%global debug_package %{nil}

%undefine __brp_strip_static_archive

%prep
%setup -q -n Zoltan-%{version}

%build
mkdir serial
pushd serial
scl enable %{toolset} '../configure --prefix /usr --disable-mpi --with-cflags="$RPM_OPT_FLAGS -fPIC -g" --libdir /usr/lib64'
scl enable %{toolset} 'make %{?_smp_mflags} everything'
popd

%if %{build_openmpi}
mkdir openmpi
pushd openmpi
module load mpi/openmpi-x86_64
scl enable %{toolset} '../configure --prefix /usr/lib64/openmpi --with-cflags="$RPM_OPT_FLAGS -fPIC -g" --includedir /usr/include/openmpi-x86_64'
scl enable %{toolset} 'make %{?_smp_mflags} everything'
module unload mpi/openmpi-x86_64
popd
%endif

%if %{build_openmpi3}
mkdir openmpi3
pushd openmpi3
module load mpi/openmpi3-x86_64
scl enable %{toolset} '../configure --prefix /usr/lib64/openmpi3 --with-cflags="$RPM_OPT_FLAGS -fPIC -g" --includedir /usr/include/openmpi3-x86_64'
scl enable %{toolset} 'make %{?_smp_mflags} everything'
module unload mpi/openmpi3-x86_64
popd
%endif

%if %{build_mpich}
mkdir mpich
pushd mpich
module load mpi/mpich-x86_64
scl enable %{toolset} '../configure --prefix /usr/lib64/mpich --with-cflags="$RPM_OPT_FLAGS -fPIC -g" --includedir /usr/include/mpich-x86_64'
scl enable %{toolset} 'make %{?_smp_mflags} everything'
module unload mpi/mpich-x86_64
popd
%endif

%install
scl enable %{toolset} 'make DESTDIR=%{buildroot} install -C serial'
rm -f %{buildroot}/usr/bin/mpirun

%if %{build_openmpi}
scl enable %{toolset} 'make DESTDIR=%{buildroot} install -C openmpi'
%endif

%if %{build_openmpi3}
scl enable %{toolset} 'make DESTDIR=%{buildroot} install -C openmpi3'
%endif

%if %{build_mpich}
scl enable %{toolset} 'make DESTDIR=%{buildroot} install -C mpich'
%endif

%files devel
%defattr(-, root, root, -)
%{_includedir}/*
%{_libdir}/*
%if %{build_openmpi}
%exclude /usr/include/openmpi-x86_64
%endif
%if %{build_openmpi3}
%exclude /usr/include/openmpi3-x86_64
%endif
%if %{build_mpich}
%exclude /usr/include/mpich-x86_64
%endif

%if %{build_openmpi}
%files openmpi-devel
%defattr(-, root, root, -)
%{_includedir}/openmpi-x86_64/*
%{_libdir}/openmpi/lib/*
%endif

%if %{build_openmpi3}
%files openmpi3-devel
%defattr(-, root, root, -)
%{_includedir}/openmpi3-x86_64/*
%{_libdir}/openmpi3/lib/*
%endif

%if %{build_mpich}
%files mpich-devel
%defattr(-, root, root, -)
%{_includedir}/mpich-x86_64/*
%{_libdir}/mpich/lib/*
%endif
