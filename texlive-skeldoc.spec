Name:		texlive-skeldoc
Version:	57922
Release:	2
Summary:	Placeholders for unfinished documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/skeldoc
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skeldoc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skeldoc.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package lets you produce placeholder elements for
documents under development, similar to the skeleton screens
used while loading contents in many applications and websites.
It also has a mechanism for attaching explanatory endnotes to
these placeholders, or to anything else in your document. The
same note mechanism can also be used with ordinary content,
e.g., as a to-do mechanism.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/skeldoc
%doc %{_texmfdistdir}/doc/latex/skeldoc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
