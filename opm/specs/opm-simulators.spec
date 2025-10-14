#
# spec file for package opm-simulators
#

%define tag final
%define rtype release

Version:        2025.10

%if 0%{?_build_versioned} == 1
%define postfix %{version}
%endif

Name:           opm-simulators%{?postfix}
Release:        0
Summary:        Open Porous Media - core library
License:        GPL-3.0
Group:          Development/Libraries/C and C++
Url:            http://www.opm-project.org/
Source0:        https://github.com/OPM/opm-simulators/archive/release/%{version}/%{tag}.tar.gz#/opm-simulators-%{version}.tar.gz
Patch0:         0001-opm-simulators_skip_test_boost_return_code.patch
Patch1:         0002-opm-simulators_avoid_negative_rs_rv_max.patch
BuildRequires:  lapack-devel openblas-devel
BuildRequires:  git suitesparse-devel doxygen bc graphviz texlive-dvips-bin
BuildRequires:  tinyxml-devel zlib-devel fmt-devel
BuildRequires: zoltan-devel
BuildRequires: cmake3
BuildRequires: %{_toolset}
BuildRequires: boost-devel python3-devel tbb-devel
BuildRequires: hdf5-devel
BuildRequires: dune-common-devel
BuildRequires: dune-geometry-devel
BuildRequires: dune-uggrid-devel
BuildRequires: dune-grid-devel
BuildRequires: dune-localfunctions-devel
BuildRequires: dune-istl-devel
BuildRequires: opm-common-devel
BuildRequires: opm-grid-devel

%if 0%{?_build_openmpi}
BuildRequires: openmpi-devel
BuildRequires: zoltan-openmpi-devel
BuildRequires: hdf5-openmpi-devel
BuildRequires: dune-common-openmpi-devel
BuildRequires: dune-geometry-openmpi-devel
BuildRequires: dune-uggrid-openmpi-devel
BuildRequires: dune-grid-openmpi-devel
BuildRequires: dune-localfunctions-openmpi-devel
BuildRequires: dune-istl-openmpi-devel
BuildRequires: opm-grid-openmpi-devel
%endif

%if 0%{?_build_mpich}
BuildRequires: mpich-devel
BuildRequires: zoltan-mpich-devel
BuildRequires: hdf5-mpich-devel
BuildRequires: dune-common-mpich-devel
BuildRequires: dune-geometry-mpich-devel
BuildRequires: dune-uggrid-mpich-devel
BuildRequires: dune-grid-mpich-devel
BuildRequires: dune-localfunctions-mpich-devel
BuildRequires: dune-istl-mpich-devel
BuildRequires: opm-grid-mpich-devel
%endif

BuildRoot:      %{_tmppath}/opm-simulators-%{version}-build

%description
The Open Porous Media (OPM) initiative provides a set of open-source tools centered around the simulation of flow and transport of fluids in porous media. The goal of the initiative is to establish a sustainable environment for the development of an efficient and well-maintained software suite.

%package -n libopm-simulators%{?postfix}
Summary:        Open Porous Media - automatic differentiation library
Group:          System/Libraries
Requires:       libopm-grid%{?postfix} = %{version}

%description -n libopm-simulators%{?postfix}
The Open Porous Media (OPM) initiative provides a set of open-source tools centered around the simulation of flow and transport of fluids in porous media. The goal of the initiative is to establish a sustainable environment for the development of an efficient and well-maintained software suite.

%package devel
Summary:        Development and header files for opm-simulators
Group:          Development/Libraries/C and C++
Requires:       libopm-simulator%{?postfix} = %{version}

%description devel
This package contains the development and header files for opm-simulators

%package doc
Summary:        Documentation files for opm-simulators
Group:          Documentation
BuildArch:	    noarch

%description doc
This package contains the documentation files for opm-simulators

%package bin
Summary:        Applications in opm-simulators
Group:          Scientific
Requires:       libopm-simulators%{?postfix} = %{version}

%description bin
This package contains the applications for opm-simulators

%if 0%{?_build_versioned} == 1
%package -n opm-simulators-bin
Summary:        Applications in opm-simulators
Group:          Scientific
Requires:       opm-simulators%{postfix}-bin = %{version}
Requires:       opm-simulators2024.10-bin
Requires:       opm-simulators2025.04-bin

%description -n opm-simulators-bin
This package contains the applications for opm-simulators
%endif

%if 0%{?_build_openmpi}
%package -n libopm-simulators%{?postfix}-openmpi
Summary:        Open Porous Media - automatic differentiation library
Group:          System/Libraries
Requires:       libopm-grid%{?postfix}-openmpi = %{version}

%description -n libopm-simulators%{?postfix}-openmpi
The Open Porous Media (OPM) initiative provides a set of open-source tools centered around the simulation of flow and transport of fluids in porous media. The goal of the initiative is to establish a sustainable environment for the development of an efficient and well-maintained software suite.

%package openmpi-devel
Summary:        Development and header files for opm-simulators
Group:          Development/Libraries/C and C++
Requires:       libopm-simulators%{?postfix}-openmpi = %{version}

%description openmpi-devel
This package contains the development and header files for opm-simulators

%package openmpi-bin
Summary:        Applications in opm-simulators
Group:          Scientific
Requires:       libopm-simulators%{?postfix}-openmpi = %{version}

%description openmpi-bin
This package contains the applications for opm-simulators

%if 0%{?_build_versioned} == 1
%package -n opm-simulators-openmpi-bin
Summary:        Applications in opm-simulators
Group:          Scientific
Requires:       opm-simulators%{postfix}-openmpi-bin = %{version}
Requires:       opm-simulators2024.10-openmpi-bin
Requires:       opm-simulators2025.04-openmpi-bin

%description -n opm-simulators-openmpi-bin
This package contains the applications for opm-simulators
%endif

%endif

%if 0%{?_build_mpich}
%package -n libopm-simulators%{?postfix}-mpich
Summary:        Open Porous Media - automatic differentiation library
Group:          System/Libraries
Requires:       libopm-grid%{?postfix}-mpich = %{version}

%description -n libopm-simulators%{?postfix}-mpich
The Open Porous Media (OPM) initiative provides a set of open-source tools centered around the simulation of flow and transport of fluids in porous media. The goal of the initiative is to establish a sustainable environment for the development of an efficient and well-maintained software suite.

%package mpich-devel
Summary:        Development and header files for opm-simulators
Group:          Development/Libraries/C and C++
Requires:       libopm-simulators%{?postfix}-mpich = %{version}

%description mpich-devel
This package contains the development and header files for opm-simulators

%package mpich-bin
Summary:        Applications in opm-simulators
Group:          Scientific
Requires:       libopm-simulators%{?postfix}-mpich = %{version}

%description mpich-bin
This package contains the applications for opm-simulators

%if 0%{?_build_versioned} == 1
%package -n opm-simulators-mpich-bin
Summary:        Applications in opm-simulators
Group:          Scientific
Requires:       opm-simulators%{postfix}-mpich-bin = %{version}
Requires:       opm-simulators2024.10-mpich-bin
Requires:       opm-simulators2025.04-mpich-bin

%description -n opm-simulators-mpich-bin
This package contains the applications for opm-simulators
%endif

%endif

%prep
%setup -q -n opm-simulators-%{rtype}-%{version}-%{tag}
%patch0 -p1
%patch1 -p1

%build
mkdir serial
pushd serial
scl enable %{_toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 -DUSE_MPI=0 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_DOCDIR=share/doc/opm-simulators-%{version} -DUSE_RUNPATH=OFF -DWITH_NATIVE=OFF -DCMAKE_INSTALL_SYSCONFDIR=/etc .. '
scl enable %{_toolset} 'make %{?_smp_mflags}'
scl enable %{_toolset} 'ctest3 --output-on-failure'
popd

%if 0%{?_build_openmpi}
mkdir openmpi
pushd openmpi
module load mpi/openmpi-x86_64
scl enable %{_toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 -DUSE_MPI=1 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/openmpi -DCMAKE_INSTALL_LIBDIR=lib -DCMAKE_INSTALL_DOCDIR=share/doc/opm-simulators-%{version} -DUSE_RUNPATH=OFF -DWITH_NATIVE=OFF -DZOLTAN_INCLUDE_DIR=/usr/include/openmpi-x86_64/zoltan -DCMAKE_INSTALL_SYSCONFDIR=/etc ..'
scl enable %{_toolset} 'make %{?_smp_mflags}'
scl enable %{_toolset} 'ctest3 --output-on-failure'
module unload mpi/openmpi-x86_64
popd
%endif

%if 0%{?_build_mpich}
mkdir mpich
pushd mpich
module load mpi/mpich-x86_64
scl enable %{_toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 -DUSE_MPI=1 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/mpich -DCMAKE_INSTALL_LIBDIR=lib -DCMAKE_INSTALL_DOCDIR=share/doc/opm-simulators-%{version} -DUSE_RUNPATH=OFF -DWITH_NATIVE=OFF -DZOLTAN_INCLUDE_DIR=/usr/include/mpich-x86_64/zoltan -DCMAKE_INSTALL_SYSCONFDIR=/etc ..'
scl enable %{_toolset} 'make %{?_smp_mflags}'
scl enable %{_toolset} 'ctest3 --output-on-failure'
module unload mpi/mpich-x86_64
popd
%endif

%install
scl enable %{_toolset} 'make install DESTDIR=${RPM_BUILD_ROOT} -C serial'
scl enable %{_toolset} 'make install-html DESTDIR=${RPM_BUILD_ROOT} -C serial'
%if 0%{?_build_versioned} == 1
mv ${RPM_BUILD_ROOT}/usr/bin/flow ${RPM_BUILD_ROOT}/usr/bin/flow-%{version}
ln -sfr ${RPM_BUILD_ROOT}/usr/bin/flow-%{version} ${RPM_BUILD_ROOT}/usr/bin/flow
%endif

%if 0%{?_build_openmpi}
scl enable %{_toolset} 'make install DESTDIR=${RPM_BUILD_ROOT} -C openmpi'
mkdir -p ${RPM_BUILD_ROOT}/usr/include/openmpi-x86_64/
mv ${RPM_BUILD_ROOT}/usr/lib64/openmpi/include/* ${RPM_BUILD_ROOT}/usr/include/openmpi-x86_64/
%if 0%{?_build_versioned} == 1
mv ${RPM_BUILD_ROOT}/usr/lib64/openmpi/bin/flow ${RPM_BUILD_ROOT}/usr/lib64/openmpi/bin/flow-%{version}
ln -sfr ${RPM_BUILD_ROOT}/usr/lib64/openmpi/bin/flow-%{version} ${RPM_BUILD_ROOT}/usr/lib64/openmpi/bin/flow
%endif
%endif

%if 0%{?_build_mpich}
scl enable %{_toolset} 'make install DESTDIR=${RPM_BUILD_ROOT} -C mpich'
mkdir -p ${RPM_BUILD_ROOT}/usr/include/mpich-x86_64/
mv ${RPM_BUILD_ROOT}/usr/lib64/mpich/include/* ${RPM_BUILD_ROOT}/usr/include/mpich-x86_64/
%if 0%{?_build_versioned} == 1
mv ${RPM_BUILD_ROOT}/usr/lib64/mpich/bin/flow ${RPM_BUILD_ROOT}/usr/lib64/mpich/bin/flow-%{version}
ln -sfr ${RPM_BUILD_ROOT}/usr/lib64/mpich/bin/flow-%{version} ${RPM_BUILD_ROOT}/usr/lib64/mpich/bin/flow
%endif
%endif

%clean
rm -rf %{buildroot}

%post -n libopm-simulators%{?postfix} -p /sbin/ldconfig
%postun -n libopm-simulators%{?postfix} -p /sbin/ldconfig

%if 0%{?_build_openmpi}
%post -n libopm-simulators%{?postfix}-openmpi -p /sbin/ldconfig
%postun -n libopm-simulators%{?postfix}-openmpi -p /sbin/ldconfig
%endif

%if 0%{?_build_mpich}
%post -n libopm-simulators%{?postfix}-mpich -p /sbin/ldconfig
%postun -n libopm-simulators%{?postfix}-mpich -p /sbin/ldconfig
%endif

%files doc
%{_docdir}/*

%files -n libopm-simulators%{?postfix}
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
%if 0%{?_build_versioned} == 1
%{_bindir}/flow-*
%else
%{_bindir}/flow
%endif
/etc/bash_completion.d/*
%if 0%{?_build_versioned} == 1
%exclude %{_datadir}/man/*
%else
%{_datadir}/man/*
%endif

%if 0%{?_build_versioned} == 1
%files -n opm-simulators-bin
%{_bindir}/flow
%endif

%if 0%{?_build_openmpi}
%files -n libopm-simulators%{?postfix}-openmpi
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
%if 0%{?_build_versioned} == 1
%{_libdir}/openmpi/bin/flow-*
%else
%{_libdir}/openmpi/bin/flow
%endif
%if 0%{?_build_versioned} == 1
%exclude %{_libdir}/openmpi/share/man/*
%else
%{_libdir}/openmpi/share/man/*
%endif

%if 0%{?_build_versioned} == 1
%files -n opm-simulators-openmpi-bin
%{_libdir}/openmpi/bin/flow
%endif

%endif

%if 0%{?_build_mpich}
%files -n libopm-simulators%{?postfix}-mpich
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
%if 0%{?_build_versioned} == 1
%{_libdir}/mpich/bin/flow-*
%else
%{_libdir}/mpich/bin/flow
%endif
%if 0%{?_build_versioned} == 1
%exclude %{_libdir}/mpich/share/man/*
%else
%{_libdir}/mpich/share/man/*
%endif

%if 0%{?_build_versioned} == 1
%files -n opm-simulators-mpich-bin
%{_libdir}/mpich/bin/flow
%endif

%endif
