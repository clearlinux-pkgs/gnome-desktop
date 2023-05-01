#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : gnome-desktop
Version  : 44.0
Release  : 89
URL      : https://download.gnome.org/sources/gnome-desktop/44/gnome-desktop-44.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-desktop/44/gnome-desktop-44.0.tar.xz
Summary  : Utility library for loading .desktop files
Group    : Development/Tools
License  : GFDL-1.1 GPL-2.0 LGPL-2.0
Requires: gnome-desktop-data = %{version}-%{release}
Requires: gnome-desktop-lib = %{version}-%{release}
Requires: gnome-desktop-libexec = %{version}-%{release}
Requires: gnome-desktop-license = %{version}-%{release}
Requires: gnome-desktop-locales = %{version}-%{release}
Requires: bubblewrap
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: better-debug.patch
Patch2: 0001-Mount-CLR-ld.so.cache.patch
Patch3: 0002-liblocaledir-is-located-in-usr-share-local.patch

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


%package tests
Summary: tests components for the gnome-desktop package.
Group: Default
Requires: gnome-desktop = %{version}-%{release}

%description tests
tests components for the gnome-desktop package.


%prep
%setup -q -n gnome-desktop-44.0
cd %{_builddir}/gnome-desktop-44.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
pushd ..
cp -a gnome-desktop-44.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1682973635
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dinstalled_tests=true  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dinstalled_tests=true  builddiravx2
ninja -v -C builddiravx2

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-desktop
cp %{_builddir}/gnome-desktop-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-desktop/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/gnome-desktop-%{version}/COPYING-DOCS %{buildroot}/usr/share/package-licenses/gnome-desktop/4f485ab7059ac53d9e3818278ad82217ce976a36 || :
cp %{_builddir}/gnome-desktop-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/gnome-desktop/ba8966e2473a9969bdcab3dc82274c817cfd98a1 || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-desktop-3.0
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GnomeBG-4.0.typelib
/usr/lib64/girepository-1.0/GnomeDesktop-3.0.typelib
/usr/lib64/girepository-1.0/GnomeDesktop-4.0.typelib
/usr/lib64/girepository-1.0/GnomeRR-4.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/libgnome-bg-4.so
/V3/usr/lib64/libgnome-desktop-3.so
/V3/usr/lib64/libgnome-desktop-4.so
/V3/usr/lib64/libgnome-rr-4.so
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-bg-crossfade.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-bg-slide-show.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-bg.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-desktop-thumbnail.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-desktop-version.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-idle-monitor.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-languages.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-pnp-ids.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-rr-config.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-rr.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-systemd.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-wall-clock.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-xkb-info.h
/usr/include/gnome-desktop-4.0/gnome-bg/gnome-bg-slide-show.h
/usr/include/gnome-desktop-4.0/gnome-bg/gnome-bg.h
/usr/include/gnome-desktop-4.0/gnome-rr/gnome-rr-config.h
/usr/include/gnome-desktop-4.0/gnome-rr/gnome-rr-output-info.h
/usr/include/gnome-desktop-4.0/gnome-rr/gnome-rr-screen.h
/usr/include/gnome-desktop-4.0/gnome-rr/gnome-rr-types.h
/usr/include/gnome-desktop-4.0/gnome-rr/gnome-rr.h
/usr/include/gnome-desktop-4.0/libgnome-desktop/gnome-desktop-thumbnail.h
/usr/include/gnome-desktop-4.0/libgnome-desktop/gnome-desktop-version.h
/usr/include/gnome-desktop-4.0/libgnome-desktop/gnome-idle-monitor.h
/usr/include/gnome-desktop-4.0/libgnome-desktop/gnome-languages.h
/usr/include/gnome-desktop-4.0/libgnome-desktop/gnome-pnp-ids.h
/usr/include/gnome-desktop-4.0/libgnome-desktop/gnome-systemd.h
/usr/include/gnome-desktop-4.0/libgnome-desktop/gnome-wall-clock.h
/usr/include/gnome-desktop-4.0/libgnome-desktop/gnome-xkb-info.h
/usr/lib64/libgnome-bg-4.so
/usr/lib64/libgnome-desktop-3.so
/usr/lib64/libgnome-desktop-4.so
/usr/lib64/libgnome-rr-4.so
/usr/lib64/pkgconfig/gnome-bg-4.pc
/usr/lib64/pkgconfig/gnome-desktop-3.0.pc
/usr/lib64/pkgconfig/gnome-desktop-4.pc
/usr/lib64/pkgconfig/gnome-rr-4.pc

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
/usr/share/help/gl/lgpl/index.docbook
/usr/share/help/hr/fdl/index.docbook
/usr/share/help/hr/gpl/index.docbook
/usr/share/help/hr/lgpl/index.docbook
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
/usr/share/help/sr/fdl/index.docbook
/usr/share/help/sr/gpl/index.docbook
/usr/share/help/sr@latin/gpl/index.docbook
/usr/share/help/sv/fdl/index.docbook
/usr/share/help/sv/gpl/index.docbook
/usr/share/help/sv/lgpl/index.docbook
/usr/share/help/tr/fdl/index.docbook
/usr/share/help/tr/gpl/index.docbook
/usr/share/help/tr/lgpl/index.docbook
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
/V3/usr/lib64/libgnome-bg-4.so.2
/V3/usr/lib64/libgnome-bg-4.so.2.1.0
/V3/usr/lib64/libgnome-desktop-3.so.20
/V3/usr/lib64/libgnome-desktop-3.so.20.0.0
/V3/usr/lib64/libgnome-desktop-4.so.2
/V3/usr/lib64/libgnome-desktop-4.so.2.1.0
/V3/usr/lib64/libgnome-rr-4.so.2
/V3/usr/lib64/libgnome-rr-4.so.2.1.0
/usr/lib64/libgnome-bg-4.so.2
/usr/lib64/libgnome-bg-4.so.2.1.0
/usr/lib64/libgnome-desktop-3.so.20
/usr/lib64/libgnome-desktop-3.so.20.0.0
/usr/lib64/libgnome-desktop-4.so.2
/usr/lib64/libgnome-desktop-4.so.2.1.0
/usr/lib64/libgnome-rr-4.so.2
/usr/lib64/libgnome-rr-4.so.2.1.0

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/gnome-desktop-debug/gnome-rr-debug
/V3/usr/libexec/gnome-desktop-debug/test-desktop-thumbnail
/V3/usr/libexec/gnome-desktop-debug/test-idle-monitor
/V3/usr/libexec/gnome-desktop-debug/test-languages
/V3/usr/libexec/gnome-desktop-debug/test-pnp-ids
/V3/usr/libexec/gnome-desktop-debug/test-wall-clock
/V3/usr/libexec/gnome-desktop-debug/test-xkb-info
/usr/libexec/gnome-desktop-debug/gnome-rr-debug
/usr/libexec/gnome-desktop-debug/test-desktop-thumbnail
/usr/libexec/gnome-desktop-debug/test-idle-monitor
/usr/libexec/gnome-desktop-debug/test-languages
/usr/libexec/gnome-desktop-debug/test-pnp-ids
/usr/libexec/gnome-desktop-debug/test-wall-clock
/usr/libexec/gnome-desktop-debug/test-xkb-info

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-desktop/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/gnome-desktop/4f485ab7059ac53d9e3818278ad82217ce976a36
/usr/share/package-licenses/gnome-desktop/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files tests
%defattr(-,root,root,-)
/V3/usr/libexec/installed-tests/gnome-desktop/bg-slide-show
/V3/usr/libexec/installed-tests/gnome-desktop/languages
/V3/usr/libexec/installed-tests/gnome-desktop/wall-clock
/V3/usr/libexec/installed-tests/gnome-desktop/wallclock-reftest
/usr/libexec/installed-tests/gnome-desktop/C.ref.ui
/usr/libexec/installed-tests/gnome-desktop/C.ui
/usr/libexec/installed-tests/gnome-desktop/bg-slide-show
/usr/libexec/installed-tests/gnome-desktop/en_US.utf-8.ref.ui
/usr/libexec/installed-tests/gnome-desktop/en_US.utf-8.ui
/usr/libexec/installed-tests/gnome-desktop/he_IL.utf8.ref.ui
/usr/libexec/installed-tests/gnome-desktop/he_IL.utf8.ui
/usr/libexec/installed-tests/gnome-desktop/ja_JP.utf8.ref.ui
/usr/libexec/installed-tests/gnome-desktop/ja_JP.utf8.ui
/usr/libexec/installed-tests/gnome-desktop/languages
/usr/libexec/installed-tests/gnome-desktop/starttime.xml
/usr/libexec/installed-tests/gnome-desktop/wall-clock
/usr/libexec/installed-tests/gnome-desktop/wallclock-reftest
/usr/share/installed-tests/gnome-desktop/bg-slide-show.test
/usr/share/installed-tests/gnome-desktop/languages.test
/usr/share/installed-tests/gnome-desktop/wall-clock.test
/usr/share/installed-tests/gnome-desktop/wallclock-reftest.test

%files locales -f gnome-desktop-3.0.lang
%defattr(-,root,root,-)

