Summary:	Tape Oriented Backup
Summary(pl):	Kopie zapasowone na ta¶mie
Name:		tob
Version:	0.25
Release:	1
License:	GPL
Group:		Applications/Archiving
Source0:	http://tinyplanet.ca/projects/tob/%{name}-%{version}.tgz
# Source0-md5:	fd24b96e9bce5129e22f14f17a3ff587
URL:		http://tinyplanet.ca/projects/tob/
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

%description -l pl
tob jest programem s³u¿±cym do tworzenia i zarz±dzania kopiami
zapasowymi.

Patrafi tworzyæ kopie zapasowe w formacie tar lub afio i sk³adowaæ je
w na urz±dzeniach w /dev (streamer) lub w plikach, dla pó¿niejszego
nagrania ich na no¶niku optycznym. Poprzez plik konfiguracyjny mo¿na
wskazac tobowi, ¿e ma montowaæ i odmontowywaæ urz±dzenia przed
rozpoczêciem zgrywania kopii zapasowej.

tob obs³uguje kopie pe³ne, ró¿nicowe i przyrostowe, potrafi oszacowac
potrzebna ilo¶æ miejsca przed przyst±pieniem do kopiowania, a tak¿e
wykonywaæ kopie maszyn zdalnych.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
