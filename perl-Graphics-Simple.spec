%include	/usr/lib/rpm/macros.perl
Summary:	Graphics-Simple perl module
Summary(pl):	Modu� perla Graphics-Simple
Name:		perl-Graphics-Simple
Version:	0.04
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Graphics/Graphics-Simple-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphics-Simple - a simple, device-independent graphics API for Perl.

%description -l pl
Graphics-Simple - prosty, niezale�ny sprz�towo graficzny API dla
perla.

%prep
%setup -q -n Graphics-Simple-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Graphics/Simple.pm
%{perl_sitelib}/Graphics/Simple
%{_mandir}/man3/*
