%define modname	Test-Fatal
%define modver 0.013

Summary:	Incredibly simple helpers for testing code with exceptions
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-Fatal-%{modver}.tar.gz
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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE META.yml META.json
%{perl_vendorlib}/*
%{_mandir}/man3/*


