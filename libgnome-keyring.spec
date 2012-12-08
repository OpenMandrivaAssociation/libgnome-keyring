%define url_ver %(echo %{version} | cut -d. -f1,2)

%define major		0
%define gir_major	1.0
%define libname %mklibname gnome-keyring %{major}
%define girname	%mklibname gnome-keyring-gir %{gir_major}
%define develname %mklibname -d gnome-keyring

Summary:	Keyring library for the GNOME desktop
Name:		libgnome-keyring
Version:	3.6.0
Release:	1
License:	LGPLv2+
Group:		Networking/Remote access
URL:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/libgnome-keyring/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	gtk-doc
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

%package -n %{develname}
Group:		Development/C
Summary:	Library for integration with the gnome keyring system
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d libgnome-keyring 0} < 3.4.1

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
%makeinstall_std

%find_lang %{name}

%files i18n -f %{name}.lang

%files -n %{libname}
%{_libdir}/libgnome-keyring.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GnomeKeyring-%{gir_major}.typelib

%files -n %{develname}
%doc ChangeLog README NEWS
%dir %{_includedir}/gnome-keyring-1/
%{_includedir}/gnome-keyring-1/*.h
%{_libdir}/libgnome-keyring.so
%{_libdir}/pkgconfig/gnome-keyring-1.pc
%doc %{_datadir}/gtk-doc/html/gnome-keyring
%{_datadir}/gir-1.0/GnomeKeyring-%{gir_major}.gir

%changelog
* Fri Sep 28 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Tue Apr 24 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.1-1
+ Revision: 793221
- new version 3.4.1
- new gir pkg

* Wed Nov 16 2011 Matthew Dawkins <mattydaw@mandriva.org> 3.2.2-1
+ Revision: 731126
- new version 3.2.2
  removed defattr
  removed .la files
  removed old ldconfig scriptlets
  removed clean section
  cleaned up spec
  removed reqs for devel pkg in devel pkg
  removed req for i18n by lib pkg
  convert BRs to pkgconfig provides
  removed mkrel
  removed BuildRoot

* Thu May 26 2011 Götz Waschk <waschk@mandriva.org> 3.0.3-1
+ Revision: 679199
- new version

* Sun May 22 2011 Götz Waschk <waschk@mandriva.org> 3.0.2-1
+ Revision: 677308
- new version

* Tue Apr 26 2011 Funda Wang <fwang@mandriva.org> 3.0.1-1
+ Revision: 659092
- update to new version 3.0.1

* Fri Apr 08 2011 Funda Wang <fwang@mandriva.org> 3.0.0-1
+ Revision: 651941
- new version 3.0.0

* Tue Sep 28 2010 Götz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581611
- update to new version 2.32.0

* Mon Sep 13 2010 Funda Wang <fwang@mandriva.org> 2.31.92-1mdv2011.0
+ Revision: 577846
- new version 2.31.92

* Tue Aug 31 2010 Götz Waschk <waschk@mandriva.org> 2.31.91-1mdv2011.0
+ Revision: 574607
- new version
- drop patch 0

* Tue Jun 22 2010 Frederic Crozat <fcrozat@mandriva.com> 2.30.1-4mdv2010.1
+ Revision: 548612
- Patch0 (GIT): fix crash in threading (GNOME bug #616512) (GIT)

* Wed Apr 28 2010 Christophe Fergeau <cfergeau@mandriva.com> 2.30.1-3mdv2010.1
+ Revision: 540419
- rebuild so that shared libraries are properly stripped again
- rebuild so that shared libraries are properly stripped again

* Tue Apr 27 2010 Götz Waschk <waschk@mandriva.org> 2.30.1-1mdv2010.1
+ Revision: 539444
- update to new version 2.30.1

* Wed Mar 31 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 530223
- new version
- add translations
- drop patch, it is fixed upstream

* Sat Feb 13 2010 Götz Waschk <waschk@mandriva.org> 2.29.4-4mdv2010.1
+ Revision: 505509
- fix assertation failure in empathy (bug #54291)

* Tue Dec 22 2009 Götz Waschk <waschk@mandriva.org> 2.29.4-3mdv2010.1
+ Revision: 481228
- fix devel deps

* Tue Dec 22 2009 Götz Waschk <waschk@mandriva.org> 2.29.4-2mdv2010.1
+ Revision: 481215
- fix dep (bug #56586)

* Mon Dec 21 2009 Götz Waschk <waschk@mandriva.org> 2.29.4-1mdv2010.1
+ Revision: 480981
- new version
- drop patch
- update file list
- update build deps

* Mon Dec 14 2009 Götz Waschk <waschk@mandriva.org> 2.28.2-1mdv2010.1
+ Revision: 478590
- new version
- regenerate libtool

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 2.28.1-1mdv2010.1
+ Revision: 460930
- new version
- drop patch

* Mon Oct 05 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.0-3mdv2010.0
+ Revision: 454049
- Patch1 (vuntz): fix 10s timeout at logout (GNOME bug #595698)

* Wed Sep 30 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.0-2mdv2010.0
+ Revision: 451795
- Disable ACL prompts, they are more confusing than anything

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446733
- update to new version 2.28.0
- update build deps

* Mon Sep 14 2009 Götz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 439071
- new version
- fix linking

* Mon Aug 10 2009 Götz Waschk <waschk@mandriva.org> 2.27.90-1mdv2010.0
+ Revision: 414391
- update to new version 2.27.90

* Mon Jul 27 2009 Götz Waschk <waschk@mandriva.org> 2.27.5-1mdv2010.0
+ Revision: 400788
- update to new version 2.27.5

* Mon Jul 13 2009 Götz Waschk <waschk@mandriva.org> 2.27.4-1mdv2010.0
+ Revision: 395678
- update to new version 2.27.4

* Mon Jun 29 2009 Götz Waschk <waschk@mandriva.org> 2.26.3-1mdv2010.0
+ Revision: 390726
- update to new version 2.26.3

* Tue Apr 14 2009 Götz Waschk <waschk@mandriva.org> 2.26.1-1mdv2009.1
+ Revision: 366983
- new version
- drop patch

* Thu Apr 02 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-2mdv2009.1
+ Revision: 363504
- fix hanging ssh-agent (upstream bug #575247)
- remove all build workarounds
- spec fixes

* Sat Mar 14 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 355139
- new version
- update build deps

* Mon Mar 02 2009 Götz Waschk <waschk@mandriva.org> 2.25.92-1mdv2009.1
+ Revision: 347290
- update to new version 2.25.92

* Sat Feb 14 2009 Götz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 340324
- update to new version 2.25.91

* Mon Feb 02 2009 Götz Waschk <waschk@mandriva.org> 2.25.90-1mdv2009.1
+ Revision: 336659
- new version
- drop patch
- update file list

  + Funda Wang <fwang@mandriva.org>
    - drop static lib
    - use system libtool
    - Partial fix linkage

* Tue Jan 20 2009 Götz Waschk <waschk@mandriva.org> 2.25.5-1mdv2009.1
+ Revision: 331621
- new version
- disable --no-undefined
- update file list

* Fri Jan 09 2009 Götz Waschk <waschk@mandriva.org> 2.25.4.2-1mdv2009.1
+ Revision: 327381
- update to new version 2.25.4.2

* Tue Jan 06 2009 Götz Waschk <waschk@mandriva.org> 2.25.4.1-1mdv2009.1
+ Revision: 325242
- update to new version 2.25.4.1

* Mon Jan 05 2009 Götz Waschk <waschk@mandriva.org> 2.25.4-1mdv2009.1
+ Revision: 324946
- update to new version 2.25.4

* Thu Dec 18 2008 Götz Waschk <waschk@mandriva.org> 2.25.2-1mdv2009.1
+ Revision: 315883
- new version
- update file list

* Tue Nov 04 2008 Götz Waschk <waschk@mandriva.org> 2.25.1-1mdv2009.1
+ Revision: 299938
- update to new version 2.25.1

* Sun Oct 19 2008 Götz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 295218
- update to new version 2.24.1

* Sun Sep 21 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 286289
- fix build deps
- new version

* Mon Sep 08 2008 Götz Waschk <waschk@mandriva.org> 2.23.92-1mdv2009.0
+ Revision: 282460
- new version

* Wed Sep 03 2008 Götz Waschk <waschk@mandriva.org> 2.23.91-1mdv2009.0
+ Revision: 279783
- new version
- drop patch

* Tue Aug 19 2008 Götz Waschk <waschk@mandriva.org> 2.23.90-1mdv2009.0
+ Revision: 273785
- fix build deps
- new version
- fix build
- update file list

* Mon Aug 04 2008 Götz Waschk <waschk@mandriva.org> 2.23.6-1mdv2009.0
+ Revision: 262939
- new version

* Tue Jul 22 2008 Götz Waschk <waschk@mandriva.org> 2.23.5-1mdv2009.0
+ Revision: 240069
- new version
- update file list

* Mon Jun 30 2008 Götz Waschk <waschk@mandriva.org> 2.22.3-1mdv2009.0
+ Revision: 230367
- new version
- update license

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue May 27 2008 Götz Waschk <waschk@mandriva.org> 2.22.2-1mdv2009.0
+ Revision: 211558
- new version

* Wed Apr 09 2008 Götz Waschk <waschk@mandriva.org> 2.22.1-1mdv2009.0
+ Revision: 192453
- new version
- drop patch

* Wed Apr 02 2008 Frederic Crozat <fcrozat@mandriva.com> 2.22.0-2mdv2008.1
+ Revision: 191700
- Patch0 (SVN): fix daemon startup through dbus (GNOME bug #522253)

* Sun Mar 09 2008 Götz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183037
- new version

* Mon Feb 25 2008 Götz Waschk <waschk@mandriva.org> 2.21.92-1mdv2008.1
+ Revision: 174579
- new version

* Tue Feb 12 2008 Götz Waschk <waschk@mandriva.org> 2.21.91-1mdv2008.1
+ Revision: 165742
- new version

* Mon Jan 28 2008 Götz Waschk <waschk@mandriva.org> 2.21.90-1mdv2008.1
+ Revision: 159441
- new version

* Fri Jan 18 2008 Frederic Crozat <fcrozat@mandriva.com> 2.21.5-2mdv2008.1
+ Revision: 154728
- Fix the way pam module is installed and don't install .la file for it

* Mon Jan 14 2008 Götz Waschk <waschk@mandriva.org> 2.21.5-1mdv2008.1
+ Revision: 151325
- new version
- add gconf schema

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Götz Waschk <waschk@mandriva.org> 2.21.4-1mdv2008.1
+ Revision: 130172
- new version
- update file list

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 05 2007 Götz Waschk <waschk@mandriva.org> 2.21.3.2-1mdv2008.1
+ Revision: 115659
- new version

* Wed Dec 05 2007 Götz Waschk <waschk@mandriva.org> 2.21.3.1-1mdv2008.1
+ Revision: 115621
- new version
- update file list

* Mon Dec 03 2007 Götz Waschk <waschk@mandriva.org> 2.21.3-1mdv2008.1
+ Revision: 114601
- new version
- drop patch
- update buildrequires
- update file list

* Mon Dec 03 2007 Götz Waschk <waschk@mandriva.org> 2.20.2-2mdv2008.1
+ Revision: 114531
- fix environment in the pam module

* Sun Nov 25 2007 Götz Waschk <waschk@mandriva.org> 2.20.2-1mdv2008.1
+ Revision: 111863
- new version

* Mon Oct 15 2007 Götz Waschk <waschk@mandriva.org> 2.20.1-1mdv2008.1
+ Revision: 98576
- new version
- update file list

* Wed Sep 19 2007 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 90415
- new version
- new version

* Sun Aug 26 2007 Götz Waschk <waschk@mandriva.org> 2.19.91-1mdv2008.0
+ Revision: 71579
- new version

* Tue Aug 14 2007 Götz Waschk <waschk@mandriva.org> 2.19.90-1mdv2008.0
+ Revision: 62967
- new version
- new devel name

* Mon Jul 30 2007 Götz Waschk <waschk@mandriva.org> 2.19.6.1-2mdv2008.0
+ Revision: 56619
- fix buildrequires

* Mon Jul 30 2007 Götz Waschk <waschk@mandriva.org> 2.19.6.1-1mdv2008.0
+ Revision: 56586
- new version
- fix installation
- new version
- add pam module

* Sat Jul 07 2007 Götz Waschk <waschk@mandriva.org> 2.19.5-1mdv2008.0
+ Revision: 49369
- new version

* Mon Jun 18 2007 Götz Waschk <waschk@mandriva.org> 2.19.4.1-1mdv2008.0
+ Revision: 40993
- new version

* Sun Jun 17 2007 Götz Waschk <waschk@mandriva.org> 2.19.4-1mdv2008.0
+ Revision: 40610
- new version
- update file list

* Wed Jun 06 2007 Götz Waschk <waschk@mandriva.org> 2.19.2-2mdv2008.0
+ Revision: 36055
- fix buildrequires
- new version

* Tue Apr 17 2007 Götz Waschk <waschk@mandriva.org> 0.8.1-1mdv2008.0
+ Revision: 13824
- new version

