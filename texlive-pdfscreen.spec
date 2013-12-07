# revision 27510
# category Package
# catalog-ctan /macros/latex/contrib/pdfscreen
# catalog-date 2012-07-18 20:44:29 +0200
# catalog-license lppl
# catalog-version 1.5
Name:		texlive-pdfscreen
Version:	1.5
Release:	4
Summary:	Support screen-based document design
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdfscreen
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfscreen.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfscreen.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
An extension of the hyperref package to provide a screen-based
document design. This package helps to generate pdf documents
that are readable on screen and will fit the screen's aspect
ratio. Also it can be used with various options to produce
regular print versions of the same document without any extra
effort.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pdfscreen/but.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/button.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/left.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay0.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay1.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay10.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay2.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay3.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay4.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay5.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay6.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay7.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay8.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/overlay9.pdf
%{_texmfdistdir}/tex/latex/pdfscreen/pdfscreen.sty
%{_texmfdistdir}/tex/latex/pdfscreen/right.pdf
%doc %{_texmfdistdir}/doc/latex/pdfscreen/logo.pdf
%doc %{_texmfdistdir}/doc/latex/pdfscreen/manual-print.pdf
%doc %{_texmfdistdir}/doc/latex/pdfscreen/manual-screen.pdf
%doc %{_texmfdistdir}/doc/latex/pdfscreen/manual.tex
%doc %{_texmfdistdir}/doc/latex/pdfscreen/nopanel.pdf
%doc %{_texmfdistdir}/doc/latex/pdfscreen/pdfscreen.cfg.specimen
%doc %{_texmfdistdir}/doc/latex/pdfscreen/portrait.pdf
%doc %{_texmfdistdir}/doc/latex/pdfscreen/print.pdf
%doc %{_texmfdistdir}/doc/latex/pdfscreen/slide.pdf
%doc %{_texmfdistdir}/doc/latex/pdfscreen/slide.tex
%doc %{_texmfdistdir}/doc/latex/pdfscreen/square.pdf
%doc %{_texmfdistdir}/doc/latex/pdfscreen/tex.png
%doc %{_texmfdistdir}/doc/latex/pdfscreen/widepanel.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
