#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Foreign Function Interface library
Summary(pl.UTF-8):	Biblioteka Foreign Function Interface
Name:		libffi
Version:	3.3
Release:	1
Epoch:		7
License:	MIT-like
Group:		Libraries
Source0:	ftp://sourceware.org/pub/libffi/%{name}-%{version}.tar.gz
# Source0-md5:	6313289e32f1d38a9df4770b014a2ca7
Patch0:		%{name}-info.patch
URL:		http://www.sourceware.org/libffi/
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	texinfo
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

%description -l pl.UTF-8
Biblioteka libffi dostarcza przenośny, wysokopoziomowy interfejs do
różnych konwencji wywołań funkcji. Pozwala to programiście wywołać
dowolną funkcję podaną przez opis interfejsu wywołania w czasie
działania programu.

FFI to skrót od Foreign Function Interface, czyli interfejsu do obcych
funkcji. Jest to potoczna nazwa interfejsu pozwalającego programowi
napisanemu w jednym języku wywoływać kod napisany w innym języku.
Biblioteka libffi daje tylko najniższą, zależną od maszyny warstwę
pełnego interfejsu. Potrzebne są wyższe warstwy do obsługi konwersji
typów dla wartości przekazywanych pomiędzy różnymi językami.

%package devel
Summary:	libffi development package
Summary(pl.UTF-8):	libffi - część dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for libffi.

%description devel -l pl.UTF-8
Pliki nagłówkowe do biblioteki libffi.

%package static
Summary:	libffi static library
Summary(pl.UTF-8):	Statyczna biblioteka libffi
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static version of libffi.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libffi.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-multi-os-directory \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc ChangeLog* LICENSE README.md
%attr(755,root,root) %{_libdir}/libffi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libffi.so.7

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libffi.so
%{_libdir}/libffi.la
%{_includedir}/ffi*.h
%{_pkgconfigdir}/libffi.pc
%{_mandir}/man3/ffi*.3*
%{_infodir}/libffi.info*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libffi.a
%endif
