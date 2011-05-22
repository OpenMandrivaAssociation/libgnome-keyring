%define lib_major 0
%define libname %mklibname gnome-keyring %{lib_major}
%define libnamedev %mklibname -d gnome-keyring

Summary: Keyring library for the GNOME desktop
Name: libgnome-keyring
Version: 3.0.2
Release: %mkrel 1
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
URL: http://www.gnome.org/
License: LGPLv2+
Group: Networking/Remote access
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libgcrypt-devel
BuildRequires: dbus-devel
BuildRequires: glib2-devel
BuildRequires: intltool
BuildRequires: gtk-doc

%description
gnome-keyring is a program that keep password and other secrets for
users. It is run as a damon in the session, similar to ssh-agent, and
other applications can locate it by an environment variable.
 
The program can manage several keyrings, each with its own master
password, and there is also a session keyring which is never stored to
disk, but forgotten when the session ends.

%package i18n
Group: System/Libraries
Summary: Localization data files for %name
%description i18n
This package contains the translations for %name.

%package -n %{libname}
Group: System/Libraries
Summary: Library for integration with the gnome keyring system
Requires: gnome-keyring
Requires: %name-i18n >= %version-%release

%description -n %{libname}
The library libgnome-keyring is used by applications to integrate with
the gnome keyring system. However, at this point the library hasn't been
tested and used enought to consider the API to be publically
exposed. Therefore use of libgnome-keyring is at the moment limited to
internal use in the gnome desktop. However, we hope that the
gnome-keyring API will turn out useful and good, so that later it
can be made public for any application to use.


%package -n %{libnamedev}
Group: Development/C
Summary: Library for integration with the gnome keyring system
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %mklibname -d %name 0
#gw libtool dep
Requires: eggdbus-devel

%description -n %{libnamedev}
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
%configure2_5x  --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot/%_lib/security/{*.la,*.a} %buildroot%_libdir/*.a
%find_lang %{name}



%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files i18n -f %name.lang


%files -n %{libname}
%doc README NEWS
%defattr(-,root,root)
%{_libdir}/libgnome-keyring.so.%{lib_major}*

%files -n %{libnamedev}
%defattr(-,root,root)
%doc ChangeLog
%{_libdir}/libgnome-keyring.so
%attr(644,root,root) %{_libdir}/*.la
%dir %{_includedir}/gnome-keyring-1/
%{_includedir}/gnome-keyring-1/*.h
%{_libdir}/pkgconfig/gnome-keyring-1.pc
%_datadir/gtk-doc/html/gnome-keyring
