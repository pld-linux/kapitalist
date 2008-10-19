#
# TODO
# - install documentation
# - call autotools
#
Summary:	The Monopoly®-like board game.
Summary(pl.UTF-8):	Gra planszowa typu Monopoly®.
Name:		kapitalist
Version:	0.4
Release:	0.1
License:	GPL v2
Group:		Applications/Games/Boards
Source0:	http://dl.sourceforge.net/capitalist/kapitalist-0.4.tar.gz
# Source0-md5:	6733eec1d441d05b8df8ce3d91d5e7ca
Suggests:	capitalist
URL:		http://kapitalist.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kapitalist is a Monopoly®-like board game for 2-8 players. Walk around the
board, buy properties, receive rent from your competitors, try to get
monopolies to build houses and hotels on them and finally be the richest on
the board.

This package contains a client. You should also install the capitalist
package.

%description -l pl.UTF-8
Kapitalist jest grą planszową typu Monopoly® dla 2-8 graczy. Przemierzaj
planszę, kupuj nieruchomości, otrzymuj renty od współzawodników, spróbuj
zdobyć wyłączność na budowę domów i hoteli na poszczególnych posiadłościach,
ostatecznie zostań najbogatszym z graczy na planszy.

Ten pakiet zawiera klienta. Aby móc grać powinieneś również zainstalować pakiet
capitalist.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/applnk

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/kapitalist

%{_datadir}/apps/kapitalist
%{_datadir}/icons/hicolor/16x16/apps/kapitalist.png
%{_datadir}/icons/hicolor/32x32/apps/kapitalist.png
