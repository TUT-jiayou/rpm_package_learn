Name:           pello
Version:        0.1.1 
Release:        1%{?dist}
Summary:        Hello World example implemented in Python 

License:        GPLV+3 
URL:            https://example.com/%{name}
Source0:        https://example.com/%{name}/release/%{name}-%{version}.tar.gz

BuildRequires:  python3 
Requires:       python3
Requires:       bash

BuildArch:      noarch
%description
 Hello World example implemented in Python

%prep
%setup -q


%build
python3 -m compileall pello.py


%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/usr/lib/%{name}

cat > %{buildroot}/%{_bindir}/%{name} <<-EOF

#!/bin/bash
/usr/bin/python3 /usr/lib/%{name}/%{name}.py
EOF

chmod 0755 %{buildroot}/%{_bindir}/%{name}
install -m 0755 %{name}.py %{buildroot}/usr/lib/%{name}/ 

%files
%license LICENSE
%dir /usr/lib/%{name}/
%dir /usr/lib/%{name}/__pycache__/
%{_bindir}/%{name}
/usr/lib/%{name}/%{name}.py
/usr/lib/%{name}/__pycache__/*.pyc



%changelog
* Wed Aug 24 2022 FengtuWang 
- First pello package
- Example second item in the changelog for version-release 0.1.1-1
