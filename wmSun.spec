Summary:	wmSun displays the current day's Sun Rise and Set Times
Summary(pl):	wmSun wy¶wietla aktualny czas wschodu i zachodu S³oñca
Name:		wmSun
Version:	1.03
Release:	6
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://nis-www.lanl.gov/~mgh/WindowMaker/%{name}-%{version}.tar.gz
# Source0-md5:	defc6747ebdb64b5d3afe91f916d3acc
Source1:	%{name}.desktop
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmSun displays the current day's Sun Rise and Set Times. You must
enter your LAtitude and Longitude correctly for it to work.

%description -l pl
wmSun wy¶wietla aktualne godziny wschodu i zachodu S³oñca. Aby program
dzia³a³ poprawnie trzeba podaæ d³ugo¶æ i szeroko¶æ geograficzn± dla
miejsca, w którym przebywamy.

%prep
%setup -q

%build
%{__make} -C %{name} clean
%{__make} -C %{name} \
	CFLAGS="%{rpmcflags} -Wall" \
	LIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_desktopdir}/docklets}

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_desktopdir}/docklets/wmSun.desktop
