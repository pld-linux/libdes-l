Summary:	DES encryption library
Summary(pl.UTF-8):	Biblioteka kodowania DES
Name:		libdes-l
Version:	4.04b
Release:	1
License:	distributable
Group:		Libraries
Source0:	ftp://ftp.psy.uq.oz.au/pub/Crypto/DES/%{name}-%{version}.tar.gz
# Source0-md5:	951475d248a5c675daed508ee2b82a5b
Patch0:		%{name}-makefiles.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This kit builds a DES encryption library and a DES encryption program.
It supports ecb, cbc, ofb, cfb, triple ecb, triple cbc, triple ofb,
triple cfb, desx, and MIT's pcbc encryption modes and also has a fast
implementation of crypt(3).

%description -l pl.UTF-8
Jest to zestaw bibliotek kryptograficznych DES oraz program
szyfrujący. Wspiera tryby szyfrowania: ecb, cbc, ofb, cfb, triple ecb,
triple cbc, triple ofb, triple cfb, desx oraz MIT's pcbc. Ma także
szybką implementację crypt(3).

%package devel
Summary:	libdes-l Library Development
Summary(pl.UTF-8):	Część dla programistów biblioteki libdes-l
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The libdes-l-devel package contains the header files and some
documentation needed to develop application with libdes-l.

%description devel -l pl.UTF-8
Pakiet libdes-l-devel zawiera pliki nagłówkowe i dokumentację,
potrzebne do kompilowania aplikacji korzystających z libdes-l.

%package static
Summary:	Static libdes-l Library
Summary(pl.UTF-8):	Statyczna biblioteka libdes-l
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdes-l library.

%description static -l pl.UTF-8
Statyczna biblioteka libdes-l.

%prep
%setup -q -n des
%patch0 -p1

%build
%{__make}
%{__make} -f Makefile.shared clean
%{__make} -f Makefile.shared

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}
install -d $RPM_BUILD_ROOT%{_libdir}

install libdes.so $RPM_BUILD_ROOT%{_libdir}/liblibdes.so.%{version}
install libdes.a $RPM_BUILD_ROOT%{_libdir}/liblibdes.a
install des.h $RPM_BUILD_ROOT%{_includedir}

ln -sf %{_libdir}/liblibdes.so.%{version} $RPM_BUILD_ROOT%{_libdir}/liblibdes.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblibdes.so.%{version}

%files devel
%defattr(644,root,root,755)
%doc COPYRIGHT INSTALL README VERSION *.man options.txt
%attr(755,root,root) %{_libdir}/liblibdes.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/liblibdes.a
