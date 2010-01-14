Name:           sonic-visualiser-freeworld
Version:        1.7.1
Release:        1%{?dist}
Summary:        A program for viewing and exploring audio data

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://www.sonicvisualiser.org/
Source0:        http://downloads.sourceforge.net/sv1/sonic-visualiser-%{version}.tar.bz2
Source1:        sonic-visualiser-freeworld.desktop
Patch0:         sonic-visualiser-1.5-gcc44.patch
Patch1:         sonic-visualiser-1.5-alsa.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  qt4-devel vamp-plugin-sdk-devel
BuildRequires:  libsndfile-devel libsamplerate-devel fftw-devel bzip2-devel
BuildRequires:  alsa-lib-devel jack-audio-connection-kit-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  redland-devel rubberband-devel
BuildRequires:  libmad-devel
BuildRequires:  liboggz-devel libfishsound-devel liblo-devel
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
Sonic Visualiser is an application for viewing and analysing the
contents of music audio files.

The aim of Sonic Visualiser is to be the first program you reach for
when want to study a musical recording rather than simply listen to
it.

As well as a number of features designed to make exploring audio data
as revealing and fun as possible, Sonic Visualiser also has powerful
annotation capabilities to help you to describe what you find, and the
ability to run automated annotation and analysis plugins in the Vamp
analysis plugin format – as well as applying standard audio effects.


%prep
%setup -q -n sonic-visualiser-%{version}
# https://sourceforge.net/tracker/?func=detail&aid=2715387&group_id=162924&atid=825705
%patch0 -p1 -b .gcc44
# https://sourceforge.net/tracker/?func=detail&aid=2715381&group_id=162924&atid=825705
%patch1 -p1 -b .alsa


%build
qmake-qt4
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
# install does nothing right now
# make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 -p sv/sonic-visualiser \
        $RPM_BUILD_ROOT%{_bindir}/%{name}
# desktop file and icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -m 644 -p sv/icons/sv-48x48.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
                     %{SOURCE1}


%clean
rm -rf $RPM_BUILD_ROOT


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%defattr(-,root,root,-)
%doc COPYING README README.OSC
%{_bindir}/sonic-visualiser-freeworld
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png


%changelog
* Wed Jan 13 2010 Michel Salim <salimma@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1

* Wed Sep 23 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.6-4
- Update desktop file according to F-12 FedoraStudio feature

* Sun Sep 13 2009 Michel Salim <salimma@fedoraproject.org> - 1.6-3
- Make parallel-installable with sonic-visualiser
- Updated icon cache scriplet

* Sun Aug 23 2009 Michel Salim <salimma@fedoraproject.org> - 1.6-2
- RPM Fusion packaging, based on Fedora spec

* Fri Aug 21 2009 Michel Salim <salimma@fedoraproject.org> - 1.6-1
- Update to 1.6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 26 2009 Michel Salim <salimma@fedoraproject.org> - 1.5-1
- Update to 1.5

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 Michel Salim <salimma@fedoraproject.org> - 1.4-3
- Fix compilation problem with GCC 4.4

* Sun Dec 14 2008 Michel Salim <salimma@fedoraproject.org> - 1.4-2
- Fix qmake profiles to properly detect 64-bit Linux

* Sun Dec 14 2008 Michel Salim <salimma@fedoraproject.org> - 1.4-1
- Update to 1.4
- Replace PortAudio dependency with PulseAudio

* Thu Jul 17 2008 Michel Salim <salimma@fedoraproject.org> - 1.3-1
- Update to 1.3

* Sun Mar 30 2008 Michel Salim <michel.sylvan@gmail.com> - 1.2-1
- Update to 1.2

* Fri Feb 15 2008 Michel Salim <michel.sylvan@gmail.com> - 1.0-5
- Use correct optflags

* Wed Feb 13 2008 Michel Salim <michel.sylvan@gmail.com> - 1.0-4
- Exclude ppc for now. On it, qmake uses wrong (x86) optflags (#432733).
- Add missing BR on libfishsound-devel
 
* Sun Feb  3 2008 Michel Salim <michel.sylvan@gmail.com> - 1.0-3
- Add some #includes, needed due to GCC 4.3's header dependency cleanup

* Sun Jan 27 2008 Michel Salim <michel.sylvan@gmail.com> - 1.0-2
- Fix icon placement and license

* Wed Jan 16 2008 Michel Salim <michel.sylvan@gmail.com> - 1.0-1
- Initial Fedora package

