# revision 20538
# category Package
# catalog-ctan /macros/latex/contrib/advdate
# catalog-date 2010-11-22 09:08:01 +0100
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-advdate
Version:	20180303
Release:	2
Summary:	Print a date relative to "today"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/advdate
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/advdate.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/advdate.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides macros which can add a specified number of days to the
current date (as specified in \today), to save, set and restore
the 'current date' and print it. Intended for use, for example,
in invoices payable within 14 days from today etc. Has only
been tested with Czech dates.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/advdate/advdate.sty
%doc %{_texmfdistdir}/doc/latex/advdate/advdate.pdf
%doc %{_texmfdistdir}/doc/latex/advdate/advdate.tex
%doc %{_texmfdistdir}/doc/latex/advdate/manifest.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20101122-2
+ Revision: 749091
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20101122-1
+ Revision: 717799
- texlive-advdate
- texlive-advdate
- texlive-advdate
- texlive-advdate
- texlive-advdate

