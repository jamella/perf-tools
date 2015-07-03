%define planex_version 0.0.0
%define planex_release 1

Name:           rrd2csv
Version:        %{planex_version}
Release:        %{planex_release}
Summary:        Tool for converting Xen API RRDs to CSV
License:        LGPL+linking exception
Group:          System/Hypervisor
URL:            https://github.com/xenserver/rrd2csv/
Source0:        git://github.com/xenserver/rrd2csv
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml
BuildRequires:  omake
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  xapi-client-devel
BuildRequires:  ocaml-xen-api-libs-transitional-devel
BuildRequires:  ocaml-xcp-rrd-devel

%description
This package contains the rrd2csv tool, useful to expose live RRDD metrics on
standard output, in the CSV format.

%prep
%setup -q

%build
mkdir -p %{buildroot}
DESTDIR=%{buildroot} %{__make}

%install
rm -rf %{buildroot}
DESTDIR=%{buildroot} %{__make} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/opt/xensource/bin/rrd2csv
/opt/xensource/man/man1/rrd2csv.1.man

%changelog
* Fri Jul 11 2014 John Else <john.else@citrix.com> - 0.1.0-1
- Initial package for planex
