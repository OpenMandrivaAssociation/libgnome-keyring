%define url_ver %(echo %{version} | cut -d. -f1,2)

%define major	0
%define api	1.0
%define libname	%mklibname gnome-keyring %{major}
%define girname	%mklibname gnome-keyring-gir %{api}
%define devname	%mklibname -d gnome-keyring

Summary:	Keyring library for the GNOME desktop
Name:		libgnome-keyring
Version:	3.12.0
Release:	1
License:	LGPLv2+
Group:		Networking/Remote access
Url:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/libgnome-keyring/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libgcrypt-devel
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

%description
gnome-keyring is a program that keep password and other secrets for
users. It is run as a damon in the session, similar to ssh-agent, and
other applications can locate it by an environment variable.
 
The program can manage several keyrings, each with its own master
password, and there is also a session keyring which is never stored to
disk, but forgotten when the session ends.

%package i18n
Group:		System/Libraries
Summary:	Localization data files for %{name}

%description i18n
This package contains the translations for %{name}.

%package -n %{libname}
Group:		System/Libraries
Summary:	Library for integration with the gnome keyring system
Requires:	%{name}-i18n >= %{version}-%{release}
Provides:	libgnome-keyring = %{version}-%{release}

%description -n %{libname}
The library libgnome-keyring is used by applications to integrate with
the gnome keyring system. However, at this point the library hasn't been
tested and used enought to consider the API to be publically
exposed. Therefore use of libgnome-keyring is at the moment limited to
internal use in the gnome desktop. However, we hope that the
gnome-keyring API will turn out useful and good, so that later it
can be made public for any application to use.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Group:		Development/C
Summary:	Library for integration with the gnome keyring system
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q
%apply_patches

%build
%configure \
	--disable-static

%make

%install
%makeinstall_std

%find_lang %{name}

%files i18n -f %{name}.lang

%files -n %{libname}
%{_libdir}/libgnome-keyring.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GnomeKeyring-%{api}.typelib

%files -n %{devname}
%doc ChangeLog README NEWS
%dir %{_includedir}/gnome-keyring-1/
%{_includedir}/gnome-keyring-1/*.h
%{_libdir}/libgnome-keyring.so
%{_libdir}/pkgconfig/gnome-keyring-1.pc
%doc %{_datadir}/gtk-doc/html/gnome-keyring
%{_datadir}/gir-1.0/GnomeKeyring-%{api}.gir

