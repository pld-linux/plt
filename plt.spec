Summary:	PLT Scheme programming environment
Summary(pl):	¦rodowisko programistyczne PLT Scheme
Name:		plt
Version:	208
Release:	1
License:	LGPL
Group:		Development/Languages
Source0:	http://download.plt-scheme.org/bundles/%{version}/plt/%{name}-%{version}-src-unix.tgz
# Source0-md5:	0036e215d9402f7755b23cc875090f9e
Patch0:		%{name}-install.patch
URL:		http://www.drscheme.org/
BuildRequires:	expat-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	zlib-devel
ExcludeArch:	%{x8664} alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLT Scheme is an umbrella name for a family of implementations of the
Scheme programming language.

%description -l pl
PLT Scheme jest wspóln± nazw± dla rodziny implementacji jêzyków
programowania Scheme.

%package mzscheme
Summary:	PLT Scheme implementation
Summary(pl):	Implementacja jêzyka PLT Scheme
Group:		Development/Languages

%description mzscheme
MzScheme is the PLT Scheme implementation. It implements the language
as described in the Revised^5 Report on the Algorithmic Language
Scheme and adds numerous extensions.

%description mzscheme -l pl
MzScheme jest implementacj± PLT Scheme. Implementuje jêzyk
zdefiniowany w raporcie Revised^5 algorytmicznego jêzyka Scheme oraz
dodaje ró¿ne rozszerzenia.

%package mred
Summary:	PLT graphical Scheme implementation
Summary(pl):	Graficzna implementacja jêzyka PLT Scheme
Group:		Development/Languages
Requires:	%{name}-mzscheme = %{version}-%{release}

%description mred
MrEd is the PLT's graphical Scheme implementation. It embeds and
extends MzScheme with a graphical user interface (GUI) toolbox.

%description mred -l pl
MrEd jest graificzn± implementacj± jêzyka Scheme z PLT. Zawiera i
rozszerza MzScheme o zestaw narzêdzi do graficznego interfejsu
u¿ytkownika(GUI).

%package drscheme
Summary:	PLT Scheme graphical development environment
Summary(pl):	Graficzne ¶rodowisko programistyczne PLT Scheme
Group:		Development/Languages
Requires:	%{name}-mred = %{version}-%{release}

%description drscheme
DrScheme is the graphical development environment for creating
MzScheme and MrEd applications.

%description drscheme -l pl
DrScheme jest graficznym ¶rodowiskiem do tworzenia aplikacji MzScheme
i MrEd.

%package games
Summary:	Sample games from PLT Scheme
Summary(pl):	Przyk³adowe gry z projektu PLT Scheme
Group:		Applications/Games
Requires:	%{name}-mred = %{version}-%{release}

%description games
This package contains sample games from PLT Scheme project.

%description games -l pl
Pakiet zawiera przyk³adowe gry z projektu PLT Scheme.

%package help-desk
Summary:	Help desk for PLT Scheme
Summary(pl):	Pomoc dla PLT Scheme
Group:		Documentation
Requires:	%{name}-mred = %{version}-%{release}

%description help-desk
Help desk for PLT Scheme.

%description help-desk -l pl
Pakiet zawiera graficzn± pomoc dla PLT Scheme.

%package slideshow
Summary:	Slideshow from PLT Scheme
Summary(pl):	Pokaz slajdów z PLT Scheme
Group:		Applications/Graphics
Requires:	%{name}-mred = %{version}-%{release}

%description slideshow
Slideshow from PLT Scheme.

%description slideshow -l pl
Pokaz slajdów z PLT Scheme.

%package webserver
Summary:	Webserver from PLT Scheme
Summary(pl):	Serwer WEB z PLT Scheme
Group:		Applications/WWW
Requires:	%{name}-mred = %{version}-%{release}

%description webserver
Webserver from PLT Scheme.

%description slideshow -l pl
Serwer web z PLT Scheme.

%package devel
Summary:	Development header files for PLT
Summary(pl):	Pliki nag³ówkowe dla PLT
Group:		Development/Languages
Requires:	%{name}-mzscheme = %{version}-%{release}

%description devel
This package contains the symlinks, headers and object files needed to
compile and link programs which use PLT.

%description devel -l pl
Pakiet zawiera linki symboliczne, pliki nag³ówkowe i biblioteki
niezbêdne do kompilacji i inkowania programów wykorzystuj±cych PLT.

%prep
%setup -q -n %{name}

%build
cd src
%configure \
	--enable-shared \
	--prefix=$RPM_BUILD_ROOT%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir},%{_includedir},%{_libdir}/%{name}}

%{__make} -C src install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

mv $RPM_BUILD_ROOT%{_prefix}/{collects,teachpack} $RPM_BUILD_ROOT%{_libdir}/%{name}
mv $RPM_BUILD_ROOT%{_prefix}/man/man1 $RPM_BUILD_ROOT%{_mandir}

#temporary
ln -sf $RPM_BUILD_ROOT{%{_bindir},%{_includedir}} $RPM_BUILD_ROOT%{_libdir}/%{name}
ln -sf $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_libdir}/%{name}/lib

# emulate setup procedure
export PLTHOME=$RPM_BUILD_ROOT%{_libdir}/%{name}
cd $RPM_BUILD_ROOT%{_libdir}/%{name}
bin/mzscheme -qe "(dynamic-require '(lib \"setup.ss\" \"setup\") #f)"
cd -
for script in drscheme help-desk mzc setup-plt tex2page mzpp games mztext pdf-slatex slatex slideshow web* framework*; do
	perl -pi -e "s|PLTHOME=\"$RPM_BUILD_ROOT%{_libdir}/%{name}\"|PLTHOME=\"%{_libdir}/%{name}\"|" \
		$RPM_BUILD_ROOT%{_bindir}/$script
done
for file in `find $RPM_BUILD_ROOT/%{_libdir}/%{name}/collects -name *.dep`; do
	perl -pi -e 's|'$RPM_BUILD_ROOT'||' $file
done

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/{bin,lib,include}
ln -sf %{_bindir} %{_includedir}  $RPM_BUILD_ROOT%{_libdir}/%{name}
ln -sf %{_libdir} $RPM_BUILD_ROOT%{_libdir}/%{name}/lib

mv notes/teachpack/HISTORY teachpack.history

%clean
rm -rf $RPM_BUILD_ROOT

%files mzscheme
%defattr(644,root,root,755)
%doc notes/mzscheme/*
%doc notes/stepper
%attr(755,root,root) %{_bindir}/mzscheme
%attr(755,root,root) %{_bindir}/mzc
%attr(755,root,root) %{_bindir}/mzpp
%attr(755,root,root) %{_bindir}/mztext
%attr(755,root,root) %{_bindir}/pdf-slatex
%attr(755,root,root) %{_bindir}/slatex
%attr(755,root,root) %{_bindir}/setup-plt
%attr(755,root,root) %{_bindir}/tex2page

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/collects
%{_libdir}/%{name}/collects/xml
%{_libdir}/%{name}/collects/version
%{_libdir}/%{name}/collects/t*
%{_libdir}/%{name}/collects/setup
%{_libdir}/%{name}/collects/sgl
%{_libdir}/%{name}/collects/slatex
%{_libdir}/%{name}/collects/slibinit
%{_libdir}/%{name}/collects/srfi
%{_libdir}/%{name}/collects/stepper
%{_libdir}/%{name}/collects/string-constants
%{_libdir}/%{name}/collects/syntax*
%{_libdir}/%{name}/collects/p*
%{_libdir}/%{name}/collects/o*
%{_libdir}/%{name}/collects/n*
%{_libdir}/%{name}/collects/mz*
%{_libdir}/%{name}/collects/mrlib
%{_libdir}/%{name}/collects/make
%{_libdir}/%{name}/collects/l*
%{_libdir}/%{name}/collects/i*
%{_libdir}/%{name}/collects/hi*
%{_libdir}/%{name}/collects/ht*
%{_libdir}/%{name}/collects/graphics
%{_libdir}/%{name}/collects/f*
%{_libdir}/%{name}/collects/e*
%{_libdir}/%{name}/collects/dynext
%{_libdir}/%{name}/collects/compiler
%{_libdir}/%{name}/collects/browser
%{_libdir}/%{name}/collects/a*
%{_libdir}/%{name}/bin
%{_libdir}/%{name}/lib
%{_libdir}/%{name}/include
%{_mandir}/man1/mzscheme.1*
%{_mandir}/man1/tex2page.1*
%{_libdir}/*.so

%files games
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/games
%{_libdir}/%{name}/collects/games

%files help-desk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/help-desk
%{_libdir}/%{name}/collects/help
%{_libdir}/%{name}/collects/doc
%{_mandir}/man1/help-desk.1*

%files webserver
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/web-server*
%{_libdir}/%{name}/collects/web-server

%files slideshow
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/slideshow
%{_libdir}/%{name}/collects/slideshow

%files mred
%defattr(644,root,root,755)
%doc notes/mred/*
%attr(755,root,root) %{_bindir}/mred
%{_libdir}/%{name}/collects/mred
%{_mandir}/man1/mred.1*

%files drscheme
%defattr(644,root,root,755)
%doc notes/drscheme/* teachpack.history
%attr(755,root,root) %{_bindir}/drscheme
%{_libdir}/%{name}/collects/drscheme
%{_libdir}/%{name}/teachpack
%{_mandir}/man1/drscheme.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.la
%{_libdir}/*.o
%{_includedir}/*
