#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-service-restart
Version  : 4
Release  : 6
URL      : https://github.com/clearlinux/clr-service-restart/releases/download/v4/clr-service-restart-4.tar.xz
Source0  : https://github.com/clearlinux/clr-service-restart/releases/download/v4/clr-service-restart-4.tar.xz
Source1  : clr-service-restart-motd.service
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: clr-service-restart-bin
Requires: clr-service-restart-config
Requires: clr-service-restart-doc
Patch1: 0001-Motd-updating-script-for-clearlinux.patch

%description
No detailed description available

%package bin
Summary: bin components for the clr-service-restart package.
Group: Binaries
Requires: clr-service-restart-config

%description bin
bin components for the clr-service-restart package.


%package config
Summary: config components for the clr-service-restart package.
Group: Default

%description config
config components for the clr-service-restart package.


%package doc
Summary: doc components for the clr-service-restart package.
Group: Documentation

%description doc
doc components for the clr-service-restart package.


%prep
%setup -q -n clr-service-restart-4
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517340316
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1517340316
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/clr-service-restart-motd.service
## make_install_append content
mkdir -p %{buildroot}/usr/bin
install -m0755 clr-service-restart-motd.sh %{buildroot}/usr/bin/clr-service-restart-motd.sh
mkdir -p %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants
ln -sf ../clr-service-restart-motd.service %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/clr-service-restart-motd.service
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/clr-service-restart
/usr/bin/clr-service-restart-motd.sh

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/clr-service-restart-motd.service
/usr/lib/systemd/system/update-triggers.target.wants/clr-service-restart-motd.service

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
