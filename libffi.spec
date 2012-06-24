Summary:	Foreign Function Interface library
Summary(pl):	Biblioteka Foreign Function Interface
Name:		libffi
Version:	1.20
Release:	3
License:	distributable
Group:		Libraries
Vendor:		Cygnus
Source0:	ftp://sourceware.cygnus.com/pub/libffi/%{name}-%{version}.tar.gz
URL:		http://sources.redhat.com/libffi/
#Note: this package is platform independent though it is (currently) only
#      needed on ppc (to build kaffe)
ExclusiveArch:	ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libffi library provides a portable, high level programming
interface to various calling conventions. This allows a programmer to
call any function specified by a call interface description at
run-time.

Ffi stands for Foreign Function Interface. A foreign function
interface is the popular name for the interface that allows code
written in one language to call code written in another language. The
libffi library really only provides the lowest, machine dependent
layer of a fully featured foreign function interface. A layer must
exist above libffi that handles type conversions for values passed
between the two languages. 

%description -l pl
Biblioteka libffi dostarcza przeno�ny, wysokopoziomowy interfejs do
r�nych konwencji wywo�a� funkcji. Pozwala to programi�cie wywo�a�
dowoln� funkcj� podan� przez opis interfejsu wywo�ania w czasie
dzia�ania programu.

FFI to skr�t od Foreign Function Interface, czyli interfejsu do obcych
funkcji. Jest to potoczna nazwa interfejsu pozwalaj�cego programowi
napisanemu w jednym j�zyku wywo�ywa� kod napisany w innym j�zyku.
Biblioteka libffi daje tylko najni�sz�, zale�n� od maszyny warstw�
pe�nego interfejsu. Potrzebne s� wy�sze warstwy do obs�ugi konwersji
typ�w dla warto�ci przekazywanych pomi�dzy r�nymi j�zykami.

%package devel
Summary:	libffi development package
Summary(pl):	libffi - cz�� dla programist�w
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libffi.

%description devel -l pl
Pliki nag��wkowe do biblioteki libffi.

%package static
Summary:	libffi static library
Summary(pl):	Statyczna biblioteka libffi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of libffi.

%description static -l pl
Statyczna wersja biblioteki libffi.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/libffi.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libffi.so
%{_libdir}/*.la
%{_includedir}

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
