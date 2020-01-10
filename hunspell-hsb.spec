Name: hunspell-hsb
Summary: Upper Sorbian hunspell dictionaries
Version: 0.20060327.3
Release: 5%{?dist}
Source: https://addons.mozilla.org/firefox/downloads/file/113003/upper_sorbian_spelling_dictionary-0.0.20060327.3-tb+fx+sm.xpi
Group: Applications/Text
URL: http://sorbzilla.de/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Upper Sorbian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-hsb

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/hsb.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/hsb_DE.aff
cp -p dictionaries/hsb.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/hsb_DE.dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING README
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.20060327.3-5
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060327.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060327.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060327.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 20 2011 Caolán McNamara <caolanm@redhat.com> - 0.0.20060327.3-1
- latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060327.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060327.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060327.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Oct 3 2008 Caolán McNamara <caolanm@redhat.com> - 0.20060327.2-1
- initial version
