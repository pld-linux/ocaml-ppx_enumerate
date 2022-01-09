#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Generate a list containing all values of a finite type
Summary(pl.UTF-8):	Generowanie listy zawierającej wszystkie wartości typu skończonego
Name:		ocaml-ppx_enumerate
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_enumerate/tags
Source0:	https://github.com/janestreet/ppx_enumerate/archive/v%{version}/ppx_enumerate-%{version}.tar.gz
# Source0-md5:	ee9931e4404e0378eb704889745ffe17
URL:		https://github.com/janestreet/ppx_enumerate
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppxlib-devel >= 0.11.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Generate a list containing all values of a finite type.

This package contains files needed to run bytecode executables using
ppx_enumerate library.

%description -l pl.UTF-8
Generowanie listy zawierającej wszystkie wartości typu skończonego.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_enumerate.

%package devel
Summary:	Generate a list containing all values of a finite type - development part
Summary(pl.UTF-8):	Generowanie listy zawierającej wszystkie wartości typu skończonego - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.11.0

%description devel
This package contains files needed to develop OCaml programs using
ppx_enumerate library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_enumerate.

%prep
%setup -q -n ppx_enumerate-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_enumerate/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_enumerate/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_enumerate

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/ppx_enumerate
%{_libdir}/ocaml/ppx_enumerate/META
%{_libdir}/ocaml/ppx_enumerate/*.cma
%dir %{_libdir}/ocaml/ppx_enumerate/runtime-lib
%{_libdir}/ocaml/ppx_enumerate/runtime-lib/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_enumerate/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_enumerate/runtime-lib/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_enumerate/*.cmi
%{_libdir}/ocaml/ppx_enumerate/*.cmt
%{_libdir}/ocaml/ppx_enumerate/*.cmti
%{_libdir}/ocaml/ppx_enumerate/*.mli
%{_libdir}/ocaml/ppx_enumerate/runtime-lib/*.cmi
%{_libdir}/ocaml/ppx_enumerate/runtime-lib/*.cmt
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_enumerate/ppx_enumerate.a
%{_libdir}/ocaml/ppx_enumerate/*.cmx
%{_libdir}/ocaml/ppx_enumerate/*.cmxa
%{_libdir}/ocaml/ppx_enumerate/runtime-lib/ppx_enumerate_lib.a
%{_libdir}/ocaml/ppx_enumerate/runtime-lib/*.cmx
%{_libdir}/ocaml/ppx_enumerate/runtime-lib/*.cmxa
%endif
%{_libdir}/ocaml/ppx_enumerate/dune-package
%{_libdir}/ocaml/ppx_enumerate/opam
%{_examplesdir}/%{name}-%{version}
