#
# spec file for package opm-common
#

%define tag final
%define rtype release

%if 0%{?_build_versioned} == 1
%define postfix %{version}
%endif

Name:           opm-common
Version:        2025.04
Release:        0
Summary:        Open Porous Media - common helpers and buildsystem
License:        GPL-3.0
Group:          Development/Libraries/C and C++
Url:            http://www.opm-project.org/
Source0:        https://github.com/OPM/%{name}/archive/release/%{version}/%{tag}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-opm-common_disable_data_interregflow.patch
Patch1:         0002-opm-common_remove_ml_tools.patch
BuildRequires:  git doxygen bc latexmk texlive-cm texlive-dvips-bin
BuildRequires:  %{_toolset}
BuildRequires:  boost-devel graphviz dune-common-devel tbb-devel
BuildRequires:  cmake3 python3-devel fmt-devel
BuildRequires:  python3-numpy python3-setuptools_scm python3-pytest-runner python3-decorator

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Open Porous Media (OPM) initiative provides a set of open-source tools centered around the simulation of flow and transport of fluids in porous media. The goal of the initiative is to establish a sustainable environment for the development of an efficient and well-maintained software suite.

%package -n libopm-common%{?postfix}
Summary:        opm-common - library
Group:          System/Libraries

%description -n libopm-common%{?postfix}
This package contains library for opm-common

%package devel
Summary:        Development and header files for opm-common
Group:          Development/Libraries/C and C++
Requires:       libopm-common%{?postfix} = %{version}

%description devel
This package contains the development and header files for opm-common

%package -n python3-opm-common
Summary:        opm-common - python library
Group:          Python/Libraries
Requires:       libopm-common%{?postfix} = %{version}

%description -n python3-opm-common
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
BuildArch:	    noarch

%description doc
This package contains the documentation files for opm-common

%prep
%setup -q -n %{name}-%{rtype}-%{version}-%{tag}
%patch0 -p1
%patch1 -p1

# consider using -DUSE_VERSIONED_DIR=ON if backporting
%build
rm -f python/pybind11/tools/mkdoc.py
mkdir serial
pushd serial
echo $RPM_OPT_FLAGS
scl enable %{_toolset} 'CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" cmake3 -DUSE_MPI=0 -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_DOCDIR=share/doc/%{name}-%{version} -DUSE_RUNPATH=OFF -DWITH_NATIVE=OFF -DOPM_ENABLE_PYTHON=1 -DOPM_ENABLE_EMBEDDED_PYTHON=1 -DOPM_INSTALL_PYTHON=1 ..'
scl enable %{_toolset} 'make %{?_smp_mflags}'
scl enable %{_toolset} 'ctest3 --output-on-failure'
popd

%install
scl enable %{_toolset} 'make install DESTDIR=%{buildroot} -C serial'
scl enable %{_toolset} 'make install-html DESTDIR=%{buildroot} -C serial'

%clean
rm -rf %{buildroot}

%define _unpackaged_files_terminate_build 0

%post -n libopm-common%{?postfix} -p /sbin/ldconfig
%postun -n libopm-common%{?postfix} -p /sbin/ldconfig
%post -n python3-opm-common -p /sbin/ldconfig
%postun -n python3-opm-common -p /sbin/ldconfig

%files
%doc README.md

%files doc
%{_docdir}/*

%files bin
%{_bindir}/*
%{_datadir}/man/*

%files -n libopm-common%{?postfix}
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
/usr/lib/dunecontrol/*
%{_includedir}/*
%{_datadir}/cmake/*
%{_datadir}/opm/*
%{_libdir}/*.so

%files -n python3-opm-common
%{_prefix}/lib/python3.6/site-packages/opm/*
%{_prefix}/lib/python3.6/site-packages/opm_embedded/*
