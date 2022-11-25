#
# spec file for package dune-grid
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


Name:           dune-grid
Version:        2.8.0
Release:        0
Summary:        Grid management module for DUNE
License:        GPL-2.0
Group:          Development/Libraries/C and C++
Url:            http://www.dune-project.org/
Source0:        https://dune-project.org/download/2.8.0/dune-grid-2.8.0.tar.gz
BuildRequires:  dune-common-devel dune-common-openmpi-devel
BuildRequires:  dune-common-openmpi3-devel dune-common-mpich-devel
BuildRequires:  dune-geometry-devel dune-geometry-openmpi-devel
BuildRequires:  dune-geometry-openmpi3-devel dune-geometry-mpich-devel
BuildRequires:  dune-uggrid-devel dune-uggrid-openmpi-devel
BuildRequires:  dune-uggrid-openmpi3-devel dune-uggrid-mpich-devel
BuildRequires:  mesa-libGL-devel metis-devel
BuildRequires:  pkgconfig devtoolset-9-toolchain
BuildRequires:  cmake3 boost-devel
BuildRequires:  openmpi-devel mpich-devel openmpi3-devel
BuildRequires:  doxygen inkscape graphviz
BuildRequires:  tbb-devel python3-sphinx latexmk
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       libdune-grid = %{version}

%description
dune-grid defines nonconforming, hierarchically nested, multi-element-type,
parallel grids in arbitrary space dimensions. Graphical output with several
packages is available, e.g. file output to IBM data explorer and VTK (parallel
XML format for unstructured grids). The graphics package Grape has been integrated
in interactive mode. This module also provides some grid implementations and
further grid managers can be added through seprate modules.

%package -n libdune-grid
Summary:        Grid management module for DUNE
Group:          System/Libraries

%description -n libdune-grid
dune-grid defines nonconforming, hierarchically nested, multi-element-type,
parallel grids in arbitrary space dimensions. Graphical output with several
packages is available, e.g. file output to IBM data explorer and VTK (parallel
XML format for unstructured grids). The graphics package Grape has been integrated
in interactive mode. This module also provides some grid implementations and
further grid managers can be added through separate modules.

%package devel
Summary:        Development and header files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libdune-grid = %{version}

%description devel
This package contains the development and header files for %{name}.

%package doc
Summary:        Doxygen documentation for %{name}
Group:          Documentation
BuildArch:      noarch

%description doc
This package contains the doxygen documentation for %{name}.

%package -n libdune-grid-openmpi
Summary:        Grid management module for DUNE - openmpi version
Group:          System/Libraries

%description -n libdune-grid-openmpi
dune-grid defines nonconforming, hierarchically nested, multi-element-type,
parallel grids in arbitrary space dimensions. Graphical output with several
packages is available, e.g. file output to IBM data explorer and VTK (parallel
XML format for unstructured grids). The graphics package Grape has been integrated
in interactive mode. This module also provides some grid implementations and
further grid managers can be added through separate modules. OpenMPI version.

%package openmpi-devel
Summary:        Development and header files for %{name} - openmpi version
Group:          Development/Libraries/C and C++
Requires:       libdune-grid-openmpi = %{version}

%description openmpi-devel
This package contains the development and header files for %{name} - openmpi version.

%package -n libdune-grid-openmpi3
Summary:        Grid management module for DUNE - openmpi3 version
Group:          System/Libraries

%description -n libdune-grid-openmpi3
dune-grid defines nonconforming, hierarchically nested, multi-element-type,
parallel grids in arbitrary space dimensions. Graphical output with several
packages is available, e.g. file output to IBM data explorer and VTK (parallel
XML format for unstructured grids). The graphics package Grape has been integrated
in interactive mode. This module also provides some grid implementations and
further grid managers can be added through separate modules. OpenMPI3 version.

%package openmpi3-devel
Summary:        Development and header files for %{name} - openmpi3 version
Group:          Development/Libraries/C and C++
Requires:       libdune-grid-openmpi3 = %{version}

%description openmpi3-devel
This package contains the development and header files for %{name} - openmpi3 version.

%package -n libdune-grid-mpich
Summary:        Grid management module for DUNE - mpich version
Group:          System/Libraries

%description -n libdune-grid-mpich
dune-grid defines nonconforming, hierarchically nested, multi-element-type,
parallel grids in arbitrary space dimensions. Graphical output with several
packages is available, e.g. file output to IBM data explorer and VTK (parallel
XML format for unstructured grids). The graphics package Grape has been integrated
in interactive mode. This module also provides some grid implementations and
further grid managers can be added through separate modules. MPICH version.

%package mpich-devel
Summary:        Development and header files for %{name} - mpich version
Group:          Development/Libraries/C and C++
Requires:       libdune-grid-mpich = %{version}

%description mpich-devel
This package contains the development and header files for %{name} - mpich version.

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

%post -n libdune-grid -p /sbin/ldconfig
%postun -n libdune-grid -p /sbin/ldconfig
%post -n libdune-grid-openmpi -p /sbin/ldconfig
%postun -n libdune-grid-openmpi -p /sbin/ldconfig
%post -n libdune-grid-openmpi3 -p /sbin/ldconfig
%postun -n libdune-grid-openmpi3 -p /sbin/ldconfig
%post -n libdune-grid-mpich -p /sbin/ldconfig
%postun -n libdune-grid-mpich -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING README.md
%{_datadir}/doc/dune-grid

%files -n libdune-grid
%defattr(-,root,root,-)
%{_libdir}/*.so

%files devel
%defattr(-,root,root,-)
%{_includedir}/dune/*
%{_libdir}/cmake/*
%{_datadir}/%{name}
%{_datadir}/dune
%{_libdir}/pkgconfig/*.pc
%{_prefix}/lib/dune*
%exclude /usr/include/openmpi-x86_64
%exclude /usr/include/openmpi3-x86_64
%exclude /usr/include/mpich-x86_64

%files doc
%{_datadir}/doc/*

%files -n libdune-grid-openmpi
%defattr(-,root,root,-)
%{_libdir}/openmpi/lib/*.so

%files openmpi-devel
%defattr(-,root,root,-)
%{_includedir}/openmpi-x86_64/dune/*
%{_libdir}/openmpi/lib/dune*
%{_libdir}/openmpi/lib/pkgconfig/*.pc
%{_libdir}/openmpi/lib/cmake
%{_libdir}/openmpi/share/*

%files -n libdune-grid-openmpi3
%defattr(-,root,root,-)
%{_libdir}/openmpi3/lib/*.so

%files openmpi3-devel
%defattr(-,root,root,-)
%{_includedir}/openmpi3-x86_64/dune/*
%{_libdir}/openmpi3/lib/dune*
%{_libdir}/openmpi3/lib/pkgconfig/*.pc
%{_libdir}/openmpi3/lib/cmake
%{_libdir}/openmpi3/share/*

%files -n libdune-grid-mpich
%defattr(-,root,root,-)
%{_libdir}/mpich/lib/*.so

%files mpich-devel
%defattr(-,root,root,-)
%{_includedir}/mpich-x86_64/dune/*
%{_libdir}/mpich/lib/dune*
%{_libdir}/mpich/lib/pkgconfig/*.pc
%{_libdir}/mpich/lib/cmake
%{_libdir}/mpich/share/*
