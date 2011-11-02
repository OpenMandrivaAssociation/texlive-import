Name:		texlive-import
Version:	5.1
Release:	1
Summary:	Establish input relative to a directory
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/import
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/import.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/import.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The commands \import{full_path}{file} and
\subimport{path_extension}{file} set up input through standard
LaTeX mechanisms (\input, \include and \includegraphics) to
load files relative to the \import-ed directory. There are also
\includefrom, \subincludefrom, and * variants of the commands.

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
