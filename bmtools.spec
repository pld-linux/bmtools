#
# TODO:
# - change group, wait for stable version (maybe)
#
Summary:	bmtools - Bandwidth Measurement Tools
Summary(pl.UTF-8):   bmtools - Narzędzia do mierzenia przepustowości łącza
Name:		bmtools
Version:	0.7
Release:	0.9.experimential
License:	GPL
Group:		Applications
Source0:	http://s-tech.elsat.net.pl/bmtools/%{name}-%{version}-EXPERIMENTAL-UNSTABLE-UNTESTED-ETC.tar.gz
# Source0-md5:	e53aac82dcb57a751102eeaf212ca8f5
Patch0:		%{name}-gcc2.95.4.patch
URL:		http://s-tech.elsat.net.pl/
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bmtools (Bandwidth Measurement Tools) is a pair of simple traffic
measurement tools which can really help a network administrator see
what is happening on a Linux-based router. The 'rate' script
calculates the bandwidth used by packets matching a given BPF filter
on an interface. The 'bandabusers' script shows the top ten hosts
receiving and transmitting packets matching a given BPF filter. Both
programs are completely command-line based.

%description -l pl.UTF-8
bmtools (Bandwidth Measurement Tools - narzędzia do mierzenia
przepustowości łącza) to para prostych narzędzi do mierzenia ruchu,
które mogą pomóc administratorowi sieci w patrzeniu, co się dzieje z
routerem działającym pod kontrolą Linuksa. Skrypt rate oblicza
pasmo wykorzystane przez pakietu pasujące do podanego filtra BPF na
interfejsie. Skrypt bandabusers pokazuje dziesięć hostów odbierających
i wysyłających najwięcej pakietów pasujących do podanego filtra BPF.
Oba programy są w pełni oparte na linii poleceń.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bandabusers rate ratec rated $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
