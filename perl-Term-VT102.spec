#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Term
%define		pnam	VT102
Summary:	Term::VT102 - a class to emulate a DEC VT102 terminal
Summary(pl.UTF-8):	Term::VT102 - klasa emulująca terminal DEC VT102
Name:		perl-Term-VT102
Version:	0.91
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	210cfacde8d82005a3f08748e0ca8631
URL:		http://search.cpan.org/dist/Term-VT102/
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

%description -l pl.UTF-8
Klasa VT102 emuluje większość funkcji terminala DEC VT102. Po
zainicjowaniu dane przesyłane przez obiekt VT102 są przetwarzane, a
"ekran" umieszczony w pamięci odpowiednio modyfikowany. Ten "ekran"
może być badany na różne sposoby przez program zewnętrzny.

Pozwala to programom współpracować z programami pełnoekranowymi
poprzez uruchamianie ich w podprocesie i przesyłanie ich wyjścia do
klasy VT102. Dzięki temu można widzieć, co aplikacja napisała na
ekranie poprzez odpowiednie odpytywanie klasy.

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
cp -p VT102/examples/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Term/VT102.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
