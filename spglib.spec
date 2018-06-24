%define major		0
%define libname		%mklibname symspg %{major}
%define develname	%mklibname %{name} -d

Name:		spglib
Version:	1.10.3
Release:	1
Summary:	C library for finding and handling crystal symmetries
License:	BSD
Group:		System/Libraries
Url:		https://atztogo.github.io/spglib/
Source0:	https://github.com/atztogo/spglib/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool

%description
C library for finding and handling crystal symmetries.

#----------------------------------------------------

%package -n	%{libname}
Summary:	C library for finding and handling crystal symmetries
Group:		System/Libraries

%description -n	%{libname}
C library for finding and handling crystal symmetries.
This package contains library files for %{name}.

#----------------------------------------------------

%package -n	%{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libspg-devel = %{version}-%{release}

%description -n	%{develname}
The %{develname} package contains libraries and header files for
developing applications that use %{name}.

#----------------------------------------------------

%prep
%setup -q

%build
touch INSTALL NEWS README AUTHORS
autoreconf -vfi

%configure --disable-static

%make

%install
%makeinstall_std

# we don't want these
find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%{_libdir}/libsymspg.so.%{major}*

%files -n %{develname}
%doc ChangeLog README.md
%license COPYING
%{_includedir}/%{name}/
%{_libdir}/libsymspg.so

