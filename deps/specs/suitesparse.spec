%if 0%{?fedora} >= 21 || 0%{?rhel} >= 7
%bcond_without atlas310
%else
%bcond_with atlas310
%endif

%if %{with atlas310}
%global atlaslibs -lsatlas
%else
%global atlaslibs -lcblas -llapack
%endif

%global amd_version 2.4.1
%global amd_version_major 2
%global btf_version 1.2.1
%global btf_version_major 1
%global camd_version 2.4.1
%global camd_version_major 2
%global ccolamd_version 2.9.1
%global ccolamd_version_major 2
%global cholmod_version 3.0.6
%global cholmod_version_major 3
%global colamd_version 2.9.1
%global colamd_version_major 2
%global csparse_version 3.1.4
%global csparse_version_major 3
%global cxsparse_version 3.1.4
%global cxsparse_version_major 3
%global klu_version 1.3.3
%global klu_version_major 1
%global ldl_version 2.2.1
%global ldl_version_major 2
%global rbio_version 2.2.1
%global rbio_version_major 2
%global spqr_version 2.0.1
%global spqr_version_major 2
%global SuiteSparse_config_ver 4.4.4
%global SuiteSparse_config_major 4
%global umfpack_version 5.7.1
%global umfpack_version_major 5
### CHOLMOD can also be compiled to use the METIS library, but it is not
### used here because its licensing terms exclude it from Fedora Extras.
### To compile with METIS, define enable_metis as 1 below.
%global enable_metis 0
### CXSparse is a superset of CSparse, and the two share common header
### names, so it does not make sense to build both. CXSparse is built
### by default, but CSparse can be built instead by defining
### enable_csparse as 1 below.
%global enable_csparse 0

Name:           suitesparse
Version:        4.4.6
Release:        10%{?dist}
Summary:        A collection of sparse matrix libraries

Group:          System Environment/Libraries
License:        (LGPLv2+ or BSD) and LGPLv2+ and GPLv2+
URL:            http://faculty.cse.tamu.edu/davis/suitesparse.html
Source0:        http://faculty.cse.tamu.edu/davis/SuiteSparse/SuiteSparse-4.4.6.tar.gz

%if %{with atlas310}
BuildRequires:  atlas-devel >= 3.10
%else
BuildRequires:  atlas-devel
%endif
BuildRequires:  tbb-devel
BuildRequires:  hardlink
BuildRequires: gcc gcc-c++ make

Obsoletes:      umfpack <= 5.0.1
Obsoletes:      ufsparse <= 2.1.1
Provides:       ufsparse = %{version}-%{release}

%description
suitesparse is a collection of libraries for computations involving sparse
matrices.  The package includes the following libraries:
  AMD                 approximate minimum degree ordering
  BTF                 permutation to block triangular form (beta)
  CAMD                constrained approximate minimum degree ordering
  COLAMD              column approximate minimum degree ordering
  CCOLAMD             constrained column approximate minimum degree ordering
  CHOLMOD             sparse Cholesky factorization
  CSparse             a concise sparse matrix package
  CXSparse            CSparse extended: complex matrix, int and long int support
  KLU                 sparse LU factorization, primarily for circuit simulation
  LDL                 a simple LDL factorization
  SQPR                a multithread, multifrontal, rank-revealing sparse QR
                      factorization method
  UMFPACK             sparse LU factorization
  SuiteSparse_config  configuration file for all the above packages.
  RBio                read/write files in Rutherford/Boeing format


%package devel
Summary:        Development headers for SuiteSparse
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Obsoletes:      umfpack-devel <= 5.0.1
Obsoletes:      ufsparse-devel <= 2.1.1
Provides:       ufsparse-devel = %{version}-%{release}

%description devel
The suitesparse-devel package contains files needed for developing
applications which use the suitesparse libraries.


%package static
Summary:        Static version of SuiteSparse libraries
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}-%{release}
Provides:       ufsparse-static = %{version}-%{release}

%description static
The suitesparse-static package contains the statically linkable
version of the suitesparse libraries.

%package doc
Summary:        Documentation files for SuiteSparse
Group:          Documentation
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description doc
This package contains documentation files for %{name}.


%prep
%setup -q -n SuiteSparse

# Fix pragma ivdep so gcc understands it.
for fil in $(grep -Frl 'pragma ivdep' .); do
  sed -i.orig 's/pragma ivdep/pragma GCC ivdep/' $fil
  touch -r ${fil}.orig $fil
  rm -f ${fil}.orig
done

%build
mkdir -p Doc/{AMD,BTF,CAMD,CCOLAMD,CHOLMOD,COLAMD,KLU,LDL,UMFPACK,SPQR,RBio} Lib Include

# SuiteSparse_config needs to come first
pushd SuiteSparse_config
  make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIC -g"
  ar x libsuitesparseconfig.a
  pushd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libsuitesparseconfig.so.%{SuiteSparse_config_major} -o \
        libsuitesparseconfig.so.%{SuiteSparse_config_ver} ../SuiteSparse_config/*.o -lm
    ln -sf libsuitesparseconfig.so.%{SuiteSparse_config_ver} libsuitesparseconfig.so.%{SuiteSparse_config_major}
    ln -sf libsuitesparseconfig.so.%{SuiteSparse_config_ver} libsuitesparseconfig.so
    cp -p ../SuiteSparse_config/*.a ./
  popd
  cp -p *.h ../Include
popd

pushd AMD
  pushd Lib
    make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIC -g"
  popd
  pushd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libamd.so.%{amd_version_major} -o \
        libamd.so.%{amd_version} ../AMD/Lib/*.o \
        libsuitesparseconfig.so.%{SuiteSparse_config_major} -lm
    ln -sf libamd.so.%{amd_version} libamd.so.%{amd_version_major}
    ln -sf libamd.so.%{amd_version} libamd.so
    cp -p ../AMD/Lib/*.a ./
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/License.txt Doc/lesser.txt Doc/ChangeLog Doc/*.pdf ../Doc/AMD
popd

pushd BTF
  pushd Lib
    make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIC -g"
  popd
  pushd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libbtf.so.%{btf_version_major} -o \
        libbtf.so.%{btf_version} ../BTF/Lib/*.o
    ln -sf libbtf.so.%{btf_version} libbtf.so.%{btf_version_major}
    ln -sf libbtf.so.%{btf_version} libbtf.so
    cp -p ../BTF/Lib/*.a ./
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/* ../Doc/BTF
popd

pushd CAMD
  pushd Lib
    make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIC -g"
  popd
  pushd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libcamd.so.%{camd_version_major} -o \
        libcamd.so.%{camd_version} ../CAMD/Lib/*.o \
        libsuitesparseconfig.so.%{SuiteSparse_config_major} -lm
    ln -sf libcamd.so.%{camd_version} libcamd.so.%{camd_version_major}
    ln -sf libcamd.so.%{camd_version} libcamd.so
    cp -p ../CAMD/Lib/*.a ./
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/ChangeLog Doc/License Doc/*.pdf ../Doc/CAMD
popd

pushd CCOLAMD
  pushd Lib
    make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIC -g"
  popd
  pushd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libccolamd.so.%{ccolamd_version_major} -o \
        libccolamd.so.%{ccolamd_version} ../CCOLAMD/Lib/*.o \
        libsuitesparseconfig.so.%{SuiteSparse_config_major} -lm
    ln -sf libccolamd.so.%{ccolamd_version} libccolamd.so.%{ccolamd_version_major}
    ln -sf libccolamd.so.%{ccolamd_version} libccolamd.so
    cp -p ../CCOLAMD/Lib/*.a ./
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/* ../Doc/CCOLAMD
popd

pushd COLAMD
  pushd Lib
    make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIC -g"
  popd
  pushd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libcolamd.so.%{colamd_version_major} -o \
        libcolamd.so.%{colamd_version} ../COLAMD/Lib/*.o \
        libsuitesparseconfig.so.%{SuiteSparse_config_major} -lm
    ln -sf libcolamd.so.%{colamd_version} libcolamd.so.%{colamd_version_major}
    ln -sf libcolamd.so.%{colamd_version} libcolamd.so
    cp -p ../COLAMD/Lib/*.a ./
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/* ../Doc/COLAMD
popd

%if "%{?enable_metis}" == "1"
CHOLMOD_FLAGS="$RPM_OPT_FLAGS -I%{_includedir}/metis -fPIC -g"
%else
CHOLMOD_FLAGS="$RPM_OPT_FLAGS -DNPARTITION -fPIC -g"
%endif
pushd CHOLMOD
  pushd Lib
    make %{?_smp_mflags} CFLAGS="$CHOLMOD_FLAGS"
  popd
  pushd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libcholmod.so.%{cholmod_version_major} -o \
        libcholmod.so.%{cholmod_version} ../CHOLMOD/Lib/*.o \
        -L%{_libdir}/atlas %{atlaslibs} \
        libamd.so.%{amd_version_major} \
        libcamd.so.%{camd_version_major} libcolamd.so.%{colamd_version_major} \
        libccolamd.so.%{ccolamd_version_major} \
        libsuitesparseconfig.so.%{SuiteSparse_config_major} -lm
    ln -sf libcholmod.so.%{cholmod_version} libcholmod.so.%{cholmod_version_major}
    ln -sf libcholmod.so.%{cholmod_version} libcholmod.so
    cp -p ../CHOLMOD/Lib/*.a ./
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/*.pdf ../Doc/CHOLMOD
  cp -p Cholesky/License.txt ../Doc/CHOLMOD/Cholesky_License.txt
  cp -p Core/License.txt ../Doc/CHOLMOD/Core_License.txt
  cp -p MatrixOps/License.txt ../Doc/CHOLMOD/MatrixOps_License.txt
  cp -p Partition/License.txt ../Doc/CHOLMOD/Partition_License.txt
  cp -p Supernodal/License.txt ../Doc/CHOLMOD/Supernodal_License.txt
popd

%if "%{?enable_csparse}" == "1"
pushd CSparse
  pushd Source
    make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIC -g"
    cp -p cs.h ../../Include
  popd
  pushd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libcsparse.so.%{csparse_version_major} -o \
        libcsparse.so.%{csparse_version} ../CSparse/Source/*.o -lm
    ln -sf libcsparse.so.%{csparse_version} libcsparse.so.%{csparse_version_major}
    ln -sf libcsparse.so.%{csparse_version} libcsparse.so
    cp -p ../CSparse/Source/*.a ./
  popd
  mkdir ../Doc/CSparse/
  cp -p Doc/* ../Doc/CSparse
popd

%else
pushd CXSparse
  pushd Lib
    make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIC -g"
  popd
  pushd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libcxsparse.so.%{cxsparse_version_major} -o \
        libcxsparse.so.%{cxsparse_version} ../CXSparse/Lib/*.o -lm
    ln -sf libcxsparse.so.%{cxsparse_version} libcxsparse.so.%{cxsparse_version_major}
    ln -sf libcxsparse.so.%{cxsparse_version} libcxsparse.so
    cp -p ../CXSparse/Lib/*.a ./
  popd
  cp -p Include/cs.h ../Include
  mkdir ../Doc/CXSparse/
  cp -p Doc/* ../Doc/CXSparse
popd
%endif

pushd KLU
  pushd Lib
    make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIC -g"
  popd
  pushd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libklu.so.%{klu_version_major} -o \
        libklu.so.%{klu_version} ../KLU/Lib/*.o \
        libamd.so.%{amd_version_major} libcolamd.so.%{colamd_version_major} \
        libbtf.so.%{btf_version_major} \
        libsuitesparseconfig.so.%{SuiteSparse_config_major}
    ln -sf libklu.so.%{klu_version} libklu.so.%{klu_version_major}
    ln -sf libklu.so.%{klu_version} libklu.so
    cp -p ../KLU/Lib/*.a ./
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/lesser.txt ../Doc/KLU
popd

pushd LDL
  pushd Lib
    make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIC -g"
  popd
  pushd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libldl.so.%{ldl_version_major} -o \
        libldl.so.%{ldl_version} ../LDL/Lib/*.o
    ln -sf libldl.so.%{ldl_version} libldl.so.%{ldl_version_major}
    ln -sf libldl.so.%{ldl_version} libldl.so
    cp -p ../LDL/Lib/*.a ./
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/ChangeLog Doc/lesser.txt Doc/*.pdf ../Doc/LDL
popd

pushd UMFPACK
  pushd Lib
    make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIC -g"
  popd
  pushd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,libumfpack.so.%{umfpack_version_major} -o \
        libumfpack.so.%{umfpack_version} ../UMFPACK/Lib/*.o \
        -L%{_libdir}/atlas %{atlaslibs} \
        libamd.so.%{amd_version_major} \
        libcholmod.so.%{cholmod_version_major} \
        libsuitesparseconfig.so.%{SuiteSparse_config_major} -lm
    ln -sf libumfpack.so.%{umfpack_version} libumfpack.so.%{umfpack_version_major}
    ln -sf libumfpack.so.%{umfpack_version} libumfpack.so
    cp -p ../UMFPACK/Lib/*.a ./
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/License Doc/ChangeLog Doc/gpl.txt Doc/*.pdf ../Doc/UMFPACK
popd

pushd SPQR
  pushd Lib
    make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -DHAVE_TBB -DNPARTITION -fPIC -g"
  popd
  pushd ../Lib
    g++ -shared %{?__global_ldflags} -Wl,-soname,libspqr.so.%{spqr_version_major} -o \
        libspqr.so.%{spqr_version} ../SPQR/Lib/*.o \
        -L%{_libdir}/atlas -L%{_libdir} %{atlaslibs} \
        -ltbb \
        libcholmod.so.%{cholmod_version_major} \
        libsuitesparseconfig.so.%{SuiteSparse_config_major} -lm
    ln -sf libspqr.so.%{spqr_version} libspqr.so.%{spqr_version_major}
    ln -sf libspqr.so.%{spqr_version} libspqr.so
    cp -p ../SPQR/Lib/*.a ./
  popd
  cp -p Include/*.h* ../Include
  cp -p README{,_SPQR}.txt
  cp -p README_SPQR.txt Doc/* ../Doc/SPQR
popd

pushd RBio
  pushd Lib
    make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -fPIC -g"
  popd
  pushd ../Lib
    gcc -shared %{?__global_ldflags} -Wl,-soname,librbio.so.%{rbio_version_major} -o \
        librbio.so.%{rbio_version} ../RBio/Lib/*.o \
        libsuitesparseconfig.so.%{SuiteSparse_config_major}
    ln -sf librbio.so.%{rbio_version} librbio.so.%{rbio_version_major}
    ln -sf librbio.so.%{rbio_version} librbio.so
    cp -p ../RBio/Lib/*.a ./
  popd
  cp -p Include/*.h ../Include
  cp -p README.txt Doc/ChangeLog Doc/License.txt ../Doc/RBio
popd

%install
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}/%{name}
pushd Lib
  for f in *.a *.so*; do
    cp -a $f ${RPM_BUILD_ROOT}%{_libdir}/$f
  done
popd
chmod 755 ${RPM_BUILD_ROOT}%{_libdir}/*.so.*
pushd Include
  for f in *.h *.hpp;  do
    cp -a $f ${RPM_BUILD_ROOT}%{_includedir}/%{name}/$f
  done
popd

# collect licenses in one place to ship as base package documentation
rm -rf Licenses
mkdir Licenses
find */ -iname lesser.txt -o -iname license.txt -o -iname gpl.txt -o \
    -iname license | while read f; do
        b="${f%%/*}"
        r="${f#$b}"
        x="$(echo "$r" | sed 's|/doc/|/|gi')"
        install -m0644 -D "$f" "./Licenses/$b/$x"
    done

# hardlink duplicate documentation files
hardlink -cv Docs/ Licenses/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license Licenses
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib*.so

%files static
%{_libdir}/lib*.a

%files doc
%doc Doc/*

%changelog
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 07 2016 Dan Horák <dan[at]danny.cz> - 4.4.6-7
- Rebuild with fixed tbb on s390x (#1379632)

* Thu Sep 22 2016 Jerry James <loganjerry@gmail.com> - 4.4.6-6
- Rebuild for tbb 2017
- tbb is available for all arches now

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jerry James <loganjerry@gmail.com> - 4.4.6-4
- Rebuild for tbb 4.4u2

* Mon Jan 4 2016 Orion Poplawski <orion@cora.nwra.com> - 4.4.6-3
- Use %%{?__global_ldflags} when linking

* Mon Jan 4 2016 Orion Poplawski <orion@cora.nwra.com> - 4.4.6-2
- Update to 4.4.6

* Wed Aug 26 2015 Nils Philippsen <nils@redhat.com> - 4.4.5-2
- AMD is dual-licensed (LGPLv2+ or BSD)

* Wed Aug 26 2015 Nils Philippsen <nils@redhat.com> - 4.4.5-1
- version 4.4.5
- use %%license for licenses

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Nils Philippsen <nils@redhat.com> - 4.4.4-1
- update component versions

* Wed Jun 10 2015 Nils Philippsen <nils@redhat.com> - 4.4.4-1
- version 4.4.4
- fix URLs
- remove obsolete patches
- drop specifying and cleaning of buildroot

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.3.1-5
- Rebuilt for GCC 5 C++11 ABI change

* Tue Oct 14 2014 Peter Robinson <pbrobinson@fedoraproject.org> 4.3.1-4
- Only s390 doesn't have tbb

* Mon Sep 15 2014 Orion Poplawski <orion@cora.nwra.com> - 4.3.1-3
- Change patch to move math.h include into SuiteSparse_config.c
- Fix linkage and library file permission issues

* Sat Sep 13 2014 Orion Poplawski <orion@cora.nwra.com> - 4.3.1-2
- Add patch to allow octave compilation

* Mon Sep 08 2014 Clément David <c.david86@gmail.com> - 4.3.1-1
- Update to release 4.3.1.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Nils Philippsen <nils@redhat.com> - 4.2.2-2
- ship licenses as documentation in the base package
- hardlink duplicate documentation/license files

* Thu Dec 05 2013 Nils Philippsen <nils@redhat.com> - 4.2.1-1
- version 4.2.1

* Fri Sep 20 2013 Nils Philippsen <nils@redhat.com> - 4.0.2-7
- build against atlas 3.10.x

* Tue Sep 03 2013 Nils Philippsen <nils@redhat.com> - 4.0.2-6
- include C++ headers (#1001943)
- fix bogus dates in changelog

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 24 2013 Petr Machata <pmachata@redhat.com> - 4.0.2-4
- Rebuild for TBB memory barrier bug

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Nils Philippsen <nils@redhat.com> - 4.0.2-2
- explicitly link libsuitesparseconfig where necessary

* Fri Nov 16 2012 Deji Akingunola <dakingun@gmail.com> - 4.0.2-1
- Update to 4.0.2

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 11 2011 Dan Horák <dan[at]danny.cz> - 3.6.1-2
- fix build without TBB

* Fri Sep 23 2011 Deji Akingunola <dakingun@gmail.com> - 3.6.1-1
- Update to 3.6.1
- Fix undefine symbols in libspqr

* Sun Feb 13 2011 Deji Akingunola <dakingun@gmail.com> - 3.6.0-3
- Fix a couple of undefined reference errors in umfpack and Rbio (#677061)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Deji Akingunola <dakingun@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 28 2009 Deji Akingunola <dakingun@gmail.com> - 3.4.0-1
- Update to version 3.4.0.

* Tue May 19 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 3.3.0-2
- Split documentation into separate -doc subpackage (resolves BZ#492451).

* Mon Apr 27 2009 Deji Akingunola <dakingun@gmail.com> - 3.3.0-1
- Update to release 3.3.0.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Deji Akingunola <dakingun@gmail.com> - 3.2.0-5
- More fixes for the undefined symbol issue (BZ #475411)

* Sat Dec 20 2008 Deji Akingunola <dakingun@gmail.com> - 3.2.0-4
- Also build SPQR
- Further fixes for BZ #475411

* Wed Dec 17 2008 Deji Akingunola <dakingun@gmail.com> - 3.2.0-3
- Rearrange the spec
- Link in necessary libs when making shared CHOLMOD lib (BZ #475411)
- Link with ATLAS' blas and lapack libs

* Wed Dec 17 2008 Deji Akingunola <dakingun@gmail.com> - 3.2.0-2
- Rebuild for updated atlas

* Mon Dec 15 2008 Deji Akingunola <dakingun@gmail.com> - 3.2.0-1
- New upstream version

* Mon Mar  3 2008 Quentin Spencer <qspencer@users.sourceforge.net> 3.1.0-1
- Update to release 3.1.0.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.0.0-4
- Autorebuild for GCC 4.3

* Tue Oct 16 2007 Quentin Spencer <qspencer@users.sourceforge.net> 3.0.0-3
- Update license tag. Fix minor issues found by rpmlint.

* Fri Aug 24 2007 Quentin Spencer <qspencer@users.sourceforge.net> 3.0.0-2
- Rebuild for F8.

* Tue Jul  3 2007 Quentin Spencer <qspencer@users.sourceforge.net> 3.0.0-1
- Change package name to match upstream, including provides and obsoletes.
- New release. Numerous changes in build to reflect source reorganization.
- Moved static libs into separate package.

* Mon Oct 16 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.1.1-1
- New release, and package name change from UFsparse to SuiteSparse. Fixes
  bug #210846. Keep the ufsparse package name for now.

* Thu Sep  7 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.1.0-1
- New release. Increment versions of some libraries.
- Rearrange and clean up spec file so all definitions are in one place.

* Mon Aug  7 2006 Quentin Spencer <qspencer@users.sourceforge.net> 2.0.0-1
- New release.
- Build newly added CAMD library.
- Misc minor spec changes.

* Tue Mar  7 2006 Quentin Spencer <qspencer@users.sourceforge.net> 1.2-1
- New release.
- Build newly added library CXSparse (but not CSparse--see comments
  in build section).

* Wed Feb 15 2006 Quentin Spencer <qspencer@users.sourceforge.net> 0.93-2
- Rebuild for Fedora Extras 5.

* Thu Feb  9 2006 Quentin Spencer <qspencer@users.sourceforge.net> 0.93-1
- New release. Remove old patch.

* Wed Dec 14 2005 Quentin Spencer <qspencer@users.sourceforge.net> 0.92-2
- Add patch0--fixes LDL/Makefile so CFLAGS are used when compiling ldl.a.

* Wed Dec 14 2005 Quentin Spencer <qspencer@users.sourceforge.net> 0.92-1
- Update to Dec 8 2005 version.

* Tue Oct 25 2005 Quentin Spencer <qspencer@users.sourceforge.net> 0.91-2
- Rebuild.

* Tue Oct 18 2005 Quentin Spencer <qspencer@users.sourceforge.net> 0.91-1
- New upstream release, incorporating previous patches
- chmod the build directory to ensure all headers are world readable

* Fri Oct 07 2005 Quentin Spencer <qspencer@users.sourceforge.net> 0.9-3
- Build cholmod, but disable METIS using -DNPARTITION flag.

* Sat Oct 01 2005 Quentin Spencer <qspencer@users.sourceforge.net> 0.9-2
- Modify description, other modifications for import into FE.
- Add dist tag, cosmetic changes.

* Thu Sep 08 2005 David Bateman <dbateman@free.fr> 0.9-1
- First version.
