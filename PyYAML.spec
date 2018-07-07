#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : PyYAML
Version  : 3.13
Release  : 41
URL      : http://pypi.debian.net/PyYAML/PyYAML-3.13.tar.gz
Source0  : http://pypi.debian.net/PyYAML/PyYAML-3.13.tar.gz
Summary  : YAML parser and emitter for Python
Group    : Development/Tools
License  : MIT
Requires: PyYAML-python3
Requires: PyYAML-license
Requires: PyYAML-python
BuildRequires : Cython
BuildRequires : Cython-legacypython
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-core
BuildRequires : python-dev
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : yaml-dev

%description
and interaction with scripting languages.  PyYAML is a YAML parser
        and emitter for Python.
        
        PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
        support, capable extension API, and sensible error messages.  PyYAML
        supports standard YAML tags and provides Python-specific tags that
        allow to represent an arbitrary Python object.
        
        PyYAML is applicable for a broad range of tasks from complex
        configuration files to object serialization and persistance.

%package legacypython
Summary: legacypython components for the PyYAML package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the PyYAML package.


%package license
Summary: license components for the PyYAML package.
Group: Default

%description license
license components for the PyYAML package.


%package python
Summary: python components for the PyYAML package.
Group: Default
Requires: PyYAML-python3
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
%setup -q -n PyYAML-3.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530988711
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python setup.py test
%install
export SOURCE_DATE_EPOCH=1530988711
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/PyYAML
cp LICENSE %{buildroot}/usr/share/doc/PyYAML/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/PyYAML/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
