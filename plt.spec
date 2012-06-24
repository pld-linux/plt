Summary:	PLT Scheme programming environment
Summary(pl):	�rodowisko programistyczne PLT Scheme
Name:		plt
Version:	208
Release:	0.1
License:	LGPL
Group:		Development/Languages
Source0:	http://download.plt-scheme.org/bundles/%{version}/plt/%{name}-%{version}-src-unix.tgz
# Source0-md5:	0036e215d9402f7755b23cc875090f9e
Patch0:		%{name}-install.patch
URL:		http://www.drscheme.org/
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLT Scheme is an umbrella name for a family of implementations of the                                                      
Scheme programming language.                                                                                               

%description -l pl
PLT Scheme jest wsp�ln� nazw� dla rodziny implementacji j�zyk�w 
programowania Scheme.

%package mzscheme
Summary:	PLT Scheme implementation
Summary(pl):	Implementacja j�zyka PLT Scheme
Group:		Development/Languages

%description mzscheme
MzScheme is the PLT Scheme implementation. It implements
the language as described in the Revised^5 Report on the
Algorithmic Language Scheme and adds numerous extensions.

%description mzscheme -l pl
MzScheme jest implementacj� PLT Scheme. Implementuje j�zyk 
jak zdefiniowano w raporcie Revised^5 algorytmicznego j�zyka 
Scheme oraz dodaje r�ne rozszerzenia.

%package mred
Summary:	PLT graphical Scheme implementation
Summary(pl):	Graficzna implementacja j�zyka PLT Scheme
Group:		Development/Languages
Requires:	%{name}-mzscheme = %{version}-%{release}

%description mred
MrEd is the PLT's graphical Scheme implementation. It embeds and 
extends MzScheme with a graphical user interface (GUI) toolbox.

%description mred -l pl
MrEd jest graificzn� implementacj� j�zyka Scheme z PLT. Zawiera i
rozszerza MzScheme o zestaw narz�dzi do graficznego interfejsu 
u�ytkownika(GUI).

%package drscheme
Summary:	PLT Scheme graphical development environment
Summary(pl):	Graficzne �rodowisko programistyczne PLT Scheme
Group:		Development/Languages
Requires:	%{name}-mred = %{version}-%{release}

%description drscheme
DrScheme is the graphical development environment for creating
MzScheme and MrEd applications.

%description drscheme -l pl
DrScheme jest graficznym �rodowiskiem do tworzenia aplikacji MzScheme 
i MrEd.

%package games
Summary:	Sample games from PLT Scheme
Summary(pl):	Przyk�adowe gry z projektu PLT Scheme
Group:		Applications/Games
Requires:	%{name}-mred = %{version}-%{release}

%description games
This package contains sample games from PLT Scheme project.

%description games -l pl
Pakiet zawiera przyk�adowe gry z projektu PLT Scheme.

%package devel
Summary:	Development header files for PLT
Summary(pl):	Pliki nag��wkowe dla PLT
Group:		Development/Languages
Requires:	%{name}-mzscheme = %{version}-%{release}

%description devel
This package contains the symlinks, headers and object files needed to 
compile and link programs which use PLT.

%description devel -l pl
Pakiet zawiera linki symboliczne, pliki nag��wkowe i biblioteki niezb�dne 
do kompilacji i inkowania program�w wykorzystuj�cych PLT.

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

#cp -p -r collects teachpack $RPM_BUILD_ROOT%{_libdir}/%{name}
ln -sf %{_bindir} $RPM_BUILD_ROOT%{_libdir}/%{name}/bin

#cd src/mzscheme 
#%{__make} install \
#	 prefix=$RPM_BUILD_ROOT%{_prefix}
#cd ../..

# emulate setup procedure
export PLTHOME=$RPM_BUILD_ROOT/%{_libdir}/%{name}
(cd $RPM_BUILD_ROOT/%{_libdir}/%{name} && bin/mzscheme -qe "(dynamic-require '(lib \"setup.ss\" \"setup\") #f)")
for script in drscheme help-desk mzc setup-plt tex2page mzpp games mztext pdf-slatex slatex slideshow web* framework*; do
	perl -pi -e "s|PLTHOME=\"$RPM_BUILD_ROOT%{_prefix}\"|PLTHOME=\"%{_libdir}/%{name}\"|" \
		$RPM_BUILD_ROOT%{_bindir}/$script
done
for file in `find $RPM_BUILD_ROOT/%{_libdir}/%{name}/collects -name *.dep`; do
	perl -pi -e 's|'$RPM_BUILD_ROOT'||' $file
done

%clean
rm -rf $RPM_BUILD_ROOT

%files mzscheme
%defattr(644,root,root,755)
%doc notes/mzscheme/*
%attr(755,root,root) %{_bindir}/help-desk
%attr(755,root,root) %{_bindir}/mzscheme
%attr(755,root,root) %{_bindir}/mzc
%attr(755,root,root) %{_bindir}/setup-plt
%attr(755,root,root) %{_bindir}/tex2page
%attr(755,root,root) %{_bindir}/web-server
%attr(755,root,root) %{_bindir}/web-server-monitor
%attr(755,root,root) %{_bindir}/web-server-text

# not sure...
%attr(755,root,root) %{_bindir}/mzpp
%attr(755,root,root) %{_bindir}/mztext
%attr(755,root,root) %{_bindir}/pdf-slatex
%attr(755,root,root) %{_bindir}/slatex
%attr(755,root,root) %{_bindir}/slideshow

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/collects
%{_libdir}/%{name}/collects/xml
%{_libdir}/%{name}/collects/web-server
%{_libdir}/%{name}/collects/version
%{_libdir}/%{name}/collects/t*
%{_libdir}/%{name}/collects/s*
%{_libdir}/%{name}/collects/p*
%{_libdir}/%{name}/collects/o*
%{_libdir}/%{name}/collects/n*
%{_libdir}/%{name}/collects/mz*
%{_libdir}/%{name}/collects/mrlib
%{_libdir}/%{name}/collects/make
%{_libdir}/%{name}/collects/l*
%{_libdir}/%{name}/collects/i*
%{_libdir}/%{name}/collects/h*
%{_libdir}/%{name}/collects/graphics
%{_libdir}/%{name}/collects/f*
%{_libdir}/%{name}/collects/e*
%{_libdir}/%{name}/collects/dynext
%{_libdir}/%{name}/collects/doc
%{_libdir}/%{name}/collects/compiler
%{_libdir}/%{name}/collects/browser
%{_libdir}/%{name}/collects/a*
%{_libdir}/%{name}/bin
%{_mandir}/man1/mzscheme.1*
%{_mandir}/man1/help-desk.1*
%{_mandir}/man1/tex2page.1*
%{_libdir}/*.so

%files games
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/games
%{_libdir}/%{name}/collects/games

%files mred
%defattr(644,root,root,755)
%doc notes/mred/*
%attr(755,root,root) %{_bindir}/mred
%{_libdir}/%{name}/collects/mred
%{_mandir}/man1/mred.1*

%files drscheme
%defattr(644,root,root,755)
%doc notes/drscheme/*
%attr(755,root,root) %{_bindir}/drscheme
%{_libdir}/%{name}/collects/drscheme
%{_libdir}/%{name}/teachpack
%{_mandir}/man1/drscheme.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.o
