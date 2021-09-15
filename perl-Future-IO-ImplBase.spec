#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Future-IO-ImplBase
Version  : 0.10
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Future-IO-0.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Future-IO-0.10.tar.gz
Summary  : 'Future-returning IO methods'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Future-IO-ImplBase-license = %{version}-%{release}
Requires: perl-Future-IO-ImplBase-perl = %{version}-%{release}
Requires: perl(Future)
Requires: perl(Struct::Dumb)
BuildRequires : buildreq-cpan
BuildRequires : perl(Future)
BuildRequires : perl(Struct::Dumb)
BuildRequires : perl(Test::Identity)

%description
NAME
Future::IO - Future-returning IO methods
SYNOPSIS
use Future::IO;

my $delay = Future::IO->sleep( 5 );
# $delay will become done in 5 seconds time

my $input = Future::IO->sysread( \*STDIN, 4096 );
# $input will yield some input from the STDIN IO handle

%package dev
Summary: dev components for the perl-Future-IO-ImplBase package.
Group: Development
Provides: perl-Future-IO-ImplBase-devel = %{version}-%{release}
Requires: perl-Future-IO-ImplBase = %{version}-%{release}

%description dev
dev components for the perl-Future-IO-ImplBase package.


%package license
Summary: license components for the perl-Future-IO-ImplBase package.
Group: Default

%description license
license components for the perl-Future-IO-ImplBase package.


%package perl
Summary: perl components for the perl-Future-IO-ImplBase package.
Group: Default
Requires: perl-Future-IO-ImplBase = %{version}-%{release}

%description perl
perl components for the perl-Future-IO-ImplBase package.


%prep
%setup -q -n Future-IO-0.10
cd %{_builddir}/Future-IO-0.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Future-IO-ImplBase
cp %{_builddir}/Future-IO-0.10/LICENSE %{buildroot}/usr/share/package-licenses/perl-Future-IO-ImplBase/67825508da0c86b98557cec241ae7036d3165a11
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Future::IO.3
/usr/share/man/man3/Future::IO::ImplBase.3
/usr/share/man/man3/Test::Future::IO::Impl.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Future-IO-ImplBase/67825508da0c86b98557cec241ae7036d3165a11

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Future/IO.pm
/usr/lib/perl5/vendor_perl/5.34.0/Future/IO/ImplBase.pm
/usr/lib/perl5/vendor_perl/5.34.0/Test/Future/IO/Impl.pm
