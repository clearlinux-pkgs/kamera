#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kamera
Version  : 23.08.2
Release  : 58
URL      : https://download.kde.org/stable/release-service/23.08.2/src/kamera-23.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.2/src/kamera-23.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.2/src/kamera-23.08.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0
Requires: kamera-data = %{version}-%{release}
Requires: kamera-lib = %{version}-%{release}
Requires: kamera-license = %{version}-%{release}
Requires: kamera-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : pkgconfig(libgphoto2)
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n kamera-23.08.2
cd %{_builddir}/kamera-23.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697252145
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1697252145
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kamera
cp %{_builddir}/kamera-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kamera/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kamera-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kamera/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kamera-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kamera/ee03d68f6be20b170e5ea5d114d6acafb3f2d1dc || :
cp %{_builddir}/kamera-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kamera/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang kcmkamera
%find_lang kio5_kamera
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/applications/kcm_kamera.desktop
/usr/share/metainfo/org.kde.kamera.metainfo.xml
/usr/share/qlogging-categories5/kamera.categories
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
/usr/share/doc/HTML/tr/kcontrol/kamera/index.cache.bz2
/usr/share/doc/HTML/tr/kcontrol/kamera/index.docbook
/usr/share/doc/HTML/uk/kcontrol/kamera/index.cache.bz2
/usr/share/doc/HTML/uk/kcontrol/kamera/index.docbook

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt5/plugins/kf5/kio/kio_kamera.so
/V3/usr/lib64/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kamera.so
/usr/lib64/qt5/plugins/kf5/kio/kio_kamera.so
/usr/lib64/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kamera.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kamera/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kamera/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kamera/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kamera/ee03d68f6be20b170e5ea5d114d6acafb3f2d1dc

%files locales -f kcmkamera.lang -f kio5_kamera.lang
%defattr(-,root,root,-)

