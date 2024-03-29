# TODO: /var/backups path is invalid (see FHS)
Summary:	Tape Oriented Backup
Summary(pl.UTF-8):	Kopie zapasowe na taśmie
Name:		tob
Version:	0.26
Release:	0.1
License:	GPL
Group:		Applications/Archiving
Source0:	http://tinyplanet.ca/code/%{name}/%{name}-%{version}.tgz
# Source0-md5:	de964a6e1b2d886591c0f324f291ae83
URL:		http://tinyplanet.ca/code/tob/
Requires:	afio
Requires:	sed
Requires:	tar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tob is a general driver for making and maintaining backups.

Given a set of `volume definitions', it creates tar or afio based
backups, and stores them either to a device in /dev, or a file in the
filesystem, to be burned to optical media later. Through a
straightforward configuration file, you can instruct tob to mount and
unmount devices before beginning backups.

tob supports full backups, differential backups (of the files which
were changed since the last full backup), and incremental backups (of
files changed since any previous backups). It lets you determine the
size of the backup before actually making it, maintain listings of
made backups, make remote backups and possibly more.

%description -l pl.UTF-8
tob jest programem służącym do tworzenia i zarządzania kopiami
zapasowymi.

Patrafi tworzyć kopie zapasowe w formacie tar lub afio i składować je
w na urządzeniach w /dev (streamer) lub w plikach, dla późniejszego
nagrania ich na nośniku optycznym. Poprzez plik konfiguracyjny można
wskazać tobowi, że ma montować i odmontowywać urządzenia przed
rozpoczęciem zgrywania kopii zapasowej.

tob obsługuje kopie pełne, różnicowe i przyrostowe, potrafi oszacować
potrzebna ilość miejsca przed przystąpieniem do kopiowania, a także
wykonywać kopie maszyn zdalnych.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d	$RPM_BUILD_ROOT{%{_var}/backups,%{_var}/lib/tob} \
		$RPM_BUILD_ROOT{%{_sysconfdir}/tob/volumes,%{_sbindir},%{_mandir}/man8}

install tob		 $RPM_BUILD_ROOT%{_sbindir}/tob
install example.exclude	 $RPM_BUILD_ROOT%{_sysconfdir}/tob/volumes
install example.startdir $RPM_BUILD_ROOT%{_sysconfdir}/tob/volumes
install tob.rc 		 $RPM_BUILD_ROOT%{_sysconfdir}/tob
install tob.8		 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc example.* README doc sample-rc contrib
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%{_var}/backups
%{_var}/lib/%{name}
%{_sysconfdir}/%{name}
