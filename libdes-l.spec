Summary:	DES encryption library
Summary(pl):	Biblioteka kodowania DES
Name:		libdes-l
Version:	4.04b
Release:	1
License:	distributable
Group:		Development/Libraries
Source0:	ftp://ftp.psy.uq.oz.au/pub/Crypto/DES/%{name}-%{version}.tar.gz
Patch0:		%{name}-makefiles.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This kit builds a DES encryption library and a DES encryption program.
It supports ecb, cbc, ofb, cfb, triple ecb, triple cbc, triple ofb,
triple cfb, desx, and MIT's pcbc encryption modes and also has a fast
implementation of crypt(3).

%description -l pl
Jest to zestaw bibliotek kryptograficznych DES oraz program
szyfruj±cy. Wspiera tryby szyfrowania: ecb, cbc, ofb, cfb, triple ecb,
triple cbc, triple ofb, triple cfb, desx oraz MIT's pcbc. Ma tak¿e
szybk± implementacjê crypt(3).

%package devel
Summary:	libdes-l Library Development
Summary(pl):	Czê¶æ dla programistów biblioteki libdes-l
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
The libdes-l-devel package contains the header files and some
documentation needed to develop application with libdes-l.

%description devel -l pl
Pakiet libdes-l-devel zawiera pliki nag³ówkowe i dokumentacjê,
potrzebne do kompilowania aplikacji korzystaj±cych z libdes-l.

%package static
Summary:	Static libdes-l Library
Summary(pl):	Statyczna biblioteka libdes-l
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libdes-l library.

%description static -l pl
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
%attr(644,root,root) %{_libdir}/liblibdes.so.%{version}

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/liblibdes.so
%attr(644,root,root) %{_includedir}/*
%doc COPYRIGHT INSTALL README VERSION *.man options.txt

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/liblibdes.a
