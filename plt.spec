Summary:	PLT DrScheme
Name:		plt
Version:	202
Release:	0.1
License:	LGPL
Group:		Development/Languages
Source0:	%{name}.src.x.tar.gz
Patch0:		%{name}-install.patch
Url:		http://www.drscheme.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DrScheme, a pedagogical programming environment.

%prep
%setup -q -n plt

%build
cd src
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir},%{_datadir}/drscheme}

%{__make} -C src install prefix=$RPM_BUILD_ROOT%{_prefix}

mv $RPM_BUILD_ROOT%{_prefix}/{collects,teachpack} $RPM_BUILD_ROOT%{_datadir}/drscheme
mv $RPM_BUILD_ROOT%{_prefix}/man/man1 $RPM_BUILD_ROOT%{_mandir}

patch -p1 <%PATCH0
install install $RPM_BUILD_ROOT%{_bindir}/drscheme-install

perl -pi -e "s#$RPM_BUILD_ROOT##g" $RPM_BUILD_ROOT%{_bindir}/{background-help-desk,drscheme,drscheme-install,help-desk,mzc,setup-plt,tex2page}

%post
PLTHOME=%{_prefix}
PLTCOLLECTS=%{_datadir}/drscheme/collects
export PLTHOME PLTCOLLECTS
echo -e "n\ny\n" | %{_bindir}/drscheme-install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc notes/*
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.o
%{_datadir}/drscheme
%{_mandir}/man1/*
