# TODO:
# - build shared version
Summary:	PLT Scheme programming environment
Summary(pl):	¦rodowisko programistyczne PLT Scheme
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
PLT Scheme jest wspóln± nazw± dla rodziny implementacji jêzyków 
programowania Scheme.

%package mzscheme
Summary:	PLT Scheme implementation
Summary(pl):	Implementacja jêzyka PLT Scheme
Group:		Development/Languages

%description mzscheme
MzScheme is the PLT Scheme implementation. It implements
the language as described in the Revised^5 Report on the
Algorithmic Language Scheme and adds numerous extensions.

%description mzscheme -l pl
MzScheme jest implementacj± PLT Scheme. Implementuje jêzyk 
jak zdefiniowano w raporcie Revised^5 algorytmicznego jêzyka 
Scheme oraz dodaje ró¿ne rozszerzenia.

%package mred
Summary:	PLT graphical Scheme implementation
Summary(pl):	Graficzna implementacja jêzyka PLT Scheme
Group:		Development/Languages

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

%description drscheme
DrScheme is the graphical development environment for creating
MzScheme and MrEd applications.

%description drscheme -l pl
DrScheme jest graficznym ¶rodowiskiem do tworzenia aplikacji MzScheme 
i MrEd.

%package devel
Summary:	Development header files for PLT
Summary(pl):	Pliki nag³ówkowe dla PLT
Group:		Development/Languages

%description devel
This package contains the symlinks, headers and object files needed to 
compile and link programs which use PLT.

%description devel -l pl
Pakiet zawiera linki symboliczne, pliki nag³ówkowe i biblioteki niezbêdne 
do kompilacji i inkowania programów wykorzystuj±cych PLT.

%prep
%setup -q -n %{name}

%build
cd src
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir},%{_datadir}/drscheme}

%{__make} -C src install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

mv $RPM_BUILD_ROOT%{_prefix}/{collects,teachpack} $RPM_BUILD_ROOT%{_datadir}/drscheme
mv $RPM_BUILD_ROOT%{_prefix}/man/man1 $RPM_BUILD_ROOT%{_mandir}

#patch -p1 <%PATCH0
#install install $RPM_BUILD_ROOT%{_bindir}/drscheme-install

#perl -pi -e "s#$RPM_BUILD_ROOT##g" $RPM_BUILD_ROOT%{_bindir}/{background-help-desk,drscheme,drscheme-install,help-desk,mzc,setup-plt,tex2page}

#%post
#PLTHOME=%{_prefix}
#PLTCOLLECTS=%{_datadir}/drscheme/collects
#export PLTHOME PLTCOLLECTS
#echo -e "n\ny\n" | %{_bindir}/drscheme-install

%clean
rm -rf $RPM_BUILD_ROOT

%files mzscheme
%defattr(644,root,root,755)
%doc notes/mzscheme/*

%files mred
%defattr(644,root,root,755)

%files drscheme
%defattr(644,root,root,755)

%files devel
%defattr(644,root,root,755)

#%attr(755,root,root) %{_bindir}/*
#%{_includedir}/*
#%{_libdir}/*.a
#%{_libdir}/*.o
#%{_datadir}/drscheme
#%{_mandir}/man1/*
