%define module CryptX
%undefine _debugsource_packages

Name:		perl-%{module}
Version:	0.081
Release:	2
Summary:	Perl modules providing a cryptography based on LibTomCrypt library
URL:		https://metacpan.org/pod/CryptX
Source:		https://cpan.metacpan.org/authors/id/M/MI/MIK/CryptX-%{version}.tar.gz
License:	Perl (Artistic or GPL)
Group:		Development/Perl
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Math::Complex)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)

%description
Perl modules providing a cryptography based on LibTomCrypt library.

%prep
%autosetup -p1 -n %{module}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install INSTALLDIRS=vendor

%files
%doc Changes MANIFEST
%{perl_vendorarch}/CryptX.pm
%{perl_vendorarch}/Crypt/*
%{perl_vendorarch}/Math/BigInt/LTM.pm
%{perl_vendorarch}/auto/CryptX
%{_mandir}/man3/*.3pm*
