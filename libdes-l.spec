Summary:	DES encryption library 
Summary(pl):	Biblioteka DES
Name:		libdes-l		
Version:	4.04b
Release:	1
License:	distributable
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Source0:	ftp://ftp.psy.uq.oz.au/pub/Crypto/DES/%{name}-%{version}.tar.gz
Patch0:		%{name}-makefiles.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This kit builds a DES encryption library and a DES encryption program.
It supports ecb, cbc, ofb, cfb, triple ecb, triple cbc, triple ofb,
triple cfb, desx, and MIT's pcbc encryption modes and also has a fast
implementation of crypt(3).

%description -l pl
Jest to zestaw bibliotek kryptograficznych DES oraz program szyfruj╠cy.
Wspiera tryby szyfrowania: ecb, cbc, ofb, cfb, triple ecb, triple cbc, 
triple ofb, triple cfb, desx oraz MIT's pcbc. Ma tak©e szybk╠ 
implementacjЙ crypt(3).

%package -n libdes-l-devel
Summary:	libdes-l Library Development 
Summary(pl):	CzЙ╤Ф dla programistСw biblioteki libdes-l
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	libdes-l

%description -n libdes-l-devel
The libdes-l-devel package contains the header files and some
documentation needed to develop application with libdes-l.

%description -n libdes-l-devel -l pl
Pakiet libdes-l-devel zawiera pliki nagЁСwkowe i dokumentacjЙ,
potrzebne do kompilowania aplikacji korzystaj╠cych z libdes-l

%package -n libdes-l-static
Summary:	Static libdes-l Library 
Summary(pl):	Statyczna biblioteka libdes-l
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	libdes-l-devel 

%description -n libdes-l-static
Static libdes-l library.

%description -n libdes-l-static -l pl
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

ln -s %{_libdir}/liblibdes.so.%{version} $RPM_BUILD_ROOT%{_libdir}/liblibdes.so

gzip -9nf COPYRIGHT INSTALL README VERSION *.man options.txt

%post -p /sbin/ldconfig 
%postun -p /sbin/ldconfig 

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/liblibdes.so.%{version}

%files -n libdes-l-devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/liblibdes.so
%attr(644,root,root) %{_includedir}/* 
%doc *.gz

%files -n libdes-l-static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/liblibdes.a
