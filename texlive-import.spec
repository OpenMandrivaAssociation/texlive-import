# revision 17361
# category Package
# catalog-ctan /macros/latex/contrib/import
# catalog-date 2010-03-09 13:05:51 +0100
# catalog-license pd
# catalog-version 5.1
Name:		texlive-import
Version:	5.1
Release:	5
Summary:	Establish input relative to a directory
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/import
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/import.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/import.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The commands \import{full_path}{file} and
\subimport{path_extension}{file} set up input through standard
LaTeX mechanisms (\input, \include and \includegraphics) to
load files relative to the \import-ed directory. There are also
\includefrom, \subincludefrom, and * variants of the commands.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/import/import.sty
%doc %{_texmfdistdir}/doc/latex/import/import.pdf
%doc %{_texmfdistdir}/doc/latex/import/import.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 5.1-2
+ Revision: 752736
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 5.1-1
+ Revision: 718714
- texlive-import
- texlive-import
- texlive-import
- texlive-import

