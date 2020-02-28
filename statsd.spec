#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : statsd
Version  : 3.3.0
Release  : 9
URL      : https://files.pythonhosted.org/packages/2d/f2/48ffc8d0051849e4417e809dc9420e76084c8a62749b3442915402127caa/statsd-3.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/2d/f2/48ffc8d0051849e4417e809dc9420e76084c8a62749b3442915402127caa/statsd-3.3.0.tar.gz
Summary  : A network daemon for aggregating statistics
Group    : Development/Tools
License  : MIT
Requires: statsd-license = %{version}-%{release}
Requires: statsd-python = %{version}-%{release}
Requires: statsd-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : nose
BuildRequires : python-mock

%description
======================
A Python statsd client
======================

statsd_ is a friendly front-end to Graphite_. This is a Python client
for the statsd daemon.

.. image:: https://travis-ci.org/jsocol/pystatsd.png?branch=master
   :target: https://travis-ci.org/jsocol/pystatsd
   :alt: Travis-CI build status

.. image:: https://img.shields.io/pypi/v/statsd.svg
   :target: https://pypi.python.org/pypi/statsd/
   :alt: Latest release

.. image:: https://img.shields.io/pypi/pyversions/statsd.svg
   :target: https://pypi.python.org/pypi/statsd/
   :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/wheel/statsd.svg
   :target: https://pypi.python.org/pypi/statsd/
   :alt: Wheel Status

:Code:          https://github.com/jsocol/pystatsd
:License:       MIT; see LICENSE file
:Issues:        https://github.com/jsocol/pystatsd/issues
:Documentation: https://statsd.readthedocs.io/

Quickly, to use:

.. code-block:: python

    >>> import statsd
    >>> c = statsd.StatsClient('localhost', 8125)
    >>> c.incr('foo')  # Increment the 'foo' counter.
    >>> c.timing('stats.timed', 320)  # Record a 320ms 'stats.timed'.

You can also add a prefix to all your stats:

.. code-block:: python

    >>> import statsd
    >>> c = statsd.StatsClient('localhost', 8125, prefix='foo')
    >>> c.incr('bar')  # Will be 'foo.bar' in statsd/graphite.


Installing
==========

The easiest way to install statsd is with pip!

You can install from PyPI::

    $ pip install statsd

Or GitHub::

    $ pip install -e git+https://github.com/jsocol/pystatsd#egg=statsd

Or from source::

    $ git clone https://github.com/jsocol/pystatsd
    $ cd statsd
    $ python setup.py install


Docs
====

There are lots of docs in the ``docs/`` directory and on ReadTheDocs_.


.. _statsd: https://github.com/etsy/statsd
.. _Graphite: https://graphite.readthedocs.io/
.. _ReadTheDocs: https://statsd.readthedocs.io/en/latest/index.html

%package license
Summary: license components for the statsd package.
Group: Default

%description license
license components for the statsd package.


%package python
Summary: python components for the statsd package.
Group: Default
Requires: statsd-python3 = %{version}-%{release}

%description python
python components for the statsd package.


%package python3
Summary: python3 components for the statsd package.
Group: Default
Requires: python3-core
Provides: pypi(statsd)

%description python3
python3 components for the statsd package.


%prep
%setup -q -n statsd-3.3.0
cd %{_builddir}/statsd-3.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582916057
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/statsd
cp %{_builddir}/statsd-3.3.0/LICENSE %{buildroot}/usr/share/package-licenses/statsd/38d12aa5966784f0ee6a595a274ef0b8ea46945e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/statsd/38d12aa5966784f0ee6a595a274ef0b8ea46945e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
