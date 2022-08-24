Name:           bello
Version:        0.1 
Release:        1%{?dist}
Summary:        bash software print hello 

License:        GPLv3+ 
URL:            https://example.com/bello
Source0:        https://example.com/bello/releases/bello-0.1.tar.gz

Requires:       bash 

BuildArch:      noarch
%description
bash software print hello

%prep
%setup -q


%build


%install
mkdir -p %{buildroot}/%{_bindir}

install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}


%files
%license LICENSE
%{_bindir}/%{name}



%changelog
* Wed Aug 24 2022 FengtuWang 
- First bello package
- Example second item in the changelog for version-release 0.1-1
