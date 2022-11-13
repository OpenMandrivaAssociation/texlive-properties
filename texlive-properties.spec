Name:		texlive-properties
Version:	15878
Release:	1
Summary:	Load properties from a file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/properties
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/properties.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/properties.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
