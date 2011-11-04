# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/properties
# catalog-date 2009-11-10 09:17:41 +0100
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-properties
Version:	0.2
Release:	1
Summary:	Load properties from a file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/properties
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/properties.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/properties.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package loads properties (key, value) from a properties
file, e.g. \jobname.properties.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/properties/properties.sty
%doc %{_texmfdistdir}/doc/latex/properties/readme.de
%doc %{_texmfdistdir}/doc/latex/properties/testprop.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
