#
# spec file for package dune-grid
#

Name:           dune-grid
Version:        2.11.0
Release:        1
Summary:        Grid management module for DUNE
License:        GPL-2.0
Group:          Development/Libraries/C and C++
Url:            http://www.dune-project.org/
Source0:        https://gitlab.dune-project.org/core/dune-grid/-/archive/v2.11.0/dune-grid-v2.11.0.tar.gz
BuildRequires:  dune-common-devel dune-geometry-devel dune-uggrid-devel
BuildRequires:  mesa-libGL-devel metis-devel
BuildRequires:  pkgconfig %{_toolset}
BuildRequires:  cmake3 boost-devel
BuildRequires:  openmpi-devel mpich-devel
%if 0%{?_build_openmpi}
BuildRequires: openmpi-devel dune-common-openmpi-devel
BuildRequires: dune-geometry-openmpi-devel dune-uggrid-openmpi-devel
%endif
%if 0%{?_build_mpich}
BuildRequires: mpich-devel dune-common-mpich-devel
BuildRequires: dune-geometry-mpich-devel dune-uggrid-mpich-devel
%endif
#BuildRequires:  doxygen inkscape graphviz latexmk texlive-bibtex python3-sphinx
#BuildRequires:  texlive-amscls texlive-psfrag texlive-subfigure texlive-metafont
#BuildRequires:  texlive-cm texlive-mfware
BuildRequires:  tbb-devel
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

%if 0%{?_build_openmpi}
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
%endif

%if 0%{?_build_mpich}
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
%endif

%prep
%setup -q -n dune-grid-v2.11.0

%build
mkdir serial
pushd serial
scl enable %{_toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON -DCMAKE_DISABLE_FIND_PACKAGE_Doxygen=ON'
scl enable %{_toolset} 'make %{?_smp_mflags}'
popd

%if 0%{?_build_openmpi}
mkdir openmpi
pushd openmpi
module load mpi/openmpi-x86_64
scl enable %{_toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/openmpi -DCMAKE_INSTALL_INCLUDEDIR=/usr/include/openmpi-x86_64 -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_LIBDIR=lib -DCMAKE_DISABLE_FIND_PACKAGE_Doxygen=ON'
scl enable %{_toolset} 'make %{?_smp_mflags}'
module unload mpi/openmpi-x86_64
popd
%endif

%if 0%{?_build_mpich}
mkdir mpich
pushd mpich
module load mpi/mpich-x86_64
scl enable %{_toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/mpich -DCMAKE_INSTALL_INCLUDEDIR=/usr/include/mpich-x86_64 -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_LIBDIR=lib -DCMAKE_DISABLE_FIND_PACKAGE_Doxygen=ON'
scl enable %{_toolset} 'make %{?_smp_mflags}'
module unload mpi/mpich-x86_64
popd
%endif

%install
rm -rf %{buildroot}
cd serial
scl enable %{_toolset} 'make install DESTDIR=%{buildroot}'
cd ..
%if 0%{?_build_openmpi}
cd openmpi
scl enable %{_toolset} 'make install DESTDIR=%{buildroot}'
rm -rf %{buildroot}/usr/lib64/openmpi/share/doc
cd ..
%endif

%if 0%{?_build_mpich}
cd mpich
scl enable %{_toolset} 'make install DESTDIR=%{buildroot}'
rm -rf %{buildroot}/usr/lib64/mpich/share/doc
cd ..
%endif

%clean
rm -rf %{buildroot}

%post -n libdune-grid -p /sbin/ldconfig
%postun -n libdune-grid -p /sbin/ldconfig

%if 0%{?_build_openmpi}
%post -n libdune-grid-openmpi -p /sbin/ldconfig
%postun -n libdune-grid-openmpi -p /sbin/ldconfig
%endif

%if 0%{?_build_mpich}
%post -n libdune-grid-mpich -p /sbin/ldconfig
%postun -n libdune-grid-mpich -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
%doc COPYING README.md
%{_datadir}/doc/dune-grid

%files -n libdune-grid
%defattr(-,root,root,-)
%{_libdir}/*.so

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/cmake/*
%{_datadir}/%{name}
%{_datadir}/dune
%{_libdir}/pkgconfig/*.pc
%{_prefix}/lib/dune*
%{_docdir}/dune-grid/grids/*
%if 0%{?_build_openmpi}
%exclude /usr/include/openmpi-x86_64
%endif
%if 0%{?_build_mpich}
%exclude /usr/include/mpich-x86_64
%endif

%files doc
%{_docdir}/*

%if 0%{?_build_openmpi}
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
%endif

%if 0%{?_build_mpich}
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
%endif
