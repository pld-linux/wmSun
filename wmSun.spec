Summary:	wmSun displays the current day's Sun Rise and Set Times
Summary(pl):	wmSun wy¶wietla aktualny czas wschodu i zachodu s³oñca
Name:		wmSun
Version:	1.03
Release:	3
Copyright:	GPL
Group:          X11/Window Managers/Tools
Group(pl):      X11/Zarz±dcy Okien/Narzêdzia
Source0: 	ftp://leadbelly.lanl.gov/pub/mgh/%{name}-%{version}.tar.gz
Source1:	wmSun.desktop
BuildRequires:    XFree86-devel
BuildRequires:    xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6
%define _mandir %{_prefix}/man

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
make -C %{name} clean
make -C %{name} \
        CFLAGS="$RPM_OPT_FLAGS -Wall" \
	INCDIR="-I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
        $RPM_BUILD_ROOT/usr/X11R6/share/applnk/DockApplets

install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/DockApplets

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	BUGS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,TODO}.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
/usr/X11R6/share/applnk/DockApplets/wmSun.desktop
