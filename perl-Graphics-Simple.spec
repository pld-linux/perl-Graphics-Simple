%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Graphics-Simple perl module
Summary(pl):	Modu³ perla Graphics-Simple
Name:		perl-Graphics-Simple
Version:	0.04
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Graphics/Graphics-Simple-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Graphics-Simple - a simple, device-independent graphics API for Perl.

%description -l pl
Graphics-Simple - prosty, niezale¿ny sprzêtowo graficzny API dla perla.

%prep
%setup -q -n Graphics-Simple-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Graphics/Simple
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README,TODO}.gz

%{perl_sitelib}/Graphics/Simple.pm
%{perl_sitelib}/Graphics/Simple
%{perl_sitearch}/auto/Graphics/Simple

%{_mandir}/man3/*
