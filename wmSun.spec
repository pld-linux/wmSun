Summary: wmSun displays the current day's Sun Rise and Set Times
%define version 1.03
Name: wmSun
Version: %{version}
Release: 1
Copyright: GPL
Group: X Windows/Window Managers
Source: ftp://leadbelly.lanl.gov/pub/mgh/%{name}-%{version}.tar.gz
Packager: Ian Macdonald <ianmacd@xs4all.nl>
BuildRoot: /var/tmp/%{name}-root

%description
wmSun displays the current day's Sun Rise and Set Times.
You must enter your LAtitude and Longitude correctly for it to work.

%prep
%setup

%build
touch %{name}/%{name}.c
make -C %{name}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man1}
install -s -m 755 %{name}/%{name} $RPM_BUILD_ROOT/usr/X11R6/bin
install -m 444 %{name}/%{name}.1 $RPM_BUILD_ROOT/usr/X11R6/man/man1

%files
%defattr(-,root,root)
/usr/X11R6/bin/%{name}
/usr/X11R6/man/man1/%{name}.1
%doc BUGS COPYING TODO

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Feb 9 1998 Ian Macdonald <ianmacd@xs4all.nl>

- first RPM release
