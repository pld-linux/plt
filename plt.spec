Summary:	PLT Scheme programming environment
Summary(pl.UTF-8):	Środowisko programistyczne PLT Scheme
Name:		plt
Version:	4.2.4
Release:	3
License:	LGPL
Group:		Development/Languages
Source0:	http://download.plt-scheme.org/bundles/%{version}/plt/%{name}-%{version}-src-unix.tgz
# Source0-md5:	7a21fcb5b565b8c352aa22e1698eb05b
Patch0:		%{name}-libpng14.patch
URL:		http://www.drscheme.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	expat-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
%if "%{pld_release}" == "ac"
BuildRequires:	xrender-devel
BuildRequires:	X11-OpenGL-libGL
%else
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXt-devel
%endif
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLT Scheme is an umbrella name for a family of implementations of the
Scheme programming language.

%description -l pl.UTF-8
PLT Scheme jest wspólną nazwą dla rodziny implementacji języków
programowania Scheme.

%package mzscheme
Summary:	PLT Scheme implementation
Summary(pl.UTF-8):	Implementacja języka PLT Scheme
Group:		Development/Languages

%description mzscheme
MzScheme is the PLT Scheme implementation. It implements the language
as described in the Revised^5 Report on the Algorithmic Language
Scheme and adds numerous extensions.

%description mzscheme -l pl.UTF-8
MzScheme jest implementacją PLT Scheme. Implementuje język
zdefiniowany w raporcie Revised^5 algorytmicznego języka Scheme oraz
dodaje różne rozszerzenia.

%package mred
Summary:	PLT graphical Scheme implementation
Summary(pl.UTF-8):	Graficzna implementacja języka PLT Scheme
Group:		Development/Languages
Requires:	%{name}-mzscheme = %{version}-%{release}

%description mred
MrEd is the PLT's graphical Scheme implementation. It embeds and
extends MzScheme with a graphical user interface (GUI) toolbox.

%description mred -l pl.UTF-8
MrEd jest graificzną implementacją języka Scheme z PLT. Zawiera i
rozszerza MzScheme o zestaw narzędzi do graficznego interfejsu
użytkownika(GUI).

%package drscheme
Summary:	PLT Scheme graphical development environment
Summary(pl.UTF-8):	Graficzne środowisko programistyczne PLT Scheme
Group:		Development/Languages
Requires:	%{name}-mred = %{version}-%{release}

%description drscheme
DrScheme is the graphical development environment for creating
MzScheme and MrEd applications.

%description drscheme -l pl.UTF-8
DrScheme jest graficznym środowiskiem do tworzenia aplikacji MzScheme
i MrEd.

%package games
Summary:	Sample games from PLT Scheme
Summary(pl.UTF-8):	Przykładowe gry z projektu PLT Scheme
Group:		Applications/Games
Requires:	%{name}-mred = %{version}-%{release}

%description games
This package contains sample games from PLT Scheme project.

%description games -l pl.UTF-8
Pakiet zawiera przykładowe gry z projektu PLT Scheme.

%package docs
Summary:	Documentation for PLT Scheme
Summary(pl.UTF-8):	Dokumentacja dla PLT Scheme
Group:		Documentation

%description docs
Documentation for PLT Scheme.

%description docs -l pl.UTF-8
Pakiet zawiera dokumentację dla PLT Scheme.

%package slideshow
Summary:	Slideshow from PLT Scheme
Summary(pl.UTF-8):	Pokaz slajdów z PLT Scheme
Group:		Applications/Graphics
Requires:	%{name}-mred = %{version}-%{release}

%description slideshow
Slideshow from PLT Scheme.

%description slideshow -l pl.UTF-8
Pokaz slajdów z PLT Scheme.

%package webserver
Summary:	Webserver from PLT Scheme
Summary(pl.UTF-8):	Serwer WWW z PLT Scheme
Group:		Applications/WWW

%description webserver
Webserver from PLT Scheme.

%description webserver -l pl.UTF-8
Serwer web z PLT Scheme.

%package devel
Summary:	Development header files for PLT
Summary(pl.UTF-8):	Pliki nagłówkowe dla PLT
Group:		Development/Languages
Requires:	%{name}-mzscheme = %{version}-%{release}

%description devel
This package contains the symlinks, headers and object files needed to
compile and link programs which use PLT.

%description devel -l pl.UTF-8
Pakiet zawiera linki symboliczne, pliki nagłówkowe i biblioteki
niezbędne do kompilacji i inkowania programów wykorzystujących PLT.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
cd src/mzscheme
%{__libtoolize}
%{__aclocal}
%{__autoconf}
cd ..
ln -sf mzscheme/configure .
%configure \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir},%{_includedir},%{_libdir}/%{name}}

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/collects/{mysterx,mzcom}

%clean
rm -rf $RPM_BUILD_ROOT

%files mzscheme
%defattr(644,root,root,755)
%doc doc/release-notes/{mzscheme,redex,stepper}
%attr(755,root,root) %{_bindir}/mzc
%attr(755,root,root) %{_bindir}/mzpp
%attr(755,root,root) %{_bindir}/mzscheme
%attr(755,root,root) %{_bindir}/mztext
%attr(755,root,root) %{_bindir}/pdf-slatex
%attr(755,root,root) %{_bindir}/planet
%attr(755,root,root) %{_bindir}/plt-r5rs
%attr(755,root,root) %{_bindir}/plt-r6rs
%attr(755,root,root) %{_bindir}/scribble
%attr(755,root,root) %{_bindir}/setup-plt
%attr(755,root,root) %{_bindir}/slatex
%attr(755,root,root) %{_bindir}/swindle
%attr(755,root,root) %{_bindir}/tex2page

%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/starter
%{_libdir}/%{name}/buildinfo
%dir %{_libdir}/%{name}/collects
%{_libdir}/%{name}/collects/2htdp
%{_libdir}/%{name}/collects/afm
%{_libdir}/%{name}/collects/algol60
%{_libdir}/%{name}/collects/at-exp
%{_libdir}/%{name}/collects/browser
%{_libdir}/%{name}/collects/combinator-parser
%{_libdir}/%{name}/collects/compiler
%{_libdir}/%{name}/collects/config
%{_libdir}/%{name}/collects/defaults
%{_libdir}/%{name}/collects/deinprogramm
%{_libdir}/%{name}/collects/dynext
%{_libdir}/%{name}/collects/eopl
%{_libdir}/%{name}/collects/errortrace
%{_libdir}/%{name}/collects/ffi
%{_libdir}/%{name}/collects/file
%{_libdir}/%{name}/collects/framework
%{_libdir}/%{name}/collects/frtime
%{_libdir}/%{name}/collects/graphics
%{_libdir}/%{name}/collects/help
%{_libdir}/%{name}/collects/hierlist
%{_libdir}/%{name}/collects/htdp
%{_libdir}/%{name}/collects/html
%{_libdir}/%{name}/collects/icons
%{_libdir}/%{name}/collects/info-domain
%{_libdir}/%{name}/collects/lang
%{_libdir}/%{name}/collects/launcher
%{_libdir}/%{name}/collects/lazy
%{_libdir}/%{name}/collects/make
%{_libdir}/%{name}/collects/mrlib
%{_libdir}/%{name}/collects/mzlib
%{_libdir}/%{name}/collects/mzscheme
%{_libdir}/%{name}/collects/net
%{_libdir}/%{name}/collects/openssl
%{_libdir}/%{name}/collects/parser-tools
%{_libdir}/%{name}/collects/planet
%{_libdir}/%{name}/collects/plot
%{_libdir}/%{name}/collects/preprocessor
%{_libdir}/%{name}/collects/profile
%{_libdir}/%{name}/collects/r5rs
%{_libdir}/%{name}/collects/r6rs
%{_libdir}/%{name}/collects/readline
%{_libdir}/%{name}/collects/redex
%{_libdir}/%{name}/collects/rnrs
%{_libdir}/%{name}/collects/s-exp
%{_libdir}/%{name}/collects/scheme
%{_libdir}/%{name}/collects/scribble
%{_libdir}/%{name}/collects/scribblings
%{_libdir}/%{name}/collects/scriblib
%{_libdir}/%{name}/collects/setup
%{_libdir}/%{name}/collects/sgl
%{_libdir}/%{name}/collects/slatex
%{_libdir}/%{name}/collects/srfi
%{_libdir}/%{name}/collects/stepper
%{_libdir}/%{name}/collects/string-constants
%{_libdir}/%{name}/collects/swindle
%{_libdir}/%{name}/collects/syntax
%{_libdir}/%{name}/collects/syntax-color
%{_libdir}/%{name}/collects/test-box-recovery
%{_libdir}/%{name}/collects/test-engine
%{_libdir}/%{name}/collects/tests
%{_libdir}/%{name}/collects/tex2page
%{_libdir}/%{name}/collects/texpict
%{_libdir}/%{name}/collects/trace
%{_libdir}/%{name}/collects/typed
%{_libdir}/%{name}/collects/typed-scheme
%{_libdir}/%{name}/collects/unstable
%{_libdir}/%{name}/collects/version
%{_libdir}/%{name}/collects/wxme
%{_libdir}/%{name}/collects/xml
%{_mandir}/man1/mzc.1*
%{_mandir}/man1/mzscheme.1*
%{_mandir}/man1/setup-plt.1*
%{_mandir}/man1/tex2page.1*
%{_libdir}/*.so

%files games
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/plt-games
%{_libdir}/%{name}/collects/games

%files docs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/plt-help
%{_libdir}/%{name}/collects/help
%{_libdir}/%{name}/collects/scribblings
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/doc
%{_mandir}/man1/plt-help.1*

%files webserver
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/plt-web-server*
%{_libdir}/%{name}/collects/web-server

%files slideshow
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/slideshow
%{_libdir}/%{name}/collects/slideshow

%files mred
%defattr(644,root,root,755)
%doc doc/release-notes/mred/*
%attr(755,root,root) %{_bindir}/mred
%attr(755,root,root) %{_bindir}/mred-text
%{_libdir}/%{name}/collects/embedded-gui
%{_libdir}/%{name}/collects/mred
%{_mandir}/man1/mred.1*

%files drscheme
%defattr(644,root,root,755)
%doc doc/release-notes/{drscheme,teachpack}
%attr(755,root,root) %{_bindir}/drscheme
%{_libdir}/%{name}/collects/drscheme
%{_libdir}/%{name}/collects/gui-debugger
%{_libdir}/%{name}/collects/macro-debugger
%{_libdir}/%{name}/collects/teachpack
%{_mandir}/man1/drscheme.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.la
%{_libdir}/plt/*.o
%{_includedir}/*
