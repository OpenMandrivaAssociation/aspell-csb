%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.02-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Kashubian
%define languagecode csb
# FIXME: no locale yet
%define lc_ctype csb_XX

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.02.0
Release:       2
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/csb/aspell6-csb-0.02-0.tar.bz2
URL:		   http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-%{languagecode}

BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
#Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
#Provides:      aspell-%{lc_ctype}

Autoreqprov:   no

%description
An %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build
# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

chmod 644 Copyright README* 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright 
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.01.1-6mdv2011.0
+ Revision: 616608
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 0.01.1-5mdv2010.0
+ Revision: 423965
- rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 0.01.1-4mdv2009.0
+ Revision: 226180
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.01.1-3mdv2008.1
+ Revision: 182408
- provide enchant-dictionary

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.01.1-2mdv2008.1
+ Revision: 135824
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - s/Mandrake/Mandriva/


* Mon Mar 05 2007 Oden Eriksson <oeriksson@mandriva.com> 0.01.1-2mdv2007.0
+ Revision: 132947
- Import aspell-csb

* Mon Mar 05 2007 Oden Eriksson <oeriksson@mandriva.com> 0.01.1-2mdv2007.1
- disable debug packages

* Tue Nov 29 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.01.1-1mdk
- first version


