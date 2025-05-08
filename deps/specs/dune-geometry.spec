#
# spec file for package dune-geometry
#

Name:           dune-geometry
Version:        2.9.1
Release:        1
Summary:        Everything related to the DUNE reference elements
License:        GPL-2.0
Group:          Development/Libraries/C and C++
Url:            http://www.dune-project.org/
Source0:        https://dune-project.org/download/2.9.1/dune-geometry-2.9.1.tar.gz
BuildRequires:  dune-common-devel
BuildRequires:  gcc-c++ gcc-gfortran
BuildRequires:  gmp-devel
BuildRequires:  pkgconfig %{_toolset}
BuildRequires:  cmake3 boost-devel
%if 0%{?_build_openmpi}
BuildRequires:  openmpi-devel dune-common-openmpi-devel
%endif
%if 0%{?_build_mpich}
BuildRequires:  mpich-devel dune-common-mpich-devel
%endif
BuildRequires:  doxygen inkscape
BuildRequires:  tbb-devel python3-sphinx latexmk graphviz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       dune-common = %{version}
Requires:       libdune-geometry = %{version}

%description
dune-geometry includes everything related to the DUNE reference elements.
This includes the reference elements themselves, mappings on the reference
elements (geometries), and quadratures.

%package -n libdune-geometry
Summary:        Everything related to the DUNE reference elements
Group:          System/Libraries

%description -n libdune-geometry
dune-geometry includes everything related to the DUNE reference elements.
This includes the reference elements themselves, mappings on the reference
elements (geometries), and quadratures.

%package devel
Summary:        Development and header files for DUNE
Group:          Development/Libraries/C and C++
Requires:       dune-common-devel = %{version}
Requires:       gmp-devel
Requires:       libdune-geometry = %{version}

%description devel
This package contains the development and header files for DUNE.

%package doc
Summary:        doxygen documentation for dune-geometry
Group:          Documentation
BuildArch:      noarch

%description doc
Doxygen documentation for dune-geometry

%if 0%{?_build_openmpi}
%package -n libdune-geometry-openmpi
Summary:        Everything related to the DUNE reference elements - openmpi version
Group:          System/Libraries

%description -n libdune-geometry-openmpi
dune-geometry includes everything related to the DUNE reference elements - openmpi-version
This includes the reference elements themselves, mappings on the reference
elements (geometries), and quadratures.

%package openmpi-devel
Summary:        Development and header files for DUNE - openmpi version
Group:          Development/Libraries/C and C++
Requires:       dune-common-openmpi-devel = %{version}
Requires:       gmp-devel
Requires:       libdune-geometry-openmpi = %{version}

%description openmpi-devel
This package contains the development and header files for DUNE - openmpi version
%endif

%if 0%{?_build_mpich}
%package -n libdune-geometry-mpich
Summary:        Everything related to the DUNE reference elements - mpich version
Group:          System/Libraries

%description -n libdune-geometry-mpich
dune-geometry includes everything related to the DUNE reference elements - mpich-version
This includes the reference elements themselves, mappings on the reference
elements (geometries), and quadratures.

%package mpich-devel
Summary:        Development and header files for DUNE - mpich version
Group:          Development/Libraries/C and C++
Requires:       dune-common-mpich-devel = %{version}
Requires:       gmp-devel
Requires:       libdune-geometry-mpich = %{version}

%description mpich-devel
This package contains the development and header files for DUNE - mpich version
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
rm -rf %{buildroot}/usr/lib64/openmpi/share/doc
%endif

%if 0%{?_build_mpich}
scl enable %{_toolset} 'make install DESTDIR=%{buildroot} -C mpich'
rm -rf %{buildroot}/usr/lib64/mpich/share/doc
%endif

%clean
rm -rf %{buildroot}

%post -n libdune-geometry -p /sbin/ldconfig
%postun -n libdune-geometry -p /sbin/ldconfig
%if 0%{?_build_openmpi}
%post -n libdune-geometry-openmpi -p /sbin/ldconfig
%postun -n libdune-geometry-openmpi -p /sbin/ldconfig
%endif
%if 0%{?_build_mpich}
%post -n libdune-geometry-mpich -p /sbin/ldconfig
%postun -n libdune-geometry-mpich -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
%doc COPYING README.md

%files doc
%{_datadir}/doc/dune-geometry

%files -n libdune-geometry
%defattr(-,root,root,-)
%{_libdir}/*.so

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_datadir}/%{name}
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/*.pc
%{_prefix}/lib/dunecontrol/%{name}
%if 0%{?_build_openmpi}
%exclude /usr/include/openmpi-x86_64
%endif
%if 0%{?_build_mpich}
%exclude /usr/include/mpich-x86_64
%endif

%if 0%{?_build_openmpi}
%files -n libdune-geometry-openmpi
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
%files -n libdune-geometry-mpich
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
