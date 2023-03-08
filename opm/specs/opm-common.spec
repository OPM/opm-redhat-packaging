#
# spec file for package opm-common
#

%define tag final
%define rtype release
%define toolset devtoolset-9

Name:           opm-common
Version:        2022.10
Release:        0
Summary:        Open Porous Media - common helpers and buildsystem
License:        GPL-3.0
Group:          Development/Libraries/C and C++
Url:            http://www.opm-project.org/
Source0:        https://github.com/OPM/%{name}/archive/release/%{version}/%{tag}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  git doxygen bc latexmk texlive-cm texlive-dvips-bin
BuildRequires: %{toolset}-toolchain
BuildRequires: boost-devel graphviz dune-common-devel tbb-devel
BuildRequires: cmake3 python3-devel python36-numpy
BuildRequires: python36-setuptools_scm python36-pytest-runner

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Open Porous Media (OPM) initiative provides a set of open-source tools centered around the simulation of flow and transport of fluids in porous media. The goal of the initiative is to establish a sustainable environment for the development of an efficient and well-maintained software suite.

%package -n libopm-common
Summary: OPM-common - library
Group:          System/Libraries

%description -n libopm-common
This package contains library for opm-common

%package -n libopm-common%{version}
Summary: OPM-common - library
Group:          System/Libraries

%description -n libopm-common%{version}
This package contains library for opm-common

%package devel
Summary:        Development and header files for opm-common
Group:          Development/Libraries/C and C++
Requires:       libopm-common = %{version}

%description devel
This package contains the development and header files for opm-common

%package -n python3-opm-common
Summary: OPM-common - python library
Group:          Python/Libraries
Requires:       libopm-common = %{version}

%description -n python3-opm-common
This package contains the python library for opm-common

%package -n python3-opm-common%{version}
Summary: OPM-common - python library
Group:          Python/Libraries
Requires:       libopm-common%{version} = %{version}

%description -n python3-opm-common%{version}
This package contains the python library for opm-common

%package bin
Summary:        Applications for opm-common
Group:          System/Binaries
Requires:       %{name} = %{version}

%description bin
This package the applications for opm-common

%package doc
Summary:        Documentation files for opm-common
Group:          Documentation
BuildArch:	noarch

%description doc
This package contains the documentation files for opm-common

%prep
%setup -q -n %{name}-%{rtype}-%{version}-%{tag}

# consider using -DUSE_VERSIONED_DIR=ON if backporting
%build
rm -f python/pybind11/tools/mkdoc.py
mkdir serial
pushd serial
scl enable %{toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 -DUSE_MPI=0 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_DOCDIR=share/doc/%{name}-%{version} -DUSE_RUNPATH=OFF -DWITH_NATIVE=OFF -DOPM_ENABLE_PYTHON=1 -DOPM_ENABLE_EMBEDDED_PYTHON=1 -DOPM_INSTALL_PYTHON=1 ..'
scl enable %{toolset} 'make %{?_smp_mflags}'
#scl enable %{toolset} 'make test'
popd

%install
scl enable %{toolset} 'make install DESTDIR=%{buildroot} -C serial'
scl enable %{toolset} 'make install-html DESTDIR=%{buildroot} -C serial'

%clean
rm -rf %{buildroot}

%define _unpackaged_files_terminate_build 0

%post -n libopm-common -p /sbin/ldconfig
%postun -n libopm-common -p /sbin/ldconfig
%post -n libopm-common%{version} -p /sbin/ldconfig
%postun -n libopm-common%{version} -p /sbin/ldconfig
%post -n python3-opm-common -p /sbin/ldconfig
%postun -n python3-opm-common -p /sbin/ldconfig
%post -n python3-opm-common%{version} -p /sbin/ldconfig
%postun -n python3-opm-common%{version} -p /sbin/ldconfig

%files
%doc README.md

%files doc
%{_docdir}/*

%files bin
%{_bindir}/*
%{_datadir}/man/*

%files -n libopm-common
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files -n libopm-common%{version}
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
/usr/lib/dunecontrol/*
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/cmake/*
%{_datadir}/opm/*
%{_libdir}/*.so

%files -n python3-opm-common
%{_prefix}/lib/python3.6/site-packages/opm/*

%files -n python3-opm-common%{version}
%{_prefix}/lib/python3.6/site-packages/opm/*
