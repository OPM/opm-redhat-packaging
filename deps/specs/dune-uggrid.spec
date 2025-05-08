#
# spec file for package dune-uggrid
#

Name:           dune-uggrid
Version:        2.9.1
Release:        1
Summary:        UG Grid module for DUNE
License:        GPL-2.0
Group:          Development/Libraries/C and C++
Source0:        https://dune-project.org/download/2.9.1/dune-uggrid-2.9.1.tar.gz
BuildRequires:  dune-common-devel dune-geometry-devel
BuildRequires:  openmpi-devel mpich-devel
%if 0%{?_build_openmpi}
BuildRequires: openmpi-devel dune-common-openmpi-devel dune-geometry-openmpi-devel
%endif
%if 0%{?_build_mpich}
BuildRequires: mpich-devel dune-common-mpich-devel dune-geometry-mpich-devel
%endif
BuildRequires:  mesa-libGL-devel gmp-devel metis-devel
BuildRequires:  pkgconfig %{_toolset}
BuildRequires:  cmake3 boost-devel doxygen inkscape
BuildRequires:  tbb-devel python3-sphinx latexmk graphviz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       libdune-uggrid = %{version}

%description
dune-uggrid defines nonconforming, hierarchically nested, multi-element-type,
parallel grids in arbitrary space dimensions. Graphical output with several
packages is available, e.g. file output to IBM data explorer and VTK (parallel
XML format for unstructured grids). The graphics package Grape has been integrated
in interactive mode. This module also provides some grid implementations and
further grid managers can be added through seprate modules.

%package -n libdune-uggrid
Summary:        Grid management module for DUNE
Group:          System/Libraries

%description -n libdune-uggrid
dune-grid defines nonconforming, hierarchically nested, multi-element-type,
parallel grids in arbitrary space dimensions. Graphical output with several
packages is available, e.g. file output to IBM data explorer and VTK (parallel
XML format for unstructured grids). The graphics package Grape has been integrated
in interactive mode. This module also provides some grid implementations and
further grid managers can be added through separate modules.

%package devel
Summary:        Development and header files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libdune-uggrid = %{version}

%description devel
This package contains the development and header files for %{name}.

%package doc
Summary:        Doxygen documentation for %{name}
Group:          Documentation
BuildArch:      noarch

%description doc
This package contains the doxygen documentation for %{name}.

%if 0%{?_build_openmpi}
%package -n libdune-uggrid-openmpi
Summary:        Grid management module for DUNE - openmpi version
Group:          System/Libraries

%description -n libdune-uggrid-openmpi
dune-grid defines nonconforming, hierarchically nested, multi-element-type,
parallel grids in arbitrary space dimensions. Graphical output with several
packages is available, e.g. file output to IBM data explorer and VTK (parallel
XML format for unstructured grids). The graphics package Grape has been integrated
in interactive mode. This module also provides some grid implementations and
further grid managers can be added through separate modules.

%package openmpi-devel
Summary:        Development and header files for %{name} - openmpi version
Group:          Development/Libraries/C and C++
Requires:       libdune-uggrid-openmpi = %{version}

%description openmpi-devel
This package contains the development and header files for %{name} - openmpi version.
%endif

%if 0%{?_build_mpich}
%package -n libdune-uggrid-mpich
Summary:        Grid management module for DUNE - mpich version
Group:          System/Libraries

%description -n libdune-uggrid-mpich
dune-grid defines nonconforming, hierarchically nested, multi-element-type,
parallel grids in arbitrary space dimensions. Graphical output with several
packages is available, e.g. file output to IBM data explorer and VTK (parallel
XML format for unstructured grids). The graphics package Grape has been integrated
in interactive mode. This module also provides some grid implementations and
further grid managers can be added through separate modules.

%package mpich-devel
Summary:        Development and header files for %{name} - mpich version
Group:          Development/Libraries/C and C++
Requires:       libdune-uggrid-mpich = %{version}

%description mpich-devel
This package contains the development and header files for %{name} - mpich version.
%endif

%prep
%setup -q

%build
mkdir serial
pushd serial
scl enable %{_toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1'
scl enable %{_toolset} 'make %{?_smp_mflags}'
popd

%if 0%{?_build_openmpi}
mkdir openmpi
pushd openmpi
module load mpi/openmpi-x86_64
scl enable %{_toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/openmpi -DCMAKE_INSTALL_INCLUDEDIR=/usr/include/openmpi-x86_64 -DCMAKE_INSTALL_LIBDIR=lib -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1'
scl enable %{_toolset} 'make %{?_smp_mflags}'
module unload mpi/openmpi-x86_64
popd
%endif

%if 0%{?_build_mpich}
mkdir mpich
pushd mpich
module load mpi/mpich-x86_64
scl enable %{_toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/mpich -DCMAKE_INSTALL_INCLUDEDIR=/usr/include/mpich-x86_64 -DCMAKE_INSTALL_LIBDIR=lib -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1'
scl enable %{_toolset} 'make %{?_smp_mflags}'
module unload mpi/mpich-x86_64
popd
%endif

%install
rm -rf %{buildroot}
scl enable %{_toolset} 'make install DESTDIR=%{buildroot} -C serial'
%if 0%{?_build_openmpi}
scl enable %{_toolset} 'make install DESTDIR=%{buildroot} -C openmpi'
%endif

%if 0%{?_build_mpich}
scl enable %{_toolset} 'make install DESTDIR=%{buildroot} -C mpich'
%endif

%clean
rm -rf %{buildroot}

%post -n libdune-uggrid -p /sbin/ldconfig
%postun -n libdune-uggrid -p /sbin/ldconfig

%if 0%{?_build_openmpi}
%post -n libdune-uggrid-openmpi -p /sbin/ldconfig
%postun -n libdune-uggrid-openmpi -p /sbin/ldconfig
%endif

%if 0%{?_build_mpich}
%post -n libdune-uggrid-mpich -p /sbin/ldconfig
%postun -n libdune-uggrid-mpich -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
%doc COPYING CHANGELOG.md

%files -n libdune-uggrid
%defattr(-,root,root,-)
%{_libdir}/*.so

%files doc
%{_datadir}/doc/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/dune/*
%{_libdir}/cmake/*
%{_datadir}/dune
%{_datadir}/dune-uggrid
%{_datadir}/triangle.rls
%{_datadir}/tetra.rls
%{_datadir}/RefRules.data
%{_libdir}/pkgconfig/*.pc
%{_prefix}/lib/dune*
%if 0%{?_build_openmpi}
%exclude /usr/include/openmpi-x86_64
%endif
%if 0%{?_build_mpich}
%exclude /usr/include/mpich-x86_64
%endif

%if 0%{?_build_openmpi}
%files -n libdune-uggrid-openmpi
%defattr(-,root,root,-)
%{_libdir}/openmpi/lib/*.so

%files openmpi-devel
%defattr(-,root,root,-)
%{_includedir}/openmpi-x86_64/dune/*
%{_libdir}/openmpi/lib/dune*
%{_libdir}/openmpi/lib/pkgconfig/*.pc
%{_libdir}/openmpi/lib/cmake
%{_libdir}/openmpi/share/*
%endif

%if 0%{?_build_mpich}
%files -n libdune-uggrid-mpich
%defattr(-,root,root,-)
%{_libdir}/mpich/lib/*.so

%files mpich-devel
%defattr(-,root,root,-)
%{_includedir}/mpich-x86_64/dune/*
%{_libdir}/mpich/lib/dune*
%{_libdir}/mpich/lib/pkgconfig/*.pc
%{_libdir}/mpich/lib/cmake
%{_libdir}/mpich/share/*
%endif
