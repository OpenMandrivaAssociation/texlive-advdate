%global tl_name advdate
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Print a date relative to today
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/advdate
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/advdate.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/advdate.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides macros which can add a specified number of days to the current
date (as specified in \today), to save, set and restore the 'current
date' and to print it. Intended use is, for example, in invoices
"payable within 14 days from today", etc. The package has only been
tested with Czech dates.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/advdate
%dir %{_datadir}/texmf-dist/tex/latex/advdate
%doc %{_datadir}/texmf-dist/doc/latex/advdate/advdate.pdf
%doc %{_datadir}/texmf-dist/doc/latex/advdate/advdate.tex
%doc %{_datadir}/texmf-dist/doc/latex/advdate/manifest.txt
%{_datadir}/texmf-dist/tex/latex/advdate/advdate.sty
