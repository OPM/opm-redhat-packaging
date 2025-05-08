#
# spec file for package opm-upscaling
#

%define tag final
%define rtype release

%if 0%{?_build_versioned} == 1
%define postfix %{version}
%endif

Name:          opm-upscaling
Version:       2025.04
Release:       0
Summary:       Open Porous Media - upscaling library
License:       GPL-3.0
Group:         Development/Libraries/C and C++
Url:           http://www.opm-project.org/
Source0:       https://github.com/OPM/opm-upscaling/archive/release/%{version}/%{tag}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: blas-devel lapack-devel
BuildRequires: git suitesparse-devel doxygen bc tinyxml-devel
BuildRequires: cmake3 zlib-devel graphviz
BuildRequires: %{_toolset}
BuildRequires: boost-devel python3-devel tbb-devel
BuildRequires: dune-common-devel
BuildRequires: dune-geometry-devel
BuildRequires: dune-istl-devel
BuildRequires: dune-uggrid-devel
BuildRequires: dune-grid-devel
BuildRequires: opm-common-devel
BuildRequires: opm-grid-devel

%if 0%{?_build_openmpi}
BuildRequires: openmpi-devel
BuildRequires: opm-grid-openmpi-devel
BuildRequires: zoltan-openmpi-devel
BuildRequires: dune-common-openmpi-devel
BuildRequires: dune-grid-openmpi-devel
BuildRequires: dune-geometry-openmpi-devel
BuildRequires: dune-istl-openmpi-devel
BuildRequires: dune-uggrid-openmpi-devel
%endif

%if 0%{?_build_mpich}
BuildRequires: mpich-devel
BuildRequires: opm-grid-mpich-devel
BuildRequires: zoltan-mpich-devel
BuildRequires: dune-common-mpich-devel
BuildRequires: dune-grid-mpich-devel
BuildRequires: dune-geometry-mpich-devel
BuildRequires: dune-istl-mpich-devel
BuildRequires: dune-uggrid-mpich-devel
%endif

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This module provides semi-implicit pressure and transport solvers using the IMPES method.

%package -n libopm-upscaling
Summary:        Open Porous Media - upscaling library
Group:          System/Libraries
Requires:       libopm-grid%{?postfix} = %{version}

%description -n libopm-upscaling
This module implements single-phase and steady-state upscaling methods.

%package devel
Summary:        Development and header files for opm-upscaling
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       blas-devel
Requires:       lapack-devel
Requires:       suitesparse-devel
Requires:       libopm-upscaling = %{version}

%description devel
This package contains the development and header files for opm-upscaling

%package doc
Summary:        Documentation files for opm-upscaling
Group:          Documentation
BuildArch:	    noarch

%description doc
This package contains the documentation files for opm-upscaling

%package bin
Summary:        Applications in opm-upscaling
Group:          Scientific
Requires:       libopm-upscaling = %{version}

%description bin
This package contains the applications for opm-upscaling

%if 0%{?_build_openmpi}
%package -n libopm-upscaling-openmpi
Summary:        Open Porous Media - upscaling library
Group:          System/Libraries
Requires:       libopm-grid%{?postfix}-openmpi = %{version}

%description -n libopm-upscaling-openmpi
This module implements single-phase and steady-state upscaling methods.

%package openmpi-devel
Summary:        Development and header files for opm-upscaling
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       blas-devel
Requires:       lapack-devel
Requires:       suitesparse-devel
Requires:       libopm-upscaling-openmpi = %{version}

%description openmpi-devel
This package contains the development and header files for opm-upscaling

%package openmpi-bin
Summary:        Applications in opm-upscaling
Group:          Scientific
Requires:       %{name} = %{version}
Requires:       libopm-upscaling-openmpi = %{version}

%description openmpi-bin
This package contains the applications for opm-upscaling
%endif

%if 0%{?_build_mpich}
%package -n libopm-upscaling-mpich
Summary:        Open Porous Media - upscaling library
Group:          System/Libraries
Requires:       libopm-grid%{?postfix}-mpich = %{version}

%description -n libopm-upscaling-mpich
This module implements single-phase and steady-state upscaling methods.

%package mpich-devel
Summary:        Development and header files for opm-upscaling
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       blas-devel
Requires:       lapack-devel
Requires:       suitesparse-devel
Requires:       libopm-upscaling-mpich = %{version}

%description mpich-devel
This package contains the development and header files for opm-upscaling

%package mpich-bin
Summary:        Applications in opm-upscaling
Group:          Scientific
Requires:       libopm-upscaling-mpich = %{version}

%description mpich-bin
This package contains the applications for opm-upscaling
%endif

%prep
%setup -q -n %{name}-%{rtype}-%{version}-%{tag}

# consider using -DUSE_VERSIONED_DIR=ON if backporting
%build
mkdir serial
pushd serial
scl enable %{_toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 -DUSE_MPI=0 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_DOCDIR=share/doc/%{name}-%{version} -DUSE_RUNPATH=OFF -DINSTALL_BENCHMARKS=1 -DWITH_NATIVE=OFF ..'
scl enable %{_toolset} 'make %{?_smp_mflags}'
scl enable %{_toolset} 'ctest3 --output-on-failure'
popd

%if 0%{?_build_openmpi}
mkdir openmpi
pushd openmpi
module load mpi/openmpi-x86_64
scl enable %{_toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 -DUSE_MPI=1 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/openmpi -DCMAKE_INSTALL_LIBDIR=lib -DUSE_RUNPATH=OFF -DINSTALL_BENCHMARKS=1 -DWITH_NATIVE=OFF -DZOLTAN_INCLUDE_DIR=/usr/include/openmpi-x86_64/zoltan ..'
scl enable %{_toolset} 'make %{?_smp_mflags}'
scl enable %{_toolset} 'ctest3 --output-on-failure'
module unload mpi/openmpi-x86_64
popd
%endif

%if 0%{?_build_mpich}
mkdir mpich
pushd mpich
module load mpi/mpich-x86_64
scl enable %{_toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 -DUSE_MPI=1 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/mpich -DCMAKE_INSTALL_LIBDIR=lib -DUSE_RUNPATH=OFF -DINSTALL_BENCHMARKS=1 -DWITH_NATIVE=OFF -DZOLTAN_INCLUDE_DIR=/usr/include/mpich-x86_64/zoltan ..'
scl enable %{_toolset} 'make %{?_smp_mflags}'
scl enable %{_toolset} 'ctest3 --output-on-failure'
module unload mpi/mpich-x86_64
popd
%endif

%install
scl enable %{_toolset} 'make install DESTDIR=${RPM_BUILD_ROOT} -C serial'
scl enable %{_toolset} 'make install-html DESTDIR=${RPM_BUILD_ROOT} -C serial'

%if 0%{?_build_openmpi}
scl enable %{_toolset} 'make install DESTDIR=${RPM_BUILD_ROOT} -C openmpi'
mv ${RPM_BUILD_ROOT}/usr/lib64/openmpi/include/* ${RPM_BUILD_ROOT}/usr/include/openmpi-x86_64/
%endif

%if 0%{?_build_mpich}
scl enable %{_toolset} 'make install DESTDIR=${RPM_BUILD_ROOT} -C mpich'
mv ${RPM_BUILD_ROOT}/usr/lib64/mpich/include/* ${RPM_BUILD_ROOT}/usr/include/mpich-x86_64/
%endif

%clean
rm -rf %{buildroot}

%post -n libopm-upscaling -p /sbin/ldconfig
%postun -n libopm-upscaling -p /sbin/ldconfig

%if 0%{?_build_openmpi}
%post -n libopm-upscaling-openmpi -p /sbin/ldconfig
%postun -n libopm-upscaling-openmpi -p /sbin/ldconfig
%endif

%if 0%{?_build_mpich}
%post -n libopm-upscaling-mpich -p /sbin/ldconfig
%postun -n libopm-upscaling-mpich -p /sbin/ldconfig
%endif

%files
%doc README COPYING

%files doc
%{_docdir}/*

%files -n libopm-upscaling
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
%files -n libopm-upscaling-openmpi
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
%files -n libopm-upscaling-mpich
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
