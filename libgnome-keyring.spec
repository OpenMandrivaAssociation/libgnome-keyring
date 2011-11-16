%define lib_major 0
%define libname %mklibname gnome-keyring %{lib_major}
%define develname %mklibname -d gnome-keyring

Summary: Keyring library for the GNOME desktop
Name: libgnome-keyring
Version: 3.2.2
Release: 1
License: LGPLv2+
Group: Networking/Remote access
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires: intltool
BuildRequires: gtk-doc
BuildRequires: libgcrypt-devel
BuildRequires: pkgconfig(glib-2.0) >= 2.16.0
BuildRequires: pkgconfig(dbus-1) >= 1.0

%description
gnome-keyring is a program that keep password and other secrets for
users. It is run as a damon in the session, similar to ssh-agent, and
other applications can locate it by an environment variable.
 
The program can manage several keyrings, each with its own master
password, and there is also a session keyring which is never stored to
disk, but forgotten when the session ends.

%package i18n
Group: System/Libraries
Summary: Localization data files for %{name}
Requires: %{libname} = %{version}-%{release}

%description i18n
This package contains the translations for %{name}.

%package -n %{libname}
Group: System/Libraries
Summary: Library for integration with the gnome keyring system

%description -n %{libname}
The library libgnome-keyring is used by applications to integrate with
the gnome keyring system. However, at this point the library hasn't been
tested and used enought to consider the API to be publically
exposed. Therefore use of libgnome-keyring is at the moment limited to
internal use in the gnome desktop. However, we hope that the
gnome-keyring API will turn out useful and good, so that later it
can be made public for any application to use.


%package -n %{develname}
Group: Development/C
Summary: Library for integration with the gnome keyring system
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %mklibname -d %{name} 0

%description -n %{develname}
The library libgnome-keyring is used by applications to integrate with
the gnome keyring system. However, at this point the library hasn't been
tested and used enought to consider the API to be publically
exposed. Therefore use of libgnome-keyring is at the moment limited to
internal use in the gnome desktop. However, we hope that the
gnome-keyring API will turn out useful and good, so that later it
can be made public for any application to use.


%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name "*.la" -exec rm -rf {} \;

%find_lang %{name}

%files i18n -f %{name}.lang

%files -n %{libname}
%doc README NEWS
%{_libdir}/libgnome-keyring.so.%{lib_major}*

%files -n %{develname}
%doc ChangeLog
%dir %{_includedir}/gnome-keyring-1/
%{_libdir}/libgnome-keyring.so
%{_includedir}/gnome-keyring-1/*.h
%{_libdir}/pkgconfig/gnome-keyring-1.pc
%{_datadir}/gtk-doc/html/gnome-keyring

