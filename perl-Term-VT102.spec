#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Term
%define	pnam	VT102
Summary:	Term::VT102 - a class to emulate a DEC VT102 terminal
Summary(pl):	Term::VT102 - klasa emuluj�ca terminal DEC VT102
Name:		perl-Term-VT102
Version:	0.79
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5a228a24fe8ffa587da61e8f1075f966
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The VT102 class provides emulation of most of the functions of a DEC
VT102 terminal. Once initialised, data passed to a VT102 object is
processed and the in-memory "screen" modified accordingly. This
"screen" can be interrogated by the external program in a variety of
ways.

This allows your program to interface with full-screen console
programs by running them in a subprocess and passing their output to a
VT102 class. You can then see what the application has written on the
screen by querying the class appropriately.

%description -l pl

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install VT102/examples/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Term/VT102.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}