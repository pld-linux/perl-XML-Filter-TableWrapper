#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Filter-TableWrapper
Summary:	XML::Filter::TableWrapper - Wrap a table's cells in to a certain number of rows
#Summary(pl):	
Name:		perl-XML-Filter-TableWrapper
Version:	0.02
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-SAX
BuildRequires:	perl-XML-SAX-Writer >= 0.42
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Takes a list of elements and inserts (by default) <tr>...</tr> elements
to make an table with a specified number of columns (5 by default).
By default, it assumes that the container element is named "{}table"
(the "{}" means it is not namespaced), but this can be changed:

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*/*.pm
%{_mandir}/man3/*
