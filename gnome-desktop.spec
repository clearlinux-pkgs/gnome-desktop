#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-desktop
Version  : 3.34.2
Release  : 41
URL      : https://download.gnome.org/sources/gnome-desktop/3.34/gnome-desktop-3.34.2.tar.xz
Source0  : https://download.gnome.org/sources/gnome-desktop/3.34/gnome-desktop-3.34.2.tar.xz
Summary  : Utility library for loading .desktop files
Group    : Development/Tools
License  : GFDL-1.1 GPL-2.0 LGPL-2.0
Requires: gnome-desktop-data = %{version}-%{release}
Requires: gnome-desktop-lib = %{version}-%{release}
Requires: gnome-desktop-libexec = %{version}-%{release}
Requires: gnome-desktop-license = %{version}-%{release}
Requires: gnome-desktop-locales = %{version}-%{release}
Requires: bubblewrap
BuildRequires : bubblewrap
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gobject-introspection-dev
BuildRequires : itstool
BuildRequires : libseccomp-dev
BuildRequires : libxml2-dev
BuildRequires : libxml2-python
BuildRequires : pkgconfig(gsettings-desktop-schemas)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(iso-codes)
BuildRequires : pkgconfig(libseccomp)
BuildRequires : pkgconfig(xkeyboard-config)
Patch1: better-debug.patch
Patch2: Mount-CLR-ld.so.cache.patch
Patch3: 0001-liblocaledir-is-located-in-usr-share-local.patch

%description
gnome-desktop
=============
gnome-desktop contains the libgnome-desktop library as well as a data
file that exports the "GNOME" version to the Settings Details panel.

%package data
Summary: data components for the gnome-desktop package.
Group: Data

%description data
data components for the gnome-desktop package.


%package dev
Summary: dev components for the gnome-desktop package.
Group: Development
Requires: gnome-desktop-lib = %{version}-%{release}
Requires: gnome-desktop-data = %{version}-%{release}
Provides: gnome-desktop-devel = %{version}-%{release}
Requires: gnome-desktop = %{version}-%{release}

%description dev
dev components for the gnome-desktop package.


%package doc
Summary: doc components for the gnome-desktop package.
Group: Documentation

%description doc
doc components for the gnome-desktop package.


%package lib
Summary: lib components for the gnome-desktop package.
Group: Libraries
Requires: gnome-desktop-data = %{version}-%{release}
Requires: gnome-desktop-libexec = %{version}-%{release}
Requires: gnome-desktop-license = %{version}-%{release}

%description lib
lib components for the gnome-desktop package.


%package libexec
Summary: libexec components for the gnome-desktop package.
Group: Default
Requires: gnome-desktop-license = %{version}-%{release}

%description libexec
libexec components for the gnome-desktop package.


%package license
Summary: license components for the gnome-desktop package.
Group: Default

%description license
license components for the gnome-desktop package.


%package locales
Summary: locales components for the gnome-desktop package.
Group: Default

%description locales
locales components for the gnome-desktop package.


%prep
%setup -q -n gnome-desktop-3.34.2
cd %{_builddir}/gnome-desktop-3.34.2
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576618312
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-desktop
cp %{_builddir}/gnome-desktop-3.34.2/COPYING %{buildroot}/usr/share/package-licenses/gnome-desktop/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/gnome-desktop-3.34.2/COPYING-DOCS %{buildroot}/usr/share/package-licenses/gnome-desktop/4f485ab7059ac53d9e3818278ad82217ce976a36
cp %{_builddir}/gnome-desktop-3.34.2/COPYING.LIB %{buildroot}/usr/share/package-licenses/gnome-desktop/ba8966e2473a9969bdcab3dc82274c817cfd98a1
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-desktop-3.0

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GnomeDesktop-3.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/gnome/gnome-version.xml

%files dev
%defattr(-,root,root,-)
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-bg-crossfade.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-bg-slide-show.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-bg.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-desktop-thumbnail.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-idle-monitor.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-languages.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-pnp-ids.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-rr-config.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-rr.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-systemd.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-wall-clock.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-xkb-info.h
/usr/lib64/libgnome-desktop-3.so
/usr/lib64/pkgconfig/gnome-desktop-3.0.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/fdl/index.docbook
/usr/share/help/C/gpl/index.docbook
/usr/share/help/C/lgpl/index.docbook
/usr/share/help/ar/fdl/index.docbook
/usr/share/help/ar/gpl/index.docbook
/usr/share/help/ar/lgpl/index.docbook
/usr/share/help/ca/fdl/index.docbook
/usr/share/help/ca/gpl/index.docbook
/usr/share/help/ca/lgpl/index.docbook
/usr/share/help/cs/fdl/index.docbook
/usr/share/help/cs/gpl/index.docbook
/usr/share/help/cs/lgpl/index.docbook
/usr/share/help/de/fdl/index.docbook
/usr/share/help/de/gpl/index.docbook
/usr/share/help/de/lgpl/index.docbook
/usr/share/help/el/fdl/index.docbook
/usr/share/help/el/gpl/index.docbook
/usr/share/help/el/lgpl/index.docbook
/usr/share/help/es/fdl/index.docbook
/usr/share/help/es/gpl/index.docbook
/usr/share/help/es/lgpl/index.docbook
/usr/share/help/eu/fdl/index.docbook
/usr/share/help/eu/gpl/index.docbook
/usr/share/help/eu/lgpl/index.docbook
/usr/share/help/fi/gpl/index.docbook
/usr/share/help/fi/lgpl/index.docbook
/usr/share/help/fr/fdl/index.docbook
/usr/share/help/fr/gpl/index.docbook
/usr/share/help/fr/lgpl/index.docbook
/usr/share/help/gl/fdl/index.docbook
/usr/share/help/gl/gpl/index.docbook
/usr/share/help/hu/fdl/index.docbook
/usr/share/help/hu/gpl/index.docbook
/usr/share/help/hu/lgpl/index.docbook
/usr/share/help/ko/fdl/index.docbook
/usr/share/help/ko/gpl/index.docbook
/usr/share/help/ko/lgpl/index.docbook
/usr/share/help/nds/gpl/index.docbook
/usr/share/help/oc/fdl/index.docbook
/usr/share/help/oc/gpl/index.docbook
/usr/share/help/oc/lgpl/index.docbook
/usr/share/help/pa/gpl/index.docbook
/usr/share/help/pa/lgpl/index.docbook
/usr/share/help/pt_BR/fdl/index.docbook
/usr/share/help/pt_BR/gpl/index.docbook
/usr/share/help/pt_BR/lgpl/index.docbook
/usr/share/help/sl/fdl/index.docbook
/usr/share/help/sl/gpl/index.docbook
/usr/share/help/sl/lgpl/index.docbook
/usr/share/help/sr/gpl/index.docbook
/usr/share/help/sr@latin/gpl/index.docbook
/usr/share/help/sv/fdl/index.docbook
/usr/share/help/sv/gpl/index.docbook
/usr/share/help/sv/lgpl/index.docbook
/usr/share/help/uk/fdl/index.docbook
/usr/share/help/uk/gpl/index.docbook
/usr/share/help/uk/lgpl/index.docbook
/usr/share/help/vi/fdl/index.docbook
/usr/share/help/vi/gpl/index.docbook
/usr/share/help/vi/lgpl/index.docbook
/usr/share/help/zh_CN/fdl/index.docbook
/usr/share/help/zh_CN/gpl/index.docbook
/usr/share/help/zh_CN/lgpl/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgnome-desktop-3.so.18
/usr/lib64/libgnome-desktop-3.so.18.0.3

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gnome-rr-debug

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-desktop/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/gnome-desktop/4f485ab7059ac53d9e3818278ad82217ce976a36
/usr/share/package-licenses/gnome-desktop/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files locales -f gnome-desktop-3.0.lang
%defattr(-,root,root,-)

