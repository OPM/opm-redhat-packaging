
# spec file for package dune-localfunctions
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           dune-localfunctions
Version:        2.8.0
Release:        0
Summary:        An interface and implementation for shape functions defined on the DUNE
License:        GPL-2.0
Group:          Development/Libraries/C and C++
Url:            http://www.dune-project.org/
Source0:        https://dune-project.org/download/2.8.0/dune-localfunctions-2.8.0.tar.gz
BuildRequires:  dune-common-devel dune-common-openmpi-devel
BuildRequires:  dune-common-openmpi3-devel dune-common-mpich-devel
BuildRequires:  dune-geometry-devel dune-geometry-openmpi-devel
BuildRequires:  dune-geometry-openmpi3-devel dune-geometry-mpich-devel
BuildRequires:  dune-grid-devel dune-grid-openmpi-devel
BuildRequires:  dune-grid-openmpi3-devel dune-grid-mpich-devel
BuildRequires:  pkgconfig devtoolset-9-toolchain
BuildRequires:  cmake3 boost-devel metis-devel
BuildRequires:  openmpi-devel mpich-devel openmpi3-devel
BuildRequires:  doxygen inkscape graphviz
BuildRequires:  tbb-devel python3-sphinx latexmk
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
dune-localfunctions provides interface and implementation for shape functions
defined on the DUNE reference elements. In addition to the shape function,
interpolation operators and special keys are provided which can be used to
assemble global function spaces on finite-element localfunctionss.

%package devel
Summary:        Development and header files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       dune-common-devel = %{version}
Requires:       dune-geometry-devel = %{version}
Requires:       dune-grid-devel = %{version}

%description devel
This package contains the development and header files for %{name}.

%package doc
Summary:        Doxygen documentation for %{name}
Group:          Documentation
BuildArch:      noarch

%description doc
This package contains the doxygen documentation for %{name}.

%package openmpi-devel
Summary:        Development and header files for %{name} - openmpi version
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       dune-common-openmpi-devel = %{version}
Requires:       dune-geometry-openmpi-devel = %{version}
Requires:       dune-grid-openmpi-devel = %{version}

%description openmpi-devel
This package contains the development and header files for %{name} - openmpi version.

%package openmpi3-devel
Summary:        Development and header files for %{name} - openmpi3 version
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       dune-common-openmpi3-devel = %{version}
Requires:       dune-geometry-openmpi3-devel = %{version}
Requires:       dune-grid-openmpi3-devel = %{version}

%description openmpi3-devel
This package contains the development and header files for %{name} - openmpi3 version.

%package mpich-devel
Summary:        Development and header files for %{name} - mpich version
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       dune-common-mpich-devel = %{version}
Requires:       dune-geometry-mpich-devel = %{version}
Requires:       dune-grid-mpich-devel = %{version}

%description mpich-devel
This package contains the development and header files for %{name} - openmpi3 version.

%global debug_package %{nil}

%prep
%setup -q

%build
mkdir serial
pushd serial
scl enable devtoolset-9 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1'
make %{?_smp_mflags}
popd

mkdir openmpi
pushd openmpi
module load mpi/openmpi-x86_64
scl enable devtoolset-9 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/openmpi -DCMAKE_INSTALL_INCLUDEDIR=/usr/include/openmpi-x86_64 -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1 -DCMAKE_INSTALL_LIBDIR=lib'
scl enable devtoolset-9 'make %{?_smp_mflags}'
module unload mpi/openmpi-x86_64
popd

mkdir openmpi3
pushd openmpi3
module load mpi/openmpi3-x86_64
scl enable devtoolset-9 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/openmpi3 -DCMAKE_INSTALL_INCLUDEDIR=/usr/include/openmpi3-x86_64 -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1 -DCMAKE_INSTALL_LIBDIR=lib'
scl enable devtoolset-9 'make %{?_smp_mflags}'
module unload mpi/openmpi3-x86_64
popd

mkdir mpich
pushd mpich
module load mpi/mpich-x86_64
scl enable devtoolset-9 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 .. -DCMAKE_INSTALL_PREFIX=%{_prefix}/lib64/mpich -DCMAKE_INSTALL_INCLUDEDIR=/usr/include/mpich-x86_64 -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=1 -DCMAKE_INSTALL_LIBDIR=lib'
scl enable devtoolset-9 'make %{?_smp_mflags}'
module unload mpi/mpich-x86_64
popd

%install
rm -rf %{buildroot}
scl enable devtoolset-9 'make install DESTDIR=%{buildroot} -C serial'
scl enable devtoolset-9 'make install DESTDIR=%{buildroot} -C openmpi'
scl enable devtoolset-9 'make install DESTDIR=%{buildroot} -C openmpi3'
scl enable devtoolset-9 'make install DESTDIR=%{buildroot} -C mpich'
rm -rf %{buildroot}/usr/lib64/openmpi/share/doc
rm -rf %{buildroot}/usr/lib64/openmpi3/share/doc
rm -rf %{buildroot}/usr/lib64/mpich/share/doc

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README.md

%files devel
%defattr(-,root,root,-)
%{_includedir}/dune/localfunctions
%{_datadir}/dune-localfunctions
%{_prefix}/lib/cmake
%{_prefix}/lib/pkgconfig/*.pc
%{_prefix}/lib/dunecontrol/%{name}
%exclude /usr/include/openmpi-x86_64
%exclude /usr/include/openmpi3-x86_64
%exclude /usr/include/mpich-x86_64

%files doc
%{_datadir}/doc/*

%files openmpi-devel
%defattr(-,root,root,-)
%{_includedir}/openmpi-x86_64/dune/localfunctions
%{_libdir}/openmpi/share/dune-localfunctions
%{_libdir}/openmpi/lib/cmake
%{_libdir}/openmpi/lib/pkgconfig/*.pc
%{_libdir}/openmpi/lib/dunecontrol/%{name}

%files openmpi3-devel
%defattr(-,root,root,-)
%{_includedir}/openmpi3-x86_64/dune/localfunctions
%{_libdir}/openmpi3/share/dune-localfunctions
%{_libdir}/openmpi3/lib/cmake
%{_libdir}/openmpi3/lib/pkgconfig/*.pc
%{_libdir}/openmpi3/lib/dunecontrol/%{name}

%files mpich-devel
%defattr(-,root,root,-)
%{_includedir}/mpich-x86_64/dune/localfunctions
%{_libdir}/mpich/share/dune-localfunctions
%{_libdir}/mpich/lib/cmake
%{_libdir}/mpich/lib/pkgconfig/*.pc
%{_libdir}/mpich/lib/dunecontrol/%{name}
