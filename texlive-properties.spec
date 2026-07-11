%global tl_name properties
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Load properties from a file
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/properties
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/properties.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/properties.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package loads properties (key, value) from a properties file, e.g.
\jobname.properties.

