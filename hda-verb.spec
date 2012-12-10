Name:		hda-verb
Version:	0.3
Release:	%mkrel 3
Summary:	Tool to send commands (verbs) to HD-Audio codecs
License:	GPLv2+
Group:		System/Configuration/Hardware
URL:		ftp://ftp.kernel.org/pub/linux/kernel/people/tiwai/misc/
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/people/tiwai/misc/hda-verb-%{version}.tar.bz2
Source1:	ftp://ftp.kernel.org/pub/linux/kernel/people/tiwai/misc/hda-verb-%{version}.tar.bz2.sign
BuildRequires:	gcc
BuildRequires:	make
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
hda-verb is a tiny program that allows you to access the HD-audio
codecs directly, allowing you to send commands (verbs) to them. For
hda-verb to work you must be running a linux kernel with
CONFIG_SND_HDA_HWDEP option enabled.

%prep
%setup -q

%build
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
cp hda-verb %{buildroot}/%{_sbindir}

%files
%defattr(0644,root,root,0755)
%doc ChangeLog README
%attr(0755,root,root) %{_sbindir}/hda-verb


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-3mdv2011.0
+ Revision: 619357
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.3-2mdv2010.0
+ Revision: 437851
- rebuild

* Wed Jan 28 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.3-1mdv2009.1
+ Revision: 334965
- import hda-verb


