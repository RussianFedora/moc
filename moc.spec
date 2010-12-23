%define rev 20101030svn2252

Summary:	MOC (music on console) is a console audio player for LINUX/UNIX
Name:		moc
Version:	2.5.0
Release:	0.2.%{rev}%{?dist}

Group:		Applications/Multimedia
License:	GPL
URL:		http://moc.daper.net/
Source0:	ftp://ftp.daper.net/pub/soft/moc/stable/%{name}-%{version}-%{rev}.tar.bz2
Patch1:		moc-2.5.0-alpha4-ffmpeg.patch
Patch5:		moc-2.5.0-ffmpeg-mac-support.patch
Patch7:		moc-2.5.0-fix-sidplay2-plugin.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	libtool
BuildRequires:  automake
BuildRequires:	autoconf

BuildRequires:	alsa-lib-devel
BuildRequires:	curl-devel
BuildRequires:	db4-devel
BuildRequires:	faad2-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	flac-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	lame-devel
BuildRequires:  libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	libogg-devel
BuildRequires:	librcc-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
# It pull 91M of some shit. Does it really need?
#BuildRequires:	libtimidity-devel
BuildRequires:	libtool-ltdl-devel
BuildRequires:  libvorbis-devel
BuildRequires:	ncurses-devel
BuildRequires:	sidplay-libs-devel
BuildRequires:	speex-devel
BuildRequires:	taglib-devel
BuildRequires:	wavpack-devel
BuildRequires:	zlib-devel


%description
MOC (music on console) is a console audio player for 
LINUX/UNIX designed to be powerful and easy to use.


%prep
%setup -q -n %{name}-%{version}-%{rev}
%patch1 -p1
%patch5 -p1
%patch7 -p1



%build
./autogen.sh
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_datadir}/doc


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
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
