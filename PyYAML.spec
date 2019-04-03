#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : PyYAML
Version  : 5.1
Release  : 50
URL      : https://github.com/yaml/pyyaml/archive/5.1.tar.gz
Source0  : https://github.com/yaml/pyyaml/archive/5.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: PyYAML-license = %{version}-%{release}
Requires: PyYAML-python = %{version}-%{release}
Requires: PyYAML-python3 = %{version}-%{release}
BuildRequires : Cython
BuildRequires : buildreq-distutils3
BuildRequires : deprecated-Cython-legacypython
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : yaml-dev

%description
PyYAML - The next generation YAML parser and emitter for Python.
To install, type 'python setup.py install'.

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

%description python3
python3 components for the PyYAML package.


%prep
%setup -q -n pyyaml-5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554327553
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/PyYAML
cp LICENSE %{buildroot}/usr/share/package-licenses/PyYAML/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/PyYAML/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
