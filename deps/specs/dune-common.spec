#
# spec file for package dune-common
#

%if 0%{?rhel} == 7
%define toolset devtoolset-9
%else
%define toolset gcc-toolset-12
%endif

Name:           dune-common
Version:        2.8.0
Release:        1
Summary:        Distributed and Unified Numerics Environment
License:        GPL-2.0
Group:          Development/Libraries/C and C++
Url:            https://dune-project.org/
Source0:        https://dune-project.org/download/2.8.0/dune-common-2.8.0.tar.gz
Patch0:         0001-dune-common-indices.patch
Patch1:         0002-dune-common-py3.patch
BuildRequires:  blas-devel gpm-devel
BuildRequires:  lapack-devel metis-devel
BuildRequires:  pkgconfig %{toolset}
BuildRequires:  cmake3 boost-devel
BuildRequires:  openmpi-devel mpich-devel 
%if 0%{?rhel} == 7
BuildRequires: openmpi3-devel
%endif
BuildRequires:  doxygen inkscape graphviz texlive-amscls
BuildRequires:  tbb-devel python3-sphinx latexmk texlive-cm texlive-mfware
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       libdune-common = %{version}

%description
DUNE, the Distributed and Unified Numerics Environment is a modular toolbox
for solving partial differential equations (PDEs) with grid-based methods.
It supports the easy implementation of methods like Finite Elements (FE),
Finite Volumes (FV), and also Finite Differences (FD).

%package -n libdune-common
Summary:        Distributed and Unified Numerics Environment
Group:          System/Libraries

%description -n libdune-common
DUNE, the Distributed and Unified Numerics Environment is a modular toolbox
for solving partial differential equations (PDEs) with grid-based methods.
It supports the easy implementation of methods like Finite Elements (FE),
Finite Volumes (FV), and also Finite Differences (FD).

%package doc
Summary:        doxygen documentation for dune-common
Group:          Documentation
BuildArch:      noarch

%description doc
Doxygen documentation for dune-common

%package devel
Summary:        Development and header files for DUNE
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       blas-devel
Requires:       lapack-devel
Requires:       libdune-common = %{version}

%description devel
This package contains the development and header files for DUNE.

%package -n libdune-common-openmpi
Summary:        Distributed and Unified Numerics Environment - openmpi version
Group:          System/Libraries

%description -n libdune-common-openmpi
DUNE, the Distributed and Unified Numerics Environment is a modular toolbox
for solving partial differential equations (PDEs) with grid-based methods.
It supports the easy implementation of methods like Finite Elements (FE),
Finite Volumes (FV), and also Finite Differences (FD). This is built
against OpenMPI.

%package openmpi-devel
Summary:        Development and header files for DUNE - openmpi version
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       blas-devel
Requires:       lapack-devel
Requires:       libdune-common-openmpi = %{version}

%description openmpi-devel
This package contains the development and header files for DUNE. - openmpi version

%if 0%{?rhel} == 7
%package -n libdune-common-openmpi3
Summary:        Distributed and Unified Numerics Environment - openmpi3 version
Group:          System/Libraries

%description -n libdune-common-openmpi3
DUNE, the Distributed and Unified Numerics Environment is a modular toolbox
for solving partial differential equations (PDEs) with grid-based methods.
It supports the easy implementation of methods like Finite Elements (FE),
Finite Volumes (FV), and also Finite Differences (FD). This is built
against OpenMPI3.

%package openmpi3-devel
Summary:        Development and header files for DUNE - openmpi3 version
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       blas-devel
Requires:       lapack-devel
Requires:       libdune-common-openmpi3 = %{version}

%description openmpi3-devel
This package contains the development and header files for DUNE. - openmpi3 version
%endif

%package -n libdune-common-mpich
Summary:        Distributed and Unified Numerics Environment - mpich version
Group:          System/Libraries

%description -n libdune-common-mpich
DUNE, the Distributed and Unified Numerics Environment is a modular toolbox
for solving partial differential equations (PDEs) with grid-based methods.
It supports the easy implementation of methods like Finite Elements (FE),
Finite Volumes (FV), and also Finite Differences (FD). This is built
against MPICH.

%package mpich-devel
Summary:        Development and header files for DUNE - mpich version
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       blas-devel
Requires:       lapack-devel
Requires:       libdune-common-mpich = %{version}

%description mpich-devel
This package contains the development and header files for DUNE. - mpich version

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
mkdir serial
pushd serial
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1'
scl enable %{toolset} 'make %{?_smp_mflags}'
popd

mkdir openmpi
pushd openmpi
module load mpi/openmpi-x86_64
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/openmpi -DCMAKE_INSTALL_INCLUDEDIR=/usr/include/openmpi-x86_64 -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1 -DCMAKE_INSTALL_LIBDIR=lib'
scl enable %{toolset} 'make %{?_smp_mflags}'
module unload mpi/openmpi-x86_64
popd

%if 0%{?rhel} == 7
mkdir openmpi3
pushd openmpi3
module load mpi/openmpi3-x86_64
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/openmpi3 -DCMAKE_INSTALL_INCLUDEDIR=/usr/include/openmpi3-x86_64 -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1 -DCMAKE_INSTALL_LIBDIR=lib'
scl enable %{toolset} 'make %{?_smp_mflags}'
module unload mpi/openmpi3-x86_64
popd
%endif

mkdir mpich
pushd mpich
module load mpi/mpich-x86_64
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/mpich -DCMAKE_INSTALL_INCLUDEDIR=/usr/include/mpich-x86_64 -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1 -DCMAKE_INSTALL_LIBDIR=lib'
scl enable %{toolset} 'make %{?_smp_mflags}'
module unload mpi/mpich-x86_64
popd

%install
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

%post -n libdune-common -p /sbin/ldconfig
%postun -n libdune-common -p /sbin/ldconfig
%post -n libdune-common-openmpi -p /sbin/ldconfig
%postun -n libdune-common-openmpi -p /sbin/ldconfig
%post -n libdune-common-mpich -p /sbin/ldconfig
%postun -n libdune-common-mpich -p /sbin/ldconfig

%if 0%{?rhel} == 7
%post -n libdune-common-openmpi3 -p /sbin/ldconfig
%postun -n libdune-common-openmpi3 -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
%doc COPYING README.md TODO
%{_bindir}/*
%{_datadir}/dune-common
%{_datadir}/man
%{_datadir}/bash-completion/*

%files doc
%{_datadir}/doc/dune-common

%files -n libdune-common
%defattr(-,root,root,-)
%{_libdir}/*.so

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_prefix}/lib/dune*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake
%{_datadir}/dune
%exclude /usr/include/openmpi-x86_64
%exclude /usr/include/openmpi3-x86_64
%exclude /usr/include/mpich-x86_64

%files -n libdune-common-openmpi
%defattr(-,root,root,-)
%{_libdir}/openmpi/lib/*.so
%{_libdir}/openmpi/bin/*

%files openmpi-devel
%defattr(-,root,root,-)
%{_includedir}/openmpi-x86_64/dune/*
%{_libdir}/openmpi/lib/dune*
%{_libdir}/openmpi/lib/pkgconfig/*.pc
%{_libdir}/openmpi/lib/cmake
%{_libdir}/openmpi/share/*

%if 0%{?rhel} == 7
%files -n libdune-common-openmpi3
%defattr(-,root,root,-)
%{_libdir}/openmpi3/lib/*.so
%{_libdir}/openmpi3/bin/*

%files openmpi3-devel
%defattr(-,root,root,-)
%{_includedir}/openmpi3-x86_64/dune/*
%{_libdir}/openmpi3/lib/dune*
%{_libdir}/openmpi3/lib/pkgconfig/*.pc
%{_libdir}/openmpi3/lib/cmake
%{_libdir}/openmpi3/share/*
%endif

%files -n libdune-common-mpich
%defattr(-,root,root,-)
%{_libdir}/mpich/lib/*.so
%{_libdir}/mpich/bin/*

%files mpich-devel
%defattr(-,root,root,-)
%{_includedir}/mpich-x86_64/dune/*
%{_libdir}/mpich/lib/dune*
%{_libdir}/mpich/lib/pkgconfig/*.pc
%{_libdir}/mpich/lib/cmake
%{_libdir}/mpich/share/*
