Summary:	wmSun displays the current day's Sun Rise and Set Times
Summary(pl):	wmSun wy¶wietla aktualny czas wschodu i zachodu s³oñca
Name:		wmSun
Version:	1.03
Release:	2
Copyright:	GPL
Group:          X11/Window Managers/Tools
Group(pl):      X11/Zarz±dcy Okien/Narzêdzia
Source0: 	ftp://leadbelly.lanl.gov/pub/mgh/%{name}-%{version}.tar.gz
Source1:	wmSun.wmconfig
BuildPrereq:    XFree86-devel
BuildPrereq:    xpm-devel
BuildRoot:      /tmp/%{name}-%{version}-root

%description
wmSun displays the current day's Sun Rise and Set Times.
You must enter your LAtitude and Longitude correctly for it to work.

%description -l pl
wmSun wy¶wietla aktualne godziny wschodu i zachodu s³oñca.
Aby program dzia³a³ poprawnie, musisz podaæ w³a¶ciw± dla
miejsca, w którym przebywasz, d³ugo¶æ i szeroko¶æ geograficzn±.

%prep
%setup -q

%build
make -C wmSun clean
make -C wmSun \
        CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/{bin,share/man/man1} \
	$RPM_BUILD_ROOT/etc/X11/wmconfig

install -s wmSun/wmSun $RPM_BUILD_ROOT/usr/X11R6/bin
install wmSun/wmSun.1 $RPM_BUILD_ROOT/usr/X11R6/share/man/man1

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/wmSun

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/share/man/man1/* \
	BUGS TODO

%files
%defattr(644,root,root,755)
%doc {BUGS,TODO}.gz
%attr(755,root,root) /usr/X11R6/bin/wmSun
/usr/X11R6/share/man/man1/wmSun.1.gz
/etc/X11/wmconfig/wmSun

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun May 16 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.03-2]
- modified spec file for PLD use,
- package is now FHS 2.0 compliant.	

* Tue Feb 9 1998 Ian Macdonald <ianmacd@xs4all.nl>
- first RPM release.
