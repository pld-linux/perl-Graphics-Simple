%include	/usr/lib/rpm/macros.perl
%define	pdir	Graphics
%define	pnam	Simple
Summary:	Graphics::Simple - a simple, device-independent graphics API for Perl
Summary(pl):	Graphics::Simple - prosty, niezale¿ny od ¶rodowiska API grafiki dla Perla
Name:		perl-Graphics-Simple
Version:	0.04
Release:	12
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ab74296023555d2304a34e803d9447e0
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphics::Simple provides a simple, device-independent graphics API
for Perl.  This module presents a unified API to graphics devices -
currently X (using GTK+ and GNOME) and PostScript.

%description -l pl
Graphics::Simple udostêpnia prosty, niezale¿ny od ¶rodowiska graficzny
interfejs programisty dla aplikacji (API) dla Perla. Modu³ ten
aktualnie przedstawia ujednolicony API dla ¶rodowisk graficznych: X (z
u¿yciem GTK+ i GNOME) oraz dla PostScriptu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{perl_vendorlib}/Graphics/Simple.pm
%{perl_vendorlib}/Graphics/Simple
%{_mandir}/man3/*
