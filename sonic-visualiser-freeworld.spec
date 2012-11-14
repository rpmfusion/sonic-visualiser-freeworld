Name:           sonic-visualiser-freeworld
Version:        2.0
Release:        1%{?dist}
Summary:        A program for viewing and exploring audio data

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://www.sonicvisualiser.org/
Source0:        http://code.soundsoftware.ac.uk/attachments/download/539/sonic-visualiser-2.0.tar.gz
Source1:        sonic-visualiser-freeworld.desktop

BuildRequires:  qt4-devel
BuildRequires:  vamp-plugin-sdk-devel >= 2.4
BuildRequires:  libsndfile-devel libsamplerate-devel fftw-devel bzip2-devel
BuildRequires:  alsa-lib-devel jack-audio-connection-kit-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  dataquay-devel rubberband-devel
BuildRequires:  libmad-devel
BuildRequires:  liboggz-devel libfishsound-devel liblo-devel
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
Sonic Visualiser is an application for viewing and analyzing the
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
# Fix incorrect version string
%{__sed} -i.ver "s|1.9'|2.0'|" sonic-visualiser/configure


%build
%configure

# not SMP-safe
#make {?_smp_mflags}
make


%install
rm -rf $RPM_BUILD_ROOT
# install does nothing right now
# make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 -p sonic-visualiser/sonic-visualiser \
        $RPM_BUILD_ROOT%{_bindir}/%{name}
# desktop file and icon
for s in 16 22 24 32 48 64 128; do
    mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps
    install -m 644 -p sonic-visualiser/icons/sv-${s}x${s}.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}


%if 0%{?rhel}
%clean
rm -rf $RPM_BUILD_ROOT
%endif


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
update-desktop-database &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%defattr(-,root,root,-)
%doc sonic-visualiser/CHANGELOG sonic-visualiser/COPYING sonic-visualiser/README sonic-visualiser/README.OSC
%{_bindir}/sonic-visualiser-freeworld
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png


%changelog
* Wed Nov 14 2012 Michel Salim <salimma@fedoraproject.org> - 2.0-1
- Update to 2.0

* Fri Mar 23 2012 Michel Salim <salimma@fedoraproject.org> - 1.9-1
- Update to 1.9

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.8-5
- Rebuilt for c++ ABI breakage

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct  3 2011 Michel Salim <salimma@fedoraproject.org> - 1.8-3
- Fix for Qt 4.8 disallowing virtual inheritance of QObject (Radek Novacek)
- patch for raptor2 support (Rex Dieter)

* Mon Oct 03 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.8-2
- Rebuild for librasqal

* Tue Jun 21 2011 Michel Salim <salimma@fedoraproject.org> - 1.8-1
- Update to 1.8

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 20 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.7.2-2
- Rebuild against new liblo-0.26

* Wed Jun 02 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 1.7.2-1
- Updated to 1.7.2
- Release Notes:
- (reference: https://sourceforge.net/projects/sv1/files/sonic-visualiser/1.7.2/CHANGELOG/download)
-   The time-value layer now has an origin line and an option to
 show derivatives (change from one point to the next) rather than
 raw values
-   A crash when pressing Play straight after New Session has been
 fixed
-   Builds with latest liboggz

* Wed Jun 02 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 1.7.1-2
- Bump for new liboggz lib

* Wed Jan 13 2010 Michel Salim <salimma@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1

* Sun Jan 03 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.6-6
- rebuild (redland)

* Sun Jan 03 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.6-5
- rebuild (rasqal/redland)

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

