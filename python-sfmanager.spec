%global commit    master
%global owner     redhat-cip
%global srcname   python-sfmanager

Name:          python-sfmanager
Version:       1.0.0
Release:       1%{?dist}
Summary:       Software Factory managesf client

License:       APACHE
URL:           https://softwarefactory-project.io/r/python-sfmanager
Source0:       https://github.com/redhat-cip/python-sfmanager/archive/master.zip
BuildArch:     noarch

BuildRequires: python2-devel

Requires: python-requests
Requires: python-crypto
Requires: python-urllib3

%description
This client allow managing software factory deployment.

#%package doc
#Summary:       Documentation of the Advanced Python Scheduler library

#Requires:      %{name}%{?_isa} = %{version}-%{release}
#Provides:      bundled(jquery) = 1.8.3
#BuildRequires: python-sphinx

#%description doc
#Documentation of the Software Factory managesf client


%prep
%setup -q -n %{srcname}-%{commit}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%{__python} setup.py build
# generate html docs
#%{__python} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf docs/_build/html/.{doctrees,buildinfo} docs/_build/html/objects.inv


%install
%{__python} setup.py install --skip-build --root %{buildroot}

#%check
#nosetests ./tests/


%files
%doc README.md
%license LICENSE
%{python_sitelib}/sfmanager
%{python_sitelib}/sfmanager-*.egg-info
/usr/bin/sfmanager
/usr/share/man/man1/sfmanager.1.gz
#%files doc
#%doc docs/_build/html

%changelog
* Fri Dec 11 2015 Tristan de Cacqueray <tdecacqu@redhat.com> - 1.0.0.fc23
- Initial packaging
