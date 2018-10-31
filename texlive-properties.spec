# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/properties
# catalog-date 2009-11-10 09:17:41 +0100
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-properties
Version:	0.2
Release:	11
Summary:	Load properties from a file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/properties
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/properties.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/properties.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package loads properties (key, value) from a properties
file, e.g. \jobname.properties.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/properties/properties.sty
%doc %{_texmfdistdir}/doc/latex/properties/readme.de
%doc %{_texmfdistdir}/doc/latex/properties/testprop.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 755127
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 719309
- texlive-properties
- texlive-properties
- texlive-properties
- texlive-properties

