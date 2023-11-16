#
# spec file for package dune-geometry
#

%if 0%{?rhel} == 7
%define toolset devtoolset-9
%else
%define toolset gcc-toolset-12
%endif

Name:           dune-geometry
Version:        2.8.0
Release:        0
Summary:        Everything related to the DUNE reference elements
License:        GPL-2.0
Group:          Development/Libraries/C and C++
Url:            http://www.dune-project.org/
Source0:        https://dune-project.org/download/2.8.0/dune-geometry-2.8.0.tar.gz
BuildRequires:  dune-common-devel dune-common-openmpi-devel dune-common-mpich-devel
BuildRequires:  gcc-c++ gcc-gfortran
BuildRequires:  gmp-devel
BuildRequires:  pkgconfig %{toolset}
BuildRequires:  cmake3 boost-devel
BuildRequires:  openmpi-devel mpich-devel
%if 0%{?rhel} == 7
BuildRequires:  openmpi3-devel dune-common-openmpi3-devel
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

%if 0%{?rhel} == 7
%package -n libdune-geometry-openmpi3
Summary:        Everything related to the DUNE reference elements - openmpi3 version
Group:          System/Libraries

%description -n libdune-geometry-openmpi3
dune-geometry includes everything related to the DUNE reference elements - openmpi3-version
This includes the reference elements themselves, mappings on the reference
elements (geometries), and quadratures.

%package openmpi3-devel
Summary:        Development and header files for DUNE - openmpi version
Group:          Development/Libraries/C and C++
Requires:       dune-common-openmpi3-devel = %{version}
Requires:       gmp-devel
Requires:       libdune-geometry-openmpi3 = %{version}

%description openmpi3-devel
This package contains the development and header files for DUNE - openmpi version
%endif

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

%prep
%setup -q

%build
mkdir serial
pushd serial
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1'
scl enable %{toolset} 'make %{?_smp_mflags}'
popd

mkdir openmpi
pushd openmpi
module load mpi/openmpi-x86_64
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/openmpi -DCMAKE_INSTALL_INCLUDEDIR=/usr/include/openmpi-x86_64 -DCMAKE_INSTALL_LIBDIR=lib -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1'
scl enable %{toolset} 'make %{?_smp_mflags}'
module unload mpi/openmpi-x86_64
popd

%if 0%{?rhel} == 7
mkdir openmpi3
pushd openmpi3
module load mpi/openmpi3-x86_64
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/openmpi3 -DCMAKE_INSTALL_INCLUDEDIR=/usr/include/openmpi3-x86_64 -DCMAKE_INSTALL_LIBDIR=lib -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1'
scl enable %{toolset} 'make %{?_smp_mflags}'
module unload mpi/openmpi3-x86_64
popd
%endif

mkdir mpich
pushd mpich
module load mpi/mpich-x86_64
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/mpich -DCMAKE_INSTALL_INCLUDEDIR=/usr/include/mpich-x86_64 -DCMAKE_INSTALL_LIBDIR=lib -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1'
scl enable %{toolset} 'make %{?_smp_mflags}'
module unload mpi/mpich-x86_64
popd

%install
rm -rf %{buildroot}
scl enable %{toolset} 'make install DESTDIR=%{buildroot} -C serial'
scl enable %{toolset} 'make install DESTDIR=%{buildroot} -C openmpi'
scl enable %{toolset} 'make install DESTDIR=%{buildroot} -C mpich'
rm -rf %{buildroot}/usr/lib64/openmpi/share/doc
rm -rf %{buildroot}/usr/lib64/mpich/share/doc

%if 0%{?rhel} == 7
scl enable %{toolset} 'make install DESTDIR=%{buildroot} -C openmpi3'
rm -rf %{buildroot}/usr/lib64/openmpi3/share/doc
%endif

%clean
rm -rf %{buildroot}

%post -n libdune-geometry -p /sbin/ldconfig
%postun -n libdune-geometry -p /sbin/ldconfig
%post -n libdune-geometry-openmpi -p /sbin/ldconfig
%postun -n libdune-geometry-openmpi -p /sbin/ldconfig
%post -n libdune-geometry-mpich -p /sbin/ldconfig
%postun -n libdune-geometry-mpich -p /sbin/ldconfig
%if 0%{?rhel} == 7
%post -n libdune-geometry-openmpi3 -p /sbin/ldconfig
%postun -n libdune-geometry-openmpi3 -p /sbin/ldconfig
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
%exclude /usr/include/openmpi-x86_64
%exclude /usr/include/openmpi3-x86_64
%exclude /usr/include/mpich-x86_64

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

%if 0%{?rhel} == 7
%files -n libdune-geometry-openmpi3
%defattr(-,root,root,-)
%{_libdir}/openmpi3/lib/*.so

%files openmpi3-devel
%defattr(-,root,root,-)
%{_includedir}/openmpi3-x86_64/dune/*
%{_libdir}/openmpi3/lib/dune*
%{_libdir}/openmpi3/lib/pkgconfig/*.pc
%{_libdir}/openmpi3/lib/cmake
%{_libdir}/openmpi3/share/*
%endif

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
