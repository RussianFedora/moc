Name:		moc
Version:	2.5.0
Release:	0.2.%{rev}%{?dist}
Summary:        Music on console

License:        GPLv2+
URL:		http://moc.daper.net/
Source0:	ftp://ftp.daper.net/pub/soft/moc/stable/%{name}-%{version}-%{rev}.tar.bz2

BuildRequires:  alsa-lib-devel
BuildRequires:  faad2-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  file-devel
BuildRequires:  flac-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libao-devel
BuildRequires:  libcurl-devel
BuildRequires:  libdb-devel
BuildRequires:  libid3tag-devel
BuildRequires:  libmad-devel
BuildRequires:  libmodplug-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  libogg-devel
BuildRequires:  librcc-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtimidity-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libvorbis-devel
BuildRequires:  ncurses-devel
BuildRequires:  popt-devel
BuildRequires:  speex-devel
BuildRequires:  taglib-devel
BuildRequires:  wavpack-devel
BuildRequires:  zlib-devel

%description
MOC (music on console) is a console audio player for LINUX/UNIX
designed to be powerful and easy to use.

%prep
%setup -q -n %{name}-%{version}-%{rev}

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_datadir}/doc

%files
%doc AUTHORS COPYING NEWS README TODO config.example keymap.example
%{_bindir}/mocp
%{_libdir}/moc/
%{_mandir}/man?/*
%{_datadir}/moc/

%changelog
* Thu Nov  4 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 2.5.0-0.2.20101030svn2252
- update to last snapshot

* Mon Apr 26 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 2.5.0-0.1.alpha4
- update to 2.5.0-alpha4

* Wed May 13 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 2.4.4-1
- update to 2.4.4

* Wed Nov 21 2007 Arkady L. Shane <ashejn@yandex-team.ru> - 2.4.3-1
- initial build for Fedora
