#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kamera
Version  : 19.12.2
Release  : 17
URL      : https://download.kde.org/stable/release-service/19.12.2/src/kamera-19.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.2/src/kamera-19.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.2/src/kamera-19.12.2.tar.xz.sig
Summary  : KDE integration for gphoto2 cameras
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kamera-data = %{version}-%{release}
Requires: kamera-lib = %{version}-%{release}
Requires: kamera-license = %{version}-%{release}
Requires: kamera-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : pkgconfig(libgphoto2)
BuildRequires : qtbase-dev mesa-dev

%description
Dependencies:
libgphoto2 which you can get from gphotos GIT https://github.com/gphoto/libgphoto2

%package data
Summary: data components for the kamera package.
Group: Data

%description data
data components for the kamera package.


%package doc
Summary: doc components for the kamera package.
Group: Documentation

%description doc
doc components for the kamera package.


%package lib
Summary: lib components for the kamera package.
Group: Libraries
Requires: kamera-data = %{version}-%{release}
Requires: kamera-license = %{version}-%{release}

%description lib
lib components for the kamera package.


%package license
Summary: license components for the kamera package.
Group: Default

%description license
license components for the kamera package.


%package locales
Summary: locales components for the kamera package.
Group: Default

%description locales
locales components for the kamera package.


%prep
%setup -q -n kamera-19.12.2
cd %{_builddir}/kamera-19.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581014159
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1581014159
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kamera
cp %{_builddir}/kamera-19.12.2/COPYING %{buildroot}/usr/share/package-licenses/kamera/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/kamera-19.12.2/COPYING.DOC %{buildroot}/usr/share/package-licenses/kamera/0c4be15f5177aafffe980ca09c0f4ca6ed741f43
pushd clr-build
%make_install
popd
%find_lang kcmkamera
%find_lang kio5_kamera

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/camera.protocol
/usr/share/kservices5/kamera.desktop
/usr/share/metainfo/org.kde.kamera.metainfo.xml
/usr/share/solid/actions/solid_camera.desktop

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kcontrol/kamera/index.cache.bz2
/usr/share/doc/HTML/ca/kcontrol/kamera/index.docbook
/usr/share/doc/HTML/cs/kcontrol/kamera/index.cache.bz2
/usr/share/doc/HTML/cs/kcontrol/kamera/index.docbook
/usr/share/doc/HTML/de/kcontrol/kamera/index.cache.bz2
/usr/share/doc/HTML/de/kcontrol/kamera/index.docbook
/usr/share/doc/HTML/en/kcontrol/kamera/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol/kamera/index.docbook
/usr/share/doc/HTML/es/kcontrol/kamera/index.cache.bz2
/usr/share/doc/HTML/es/kcontrol/kamera/index.docbook
/usr/share/doc/HTML/et/kcontrol/kamera/index.cache.bz2
/usr/share/doc/HTML/et/kcontrol/kamera/index.docbook
/usr/share/doc/HTML/fr/kcontrol/kamera/index.cache.bz2
/usr/share/doc/HTML/fr/kcontrol/kamera/index.docbook
/usr/share/doc/HTML/gl/kcontrol/kamera/index.cache.bz2
/usr/share/doc/HTML/gl/kcontrol/kamera/index.docbook
/usr/share/doc/HTML/it/kcontrol/kamera/index.cache.bz2
/usr/share/doc/HTML/it/kcontrol/kamera/index.docbook
/usr/share/doc/HTML/nl/kcontrol/kamera/index.cache.bz2
/usr/share/doc/HTML/nl/kcontrol/kamera/index.docbook
/usr/share/doc/HTML/pl/kcontrol/kamera/index.cache.bz2
/usr/share/doc/HTML/pl/kcontrol/kamera/index.docbook
/usr/share/doc/HTML/pt/kcontrol/kamera/index.cache.bz2
/usr/share/doc/HTML/pt/kcontrol/kamera/index.docbook
/usr/share/doc/HTML/pt_BR/kcontrol/kamera/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kcontrol/kamera/index.docbook
/usr/share/doc/HTML/ru/kcontrol/kamera/index.cache.bz2
/usr/share/doc/HTML/ru/kcontrol/kamera/index.docbook
/usr/share/doc/HTML/sv/kcontrol/kamera/index.cache.bz2
/usr/share/doc/HTML/sv/kcontrol/kamera/index.docbook
/usr/share/doc/HTML/uk/kcontrol/kamera/index.cache.bz2
/usr/share/doc/HTML/uk/kcontrol/kamera/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kcm_kamera.so
/usr/lib64/qt5/plugins/kio_kamera.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kamera/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/kamera/0c4be15f5177aafffe980ca09c0f4ca6ed741f43

%files locales -f kcmkamera.lang -f kio5_kamera.lang
%defattr(-,root,root,-)

