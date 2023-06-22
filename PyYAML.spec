#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : PyYAML
Version  : 6.0
Release  : 89
URL      : https://github.com/yaml/pyyaml/archive/6.0/pyyaml-6.0.tar.gz
Source0  : https://github.com/yaml/pyyaml/archive/6.0/pyyaml-6.0.tar.gz
Summary  : YAML parser and emitter for Python
Group    : Development/Tools
License  : MIT
Requires: PyYAML-license = %{version}-%{release}
Requires: PyYAML-python = %{version}-%{release}
Requires: PyYAML-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cython)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pypi-cython
BuildRequires : yaml-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
PyYAML
======
A full-featured YAML processing framework for Python
## Installation

%package license
Summary: license components for the PyYAML package.
Group: Default

%description license
license components for the PyYAML package.


%package python
Summary: python components for the PyYAML package.
Group: Default
Requires: PyYAML-python3 = %{version}-%{release}
Provides: pyyaml-python

%description python
python components for the PyYAML package.


%package python3
Summary: python3 components for the PyYAML package.
Group: Default
Requires: python3-core
Provides: pypi(pyyaml)
Provides: pypi(yaml)

%description python3
python3 components for the PyYAML package.


%prep
%setup -q -n pyyaml-6.0
cd %{_builddir}/pyyaml-6.0
pushd ..
cp -a pyyaml-6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1687467116
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python setup.py test || :

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/PyYAML
cp %{_builddir}/pyyaml-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/PyYAML/3b8919c7f020e71fc3e97cfd724f9463bbac1177 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/PyYAML/3b8919c7f020e71fc3e97cfd724f9463bbac1177

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
