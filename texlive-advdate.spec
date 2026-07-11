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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides macros which can add a specified number of days to the current
date (as specified in \today), to save, set and restore the 'current
date' and to print it. Intended use is, for example, in invoices
"payable within 14 days from today", etc. The package has only been
tested with Czech dates.

