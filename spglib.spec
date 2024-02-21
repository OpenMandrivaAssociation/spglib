%define major		2
%define libname		%mklibname symspg %{major}
%define develname	%mklibname %{name} -d

Name:		spglib
Version:	2.3.1
Release:	1
Summary:	C library for finding and handling crystal symmetries
License:	BSD
Group:		System/Libraries
Url:		https://spglib.readthedocs.io/en/latest/
Source0:	https://github.com/spglib/spglib/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja

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
%cmake -G Ninja
%ninja


%install
%ninja_install -C build

# we don't want these
find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%{_libdir}/libsymspg.so.%{major}*

%files -n %{develname}
%doc ChangeLog.md README.md
%license COPYING
%{_includedir}/%{name}.h
%{_libdir}/libsymspg.so
%{_libdir}/cmake/Spglib
%{_libdir}/pkgconfig/spglib.pc


