%define upstream_name    Padre-Plugin-Swarm
%define upstream_version 0.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Tree view panel of swarm resources
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Padre/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::XSAccessor)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Graph)
BuildRequires: perl(IO::Select)
BuildRequires: perl(IO::Socket::Multicast)
BuildRequires: perl(JSON::XS)
BuildRequires: perl-JSON-PP
BuildRequires: perl(Padre)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Patch)
BuildRequires: x11-server-xvfb

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
xvfb-run %make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml README Changes
%{_mandir}/man3/*
%perl_vendorlib/*
