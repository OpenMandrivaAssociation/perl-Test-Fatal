%define upstream_name    Test-Fatal
%define upstream_version 0.006

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Incredibly simple helpers for testing code with exceptions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl(overload)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Test::Fatal is an alternative to the popular the Test::Exception manpage.
It does much less, but should allow greater flexibility in testing
exception-throwing code with about the same amount of typing.

It exports one routine by default: 'exception'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-3mdv2012.0
+ Revision: 765679
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-2
+ Revision: 764219
- rebuilt for perl-5.14.x

* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.0-1
+ Revision: 684825
- update to new version 0.006

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-1
+ Revision: 660019
- update to new version 0.005

* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 0.3.0-3
+ Revision: 658291
- rebuild

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.3.0-2
+ Revision: 657842
- rebuild for updated spec-helper

* Sat Nov 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.0-1mdv2011.0
+ Revision: 594247
- import perl-Test-Fatal

