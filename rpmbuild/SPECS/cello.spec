Name:           cello
Version:        1.0 
Release:        1%{?dist}
Summary:        Hello World example implemented in C

License:        GPLv3+
URL:            https://example.com/%{name}
Source0:        https://example.com/%{name}/release/%{name}-%{version}.tar.gz
Patch0:         cello-output-first-patch.patch
BuildRequires:  gcc
BuildRequires:  make

%description
Hello World example implemented in C

%prep
%setup -q
%patch0

%build
make %{?_smp_mflags}

%install
%make_install


%files
%license LICENSE
%{_bindir}/%{name}



%changelog
* Wed Aug 24 2022 FengtuWang    1.0-3
- First cello package
- Add patch 0
