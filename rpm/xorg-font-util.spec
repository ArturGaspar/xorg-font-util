Name:       xorg-font-util
Version:    1.4.1
Release:    1%{?dist}
Summary:    X.Org font package creation/installation utilities
License:    MIT
URL:        https://gitlab.freedesktop.org/xorg/font/util
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
%{summary}.

%package doc
Summary:    Documentation for %{name}
Requires:   %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/bdftruncate
%{_bindir}/ucs2any
%{_datadir}/aclocal/fontutil.m4
%{_datadir}/fonts/X11/util
%{_libdir}/pkgconfig/fontutil.pc

%files doc
%license COPYING
%{_mandir}/man1/bdftruncate.1*
%{_mandir}/man1/ucs2any.1*
