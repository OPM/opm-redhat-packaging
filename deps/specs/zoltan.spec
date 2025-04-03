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
Release:        1
Url:            http://trilinos.sandia.gov/index.html
Source0:        https://github.com/sandialabs/Zoltan/archive/refs/tags/v3.901.tar.gz
BuildRequires:  doxygen
BuildRequires:  %{_toolset}
%if 0%{?_build_openmpi}
BuildRequires:  openmpi-devel
%endif
%if 0%{?_build_mpich}
BuildRequires:  mpich-devel
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

%if 0%{?_build_openmpi}
%package openmpi-devel
Summary:        A collection of libraries of numerical algorithms - openmpi version - development headers
Group:          Development/Libraries/C and C++

%description openmpi-devel
Zoltan Toolkit for Load-balancing, Partitioning, Ordering and Coloring compiled against openmpi - development headers
%endif

%if 0%{?_build_mpich}
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
scl enable %{_toolset} '../configure --prefix /usr --disable-mpi --with-cflags="$RPM_OPT_FLAGS -fPIC -g" --libdir /usr/lib64'
scl enable %{_toolset} 'make %{?_smp_mflags} everything'
popd

%if 0%{?_build_openmpi}
mkdir openmpi
pushd openmpi
module load mpi/openmpi-x86_64
scl enable %{_toolset} '../configure --prefix /usr/lib64/openmpi --with-cflags="$RPM_OPT_FLAGS -fPIC -g" --includedir /usr/include/openmpi-x86_64'
scl enable %{_toolset} 'make %{?_smp_mflags} everything'
module unload mpi/openmpi-x86_64
popd
%endif

%if 0%{?_build_mpich}
mkdir mpich
pushd mpich
module load mpi/mpich-x86_64
scl enable %{_toolset} '../configure --prefix /usr/lib64/mpich --with-cflags="$RPM_OPT_FLAGS -fPIC -g" --includedir /usr/include/mpich-x86_64'
scl enable %{_toolset} 'make %{?_smp_mflags} everything'
module unload mpi/mpich-x86_64
popd
%endif

%install
scl enable %{_toolset} 'make DESTDIR=%{buildroot} install -C serial'
rm -f %{buildroot}/usr/bin/mpirun

%if 0%{?_build_openmpi}
scl enable %{_toolset} 'make DESTDIR=%{buildroot} install -C openmpi'
%endif

%if 0%{?_build_mpich}
scl enable %{_toolset} 'make DESTDIR=%{buildroot} install -C mpich'
%endif

%files devel
%defattr(-, root, root, -)
%{_includedir}/*
%{_libdir}/*
%if 0%{?_build_openmpi}
%exclude /usr/include/openmpi-x86_64
%endif
%if 0%{?_build_mpich}
%exclude /usr/include/mpich-x86_64
%endif

%if 0%{?_build_openmpi}
%files openmpi-devel
%defattr(-, root, root, -)
%{_includedir}/openmpi-x86_64/*
%{_libdir}/openmpi/lib/*
%endif

%if 0%{?_build_mpich}
%files mpich-devel
%defattr(-, root, root, -)
%{_includedir}/mpich-x86_64/*
%{_libdir}/mpich/lib/*
%endif
