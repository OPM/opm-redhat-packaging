%global pypiname decorator
%global python3_12_sitelib %{_prefix}/lib/python3.12/site-packages

Name:           python3.12-%{pypiname}
Version:        5.3.1
Release:        0
Summary:        Better living through Python with decorators

License:        BSD
URL:            https://github.com
Source0:        https://files.pythonhosted.org/packages/60/8b/32f9823da46cde7df2087faa08cd98d01b908f8dcab982cdba9c84e85355/decorator-5.3.1.tar.gz

BuildArch:      noarch
BuildRequires:  python3.12-devel %{_toolset}
BuildRequires:  python3.12-setuptools python3.12-pip python3.12-wheel

# Ensure this package targets the specific Python 3.12 runtime environment
Requires:       python3.12

%description
The aim of the decorator module is to simplify the usage of decorators
for the average programmer, and to popularize decorators by showing
various use cases.

%prep
%autosetup -n %{pypiname}-%{version}

%build
# NOP

%install
scl enable %{_toolset} '/usr/bin/python3.12 -m pip install . \
    --root=%{buildroot} \
    --no-deps \
    --no-index \
    --no-compile \
    --no-build-isolation \
    --ignore-installed'

scl enable %{_toolset} '/usr/bin/python3.12 -m compileall %{buildroot}%{python3_12_sitelib}'

ls -R %{buildroot}%{python3_12_sitelib}

%files
%doc README.rst
%license LICENSE.txt
# Target the new directory layout instead of the old flat file layout
%{python3_12_sitelib}/%{pypiname}/
%{python3_12_sitelib}/%{pypiname}-%{version}.dist-info/
