Summary: Bloonix DBI
Name: bloonix-dbi
Version: 0.7
Release: 1%{dist}
License: Commercial
Group: Utilities/System
Distribution: RHEL and CentOS

Packager: Jonny Schulz <js@bloonix.de>
Vendor: Bloonix

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Source0: http://download.bloonix.de/sources/%{name}-%{version}.tar.gz
Requires: bloonix-core
Requires: perl(DBI)
Requires: perl(DBD::Pg)
Requires: perl(DBD::mysql)
Requires: perl(Log::Handler)
Requires: perl(Params::Validate)
AutoReqProv: no

%description
bloonix-dbi provides a database interface.

%prep
%setup -q -n %{name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
%{__perl} Build

%install
%{__perl} Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -name .packlist -exec %{__rm} {} \;
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'
%{_fixperms} %{buildroot}/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog INSTALL LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu May 14 2015 Jonny Schulz <js@bloonix.de> - 0.7-1
- Fixed/added transactions support for mysql.
* Thu May 07 2015 Jonny Schulz <js@bloonix.de> - 0.6-1
- Added accessors driver and database.
- Improved string concatination and replaced || with concat().
* Mon Feb 16 2015 Jonny Schulz <js@bloonix.de> - 0.5-1
- Fixed error "prepared statement already exist".
* Mon Feb 16 2015 Jonny Schulz <js@bloonix.de> - 0.4-1
- Fixed sth_cache_enabled errors.
* Mon Nov 03 2014 Jonny Schulz <js@bloonix.de> - 0.3-1
- sth_cache_enabled is turned off by default now.
- Updated the license information.
* Fri Oct 24 2014 Jonny Schulz <js@bloonix.de> - 0.2-1
- Disable die_on_errors by default so that the logger
  does not die on errors.
* Mon Aug 25 2014 Jonny Schulz <js@bloonix.de> - 0.1-1
- Initial release.
