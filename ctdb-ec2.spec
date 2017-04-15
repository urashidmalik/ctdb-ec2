Summary: EC2 support for Clustered Database based on Samba Trivial Database
Name: ctdb-ec2
Version: 1.3
Release: 1%{?dist}
License: GPLv3+
Group: System Environment/Daemons
URL: https://github.com/zeichenanonym/ctdb-ec2
Source0: %{name}-%{version}.tar.gz
Requires: ctdb >= 4.4.3
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
EC2 support for Clustered Database based on Samba Trivial Database

%prep
%setup -q -n %{name}-%{version}

%build
make all

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_sysconfdir}/ctdb

%{__install} -p -m 0644 ec2.rc %{buildroot}%{_sysconfdir}/ctdb
%{__install} -p -m 0644 ec2-eni-functions %{buildroot}%{_sysconfdir}/ctdb
%{__install} -p -m 0644 ec2-config %{buildroot}%{_sysconfdir}/ctdb
%{__install} -p -m 0755 interface_modify_ec2.sh %{buildroot}%{_sysconfdir}/ctdb
%{__install} -p -m 0755 functions %{buildroot}%{_sysconfdir}/ctdb/functions-ec2

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.md COPYING
%config(noreplace) /etc/ctdb/ec2.rc
%config(noreplace) /etc/ctdb/ec2-eni-functions
%config(noreplace) /etc/ctdb/ec2-config
/etc/ctdb/interface_modify_ec2.sh
/etc/ctdb/functions-ec2

%post
if [ -f /etc/ctdb/interface_modify.sh ]; then
    %{__cp} -af /etc/ctdb/interface_modify.sh /etc/ctdb/interface_modify.sh.orig
fi
if [ -f /etc/ctdb/functions ]; then
    %{__cp} -af /etc/ctdb/functions /etc/ctdb/functions.orig
    %{__mv} -f /etc/ctdb/functions-ec2 /etc/ctdb/functions.orig
fi

%postun
if [ -f /etc/ctdb/interface_modify.sh.orig ]; then
    %{__cp} -af /etc/ctdb/interface_modify.sh.orig /etc/ctdb/interface_modify.sh
    %{__rm} -f /etc/ctdb/interface_modify.sh.orig
fi
if [ -f /etc/ctdb/functions.orig ]; then
    %{__mv} -f /etc/ctdb/functions.orig /etc/ctdb/functions
fi

%changelog
* Mon Dec 09 2013 Harshavardhana <fharshav@redhat.com> - 1.0-1
* April 2017 Chris Blum <cblum@redhat.com> - 1.3
- First import build
