#
# spec file for package dune-common
#

Name:           dune-common
Version:        2.11.0
Release:        1
Summary:        Distributed and Unified Numerics Environment
License:        GPL-2.0
Group:          Development/Libraries/C and C++
Url:            https://dune-project.org/
Source0:        https://gitlab.dune-project.org/core/dune-common/-/archive/v2.11.0/dune-common-v2.11.0.tar.gz
Patch0:		0001-dune-common-py3.patch
BuildRequires:  blas-devel gpm-devel
BuildRequires:  lapack-devel metis-devel
BuildRequires:  pkgconfig %{_toolset}
BuildRequires:  cmake3 boost-devel suitesparse-devel
%if 0%{?_build_openmpi}
BuildRequires:  openmpi-devel
%endif
%if 0%{?_build_mpich}
BuildRequires:  mpich-devel
%endif
#BuildRequires:  doxygen inkscape graphviz latexmk texlive-bibtex python3-sphinx
#BuildRequires:  texlive-amscls texlive-psfrag texlive-subfigure texlive-metafont
#BuildRequires:  texlive-cm texlive-mfware
BuildRequires:  tbb-devel
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

%if 0%{?_build_openmpi}
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
%endif

%if 0%{?_build_mpich}
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
%endif

%prep
%setup -q -n dune-common-v2.11.0
%patch0 -p1

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

%post -n libdune-common -p /sbin/ldconfig
%postun -n libdune-common -p /sbin/ldconfig

%if 0%{?_build_openmpi}
%post -n libdune-common-openmpi -p /sbin/ldconfig
%postun -n libdune-common-openmpi -p /sbin/ldconfig
%endif

%if 0%{?_build_mpich}
%post -n libdune-common-mpich -p /sbin/ldconfig
%postun -n libdune-common-mpich -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
%doc CHANGELOG.md CONTRIBUTING.md README.md
%license LICENSE.md
%{_bindir}/*
%{_datadir}/dune-common
%{_datadir}/man
%{_datadir}/bash-completion/*

%files doc
%{_docdir}/dune-common/*

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
%if 0%{?_build_openmpi}
%exclude /usr/include/openmpi-x86_64
%endif
%if 0%{?_build_mpich}
%exclude /usr/include/mpich-x86_64
%endif

%if 0%{?_build_openmpi}
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
%endif

%if 0%{?_build_mpich}
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
%endif
