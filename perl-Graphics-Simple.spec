%include	/usr/lib/rpm/macros.perl
%define	pdir	Graphics
%define	pnam	Simple
Summary:	Graphics::Simple perl module
Summary(pl):	Modu³ perla Graphics::Simple
Name:		perl-Graphics-Simple
Version:	0.04
Release:	11.1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ab74296023555d2304a34e803d9447e0
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphics::Simple - a simple, device-independent graphics API for Perl.

%description -l pl
Graphics::Simple - prosty, niezale¿ny sprzêtowo graficzny API dla
perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{perl_sitelib}/Graphics/Simple.pm
%{perl_sitelib}/Graphics/Simple
%dir %{perl_sitelib}/Graphics
%{_mandir}/man3/*
