#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : PyYAML
Version  : 3.11
Release  : 17
URL      : https://pypi.python.org/packages/source/P/PyYAML/PyYAML-3.11.tar.gz
Source0  : https://pypi.python.org/packages/source/P/PyYAML/PyYAML-3.11.tar.gz
Summary  : YAML parser and emitter for Python
Group    : Development/Tools
License  : MIT
Requires: PyYAML-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : yaml-dev

%description
PyYAML - The next generation YAML parser and emitter for Python.
To install, type 'python setup.py install'.

%package python
Summary: python components for the PyYAML package.
Group: Default
Provides: pyyaml-python

%description python
python components for the PyYAML package.


%prep
%setup -q -n PyYAML-3.11

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
