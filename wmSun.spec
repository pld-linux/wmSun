Summary:	wmSun displays the current day's Sun Rise and Set Times
Summary(pl.UTF-8):	wmSun wyświetla aktualny czas wschodu i zachodu Słońca
Name:		wmSun
Version:	1.03
Release:	7
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://nis-www.lanl.gov/~mgh/WindowMaker/%{name}-%{version}.tar.gz
# Source0-md5:	defc6747ebdb64b5d3afe91f916d3acc
Source1:	%{name}.desktop
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmSun displays the current day's Sun Rise and Set Times. You must
enter your LAtitude and Longitude correctly for it to work.

%description -l pl.UTF-8
wmSun wyświetla aktualne godziny wschodu i zachodu Słońca. Aby program
działał poprawnie trzeba podać długość i szerokość geograficzną dla
miejsca, w którym przebywamy.

%prep
%setup -q

%build
%{__make} -C %{name} clean
%{__make} -C %{name} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

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
