Summary:	Measure socket and RDMA performance
Summary(pl.UTF-8):	Pomiar wydajności gniazd i RDMA
Name:		qperf
Version:	0.4.9
Release:	1
License:	BSD or GPL v2
Group:		Networking/Utilities
Source0:	http://www.openfabrics.org/downloads/qperf/%{name}-%{version}.tar.gz
# Source0-md5:	a9eea1953ee5379e57ae5fd7b09fecf2
URL:		http://www.openfabrics.org/
BuildRequires:	libibverbs-devel
BuildRequires:	librdmacm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Measure socket and RDMA performance.

%description -l pl.UTF-8
Pomiar wydajności gniazd i RDMA.

%prep
%setup -q

%build
%configure

%{__make}

#CFLAGS="%{rpmcflags}" \
#LDFLAGS="%{rpmldflags}" \
#%{__make} \
#	CC="%{__cc}" \
#	prefix=%{_prefix} \
#	libpath=%{_libdir} \
#	binpath=%{_bindir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/qperf
%{_mandir}/man1/qperf.1*
