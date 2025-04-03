#
# spec file for package opm-grid
#

%define tag final
%define rtype release

%define toolset gcc-toolset-12

%if 0%{?_build_versioned} == 1
%define postfix %{version}
%endif

Name:          opm-grid
Version:       2024.10
Release:       0
Summary:       Cornerpoint grid management module for OPM
License:       GPL-3.0
Group:         Development/Libraries/C and C++
Url:           http://www.opm-project.org/
Source0:       https://github.com/OPM/%{name}/archive/release/%{version}/%{tag}.tar.gz#/%{name}-%{version}.tar.gz
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

%if 0%{?_build_openmpi}
BuildRequires: openmpi-devel
BuildRequires: zoltan-openmpi-devel
BuildRequires: dune-uggrid-openmpi-devel
BuildRequires: dune-grid-openmpi-devel
BuildRequires: dune-geometry-openmpi-devel
BuildRequires: dune-istl-openmpi-devel
%endif

%if 0%{?_build_mpich}
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

%package -n libopm-grid%{?postfix}
Summary:        Cornerpoint grid management module for OPM
Group:          System/Libraries
Requires:       libdune-common
Requires:       libdune-grid
Requires:       libdune-uggrid
Requires:       libdune-geometry

%description -n libopm-grid%{?postfix}
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
Requires:       libopm-grid%{?postfix} = %{version}

%description devel
This package contains the development and header files for opm-grid

%package doc
Summary:        Documentation files for opm-grid
Group:          Documentation
BuildArch:	    noarch

%description doc
This package contains the documentation files for opm-grid

%package bin
Summary:        Applications in opm-grid
Group:          Scientific
Requires:       libopm-grid%{?postfix} = %{version}

%description bin
This package contains the applications for opm-grid

%if 0%{?_build_openmpi}
%package -n libopm-grid%{?postfix}-openmpi
Summary:        Cornerpoint grid management module for OPM
Group:          System/Libraries
Requires:       libdune-common-openmpi
Requires:       libdune-grid-openmpi
Requires:       libdune-uggrid-openmpi
Requires:       libdune-geometry-openmpi

%description -n libopm-grid%{?postfix}-openmpi
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
Requires:       libopm-grid%{?postfix}-openmpi = %{version}

%description openmpi-devel
This package contains the development and header files for opm-grid

%package openmpi-bin
Summary:        Applications in opm-grid
Group:          Scientific
Requires:       libopm-grid%{?postfix}-openmpi = %{version}

%description openmpi-bin
This package contains the applications for opm-grid
%endif

%if 0%{?_build_mpich}
%package -n libopm-grid%{?postfix}-mpich
Summary:        Cornerpoint grid management module for OPM
Group:          System/Libraries
Requires:       libdune-common-mpich
Requires:       libdune-grid-mpich
Requires:       libdune-uggrid-mpich
Requires:       libdune-geometry-mpich

%description -n libopm-grid%{?postfix}-mpich
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
Requires:       libopm-grid%{?postfix}-mpich = %{version}

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

# consider using -DUSE_VERSIONED_DIR=ON if backporting
%build
mkdir serial
pushd serial
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 -DUSE_MPI=0 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_DOCDIR=share/doc/%{name}-%{version} -DUSE_RUNPATH=OFF -DWITH_NATIVE=OFF ..'
scl enable %{toolset} 'make %{?_smp_mflags}'
scl enable %{toolset} 'ctest3 --output-on-failure'
popd

%if 0%{?_build_openmpi}
mkdir openmpi
pushd openmpi
module load mpi/openmpi-x86_64
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 -DUSE_MPI=1 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/openmpi -DCMAKE_INSTALL_LIBDIR=lib -DUSE_RUNPATH=OFF -DWITH_NATIVE=OFF -DZOLTAN_INCLUDE_DIR=/usr/include/openmpi-x86_64/zoltan ..'
scl enable %{toolset} 'make %{?_smp_mflags}'
scl enable %{toolset} 'ctest3 --output-on-failure'
module unload mpi/openmpi-x86_64
popd
%endif

%if 0%{?_build_mpich}
mkdir mpich
pushd mpich
module load mpi/mpich-x86_64
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3  -DUSE_MPI=1 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/mpich -DCMAKE_INSTALL_LIBDIR=lib -DUSE_RUNPATH=OFF -DWITH_NATIVE=OFF -DZOLTAN_INCLUDE_DIR=/usr/include/mpich-x86_64/zoltan ..'
scl enable %{toolset} 'make %{?_smp_mflags}'
scl enable %{toolset} 'ctest3 --output-on-failure'
module unload mpi/mpich-x86_64
popd
%endif

%install
scl enable %{toolset} 'make install DESTDIR=${RPM_BUILD_ROOT} -C serial'
scl enable %{toolset} 'make install-html DESTDIR=${RPM_BUILD_ROOT} -C serial'

%if 0%{?_build_openmpi}
scl enable %{toolset} 'make install DESTDIR=${RPM_BUILD_ROOT} -C openmpi'
mv ${RPM_BUILD_ROOT}/usr/lib64/openmpi/include/* ${RPM_BUILD_ROOT}/usr/include/openmpi-x86_64/
%endif

%if 0%{?_build_mpich}
scl enable %{toolset} 'make install DESTDIR=${RPM_BUILD_ROOT} -C mpich'
mv ${RPM_BUILD_ROOT}/usr/lib64/mpich/include/* ${RPM_BUILD_ROOT}/usr/include/mpich-x86_64/
%endif

%clean
rm -rf %{buildroot}

%post -n libopm-grid%{?postfix} -p /sbin/ldconfig
%postun -n libopm-grid%{?postfix} -p /sbin/ldconfig

%if 0%{?_build_openmpi}
%post -n libopm-grid%{?postfix}-openmpi -p /sbin/ldconfig
%postun -n libopm-grid%{?postfix}-openmpi -p /sbin/ldconfig
%endif

%if 0%{?_build_mpich}
%post -n libopm-grid%{?postfix}-mpich -p /sbin/ldconfig
%postun -n libopm-grid%{?postfix}-mpich -p /sbin/ldconfig
%endif

%files
%doc COPYING README.md

%files doc
%{_docdir}/*

%files -n libopm-grid%{?postfix}
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
/usr/lib/dunecontrol/*
%{_includedir}/*
%{_datadir}/cmake/*
%{_datadir}/opm/cmake/Modules/*
%if 0%{?_build_openmpi}
%exclude /usr/include/openmpi-x86_64
%endif
%if 0%{?_build_mpich}
%exclude /usr/include/mpich-x86_64
%endif

%files bin
%{_bindir}/*
%{_datadir}/man/*

%if 0%{?_build_openmpi}
%files -n libopm-grid%{?postfix}-openmpi
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

%if 0%{?_build_mpich}
%files -n libopm-grid%{?postfix}-mpich
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
