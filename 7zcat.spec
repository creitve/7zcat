###############################################################################

Summary:         Utility for uncompressing data from 7z archive to stdout
Name:            7zcat
Version:         1.3.0
Release:         0%{?dist}
Group:           Applications/System
License:         EKOL
URL:             https://github.com/essentialkaos/7zcat

Source0:         https://source.kaos.io/%{name}/%{name}-%{version}.tar.bz2

BuildArch:       noarch
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:        p7zip >= 16

Provides:        %{name} = %{version}-%{release}

###############################################################################

%description
Utility for uncompressing 7z files and writing uncompressed data to standart 
output.

###############################################################################

%prep
%setup -q

%build
%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{_bindir}
install -pm 775 %{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.EN LICENSE.RU
%{_bindir}/%{name}

###############################################################################

%changelog
* Tue Oct 17 2017 Anton Novojilov <andy@essentialkaos.com> - 1.3.0-0
- Using 1 CPU by default for unpacking data
- Added option '-F/--fast' for using all CPUs for unpacking data

* Mon Apr 24 2017 Anton Novojilov <andy@essentialkaos.com> - 1.2.3-0
- Arguments parser updated to v3 with fixed stderr output redirection for
  showArgWarn and showArgValWarn functions

* Wed Apr 05 2017 Anton Novojilov <andy@essentialkaos.com> - 1.2.2-0
- Fixed output to stderr for a message about an unsupported argument

* Wed Apr 05 2017 Anton Novojilov <andy@essentialkaos.com> - 1.2.1-0
- Output errors to stderr

* Wed Nov 16 2016 Anton Novojilov <andy@essentialkaos.com> - 1.2.0-0
- Code refactoring

* Sun Oct 30 2016 Anton Novojilov <andy@essentialkaos.com> - 1.1.2-0
- UI improvements

* Fri Mar 18 2016 Anton Novojilov <andy@essentialkaos.com> - 1.1.1-0
- Fixed bug with checking protected files

* Thu Dec 31 2015 Anton Novojilov <andy@essentialkaos.com> - 1.1.0-0
- Minor improvements

* Sun Nov 08 2015 Anton Novojilov <andy@essentialkaos.com> - 1.0.12-0
- Minor improvements

* Sat Jan 03 2015 Anton Novojilov <andy@essentialkaos.com> - 1.0.11-0
- Improvements

* Tue Dec 30 2014 Anton Novojilov <andy@essentialkaos.com> - 1.0.10-0
- Improved argument parsing
- Improved password reading
- Improved error handling
- Removed shmin usage

* Tue Aug 06 2013 Anton Novojilov <andy@essentialkaos.com> - 1.0.9-0
- Improved argument parsing
- Added shmin 1.2.0 usage

* Sun Jul 28 2013 Anton Novojilov <andy@essentialkaos.com> - 1.0.8-0
- Improved argument parsing

* Fri Jul 19 2013 Anton Novojilov <andy@essentialkaos.com> - 1.0.7-2
- Added shmin usage

* Fri Jun 28 2013 Anton Novojilov <andy@essentialkaos.com> - 1.0.7-1
- Sources moved to SOURCES directory

* Wed Jun 19 2013 Anton Novojilov <andy@essentialkaos.com> - 1.0.7-0
- Improved argument parsing

* Tue Jun 11 2013 Anton Novojilov <andy@essentialkaos.com> - 1.0.6-0
- Improved argument parsing
- Improved working with password protected archives
- Improved data output

* Mon Oct 22 2012 Anton Novojilov <andy@essentialkaos.com> - 1.0.5-0
- Improved argument parsing
- Added short arguments support

* Thu Oct 18 2012 Anton Novojilov <andy@essentialkaos.com> 1.0.4-0
- Updated information in spec

* Thu Oct 18 2012 Anton Novojilov <andy@essentialkaos.com> 1.0.3-0
- Changed license to MIT

* Thu Jul 12 2012 Anton Novojilov <andy@essentialkaos.com> - 1.0.2-0
- Added password support 
- Improved argument parsing
- Minor UI fixes

* Fri Mar 16 2012 Anton Novojilov <andy@essentialkaos.com> - 1.0.1-0
- First release
