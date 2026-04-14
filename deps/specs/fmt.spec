Name:           fmt
Version:        11.0.2
Release:        0

License:        BSD
Summary:        Small, safe and fast formatting library for C++
URL:            https://github.com/fmtlib/%{name}
Source0:        https://github.com/fmtlib/fmt/archive/11.0.2.tar.gz

BuildRequires:  cmake3 %{_toolset}

# This package replaces the old name of cppformat
Provides:       cppformat = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      cppformat < %{?epoch:%{epoch}:}%{version}-%{release}

%description
C++ Format is an open-source formatting library for C++. It can be used as a
safe alternative to printf or as a fast alternative to IOStreams.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

# This package replaces the old name of cppformat
Provides:       cppformat-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      cppformat-devel < %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel
This package contains the header file for using %{name}.

%global debug_package %{nil}

%undefine __brp_strip_static_archive

%prep
%autosetup -p1

%build
mkdir build
cd build
scl enable %{_toolset} 'cmake3 .. -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON -DFMT_CMAKE_DIR:STRING=%{_libdir}/cmake/%{name} -DBUILD_SHARED_LIBS=0 -DFMT_LIB_DIR:STRING=%{_libdir} -DCMAKE_INSTALL_PREFIX=/usr'
scl enable %{_toolset} 'make %{?_smp_mflags}'

%install
cd build
scl enable %{_toolset} 'make install DESTDIR=%{buildroot}'

%check
cd build
scl enable %{_toolset} 'make test'

%files
%license LICENSE
%doc ChangeLog.md README.md

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.a
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc
