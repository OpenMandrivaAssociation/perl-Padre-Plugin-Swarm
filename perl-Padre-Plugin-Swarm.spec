%define upstream_name    Padre-Plugin-Swarm
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.11
Release:	3

Summary:	Tree view panel of swarm resources
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Padre/Padre-Plugin-Swarm-0.11.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::XSAccessor)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Graph)
BuildRequires:	perl(IO::Select)
BuildRequires:	perl(IO::Socket::Multicast)
BuildRequires:	perl(JSON::XS)
BuildRequires:	perl(Padre)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::Patch)
BuildRequires:	x11-server-xvfb

BuildArch: noarch

%description
This is Swarm!

Swarm is a Padre plugin for experimenting with remote inspection, peer
programming and collaborative editing functionality.

Within this plugin all rules are suspended. No security, no efficiency, no
scalability, no standards compliance, remote code execution, everything is
allowed. The only goal is things that work, and things that look shiny in a
demo :)

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
xvfb-run %make test

%install
%makeinstall_std

%files
%doc META.yml README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 657817
- rebuild for updated spec-helper

* Thu Feb 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.100.0-1
+ Revision: 635605
- update to new version 0.1

* Sun Feb 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.93.0-1mdv2011.0
+ Revision: 505678
- update to 0.093

* Sat Feb 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.92.0-1mdv2010.1
+ Revision: 505268
- update to 0.092

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.1
+ Revision: 504828
- wrap tests in xvfb
- import perl-Padre-Plugin-Swarm


* Fri Feb 12 2010 cpan2dist 0.08-1mdv
- initial mdv release, generated with cpan2dist

