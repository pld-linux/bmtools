#
# TODO:
# - polish description, change group, wait for stable version 
#   (maybe)
# 
Summary:	bmtools - Bandwidth Measurement Tools
Summary(pl):	bmtools - Narzêdzia do ustawiania przepustowo¶ci ³±cza
Name:		bmtools
Version:	0.7
Release:	0.9.experimential
License:	GPL
Group:		Applications
Source0:	http://s-tech.elsat.net.pl/bmtools/%{name}-%{version}-EXPERIMENTAL-UNSTABLE-UNTESTED-ETC.tar.gz
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

%description -l pl

%prep
%setup -q

%build
%{__make} CC="gcc %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install {bandabusers,rate,ratec,rated} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
