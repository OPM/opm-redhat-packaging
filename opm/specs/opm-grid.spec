#
# spec file for package opm-grid
#

%define tag final
%define rtype release
%define build_openmpi 1
%define build_mpich 1

%if 0%{?rhel} == 7
%define toolset devtoolset-9
%define build_openmpi3 1
%else
%define toolset gcc-toolset-12
%define build_openmpi3 0
%endif

Name:          opm-grid
Version:       2023.10
Release:       0
Summary:       Cornerpoint grid management module for OPM
License:       GPL-3.0
Group:         Development/Libraries/C and C++
Url:           http://www.opm-project.org/
Source0:       https://github.com/OPM/%{name}/archive/release/%{version}/%{tag}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:        0001-opm-grid-fixed-explicitly-check-against-double-precision-0.0.patch
BuildRequires: blas-devel lapack-devel dune-common-devel
BuildRequires: git suitesparse-devel doxygen bc
BuildRequires: tinyxml-devel zlib-devel
BuildRequires: opm-common-devel
BuildRequires: dune-istl-devel
BuildRequires: dune-geometry-devel
BuildRequires: dune-grid-devel
BuildRequires: dune-uggrid-devel
BuildRequires: cmake3 tbb-devel
BuildRequires: %{toolset}
BuildRequires: boost-devel python3-devel

%if %{build_openmpi}
BuildRequires: openmpi-devel
BuildRequires: zoltan-openmpi-devel
BuildRequires: dune-uggrid-openmpi-devel
BuildRequires: dune-grid-openmpi-devel
BuildRequires: dune-geometry-openmpi-devel
BuildRequires: dune-istl-openmpi-devel
%endif

%if %{build_openmpi3}
BuildRequires: openmpi3-devel
BuildRequires: zoltan-openmpi3-devel
BuildRequires: dune-uggrid-openmpi3-devel
BuildRequires: dune-grid-openmpi3-devel
BuildRequires: dune-geometry-openmpi3-devel
BuildRequires: dune-istl-openmpi3-devel
%endif

%if %{build_mpich}
BuildRequires: mpich-devel
BuildRequires: zoltan-mpich-devel
BuildRequires: dune-uggrid-mpich-devel
BuildRequires: dune-grid-mpich-devel
BuildRequires: dune-geometry-mpich-devel
BuildRequires: dune-istl-mpich-devel
%endif

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This module enables working with corner-point or, more
generally, pillar grids.  A standard grid type in the petroleum
industry, corner-point grids fill space with a relatively low number
of cells while still providing sufficient flexibility to model faults,
fractures and erosion.  The grid format was originally designed with
an eye towards geological modelling rather than numerical simulation
and this design choice does limit the number of feasible numerical
methods.

%package -n libopm-grid
Summary:        Cornerpoint grid management module for OPM
Group:          System/Libraries
Requires:       libdune-common
Requires:       libdune-grid
Requires:       libdune-uggrid
Requires:       libdune-geometry

%description -n libopm-grid
This module enables working with corner-point or, more
generally, pillar grids.  A standard grid type in the petroleum
industry, corner-point grids fill space with a relatively low number
of cells while still providing sufficient flexibility to model faults,
fractures and erosion.  The grid format was originally designed with
an eye towards geological modelling rather than numerical simulation
and this design choice does limit the number of feasible numerical
methods.

%package -n libopm-grid%{version}
Summary:        Cornerpoint grid management module for OPM
Group:          System/Libraries
Requires:       libdune-common
Requires:       libdune-grid
Requires:       libdune-uggrid
Requires:       libdune-geometry

%description -n libopm-grid%{version}
This module enables working with corner-point or, more
generally, pillar grids.  A standard grid type in the petroleum
industry, corner-point grids fill space with a relatively low number
of cells while still providing sufficient flexibility to model faults,
fractures and erosion.  The grid format was originally designed with
an eye towards geological modelling rather than numerical simulation
and this design choice does limit the number of feasible numerical
methods.

%package devel
Summary:        Development and header files for opm-grid
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       blas-devel
Requires:       lapack-devel
Requires:       suitesparse-devel
Requires:       libopm-grid = %{version}

%description devel
This package contains the development and header files for opm-grid

%package doc
Summary:        Documentation files for opm-grid
Group:          Documentation
BuildArch:	noarch

%description doc
This package contains the documentation files for opm-grid

%package bin
Summary:        Applications in opm-grid
Group:          Scientific
Requires:       libopm-grid = %{version}

%description bin
This package contains the applications for opm-grid

%if %{build_openmpi}
%package -n libopm-grid-openmpi
Summary:        Cornerpoint grid management module for OPM
Group:          System/Libraries
Requires:       libdune-common-openmpi
Requires:       libdune-grid-openmpi
Requires:       libdune-uggrid-openmpi
Requires:       libdune-geometry-openmpi

%description -n libopm-grid-openmpi
This module enables working with corner-point or, more
generally, pillar grids.  A standard grid type in the petroleum
industry, corner-point grids fill space with a relatively low number
of cells while still providing sufficient flexibility to model faults,
fractures and erosion.  The grid format was originally designed with
an eye towards geological modelling rather than numerical simulation
and this design choice does limit the number of feasible numerical
methods.

%package -n libopm-grid%{version}-openmpi
Summary:        Cornerpoint grid management module for OPM
Group:          System/Libraries
Requires:       libdune-common-openmpi
Requires:       libdune-grid-openmpi
Requires:       libdune-uggrid-openmpi
Requires:       libdune-geometry-openmpi

%description -n libopm-grid%{version}-openmpi
This module enables working with corner-point or, more
generally, pillar grids.  A standard grid type in the petroleum
industry, corner-point grids fill space with a relatively low number
of cells while still providing sufficient flexibility to model faults,
fractures and erosion.  The grid format was originally designed with
an eye towards geological modelling rather than numerical simulation
and this design choice does limit the number of feasible numerical
methods.

%package openmpi-devel
Summary:        Development and header files for opm-grid
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       blas-devel
Requires:       lapack-devel
Requires:       suitesparse-devel
Requires:       libopm-grid-openmpi = %{version}

%description openmpi-devel
This package contains the development and header files for opm-grid

%package openmpi-bin
Summary:        Applications in opm-grid
Group:          Scientific
Requires:       libopm-grid-openmpi = %{version}

%description openmpi-bin
This package contains the applications for opm-grid
%endif

%if %{build_openmpi3}
%package -n libopm-grid-openmpi3
Summary:        Cornerpoint grid management module for OPM
Group:          System/Libraries
Requires:       libdune-common-openmpi3
Requires:       libdune-grid-openmpi3
Requires:       libdune-uggrid-openmpi3
Requires:       libdune-geometry-openmpi3

%description -n libopm-grid-openmpi3
This module enables working with corner-point or, more
generally, pillar grids.  A standard grid type in the petroleum
industry, corner-point grids fill space with a relatively low number
of cells while still providing sufficient flexibility to model faults,
fractures and erosion.  The grid format was originally designed with
an eye towards geological modelling rather than numerical simulation
and this design choice does limit the number of feasible numerical
methods.

%package -n libopm-grid%{version}-openmpi3
Summary:        Cornerpoint grid management module for OPM
Group:          System/Libraries
Requires:       libdune-common-openmpi3
Requires:       libdune-grid-openmpi3
Requires:       libdune-uggrid-openmpi3
Requires:       libdune-geometry-openmpi3

%description -n libopm-grid%{version}-openmpi3
This module enables working with corner-point or, more
generally, pillar grids.  A standard grid type in the petroleum
industry, corner-point grids fill space with a relatively low number
of cells while still providing sufficient flexibility to model faults,
fractures and erosion.  The grid format was originally designed with
an eye towards geological modelling rather than numerical simulation
and this design choice does limit the number of feasible numerical
methods.

%package openmpi3-devel
Summary:        Development and header files for opm-grid
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       blas-devel
Requires:       lapack-devel
Requires:       suitesparse-devel
Requires:       libopm-grid-openmpi3 = %{version}

%description openmpi3-devel
This package contains the development and header files for opm-grid

%package openmpi3-bin
Summary:        Applications in opm-grid
Group:          Scientific
Requires:       libopm-grid-openmpi3 = %{version}

%description openmpi3-bin
This package contains the applications for opm-grid
%endif

%if %{build_mpich}
%package -n libopm-grid-mpich
Summary:        Cornerpoint grid management module for OPM
Group:          System/Libraries
Requires:       libdune-common-mpich
Requires:       libdune-grid-mpich
Requires:       libdune-uggrid-mpich
Requires:       libdune-geometry-mpich

%description -n libopm-grid-mpich
This module enables working with corner-point or, more
generally, pillar grids.  A standard grid type in the petroleum
industry, corner-point grids fill space with a relatively low number
of cells while still providing sufficient flexibility to model faults,
fractures and erosion.  The grid format was originally designed with
an eye towards geological modelling rather than numerical simulation
and this design choice does limit the number of feasible numerical
methods.
%package -n libopm-grid%{version}-mpich
Summary:        Cornerpoint grid management module for OPM
Group:          System/Libraries
Requires:       libdune-common-mpich
Requires:       libdune-grid-mpich
Requires:       libdune-uggrid-mpich
Requires:       libdune-geometry-mpich

%description -n libopm-grid%{version}-mpich
This module enables working with corner-point or, more
generally, pillar grids.  A standard grid type in the petroleum
industry, corner-point grids fill space with a relatively low number
of cells while still providing sufficient flexibility to model faults,
fractures and erosion.  The grid format was originally designed with
an eye towards geological modelling rather than numerical simulation
and this design choice does limit the number of feasible numerical
methods.

%package mpich-devel
Summary:        Development and header files for opm-grid
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       blas-devel
Requires:       lapack-devel
Requires:       suitesparse-devel
Requires:       libopm-grid-mpich = %{version}

%description mpich-devel
This package contains the development and header files for opm-grid

%package mpich-bin
Summary:        Applications in opm-grid
Group:          Scientific
Requires:       libopm-grid-mpich = %{version}

%description mpich-bin
This package contains the applications for opm-grid
%endif

%prep
%setup -q -n %{name}-%{rtype}-%{version}-%{tag}

%patch0 -p1

# consider using -DUSE_VERSIONED_DIR=ON if backporting
%build
mkdir serial
pushd serial
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 -DUSE_MPI=0 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_DOCDIR=share/doc/%{name}-%{version} -DUSE_RUNPATH=OFF -DWITH_NATIVE=OFF ..'
scl enable %{toolset} 'make %{?_smp_mflags}'
scl enable %{toolset} 'make test'
popd

%if %{build_openmpi}
mkdir openmpi
pushd openmpi
module load mpi/openmpi-x86_64
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 -DUSE_MPI=1 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/openmpi -DCMAKE_INSTALL_LIBDIR=lib -DUSE_RUNPATH=OFF -DWITH_NATIVE=OFF -DZOLTAN_INCLUDE_DIR=/usr/include/openmpi-x86_64/zoltan ..'
scl enable %{toolset} 'make %{?_smp_mflags}'
scl enable %{toolset} 'make test'
module unload mpi/openmpi-x86_64
popd
%endif

%if %{build_openmpi3}
mkdir openmpi3
pushd openmpi3
module load mpi/openmpi3-x86_64
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 -DUSE_MPI=1 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/openmpi3 -DCMAKE_INSTALL_LIBDIR=lib -DUSE_RUNPATH=OFF -DWITH_NATIVE=OFF -DZOLTAN_INCLUDE_DIR=/usr/include/openmpi3-x86_64/zoltan ..'
scl enable %{toolset} 'make %{?_smp_mflags}'
scl enable %{toolset} 'make test'
module unload mpi/openmpi3-x86_64
popd
%endif

%if %{build_mpich}
mkdir mpich
pushd mpich
module load mpi/mpich-x86_64
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3  -DUSE_MPI=1 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/mpich -DCMAKE_INSTALL_LIBDIR=lib -DUSE_RUNPATH=OFF -DWITH_NATIVE=OFF -DZOLTAN_INCLUDE_DIR=/usr/include/mpich-x86_64/zoltan ..'
scl enable %{toolset} 'make %{?_smp_mflags}'
scl enable %{toolset} 'make test'
module unload mpi/mpich-x86_64
popd
%endif

%install
scl enable %{toolset} 'make install DESTDIR=${RPM_BUILD_ROOT} -C serial'
scl enable %{toolset} 'make install-html DESTDIR=${RPM_BUILD_ROOT} -C serial'

%if %{build_openmpi}
scl enable %{toolset} 'make install DESTDIR=${RPM_BUILD_ROOT} -C openmpi'
mv ${RPM_BUILD_ROOT}/usr/lib64/openmpi/include/* ${RPM_BUILD_ROOT}/usr/include/openmpi-x86_64/
%endif

%if %{build_openmpi3}
scl enable %{toolset} 'make install DESTDIR=${RPM_BUILD_ROOT} -C openmpi3'
mv ${RPM_BUILD_ROOT}/usr/lib64/openmpi3/include/* ${RPM_BUILD_ROOT}/usr/include/openmpi3-x86_64/
%endif

%if %{build_mpich}
scl enable %{toolset} 'make install DESTDIR=${RPM_BUILD_ROOT} -C mpich'
mv ${RPM_BUILD_ROOT}/usr/lib64/mpich/include/* ${RPM_BUILD_ROOT}/usr/include/mpich-x86_64/
%endif

%clean
rm -rf %{buildroot}

%post -n libopm-grid -p /sbin/ldconfig
%postun -n libopm-grid -p /sbin/ldconfig
%post -n libopm-grid%{version} -p /sbin/ldconfig
%postun -n libopm-grid%{version} -p /sbin/ldconfig

%if %{build_openmpi}
%post -n libopm-grid-openmpi -p /sbin/ldconfig
%postun -n libopm-grid-openmpi -p /sbin/ldconfig
%post -n libopm-grid%{version}-openmpi -p /sbin/ldconfig
%postun -n libopm-grid%{version}-openmpi -p /sbin/ldconfig
%endif

%if %{build_openmpi3}
%post -n libopm-grid-openmpi3 -p /sbin/ldconfig
%postun -n libopm-grid-openmpi3 -p /sbin/ldconfig
%post -n libopm-grid%{version}-openmpi3 -p /sbin/ldconfig
%postun -n libopm-grid%{version}-openmpi3 -p /sbin/ldconfig
%endif

%if %{build_mpich}
%post -n libopm-grid-mpich -p /sbin/ldconfig
%postun -n libopm-grid-mpich -p /sbin/ldconfig
%post -n libopm-grid%{version}-mpich -p /sbin/ldconfig
%postun -n libopm-grid%{version}-mpich -p /sbin/ldconfig
%endif

%files
%doc COPYING README.md

%files doc
%{_docdir}/*

%files -n libopm-grid
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files -n libopm-grid%{version}
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
/usr/lib/dunecontrol/*
%{_includedir}/*
%{_datadir}/cmake/*
%{_datadir}/opm/cmake/Modules/*
%if %{build_openmpi}
%exclude /usr/include/openmpi-x86_64
%endif
%if %{build_openmpi3}
%exclude /usr/include/openmpi3-x86_64
%endif
%if %{build_mpich}
%exclude /usr/include/mpich-x86_64
%endif

%files bin
%{_bindir}/*
%{_datadir}/man/*

%if %{build_openmpi}
%files -n libopm-grid-openmpi
%defattr(-,root,root,-)
%{_libdir}/openmpi/lib/*.so.*

%files -n libopm-grid%{version}-openmpi
%defattr(-,root,root,-)
%{_libdir}/openmpi/lib/*.so.*

%files openmpi-devel
%defattr(-,root,root,-)
%{_libdir}/openmpi/lib/*.so
%{_libdir}/openmpi/lib/dunecontrol/*
%{_includedir}/openmpi-x86_64/*
%{_libdir}/openmpi/share/cmake/*
%{_libdir}/openmpi/share/opm/cmake/Modules/*

%files openmpi-bin
%{_libdir}/openmpi/bin/*
%{_libdir}/openmpi/share/man/*
%endif

%if %{build_openmpi3}
%files -n libopm-grid-openmpi3
%defattr(-,root,root,-)
%{_libdir}/openmpi3/lib/*.so.*

%files -n libopm-grid%{version}-openmpi3
%defattr(-,root,root,-)
%{_libdir}/openmpi3/lib/*.so.*

%files openmpi3-devel
%defattr(-,root,root,-)
%{_libdir}/openmpi3/lib/*.so
%{_libdir}/openmpi3/lib/dunecontrol/*
%{_includedir}/openmpi3-x86_64/*
%{_libdir}/openmpi3/share/cmake/*
%{_libdir}/openmpi3/share/opm/cmake/Modules/*

%files openmpi3-bin
%{_libdir}/openmpi3/bin/*
%{_libdir}/openmpi3/share/man/*
%endif

%if %{build_mpich}
%files -n libopm-grid-mpich
%defattr(-,root,root,-)
%{_libdir}/mpich/lib/*.so.*

%files -n libopm-grid%{version}-mpich
%defattr(-,root,root,-)
%{_libdir}/mpich/lib/*.so.*

%files mpich-devel
%defattr(-,root,root,-)
%{_libdir}/mpich/lib/*.so
%{_libdir}/mpich/lib/dunecontrol/*
%{_includedir}/mpich-x86_64/*
%{_libdir}/mpich/share/cmake/*
%{_libdir}/mpich/share/opm/cmake/Modules/*

%files mpich-bin
%{_libdir}/mpich/bin/*
%{_libdir}/mpich/share/man/*
%endif
