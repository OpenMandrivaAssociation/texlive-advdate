Name:		texlive-advdate
Version:	20538
Release:	2
Summary:	Print a date relative to "today"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/advdate
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/advdate.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/advdate.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
