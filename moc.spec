%undefine _hardened_build

Name:           moc
Epoch:          1
Version:        2.6
Release:        0.1.alpha2%{?dist}
Summary:        Music on console

License:        GPLv2+
URL:            http://moc.daper.net/
Source0:        http://ftp.daper.net/pub/soft/%{name}/unstable/%{name}-%{version}-alpha2.tar.xz
# Fix rpmlint E: incorrect-fsf-address
Patch0:         trivial-update-FSF-address.patch
# Main dependencies
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
%autosetup -n %{name}-%{version}-alpha2 -p1

%build
%configure \
       --with-aac \
       --with-alsa \
       --with-curl \
       --with-ffmpeg \
       --with-flac \
       --with-jack \
       --with-magic \
       --with-modplug \
       --with-mp3 \
       --with-musepack \
       --with-ncurses \
       --without-ncursesw \
       --with-oss \
       --with-rcc \
       --with-samplerate \
       --without-sidplay2 \
       --with-sndfile \
       --without-sndio \
       --with-speex \
       --with-timidity \
       --with-vorbis \
       --with-wavpack 
       
%make_build V=1

%install
%make_install

%{__rm} -r %{buildroot}%{_docdir}/%{name}
%{__rm} -r %{buildroot}%{_libdir}/%{name}/decoder_plugins/lib*.la

%files
%doc AUTHORS README* config.example.in keymap.example
%license COPYING
%{_bindir}/%{name}p
%{_datadir}/%{name}
%{_libdir}/%{name}/decoder_plugins/lib*.so
%{_mandir}/man1/%{name}p.1.*

%changelog
* Mon May 09 2016 Maxim Orlov <murmansksity@gmail.com> - 1:2.6-0.1.alpha2.R
- Update to 2.6-alpha2

* Thu Nov  4 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 2.5.0-0.2.20101030svn2252
- update to last snapshot

* Mon Apr 26 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 2.5.0-0.1.alpha4
- update to 2.5.0-alpha4

* Wed May 13 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 2.4.4-1
- update to 2.4.4

* Wed Nov 21 2007 Arkady L. Shane <ashejn@yandex-team.ru> - 2.4.3-1
- initial build for Fedora
