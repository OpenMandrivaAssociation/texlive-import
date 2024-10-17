Name:		texlive-import
Version:	54683
Release:	2
Summary:	Establish input relative to a directory
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/import
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/import.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/import.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/import
%doc %{_texmfdistdir}/doc/latex/import

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
