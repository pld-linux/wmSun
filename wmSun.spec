Summary:	wmSun displays the current day's Sun Rise and Set Times
Summary(pl):	wmSun wy¶wietla aktualny czas wschodu i zachodu S³oñca
Name:		wmSun
Version:	1.03
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	ftp://leadbelly.lanl.gov/pub/mgh/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description
wmSun displays the current day's Sun Rise and Set Times. You must
enter your LAtitude and Longitude correctly for it to work.

%description -l pl
wmSun wy¶wietla aktualne godziny wschodu i zachodu S³oñca. Aby program
dzia³a³ poprawnie, musisz podaæ w³a¶ciw± dla miejsca, w którym
przebywasz, d³ugo¶æ i szeroko¶æ geograficzn±.

%prep
%setup -q

%build
%{__make} -C %{name} clean
%{__make} -C %{name} \
        CFLAGS="%{rpmcflags} -Wall" \
	INCDIR="-I%{_includedir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
        $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf BUGS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,TODO}.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_applnkdir}/DockApplets/wmSun.desktop
