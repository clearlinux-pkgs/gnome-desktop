#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-desktop
Version  : 3.28.0
Release  : 18
URL      : https://download.gnome.org/sources/gnome-desktop/3.28/gnome-desktop-3.28.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-desktop/3.28/gnome-desktop-3.28.0.tar.xz
Summary  : Utility library for loading .desktop files
Group    : Development/Tools
License  : GFDL-1.1 GPL-2.0 LGPL-2.0
Requires: gnome-desktop-data
Requires: gnome-desktop-lib
Requires: gnome-desktop-bin
Requires: gnome-desktop-doc
Requires: gnome-desktop-locales
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : itstool
BuildRequires : libxml2-dev
BuildRequires : libxml2-python
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gsettings-desktop-schemas)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(iso-codes)
BuildRequires : pkgconfig(libseccomp)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xkeyboard-config)

%description
gnome-desktop
=============
gnome-desktop contains the libgnome-desktop library as well as a data
file that exports the "GNOME" version to the Settings Details panel.

%package bin
Summary: bin components for the gnome-desktop package.
Group: Binaries
Requires: gnome-desktop-data

%description bin
bin components for the gnome-desktop package.


%package data
Summary: data components for the gnome-desktop package.
Group: Data

%description data
data components for the gnome-desktop package.


%package dev
Summary: dev components for the gnome-desktop package.
Group: Development
Requires: gnome-desktop-lib
Requires: gnome-desktop-bin
Requires: gnome-desktop-data
Provides: gnome-desktop-devel

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
Requires: gnome-desktop-data

%description lib
lib components for the gnome-desktop package.


%package locales
Summary: locales components for the gnome-desktop package.
Group: Default

%description locales
locales components for the gnome-desktop package.


%prep
%setup -q -n gnome-desktop-3.28.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522197133
%configure --disable-static --disable-desktop-docs
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1522197133
rm -rf %{buildroot}
%make_install
%find_lang gnome-desktop-3.0

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/gnome-rr-debug

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
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-wall-clock.h
/usr/include/gnome-desktop-3.0/libgnome-desktop/gnome-xkb-info.h
/usr/lib64/libgnome-desktop-3.so
/usr/lib64/pkgconfig/gnome-desktop-3.0.pc

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/gnome-desktop3/GnomeDesktopThumbnailFactory.html
/usr/share/gtk-doc/html/gnome-desktop3/GnomeIdleMonitor.html
/usr/share/gtk-doc/html/gnome-desktop3/GnomeWallClock.html
/usr/share/gtk-doc/html/gnome-desktop3/GnomeXkbInfo.html
/usr/share/gtk-doc/html/gnome-desktop3/annotation-glossary.html
/usr/share/gtk-doc/html/gnome-desktop3/background.html
/usr/share/gtk-doc/html/gnome-desktop3/gnome-desktop3-Language-Utilities.html
/usr/share/gtk-doc/html/gnome-desktop3/gnome-desktop3-gnome-bg.html
/usr/share/gtk-doc/html/gnome-desktop3/gnome-desktop3-gnome-pnp-ids.html
/usr/share/gtk-doc/html/gnome-desktop3/gnome-desktop3-gnome-rr-config.html
/usr/share/gtk-doc/html/gnome-desktop3/gnome-desktop3-gnome-rr.html
/usr/share/gtk-doc/html/gnome-desktop3/gnome-desktop3.devhelp2
/usr/share/gtk-doc/html/gnome-desktop3/home.png
/usr/share/gtk-doc/html/gnome-desktop3/idle-monitor.html
/usr/share/gtk-doc/html/gnome-desktop3/index.html
/usr/share/gtk-doc/html/gnome-desktop3/intro.html
/usr/share/gtk-doc/html/gnome-desktop3/languages.html
/usr/share/gtk-doc/html/gnome-desktop3/left-insensitive.png
/usr/share/gtk-doc/html/gnome-desktop3/left.png
/usr/share/gtk-doc/html/gnome-desktop3/randr.html
/usr/share/gtk-doc/html/gnome-desktop3/right-insensitive.png
/usr/share/gtk-doc/html/gnome-desktop3/right.png
/usr/share/gtk-doc/html/gnome-desktop3/style.css
/usr/share/gtk-doc/html/gnome-desktop3/thumbnail.html
/usr/share/gtk-doc/html/gnome-desktop3/up-insensitive.png
/usr/share/gtk-doc/html/gnome-desktop3/up.png
/usr/share/gtk-doc/html/gnome-desktop3/wall-clock.html
/usr/share/gtk-doc/html/gnome-desktop3/xkb-info.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgnome-desktop-3.so.17
/usr/lib64/libgnome-desktop-3.so.17.0.0

%files locales -f gnome-desktop-3.0.lang
%defattr(-,root,root,-)

