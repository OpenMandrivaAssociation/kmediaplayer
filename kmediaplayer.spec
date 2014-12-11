%define major 5
%define libname %mklibname KF5Mediaplayer %{major}
%define devname %mklibname KF5Mediaplayer -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kmediaplayer
Version: 5.4.0
Release: 2
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/portingAids/%{name}-%{version}.tar.xz
Summary: Plugin interface for media player features
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

%description
Plugin interface for media player features

%package -n %{libname}
Summary: Plugin interface for media player features
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Plugin interface for media player features

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Mediaplayer library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Mediaplayer library

%prep
%setup -q
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

%files
%{_datadir}/dbus-1/*/*
%{_datadir}/kservicetypes5/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
