%define modname	Test-Fatal

# Avoid nasty build dependency loop
%define dont_gprintify 1

Summary:	Incredibly simple helpers for testing code with exceptions
Name:		perl-%{modname}
Version:	0.016
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Test::Fatal
Source0:	http://www.cpan.org/modules/by-module/Test/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl(overload)
BuildRequires:	perl-devel

%description
Test::Fatal is an alternative to the popular the Test::Exception manpage.
It does much less, but should allow greater flexibility in testing
exception-throwing code with about the same amount of typing.

It exports one routine by default: 'exception'.

%prep
%autosetup -p1 -n %{modname}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
%make test

%install
%make_install

%files
%doc README Changes LICENSE META.yml META.json
%{perl_vendorlib}/*
%{_mandir}/man3/*
