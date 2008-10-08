Summary:	Distributed Make
Name:		dmake
Version:	4.11
Release:	0.1
License:	GPL
Group:		Development/Building
Source0:	http://tools.openoffice.org/dmake/%{name}_%{version}.zip
# Source0-md5:	e00deccf8817eec85ab5c0268d5a7bfb
URL:		http://tools.openoffice.org/dmake/
#BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dmake is a build utility similar to GNU make or the Sun Studio dmake.
This utility has an irregular syntax. It is currently maintained by
the OpenOffice.org team as it is part of the OpenOffice.org build
environment.

%prep
%setup -q -n dmake

%build
%configure \
	--datadir=%{_datadir}/dmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/dmake

%clean
rm -rf $RPM_BUILD_ROOT
