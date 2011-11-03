# revision 20538
# category Package
# catalog-ctan /macros/latex/contrib/advdate
# catalog-date 2010-11-22 09:08:01 +0100
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-advdate
Version:	20101122
Release:	1
Summary:	Print a date relative to "today"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/advdate
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/advdate.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/advdate.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Provides macros which can add a specified number of days to the
current date (as specified in \today), to save, set and restore
the 'current date' and print it. Intended for use, for example,
in invoices payable within 14 days from today etc. Has only
been tested with Czech dates.

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
%{_texmfdistdir}/tex/latex/advdate/advdate.sty
%doc %{_texmfdistdir}/doc/latex/advdate/advdate.pdf
%doc %{_texmfdistdir}/doc/latex/advdate/advdate.tex
%doc %{_texmfdistdir}/doc/latex/advdate/manifest.txt
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