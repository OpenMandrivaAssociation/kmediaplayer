%define major 5
%define libname %mklibname KF5Mediaplayer %{major}
%define devname %mklibname KF5Mediaplayer -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kmediaplayer
Version: 5.82.0
Release: 1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/portingAids/%{name}-%{version}.tar.xz
Summary: Plugin interface for media player features
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5XmlGui)
Requires: %{libname} = %{EVRD}

%description
Plugin interface for media player features.

%package -n %{libname}
Summary: Plugin interface for media player features
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Plugin interface for media player features.

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 Mediaplayer library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 Mediaplayer library.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

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
