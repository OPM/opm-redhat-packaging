#
# spec file for package opm-simulators
#

%define tag final
%define rtype release
%define build_openmpi 1
%define build_mpich 1

%define toolset gcc-toolset-12

Name:           opm-simulators
Version:        2024.10
Release:        0
Summary:        Open Porous Media - core library
License:        GPL-3.0
Group:          Development/Libraries/C and C++
Url:            http://www.opm-project.org/
Source0:        https://github.com/OPM/%{name}/archive/release/%{version}/%{tag}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-opm-simulators_skip_test_boost_return_code.patch
BuildRequires:  lapack-devel openblas-devel
BuildRequires:  git suitesparse-devel doxygen bc graphviz texlive-dvips-bin
BuildRequires:  tinyxml-devel zlib-devel fmt-devel
BuildRequires: zoltan-devel
BuildRequires: cmake3
BuildRequires: %{toolset}
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

%if %{build_openmpi}
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

%if %{build_mpich}
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

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Open Porous Media (OPM) initiative provides a set of open-source tools centered around the simulation of flow and transport of fluids in porous media. The goal of the initiative is to establish a sustainable environment for the development of an efficient and well-maintained software suite.

%package -n libopm-simulators
Summary:        Open Porous Media - automatic differentiation library
Group:          System/Libraries
Requires:       libopm-grid = %{version}

%description -n libopm-simulators
The Open Porous Media (OPM) initiative provides a set of open-source tools centered around the simulation of flow and transport of fluids in porous media. The goal of the initiative is to establish a sustainable environment for the development of an efficient and well-maintained software suite.

%package -n libopm-simulators%{version}
Summary:        Open Porous Media - automatic differentiation library
Group:          System/Libraries
Requires:       libopm-grid%{version} = %{version}

%description -n libopm-simulators%{version}
The Open Porous Media (OPM) initiative provides a set of open-source tools centered around the simulation of flow and transport of fluids in porous media. The goal of the initiative is to establish a sustainable environment for the development of an efficient and well-maintained software suite.

%package devel
Summary:        Development and header files for opm-simulators
Group:          Development/Libraries/C and C++
Requires:       libopm-simulator = %{version}

%description devel
This package contains the development and header files for opm-simulators

%package doc
Summary:        Documentation files for opm-simulators
Group:          Documentation
BuildArch:	noarch

%description doc
This package contains the documentation files for opm-simulators

%package bin
Summary:        Applications in opm-simulators
Group:          Scientific
Requires:       libopm-simulators = %{version}

%description bin
This package contains the applications for opm-simulators

%package -n opm-simulators%{version}-bin
Summary:        Applications in opm-simulators
Group:          Scientific
Requires:       libopm-simulators%{version} = %{version}

%description -n opm-simulators%{version}-bin
This package contains the applications for opm-simulators

%if %{build_openmpi}
%package -n libopm-simulators-openmpi
Summary:        Open Porous Media - automatic differentiation library
Group:          System/Libraries
Requires:       libopm-grid-openmpi = %{version}

%description -n libopm-simulators-openmpi
The Open Porous Media (OPM) initiative provides a set of open-source tools centered around the simulation of flow and transport of fluids in porous media. The goal of the initiative is to establish a sustainable environment for the development of an efficient and well-maintained software suite.

%package -n libopm-simulators%{version}-openmpi
Summary:        Open Porous Media - automatic differentiation library
Group:          System/Libraries
Requires:       libopm-grid%{version}-openmpi = %{version}

%description -n libopm-simulators%{version}-openmpi
The Open Porous Media (OPM) initiative provides a set of open-source tools centered around the simulation of flow and transport of fluids in porous media. The goal of the initiative is to establish a sustainable environment for the development of an efficient and well-maintained software suite.

%package openmpi-devel
Summary:        Development and header files for opm-simulators
Group:          Development/Libraries/C and C++
Requires:       libopm-simulators-openmpi = %{version}

%description openmpi-devel
This package contains the development and header files for opm-simulators

%package openmpi-bin
Summary:        Applications in opm-simulators
Group:          Scientific
Requires:       libopm-simulators-openmpi = %{version}

%description openmpi-bin
This package contains the applications for opm-simulators

%package -n opm-simulators%{version}-openmpi-bin
Summary:        Applications in opm-simulators
Group:          Scientific
Requires:       libopm-simulators%{version}-openmpi

%description -n opm-simulators%{version}-openmpi-bin
This package contains the applications for opm-simulators
%endif

%if %{build_mpich}
%package -n libopm-simulators-mpich
Summary:        Open Porous Media - automatic differentiation library
Group:          System/Libraries
Requires:       libopm-grid-mpich = %{version}

%description -n libopm-simulators-mpich
The Open Porous Media (OPM) initiative provides a set of open-source tools centered around the simulation of flow and transport of fluids in porous media. The goal of the initiative is to establish a sustainable environment for the development of an efficient and well-maintained software suite.

%package -n libopm-simulators%{version}-mpich
Summary:        Open Porous Media - automatic differentiation library
Group:          System/Libraries
Requires:       libopm-grid%{version}-mpich = %{version}

%description -n libopm-simulators%{version}-mpich
The Open Porous Media (OPM) initiative provides a set of open-source tools centered around the simulation of flow and transport of fluids in porous media. The goal of the initiative is to establish a sustainable environment for the development of an efficient and well-maintained software suite.

%package mpich-devel
Summary:        Development and header files for opm-simulators
Group:          Development/Libraries/C and C++
Requires:       libopm-simulators-mpich = %{version}

%description mpich-devel
This package contains the development and header files for opm-simulators

%package mpich-bin
Summary:        Applications in opm-simulators
Group:          Scientific
Requires:       libopm-simulators-mpich = %{version}

%description mpich-bin
This package contains the applications for opm-simulators

%package -n opm-simulators%{version}-mpich-bin
Summary:        Applications in opm-simulators
Group:          Scientific
Requires:       libopm-simulators%{version}-mpich = %{version}

%description -n opm-simulators%{version}-mpich-bin
This package contains the applications for opm-simulators

%endif

%prep
%setup -q -n %{name}-%{rtype}-%{version}-%{tag}
%patch0 -p1

%build
mkdir serial
pushd serial
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 -DUSE_MPI=0 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_DOCDIR=share/doc/%{name}-%{version} -DUSE_RUNPATH=OFF -DWITH_NATIVE=OFF -DCMAKE_INSTALL_SYSCONFDIR=/etc .. '
scl enable %{toolset} 'make %{?_smp_mflags}'
scl enable %{toolset} 'ctest3 --output-on-failure'
popd

%if %{build_openmpi}
mkdir openmpi
pushd openmpi
module load mpi/openmpi-x86_64
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 -DUSE_MPI=1 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/openmpi -DCMAKE_INSTALL_LIBDIR=lib -DCMAKE_INSTALL_DOCDIR=share/doc/%{name}-%{version} -DUSE_RUNPATH=OFF -DWITH_NATIVE=OFF -DZOLTAN_INCLUDE_DIR=/usr/include/openmpi-x86_64/zoltan -DCMAKE_INSTALL_SYSCONFDIR=/etc ..'
scl enable %{toolset} 'make %{?_smp_mflags}'
scl enable %{toolset} 'ctest3 --output-on-failure'
module unload mpi/openmpi-x86_64
popd
%endif

%if %{build_mpich}
mkdir mpich
pushd mpich
module load mpi/mpich-x86_64
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 -DUSE_MPI=1 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/mpich -DCMAKE_INSTALL_LIBDIR=lib -DCMAKE_INSTALL_DOCDIR=share/doc/%{name}-%{version} -DUSE_RUNPATH=OFF -DWITH_NATIVE=OFF -DZOLTAN_INCLUDE_DIR=/usr/include/mpich-x86_64/zoltan -DCMAKE_INSTALL_SYSCONFDIR=/etc ..'
scl enable %{toolset} 'make %{?_smp_mflags}'
scl enable %{toolset} 'ctest3 --output-on-failure'
module unload mpi/mpich-x86_64
popd
%endif

%install
scl enable %{toolset} 'make install DESTDIR=${RPM_BUILD_ROOT} -C serial'
scl enable %{toolset} 'make install-html DESTDIR=${RPM_BUILD_ROOT} -C serial'
cp ${RPM_BUILD_ROOT}/usr/bin/flow ${RPM_BUILD_ROOT}/usr/bin/flow-%{version}

%if %{build_openmpi}
scl enable %{toolset} 'make install DESTDIR=${RPM_BUILD_ROOT} -C openmpi'
mkdir -p ${RPM_BUILD_ROOT}/usr/include/openmpi-x86_64/
mv ${RPM_BUILD_ROOT}/usr/lib64/openmpi/include/* ${RPM_BUILD_ROOT}/usr/include/openmpi-x86_64/
cp ${RPM_BUILD_ROOT}/usr/lib64/openmpi/bin/flow ${RPM_BUILD_ROOT}/usr/lib64/openmpi/bin/flow-%{version}
%endif

%if %{build_mpich}
scl enable %{toolset} 'make install DESTDIR=${RPM_BUILD_ROOT} -C mpich'
mkdir -p ${RPM_BUILD_ROOT}/usr/include/mpich-x86_64/
mv ${RPM_BUILD_ROOT}/usr/lib64/mpich/include/* ${RPM_BUILD_ROOT}/usr/include/mpich-x86_64/
cp ${RPM_BUILD_ROOT}/usr/lib64/mpich/bin/flow ${RPM_BUILD_ROOT}/usr/lib64/mpich/bin/flow-%{version}
%endif

%clean
rm -rf %{buildroot}

%post -n libopm-simulators -p /sbin/ldconfig
%postun -n libopm-simulators -p /sbin/ldconfig
%post -n libopm-simulators%{version} -p /sbin/ldconfig
%postun -n libopm-simulators%{version} -p /sbin/ldconfig

%if %{build_openmpi}
%post -n libopm-simulators-openmpi -p /sbin/ldconfig
%postun -n libopm-simulators-openmpi -p /sbin/ldconfig
%post -n libopm-simulators%{version}-openmpi -p /sbin/ldconfig
%postun -n libopm-simulators%{version}-openmpi -p /sbin/ldconfig
%endif

%if %{build_mpich}
%post -n libopm-simulators-mpich -p /sbin/ldconfig
%postun -n libopm-simulators-mpich -p /sbin/ldconfig
%post -n libopm-simulators%{version}-mpich -p /sbin/ldconfig
%postun -n libopm-simulators%{version}-mpich -p /sbin/ldconfig
%endif

%files doc
%{_docdir}/*

%files -n libopm-simulators
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files -n libopm-simulators%{version}
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
%if %{build_mpich}
%exclude /usr/include/mpich-x86_64
%endif

%files bin
%{_bindir}/*
/etc/bash_completion.d/*
%{_datadir}/man/*
%exclude %{_bindir}/flow-%{version}

%files -n opm-simulators%{version}-bin
%{_bindir}/flow-%{version}

%if %{build_openmpi}
%files -n libopm-simulators-openmpi
%defattr(-,root,root,-)
%{_libdir}/openmpi/lib/*.so.*

%files -n libopm-simulators%{version}-openmpi
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
%exclude %{_libdir}/openmpi/bin/flow-%{version}

%files -n opm-simulators%{version}-openmpi-bin
%{_libdir}/openmpi/bin/flow-%{version}
%endif

%if %{build_mpich}
%files -n libopm-simulators-mpich
%defattr(-,root,root,-)
%{_libdir}/mpich/lib/*.so.*

%files -n libopm-simulators%{version}-mpich
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
%exclude %{_libdir}/mpich/bin/flow-%{version}

%files -n opm-simulators%{version}-mpich-bin
%{_libdir}/mpich/bin/flow-%{version}
%endif
