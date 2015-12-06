%global modname pacpy

Name:           python-pacpy
Version:        1.0.1
Release:        1%{?dist}
Summary:        Calculate phase-amplitude coupling in Python

License:        MIT
URL:            https://github.com/voytekresearch/pacpy
Source0:        https://github.com/voytekresearch/pacpy/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
A module to calculate phase-amplitude coupling in Python.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel python2-setuptools
BuildRequires:  python2-pytest
%if 0%{?fedora} > 23
BuildRequires:  python2-numpy python2-scipy
Requires:       python2-numpy python2-scipy
%else
BuildRequires:  numpy scipy
Requires:       numpy scipy
%endif

%description -n python2-%{modname}
A module to calculate phase-amplitude coupling in Python.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-numpy python3-scipy
Requires:       python3-numpy python3-scipy

%description -n python3-%{modname}
A module to calculate phase-amplitude coupling in Python.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
pushd %{modname}/tests
  PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} -v
  PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v
popd

%files -n python2-%{modname}
%license LICENSE.md
%doc README.md
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%license LICENSE.md
%doc README.md
%{python3_sitelib}/%{modname}*

%changelog
* Sun Dec 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.1-1
- Initial package
