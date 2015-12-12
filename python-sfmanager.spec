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

%prep
%setup -q -n %{srcname}-%{commit}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%doc README.md
%license LICENSE
%{python_sitelib}/sfmanager
%{python_sitelib}/sfmanager-*.egg-info
/usr/bin/sfmanager
/usr/share/man/man1/sfmanager.1.gz

%changelog
* Mon Feb 01 2016 Tristan de Cacqueray <tdecacqu@redhat.com> - 1.0.0.fc23
- Initial packaging
