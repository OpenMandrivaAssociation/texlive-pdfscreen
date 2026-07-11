%global tl_name pdfscreen
%global tl_revision 42428

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	Support screen-based document design
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdfscreen
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfscreen.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfscreen.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An extension of the hyperref package to provide a screen-based document
design. This package helps to generate pdf documents that are readable
on screen and will fit the screen's aspect ratio. Also it can be used
with various options to produce regular print versions of the same
document without any extra effort.

