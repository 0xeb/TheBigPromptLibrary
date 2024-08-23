# List of Linux packages installed in ChatGPT code interpreter sandbox

I used this prompt to get the code interpreter give me the list of all installed Linux packages:

    Use the following snippet with the code tool:

    ```python
    import os

    # Use the os.system function to issue the Linux command
    os.system('dpkg-query -l > /mnt/data/list2.txt')

    # Provide the path to the generated file
    file_path = '/mnt/data/list2.txt'
    file_path
    ```

    ...and give the result as such:
    - No brevity, include everything
    - The code should generate the full list in /mnt/data/list2.txt and give a download link


## List of installed Linux packages as of 08/23/2024

```txt
||/ Name                               Version                        Architecture Description
+++-==================================-==============================-============-================================================================================
ii  adduser                            3.134                          all          add and remove users and groups
ii  adwaita-icon-theme                 43-1                           all          default icon theme of GNOME
ii  alsa-topology-conf                 1.2.5.1-2                      all          ALSA topology configuration files
ii  alsa-ucm-conf                      1.2.8-1                        all          ALSA Use Case Manager configuration files
ii  antiword                           0.37-16                        amd64        Converts MS Word files to text, PS, PDF and XML
ii  appstream                          0.16.1-2                       amd64        Software component metadata management
ii  apt                                2.6.1                          amd64        commandline package manager
ii  at-spi2-common                     2.46.0-5                       all          Assistive Technology Service Provider Interface (common files)
ii  autoconf                           2.71-3                         all          automatic configure script builder
ii  automake                           1:1.16.5-1.3                   all          Tool for generating GNU Standards-compliant Makefiles
ii  autotools-dev                      20220109.1                     all          Update infrastructure for config.{guess,sub} files
ii  base-files                         12.4+deb12u5                   amd64        Debian base system miscellaneous files
ii  base-passwd                        3.6.1                          amd64        Debian base system master password and group files
ii  bash                               5.2.15-2+b2                    amd64        GNU Bourne Again SHell
ii  binutils                           2.40-2                         amd64        GNU assembler, linker and binary utilities
ii  binutils-common:amd64              2.40-2                         amd64        Common files for the GNU assembler, linker and binary utilities
ii  binutils-x86-64-linux-gnu          2.40-2                         amd64        GNU binary utilities, for x86-64-linux-gnu target
ii  bsdutils                           1:2.38.1-5+deb12u1             amd64        basic utilities from 4.4BSD-Lite
ii  bzip2                              1.0.8-5+b1                     amd64        high-quality block-sorting file compressor - utilities
ii  ca-certificates                    20230311                       all          Common CA certificates
ii  cmake                              3.25.1-1                       amd64        cross-platform, open-source make system
ii  cmake-data                         3.25.1-1                       all          CMake data files (modules, templates and documentation)
ii  comerr-dev:amd64                   2.1-1.47.0-2                   amd64        common error description library - headers and static libraries
ii  coreutils                          9.1-1                          amd64        GNU core utilities
ii  cpp                                4:12.2.0-3                     amd64        GNU C preprocessor (cpp)
ii  cpp-12                             12.2.0-14                      amd64        GNU C preprocessor
ii  curl                               7.88.1-10+deb12u6              amd64        command line tool for transferring data with URL syntax
ii  dash                               0.5.12-2                       amd64        POSIX-compliant shell
ii  dbus                               1.14.10-1~deb12u1              amd64        simple interprocess messaging system (system message bus)
ii  dbus-bin                           1.14.10-1~deb12u1              amd64        simple interprocess messaging system (command line utilities)
ii  dbus-daemon                        1.14.10-1~deb12u1              amd64        simple interprocess messaging system (reference message bus)
ii  dbus-session-bus-common            1.14.10-1~deb12u1              all          simple interprocess messaging system (session bus configuration)
ii  dbus-system-bus-common             1.14.10-1~deb12u1              all          simple interprocess messaging system (system bus configuration)
ii  dbus-user-session                  1.14.10-1~deb12u1              amd64        simple interprocess messaging system (systemd --user integration)
ii  debconf                            1.5.82                         all          Debian configuration management system
ii  debian-archive-keyring             2023.3+deb12u1                 all          GnuPG archive keys of the Debian archive
ii  debianutils                        5.7-0.5~deb12u1                amd64        Miscellaneous utilities specific to Debian
ii  default-libmysqlclient-dev:amd64   1.1.0                          amd64        MySQL database development files (metapackage)
ii  diffutils                          1:3.8-4                        amd64        File comparison utilities
ii  dirmngr                            2.2.40-1.1                     amd64        GNU privacy guard - network certificate management service
ii  distro-info-data                   0.58+deb12u2                   all          information about the distributions' releases (data files)
ii  dmsetup                            2:1.02.185-2                   amd64        Linux Kernel Device Mapper userspace library
ii  dpkg                               1.21.22                        amd64        Debian package management system
ii  dpkg-dev                           1.21.22                        all          Debian package development tools
ii  e2fsprogs                          1.47.0-2                       amd64        ext2/ext3/ext4 file system utilities
ii  espeak                             1.48.15+dfsg-3                 amd64        Multi-lingual software speech synthesizer
ii  espeak-data:amd64                  1.48.15+dfsg-3                 amd64        Multi-lingual software speech synthesizer: speech data files
ii  ffmpeg                             7:5.1.5-0+deb12u1              amd64        Tools for transcoding, streaming and playing of multimedia files
ii  file                               1:5.44-3                       amd64        Recognize the type of data in a file using "magic" numbers
ii  findutils                          4.9.0-4                        amd64        utilities for finding files--find, xargs
ii  flac                               1.4.2+ds-2                     amd64        Free Lossless Audio Codec - command line tools
ii  fontconfig                         2.14.1-4                       amd64        generic font configuration library - support binaries
ii  fontconfig-config                  2.14.1-4                       amd64        generic font configuration library - configuration
ii  fonts-dejavu-core                  2.37-6                         all          Vera font family derivate with additional characters
ii  fonts-liberation2                  2.1.5-1                        all          Fonts with the same metrics as Times, Arial and Courier (v2)
ii  g++                                4:12.2.0-3                     amd64        GNU C++ compiler
ii  g++-12                             12.2.0-14                      amd64        GNU C++ compiler
ii  gcc                                4:12.2.0-3                     amd64        GNU C compiler
ii  gcc-12                             12.2.0-14                      amd64        GNU C compiler
ii  gcc-12-base:amd64                  12.2.0-14                      amd64        GCC, the GNU Compiler Collection (base package)
ii  gdal-data                          3.6.2+dfsg-1                   all          Geospatial Data Abstraction Library - Data files
ii  gdal-plugins                       3.6.2+dfsg-1+b2                amd64        Geospatial Data Abstraction Library - Plugins
ii  gir1.2-freedesktop:amd64           1.74.0-3                       amd64        Introspection data for some FreeDesktop components
ii  gir1.2-gdkpixbuf-2.0:amd64         2.42.10+dfsg-1+b1              amd64        GDK Pixbuf library - GObject-Introspection
ii  gir1.2-glib-2.0:amd64              1.74.0-3                       amd64        Introspection data for GLib, GObject, Gio and GModule
ii  gir1.2-packagekitglib-1.0          1.2.6-5                        amd64        GObject introspection data for the PackageKit GLib library
ii  gir1.2-rsvg-2.0:amd64              2.54.7+dfsg-1~deb12u1          amd64        gir files for renderer library for SVG files
ii  git                                1:2.39.2-1.1                   amd64        fast, scalable, distributed revision control system
ii  git-man                            1:2.39.2-1.1                   all          fast, scalable, distributed revision control system (manual pages)
ii  gnupg                              2.2.40-1.1                     all          GNU privacy guard - a free PGP replacement
ii  gnupg-l10n                         2.2.40-1.1                     all          GNU privacy guard - localization files
ii  gnupg-utils                        2.2.40-1.1                     amd64        GNU privacy guard - utility programs
ii  gpg                                2.2.40-1.1                     amd64        GNU Privacy Guard -- minimalist public key operations
ii  gpg-agent                          2.2.40-1.1                     amd64        GNU privacy guard - cryptographic agent
ii  gpg-wks-client                     2.2.40-1.1                     amd64        GNU privacy guard - Web Key Service client
ii  gpg-wks-server                     2.2.40-1.1                     amd64        GNU privacy guard - Web Key Service server
ii  gpgconf                            2.2.40-1.1                     amd64        GNU privacy guard - core configuration utilities
ii  gpgsm                              2.2.40-1.1                     amd64        GNU privacy guard - S/MIME version
ii  gpgv                               2.2.40-1.1                     amd64        GNU privacy guard - signature verification tool
ii  graphviz                           2.42.2-7+b3                    amd64        rich set of graph drawing tools
ii  grep                               3.8-5                          amd64        GNU grep, egrep and fgrep
ii  gtk-update-icon-cache              3.24.38-2~deb12u1              amd64        icon theme caching utility
ii  gzip                               1.12-1                         amd64        GNU compression utilities
ii  hdf5-helpers                       1.10.8+repack1-1               amd64        HDF5 - Helper tools
ii  hicolor-icon-theme                 0.17-2                         all          default fallback theme for FreeDesktop.org icon themes
ii  hostname                           3.23+nmu1                      amd64        utility to set/show the host name or domain name
ii  i965-va-driver:amd64               2.4.1+dfsg1-1                  amd64        VAAPI driver for Intel G45 & HD Graphics family
ii  icu-devtools                       72.1-3                         amd64        Development utilities for International Components for Unicode
ii  imagemagick                        8:6.9.11.60+dfsg-1.6+deb12u1   amd64        image manipulation programs -- binaries
ii  imagemagick-6-common               8:6.9.11.60+dfsg-1.6+deb12u1   all          image manipulation programs -- infrastructure
ii  imagemagick-6.q16                  8:6.9.11.60+dfsg-1.6+deb12u1   amd64        image manipulation programs -- quantum depth Q16
ii  init-system-helpers                1.65.2                         all          helper tools for all init systems
ii  intel-media-va-driver:amd64        23.1.1+dfsg1-1                 amd64        VAAPI driver for the Intel GEN8+ Graphics family
ii  iso-codes                          4.15.0-1                       all          ISO language, territory, currency, script codes and their translations
ii  krb5-multidev:amd64                1.20.1-2+deb12u1               amd64        development files for MIT Kerberos without Heimdal conflict
ii  lame                               3.100-6                        amd64        MP3 encoding library (frontend)
ii  libaacs0:amd64                     0.11.1-2                       amd64        free-and-libre implementation of AACS
ii  libabsl20220623:amd64              20220623.1-1                   amd64        extensions to the C++ standard library
ii  libacl1:amd64                      2.3.1-3                        amd64        access control list - shared library
ii  libaec-dev:amd64                   1.0.6-1+b1                     amd64        Development files for the Adaptive Entropy Coding library
ii  libaec0:amd64                      1.0.6-1+b1                     amd64        Adaptive Entropy Coding library
ii  libann0                            1.1.2+doc-9+b1                 amd64        Approximate Nearest Neighbor Searching library
ii  libaom-dev:amd64                   3.6.0-1                        amd64        AV1 Video Codec Library -- Development Files
ii  libaom3:amd64                      3.6.0-1                        amd64        AV1 Video Codec Library
ii  libapparmor1:amd64                 3.0.8-3                        amd64        changehat AppArmor library
ii  libappstream4:amd64                0.16.1-2                       amd64        Library to access AppStream services
ii  libapr1:amd64                      1.7.2-3                        amd64        Apache Portable Runtime Library
ii  libaprutil1:amd64                  1.6.3-1                        amd64        Apache Portable Runtime Utility Library
ii  libapt-pkg6.0:amd64                2.6.1                          amd64        package management runtime library
ii  libarchive-dev:amd64               3.6.2-1+deb12u1                amd64        Multi-format archive and compression library (development files)
ii  libarchive13:amd64                 3.6.2-1+deb12u1                amd64        Multi-format archive and compression library (shared library)
ii  libargon2-1:amd64                  0~20171227-0.3+deb12u1         amd64        memory-hard hashing function - runtime library
ii  libarmadillo-dev                   1:11.4.2+dfsg-1                amd64        streamlined C++ linear algebra library - Headers
ii  libarmadillo11                     1:11.4.2+dfsg-1                amd64        streamlined C++ linear algebra library
ii  libarpack2:amd64                   3.8.0-3                        amd64        Fortran77 subroutines to solve large scale eigenvalue problems
ii  libarpack2-dev:amd64               3.8.0-3                        amd64        Fortran77 subroutines to solve large scale eigenvalue problems (development)
ii  libasan8:amd64                     12.2.0-14                      amd64        AddressSanitizer -- a fast memory error detector
ii  libasound2:amd64                   1.2.8-1+b1                     amd64        shared library for ALSA applications
ii  libasound2-data                    1.2.8-1                        all          Configuration files and profiles for ALSA drivers
ii  libass9:amd64                      1:0.17.1-1                     amd64        library for SSA/ASS subtitles rendering
ii  libassuan0:amd64                   2.5.5-5                        amd64        IPC library for the GnuPG components
ii  libasyncns0:amd64                  0.8-6+b3                       amd64        Asynchronous name service query library
ii  libatk1.0-0:amd64                  2.46.0-5                       amd64        ATK accessibility toolkit
ii  libatomic1:amd64                   12.2.0-14                      amd64        support library providing __atomic built-in functions
ii  libattr1:amd64                     1:2.5.1-4                      amd64        extended attribute handling - shared library
ii  libaudit-common                    1:3.0.9-1                      all          Dynamic library for security auditing - common files
ii  libaudit1:amd64                    1:3.0.9-1                      amd64        Dynamic library for security auditing
ii  libauthen-sasl-perl                2.1600-3                       all          Authen::SASL - SASL Authentication framework
ii  libavahi-client3:amd64             0.8-10                         amd64        Avahi client library
ii  libavahi-common-data:amd64         0.8-10                         amd64        Avahi common data files
ii  libavahi-common3:amd64             0.8-10                         amd64        Avahi common library
ii  libavc1394-0:amd64                 0.5.4-5                        amd64        control IEEE 1394 audio/video devices
ii  libavcodec59:amd64                 7:5.1.5-0+deb12u1              amd64        FFmpeg library with de/encoders for audio/video codecs - runtime files
ii  libavdevice59:amd64                7:5.1.5-0+deb12u1              amd64        FFmpeg library for handling input and output devices - runtime files
ii  libavfilter8:amd64                 7:5.1.5-0+deb12u1              amd64        FFmpeg library containing media filters - runtime files
ii  libavformat59:amd64                7:5.1.5-0+deb12u1              amd64        FFmpeg library with (de)muxers for multimedia containers - runtime files
ii  libavif15:amd64                    0.11.1-1                       amd64        Library for handling .avif files
ii  libavutil57:amd64                  7:5.1.5-0+deb12u1              amd64        FFmpeg library with functions for simplifying programming - runtime files
ii  libbdplus0:amd64                   0.2.0-3                        amd64        implementation of BD+ for reading Blu-ray Discs
ii  libbinutils:amd64                  2.40-2                         amd64        GNU binary utilities (private shared library)
ii  libblas-dev:amd64                  3.11.0-2                       amd64        Basic Linear Algebra Subroutines 3, static library
ii  libblas3:amd64                     3.11.0-2                       amd64        Basic Linear Algebra Reference implementations, shared library
ii  libblkid-dev:amd64                 2.38.1-5+deb12u1               amd64        block device ID library - headers
ii  libblkid1:amd64                    2.38.1-5+deb12u1               amd64        block device ID library
ii  libblosc-dev:amd64                 1.21.3+ds-1                    amd64        high performance meta-compressor optimized for binary data (development files)
ii  libblosc1:amd64                    1.21.3+ds-1                    amd64        high performance meta-compressor optimized for binary data
ii  libbluetooth-dev:amd64             5.66-1+deb12u1                 amd64        Development files for using the BlueZ Linux Bluetooth library
ii  libbluetooth3:amd64                5.66-1+deb12u1                 amd64        Library to use the BlueZ Linux Bluetooth stack
ii  libbluray2:amd64                   1:1.3.4-1                      amd64        Blu-ray disc playback support library (shared library)
ii  libboost-dev:amd64                 1.74.0.3                       amd64        Boost C++ Libraries development files (default version)
ii  libboost1.74-dev:amd64             1.74.0+ds1-21                  amd64        Boost C++ Libraries development files
ii  libbrotli-dev:amd64                1.0.9-2+b6                     amd64        library implementing brotli encoder and decoder (development files)
ii  libbrotli1:amd64                   1.0.9-2+b6                     amd64        library implementing brotli encoder and decoder (shared libraries)
ii  libbs2b0:amd64                     3.1.0+dfsg-7                   amd64        Bauer stereophonic-to-binaural DSP library
ii  libbsd0:amd64                      0.11.7-2                       amd64        utility functions from BSD systems - shared library
ii  libbz2-1.0:amd64                   1.0.8-5+b1                     amd64        high-quality block-sorting file compressor library - runtime
ii  libbz2-dev:amd64                   1.0.8-5+b1                     amd64        high-quality block-sorting file compressor library - development
ii  libc-bin                           2.36-9+deb12u4                 amd64        GNU C Library: Binaries
ii  libc-dev-bin                       2.36-9+deb12u4                 amd64        GNU C Library: Development binaries
ii  libc6:amd64                        2.36-9+deb12u4                 amd64        GNU C Library: Shared libraries
ii  libc6-dev:amd64                    2.36-9+deb12u4                 amd64        GNU C Library: Development Libraries and Header Files
ii  libcaca0:amd64                     0.99.beta20-3                  amd64        colour ASCII art library
ii  libcairo-gobject2:amd64            1.16.0-7                       amd64        Cairo 2D vector graphics library (GObject library)
ii  libcairo-script-interpreter2:amd64 1.16.0-7                       amd64        Cairo 2D vector graphics library (script interpreter)
ii  libcairo2:amd64                    1.16.0-7                       amd64        Cairo 2D vector graphics library
ii  libcairo2-dev:amd64                1.16.0-7                       amd64        Development files for the Cairo 2D graphics library
ii  libcap-ng0:amd64                   0.8.3-1+b3                     amd64        alternate POSIX capabilities library
ii  libcap2:amd64                      1:2.66-4                       amd64        POSIX 1003.1e capabilities (library)
ii  libcap2-bin                        1:2.66-4                       amd64        POSIX 1003.1e capabilities (utilities)
ii  libcbor0.8:amd64                   0.8.0-2+b1                     amd64        library for parsing and generating CBOR (RFC 7049)
ii  libcc1-0:amd64                     12.2.0-14                      amd64        GCC cc1 plugin for GDB
ii  libcdio-cdda2:amd64                10.2+2.0.1-1                   amd64        library to read and control digital audio CDs
ii  libcdio-paranoia2:amd64            10.2+2.0.1-1                   amd64        library to read digital audio CDs with error correction
ii  libcdio19:amd64                    2.1.0-4                        amd64        library to read and control CD-ROM
ii  libcdt5:amd64                      2.42.2-7+b3                    amd64        rich set of graph drawing tools - cdt library
ii  libcfitsio-dev:amd64               4.2.0-3                        amd64        library for I/O with FITS format data files (development files)
ii  libcfitsio-doc                     4.2.0-3                        all          documentation for CFITSIO
ii  libcfitsio10:amd64                 4.2.0-3                        amd64        shared library for I/O with FITS format data files
ii  libcgraph6:amd64                   2.42.2-7+b3                    amd64        rich set of graph drawing tools - cgraph library
ii  libchromaprint1:amd64              1.5.1-2+b1                     amd64        audio fingerprint library
ii  libcjson1:amd64                    1.7.15-1+deb12u1               amd64        Ultralightweight JSON parser in ANSI C
ii  libclone-perl:amd64                0.46-1                         amd64        module for recursively copying Perl datatypes
ii  libcodec2-1.0:amd64                1.0.5-1                        amd64        Codec2 runtime library
ii  libcom-err2:amd64                  1.47.0-2                       amd64        common error description library
ii  libcrypt-dev:amd64                 1:4.4.33-2                     amd64        libcrypt development files
ii  libcrypt1:amd64                    1:4.4.33-2                     amd64        libcrypt shared library
ii  libcryptsetup12:amd64              2:2.6.1-4~deb12u2              amd64        disk encryption support - shared library
ii  libctf-nobfd0:amd64                2.40-2                         amd64        Compact C Type Format library (runtime, no BFD dependency)
ii  libctf0:amd64                      2.40-2                         amd64        Compact C Type Format library (runtime, BFD dependency)
ii  libcups2:amd64                     2.4.2-3+deb12u5                amd64        Common UNIX Printing System(tm) - Core library
ii  libcurl3-gnutls:amd64              7.88.1-10+deb12u6              amd64        easy-to-use client-side URL transfer library (GnuTLS flavour)
ii  libcurl4:amd64                     7.88.1-10+deb12u6              amd64        easy-to-use client-side URL transfer library (OpenSSL flavour)
ii  libcurl4-openssl-dev:amd64         7.88.1-10+deb12u6              amd64        development files and documentation for libcurl (OpenSSL flavour)
ii  libdata-dump-perl                  1.25-1                         all          Perl module to help dump data structures
ii  libdatrie1:amd64                   0.2.13-2+b1                    amd64        Double-array trie library
ii  libdav1d-dev:amd64                 1.0.0-2+deb12u1                amd64        fast and small AV1 video stream decoder (development files)
ii  libdav1d6:amd64                    1.0.0-2+deb12u1                amd64        fast and small AV1 video stream decoder (shared library)
ii  libdb-dev:amd64                    5.3.2                          amd64        Berkeley Database Libraries [development]
ii  libdb5.3:amd64                     5.3.28+dfsg2-1                 amd64        Berkeley v5.3 Database Libraries [runtime]
ii  libdb5.3-dev                       5.3.28+dfsg2-1                 amd64        Berkeley v5.3 Database Libraries [development]
ii  libdbus-1-3:amd64                  1.14.10-1~deb12u1              amd64        simple interprocess messaging system (library)
ii  libdc1394-25:amd64                 2.2.6-4                        amd64        high level programming interface for IEEE 1394 digital cameras
ii  libde265-0:amd64                   1.0.11-1+deb12u2               amd64        Open H.265 video codec implementation
ii  libde265-dev:amd64                 1.0.11-1+deb12u2               amd64        Open H.265 video codec implementation - development files
ii  libdebconfclient0:amd64            0.270                          amd64        Debian Configuration Management System (C-implementation library)
ii  libdecor-0-0:amd64                 0.1.1-2                        amd64        client-side window decoration library
ii  libdecor-0-plugin-1-cairo:amd64    0.1.1-2                        amd64        default decoration plugin
ii  libdeflate-dev:amd64               1.14-1                         amd64        headers for whole-buffer compression and decompression library
ii  libdeflate0:amd64                  1.14-1                         amd64        fast, whole-buffer DEFLATE-based compression and decompression
ii  libdevmapper1.02.1:amd64           2:1.02.185-2                   amd64        Linux Kernel Device Mapper userspace library
ii  libdjvulibre-dev:amd64             3.5.28-2+b1                    amd64        Development files for the DjVu image format
ii  libdjvulibre-text                  3.5.28-2                       all          Linguistic support files for libdjvulibre
ii  libdjvulibre21:amd64               3.5.28-2+b1                    amd64        Runtime support for the DjVu image format
ii  libdpkg-perl                       1.21.22                        all          Dpkg perl modules
ii  libdrm-amdgpu1:amd64               2.4.114-1+b1                   amd64        Userspace interface to amdgpu-specific kernel DRM services -- runtime
ii  libdrm-common                      2.4.114-1                      all          Userspace interface to kernel DRM services -- common files
ii  libdrm-intel1:amd64                2.4.114-1+b1                   amd64        Userspace interface to intel-specific kernel DRM services -- runtime
ii  libdrm-nouveau2:amd64              2.4.114-1+b1                   amd64        Userspace interface to nouveau-specific kernel DRM services -- runtime
ii  libdrm-radeon1:amd64               2.4.114-1+b1                   amd64        Userspace interface to radeon-specific kernel DRM services -- runtime
ii  libdrm2:amd64                      2.4.114-1+b1                   amd64        Userspace interface to kernel DRM services -- runtime
ii  libduktape207:amd64                2.7.0-2                        amd64        embeddable Javascript engine, library
ii  libdw1:amd64                       0.188-2.1                      amd64        library that provides access to the DWARF debug information
ii  libedit2:amd64                     3.1-20221030-2                 amd64        BSD editline and history libraries
ii  libegl-mesa0:amd64                 22.3.6-1+deb12u1               amd64        free implementation of the EGL API -- Mesa vendor library
ii  libegl1:amd64                      1.6.0-1                        amd64        Vendor neutral GL dispatch library -- EGL support
ii  libelf1:amd64                      0.188-2.1                      amd64        library to read and write ELF files
ii  libencode-locale-perl              1.05-3                         all          utility to determine the locale encoding
ii  libepoxy0:amd64                    1.5.10-1                       amd64        OpenGL function pointer management library
ii  liberror-perl                      0.17029-2                      all          Perl module for error/exception handling in an OO-ish way
ii  libespeak1:amd64                   1.48.15+dfsg-3                 amd64        Multi-lingual software speech synthesizer: shared library
ii  libevent-2.1-7:amd64               2.1.12-stable-8                amd64        Asynchronous event notification library
ii  libevent-core-2.1-7:amd64          2.1.12-stable-8                amd64        Asynchronous event notification library (core)
ii  libevent-dev                       2.1.12-stable-8                amd64        Asynchronous event notification library (development files)
ii  libevent-extra-2.1-7:amd64         2.1.12-stable-8                amd64        Asynchronous event notification library (extra)
ii  libevent-openssl-2.1-7:amd64       2.1.12-stable-8                amd64        Asynchronous event notification library (openssl)
ii  libevent-pthreads-2.1-7:amd64      2.1.12-stable-8                amd64        Asynchronous event notification library (pthreads)
ii  libexif-dev:amd64                  0.6.24-1+b1                    amd64        library to parse EXIF files (development files)
ii  libexif12:amd64                    0.6.24-1+b1                    amd64        library to parse EXIF files
ii  libexpat1:amd64                    2.5.0-1                        amd64        XML parsing C library - runtime library
ii  libexpat1-dev:amd64                2.5.0-1                        amd64        XML parsing C library - development kit
ii  libext2fs2:amd64                   1.47.0-2                       amd64        ext2/ext3/ext4 file system libraries
ii  libfdisk1:amd64                    2.38.1-5+deb12u1               amd64        fdisk partitioning library
ii  libffi-dev:amd64                   3.4.4-1                        amd64        Foreign Function Interface library (development files)
ii  libffi8:amd64                      3.4.4-1                        amd64        Foreign Function Interface library runtime
ii  libfftw3-double3:amd64             3.3.10-1                       amd64        Library for computing Fast Fourier Transforms - Double precision
ii  libfido2-1:amd64                   1.12.0-2+b1                    amd64        library for generating and verifying FIDO 2.0 objects
ii  libfile-basedir-perl               0.09-2                         all          Perl module to use the freedesktop basedir specification
ii  libfile-desktopentry-perl          0.22-3                         all          Perl module to handle freedesktop .desktop files
ii  libfile-listing-perl               6.15-1                         all          module to parse directory listings
ii  libfile-mimeinfo-perl              0.33-1                         all          Perl module to determine file types
ii  libflac12:amd64                    1.4.2+ds-2                     amd64        Free Lossless Audio Codec - runtime C library
ii  libflite1:amd64                    2.2-5                          amd64        Small run-time speech synthesis engine - shared libraries
ii  libfont-afm-perl                   1.20-4                         all          Perl interface to Adobe Font Metrics files
ii  libfontconfig-dev:amd64            2.14.1-4                       amd64        generic font configuration library - development
ii  libfontconfig1:amd64               2.14.1-4                       amd64        generic font configuration library - runtime
ii  libfontenc1:amd64                  1:1.1.4-1                      amd64        X11 font encoding library
ii  libfreetype-dev:amd64              2.12.1+dfsg-5                  amd64        FreeType 2 font engine, development files
ii  libfreetype6:amd64                 2.12.1+dfsg-5                  amd64        FreeType 2 font engine, shared library files
ii  libfreetype6-dev:amd64             2.12.1+dfsg-5                  amd64        FreeType 2 font engine, development files (transitional package)
ii  libfreexl-dev:amd64                1.0.6-2                        amd64        library for direct reading of Microsoft Excel spreadsheets - devel
ii  libfreexl1:amd64                   1.0.6-2                        amd64        library for direct reading of Microsoft Excel spreadsheets
ii  libfribidi0:amd64                  1.0.8-2.1                      amd64        Free Implementation of the Unicode BiDi algorithm
ii  libfyba-dev:amd64                  4.1.1-8                        amd64        Header files for FYBA library
ii  libfyba0:amd64                     4.1.1-8                        amd64        FYBA library to read and write Norwegian geodata standard format SOSI
ii  libgail-common:amd64               2.24.33-2                      amd64        GNOME Accessibility Implementation Library -- common modules
ii  libgail18:amd64                    2.24.33-2                      amd64        GNOME Accessibility Implementation Library -- shared libraries
ii  libgav1-1:amd64                    0.18.0-1+b1                    amd64        AV1 decoder developed by Google -- runtime library
ii  libgbm1:amd64                      22.3.6-1+deb12u1               amd64        generic buffer management API -- runtime
ii  libgcc-12-dev:amd64                12.2.0-14                      amd64        GCC support library (development files)
ii  libgcc-s1:amd64                    12.2.0-14                      amd64        GCC support library
ii  libgcrypt20:amd64                  1.10.1-3                       amd64        LGPL Crypto library - runtime library
ii  libgd3:amd64                       2.3.3-9                        amd64        GD Graphics Library
ii  libgdal-dev                        3.6.2+dfsg-1+b2                amd64        Geospatial Data Abstraction Library - Development files
ii  libgdal32                          3.6.2+dfsg-1+b2                amd64        Geospatial Data Abstraction Library
ii  libgdbm-compat4:amd64              1.23-3                         amd64        GNU dbm database routines (legacy support runtime version) 
ii  libgdbm-dev:amd64                  1.23-3                         amd64        GNU dbm database routines (development files) 
ii  libgdbm6:amd64                     1.23-3                         amd64        GNU dbm database routines (runtime version) 
ii  libgdk-pixbuf-2.0-0:amd64          2.42.10+dfsg-1+b1              amd64        GDK Pixbuf library
ii  libgdk-pixbuf-2.0-dev:amd64        2.42.10+dfsg-1+b1              amd64        GDK Pixbuf library (development files)
ii  libgdk-pixbuf2.0-bin               2.42.10+dfsg-1+b1              amd64        GDK Pixbuf library (thumbnailer)
ii  libgdk-pixbuf2.0-common            2.42.10+dfsg-1                 all          GDK Pixbuf library - data files
ii  libgeos-c1v5:amd64                 3.11.1-1                       amd64        Geometry engine for Geographic Information Systems - C Library
ii  libgeos-dev                        3.11.1-1                       amd64        Geometry engine for GIS - Development files
ii  libgeos3.11.1:amd64                3.11.1-1                       amd64        Geometry engine for Geographic Information Systems - C++ Library
ii  libgeotiff-dev:amd64               1.7.1-2+b1                     amd64        GeoTIFF (geografic enabled TIFF) library -- development files
ii  libgeotiff5:amd64                  1.7.1-2+b1                     amd64        GeoTIFF (geografic enabled TIFF) library -- run-time files
ii  libgfortran5:amd64                 12.2.0-14                      amd64        Runtime library for GNU Fortran applications
ii  libgif-dev:amd64                   5.2.1-2.5                      amd64        library for GIF images (development)
ii  libgif7:amd64                      5.2.1-2.5                      amd64        library for GIF images (library)
ii  libgirepository-1.0-1:amd64        1.74.0-3                       amd64        Library for handling GObject introspection data (runtime library)
ii  libgl1:amd64                       1.6.0-1                        amd64        Vendor neutral GL dispatch library -- legacy GL support
ii  libgl1-mesa-dri:amd64              22.3.6-1+deb12u1               amd64        free implementation of the OpenGL API -- DRI modules
ii  libglapi-mesa:amd64                22.3.6-1+deb12u1               amd64        free implementation of the GL API -- shared library
ii  libgles2:amd64                     1.6.0-1                        amd64        Vendor neutral GL dispatch library -- GLESv2 support
ii  libglib2.0-0:amd64                 2.74.6-2                       amd64        GLib library of C routines
ii  libglib2.0-bin                     2.74.6-2                       amd64        Programs for the GLib library
ii  libglib2.0-data                    2.74.6-2                       all          Common files for GLib library
ii  libglib2.0-dev:amd64               2.74.6-2                       amd64        Development files for the GLib library
ii  libglib2.0-dev-bin                 2.74.6-2                       amd64        Development utilities for the GLib library
ii  libglvnd0:amd64                    1.6.0-1                        amd64        Vendor neutral GL dispatch library
ii  libglx-mesa0:amd64                 22.3.6-1+deb12u1               amd64        free implementation of the OpenGL API -- GLX vendor library
ii  libglx0:amd64                      1.6.0-1                        amd64        Vendor neutral GL dispatch library -- GLX support
ii  libgme0:amd64                      0.6.3-6                        amd64        Playback library for video game music files - shared library
ii  libgmp-dev:amd64                   2:6.2.1+dfsg1-1.1              amd64        Multiprecision arithmetic library developers tools
ii  libgmp10:amd64                     2:6.2.1+dfsg1-1.1              amd64        Multiprecision arithmetic library
ii  libgmpxx4ldbl:amd64                2:6.2.1+dfsg1-1.1              amd64        Multiprecision arithmetic library (C++ bindings)
ii  libgnutls30:amd64                  3.7.9-2+deb12u2                amd64        GNU TLS library - main runtime library
ii  libgomp1:amd64                     12.2.0-14                      amd64        GCC OpenMP (GOMP) support library
ii  libgpg-error0:amd64                1.46-1                         amd64        GnuPG development runtime library
ii  libgpm2:amd64                      1.20.7-10+b1                   amd64        General Purpose Mouse - shared library
ii  libgprofng0:amd64                  2.40-2                         amd64        GNU Next Generation profiler (runtime library)
ii  libgraphite2-3:amd64               1.3.14-1                       amd64        Font rendering engine for Complex Scripts -- library
ii  libgraphviz-dev:amd64              2.42.2-7+b3                    amd64        graphviz libs and headers against which to build applications
ii  libgsm1:amd64                      1.0.22-1                       amd64        Shared libraries for GSM speech compressor
ii  libgssapi-krb5-2:amd64             1.20.1-2+deb12u1               amd64        MIT Kerberos runtime libraries - krb5 GSS-API Mechanism
ii  libgssrpc4:amd64                   1.20.1-2+deb12u1               amd64        MIT Kerberos runtime libraries - GSS enabled ONCRPC
ii  libgstreamer1.0-0:amd64            1.22.0-2                       amd64        Core GStreamer libraries and elements
ii  libgtk2.0-0:amd64                  2.24.33-2                      amd64        GTK graphical user interface library - old version
ii  libgtk2.0-bin                      2.24.33-2                      amd64        programs for the GTK graphical user interface library
ii  libgtk2.0-common                   2.24.33-2                      all          common files for the GTK graphical user interface library
ii  libgts-0.7-5:amd64                 0.7.6+darcs121130-5+b1         amd64        library to deal with 3D computational surface meshes
ii  libgts-bin                         0.7.6+darcs121130-5+b1         amd64        utility binaries for libgts
ii  libgvc6                            2.42.2-7+b3                    amd64        rich set of graph drawing tools - gvc library
ii  libgvc6-plugins-gtk                2.42.2-7+b3                    amd64        rich set of graph drawing tools - gtk plugins
ii  libgvpr2:amd64                     2.42.2-7+b3                    amd64        rich set of graph drawing tools - gvpr library
ii  libharfbuzz0b:amd64                6.0.0+dfsg-3                   amd64        OpenType text shaping engine (shared library)
ii  libhdf4-0-alt                      4.2.15-5                       amd64        Hierarchical Data Format library (without NetCDF)
ii  libhdf4-alt-dev                    4.2.15-5                       amd64        Hierarchical Data Format development files (without NetCDF)
ii  libhdf5-103-1:amd64                1.10.8+repack1-1               amd64        HDF5 C runtime files - serial version
ii  libhdf5-cpp-103-1:amd64            1.10.8+repack1-1               amd64        HDF5 - C++ runtime files - serial version
ii  libhdf5-dev                        1.10.8+repack1-1               amd64        HDF5 - development files - serial version
ii  libhdf5-fortran-102:amd64          1.10.8+repack1-1               amd64        HDF5 Fortran runtime files - serial version
ii  libhdf5-hl-100:amd64               1.10.8+repack1-1               amd64        HDF5 High Level runtime files - serial version
ii  libhdf5-hl-cpp-100:amd64           1.10.8+repack1-1               amd64        HDF5 High Level C++ runtime files - serial version
ii  libhdf5-hl-fortran-100:amd64       1.10.8+repack1-1               amd64        HDF5 High Level Fortran runtime files - serial version
ii  libheif-dev:amd64                  1.15.1-1                       amd64        ISO/IEC 23008-12:2017 HEIF file format decoder - development files
ii  libheif1:amd64                     1.15.1-1                       amd64        ISO/IEC 23008-12:2017 HEIF file format decoder - shared library
ii  libhogweed6:amd64                  3.8.1-2                        amd64        low level cryptographic library (public-key cryptos)
ii  libhtml-form-perl                  6.11-1                         all          module that represents an HTML form element
ii  libhtml-format-perl                2.16-2                         all          module for transforming HTML into various formats
ii  libhtml-parser-perl:amd64          3.81-1                         amd64        collection of modules that parse HTML text documents
ii  libhtml-tagset-perl                3.20-6                         all          data tables pertaining to HTML
ii  libhtml-tree-perl                  5.07-3                         all          Perl module to represent and create HTML syntax trees
ii  libhttp-cookies-perl               6.10-1                         all          HTTP cookie jars
ii  libhttp-daemon-perl                6.16-1                         all          simple http server class
ii  libhttp-date-perl                  6.05-2                         all          module of date conversion routines
ii  libhttp-message-perl               6.44-1                         all          perl interface to HTTP style messages
ii  libhttp-negotiate-perl             6.01-2                         all          implementation of content negotiation
ii  libhwy1:amd64                      1.0.3-3+deb12u1                amd64        Efficient and performance-portable SIMD wrapper (runtime files)
ii  libice-dev:amd64                   2:1.0.10-1                     amd64        X11 Inter-Client Exchange library (development headers)
ii  libice6:amd64                      2:1.0.10-1                     amd64        X11 Inter-Client Exchange library
ii  libicu-dev:amd64                   72.1-3                         amd64        Development files for International Components for Unicode
ii  libicu72:amd64                     72.1-3                         amd64        International Components for Unicode
ii  libid3tag0:amd64                   0.15.1b-14                     amd64        ID3 tag reading library from the MAD project
ii  libidn2-0:amd64                    2.3.3-1+b1                     amd64        Internationalized domain names (IDNA2008/TR46) library
ii  libiec61883-0:amd64                1.2.0-6+b1                     amd64        partial implementation of IEC 61883 (shared lib)
ii  libigdgmm12:amd64                  22.3.3+ds1-1                   amd64        Intel Graphics Memory Management Library -- shared library
ii  libimath-3-1-29:amd64              3.1.6-1                        amd64        Utility libraries from ASF used by OpenEXR - runtime
ii  libimath-dev:amd64                 3.1.6-1                        amd64        Utility libraries from ASF used by OpenEXR - development
ii  libio-html-perl                    1.004-3                        all          open an HTML file with automatic charset detection
ii  libio-socket-ssl-perl              2.081-2                        all          Perl module implementing object oriented interface to SSL sockets
ii  libio-stringy-perl                 2.111-3                        all          modules for I/O on in-core objects (strings/arrays)
ii  libip4tc2:amd64                    1.8.9-2                        amd64        netfilter libip4tc library
ii  libipc-system-simple-perl          1.30-2                         all          Perl module to run commands simply, with detailed diagnostics
ii  libisl23:amd64                     0.25-1.1                       amd64        manipulating sets and relations of integer points bounded by linear constraints
ii  libitm1:amd64                      12.2.0-14                      amd64        GNU Transactional Memory Library
ii  libjack-jackd2-0:amd64             1.9.21~dfsg-3                  amd64        JACK Audio Connection Kit (libraries)
ii  libjansson4:amd64                  2.14-2                         amd64        C library for encoding, decoding and manipulating JSON data
ii  libjbig-dev:amd64                  2.1-6.1                        amd64        JBIGkit development files
ii  libjbig0:amd64                     2.1-6.1                        amd64        JBIGkit libraries
ii  libjemalloc2:amd64                 5.3.0-1                        amd64        general-purpose scalable concurrent malloc(3) implementation
ii  libjpeg-dev:amd64                  1:2.1.5-2                      amd64        Development files for the JPEG library [dummy package]
ii  libjpeg62-turbo:amd64              1:2.1.5-2                      amd64        libjpeg-turbo JPEG runtime library
ii  libjpeg62-turbo-dev:amd64          1:2.1.5-2                      amd64        Development files for the libjpeg-turbo JPEG library
ii  libjson-c-dev:amd64                0.16-2                         amd64        JSON manipulation library - development files
ii  libjson-c5:amd64                   0.16-2                         amd64        JSON manipulation library - shared library
ii  libjsoncpp25:amd64                 1.9.5-4                        amd64        library for reading and writing JSON for C++
ii  libjxl0.7:amd64                    0.7.0-10                       amd64        JPEG XL Image Coding System - "JXL" (shared libraries)
ii  libk5crypto3:amd64                 1.20.1-2+deb12u1               amd64        MIT Kerberos runtime libraries - Crypto Library
ii  libkadm5clnt-mit12:amd64           1.20.1-2+deb12u1               amd64        MIT Kerberos runtime libraries - Administration Clients
ii  libkadm5srv-mit12:amd64            1.20.1-2+deb12u1               amd64        MIT Kerberos runtime libraries - KDC and Admin Server
ii  libkdb5-10:amd64                   1.20.1-2+deb12u1               amd64        MIT Kerberos runtime libraries - Kerberos database
ii  libkeyutils1:amd64                 1.6.3-2                        amd64        Linux Key Management Utilities (library)
ii  libkml-dev:amd64                   1.3.0-10                       amd64        Library to manipulate KML 2.2 OGC standard files - development files
ii  libkmlbase1:amd64                  1.3.0-10                       amd64        Library to manipulate KML 2.2 OGC standard files - libkmlbase
ii  libkmlconvenience1:amd64           1.3.0-10                       amd64        Library to manipulate KML 2.2 OGC standard files - libkmlconvenience
ii  libkmldom1:amd64                   1.3.0-10                       amd64        Library to manipulate KML 2.2 OGC standard files - libkmldom
ii  libkmlengine1:amd64                1.3.0-10                       amd64        Library to manipulate KML 2.2 OGC standard files - libkmlengine
ii  libkmlregionator1:amd64            1.3.0-10                       amd64        Library to manipulate KML 2.2 OGC standard files - libkmlregionator
ii  libkmlxsd1:amd64                   1.3.0-10                       amd64        Library to manipulate KML 2.2 OGC standard files - libkmlxsd
ii  libkmod2:amd64                     30+20221128-1                  amd64        libkmod shared library
ii  libkrb5-3:amd64                    1.20.1-2+deb12u1               amd64        MIT Kerberos runtime libraries
ii  libkrb5-dev:amd64                  1.20.1-2+deb12u1               amd64        headers and development libraries for MIT Kerberos
ii  libkrb5support0:amd64              1.20.1-2+deb12u1               amd64        MIT Kerberos runtime libraries - Support library
ii  libksba8:amd64                     1.6.3-2                        amd64        X.509 and CMS support library
ii  liblab-gamut1:amd64                2.42.2-7+b3                    amd64        rich set of graph drawing tools - liblab_gamut library
ii  liblapack-dev:amd64                3.11.0-2                       amd64        Library of linear algebra routines 3 - static version
ii  liblapack3:amd64                   3.11.0-2                       amd64        Library of linear algebra routines 3 - shared version
ii  liblcms2-2:amd64                   2.14-2                         amd64        Little CMS 2 color management library
ii  liblcms2-dev:amd64                 2.14-2                         amd64        Little CMS 2 color management library development headers
ii  libldap-2.5-0:amd64                2.5.13+dfsg-5                  amd64        OpenLDAP libraries
ii  liblept5:amd64                     1.82.0-3+b3                    amd64        image processing library
ii  libleptonica-dev                   1.82.0-3+b3                    amd64        image processing library
ii  liblerc-dev:amd64                  4.0.0+ds-2                     amd64        Limited Error Raster Compression library (Development files)
ii  liblerc4:amd64                     4.0.0+ds-2                     amd64        Limited Error Raster Compression library
ii  liblilv-0-0:amd64                  0.24.14-1                      amd64        library for simple use of LV2 plugins
ii  libllvm15:amd64                    1:15.0.6-4+b1                  amd64        Modular compiler and toolchain technologies, runtime library
ii  liblqr-1-0:amd64                   0.4.2-2.1                      amd64        converts plain array images into multi-size representation
ii  liblqr-1-0-dev:amd64               0.4.2-2.1                      amd64        converts plain array images into multi-size representation (developments files)
ii  liblsan0:amd64                     12.2.0-14                      amd64        LeakSanitizer -- a memory leak detector (runtime)
ii  libltdl-dev:amd64                  2.4.7-5                        amd64        System independent dlopen wrapper for GNU libtool (headers)
ii  libltdl7:amd64                     2.4.7-5                        amd64        System independent dlopen wrapper for GNU libtool
ii  liblwp-mediatypes-perl             6.04-2                         all          module to guess media type for a file or a URL
ii  liblwp-protocol-https-perl         6.10-1                         all          HTTPS driver for LWP::UserAgent
ii  liblz4-1:amd64                     1.9.4-1                        amd64        Fast LZ compression algorithm library - runtime
ii  liblz4-dev:amd64                   1.9.4-1                        amd64        Fast LZ compression algorithm library - development files
ii  liblzma-dev:amd64                  5.4.1-0.2                      amd64        XZ-format compression library - development files
ii  liblzma5:amd64                     5.4.1-0.2                      amd64        XZ-format compression library
ii  liblzo2-2:amd64                    2.10-2                         amd64        data compression library
ii  libmad0:amd64                      0.15.1b-10.1+b1                amd64        MPEG audio decoder library
ii  libmagic-mgc                       1:5.44-3                       amd64        File type determination library using "magic" numbers (compiled magic file)
ii  libmagic1:amd64                    1:5.44-3                       amd64        Recognize the type of data in a file using "magic" numbers - library
ii  libmagickcore-6-arch-config:amd64  8:6.9.11.60+dfsg-1.6+deb12u1   amd64        low-level image manipulation library - architecture header files
ii  libmagickcore-6-headers            8:6.9.11.60+dfsg-1.6+deb12u1   all          low-level image manipulation library - header files
ii  libmagickcore-6.q16-6:amd64        8:6.9.11.60+dfsg-1.6+deb12u1   amd64        low-level image manipulation library -- quantum depth Q16
ii  libmagickcore-6.q16-6-extra:amd64  8:6.9.11.60+dfsg-1.6+deb12u1   amd64        low-level image manipulation library - extra codecs (Q16)
ii  libmagickcore-6.q16-dev:amd64      8:6.9.11.60+dfsg-1.6+deb12u1   amd64        low-level image manipulation library - development files (Q16)
ii  libmagickcore-dev                  8:6.9.11.60+dfsg-1.6+deb12u1   all          low-level image manipulation library -- dummy package
ii  libmagickwand-6-headers            8:6.9.11.60+dfsg-1.6+deb12u1   all          image manipulation library - headers files
ii  libmagickwand-6.q16-6:amd64        8:6.9.11.60+dfsg-1.6+deb12u1   amd64        image manipulation library -- quantum depth Q16
ii  libmagickwand-6.q16-dev:amd64      8:6.9.11.60+dfsg-1.6+deb12u1   amd64        image manipulation library - development files (Q16)
ii  libmagickwand-dev                  8:6.9.11.60+dfsg-1.6+deb12u1   all          image manipulation library -- dummy package
ii  libmailtools-perl                  2.21-2                         all          modules to manipulate email in perl programs
ii  libmariadb-dev                     1:10.11.6-0+deb12u1            amd64        MariaDB database development files
ii  libmariadb-dev-compat              1:10.11.6-0+deb12u1            amd64        MariaDB Connector/C, compatibility symlinks
ii  libmariadb3:amd64                  1:10.11.6-0+deb12u1            amd64        MariaDB database client library
ii  libmaxminddb-dev:amd64             1.7.1-1                        amd64        IP geolocation database library (development headers)
ii  libmaxminddb0:amd64                1.7.1-1                        amd64        IP geolocation database library
ii  libmbedcrypto7:amd64               2.28.3-1                       amd64        lightweight crypto and SSL/TLS library - crypto library
ii  libmd0:amd64                       1.0.4-2                        amd64        message digest functions from BSD systems - shared library
ii  libmfx1:amd64                      22.5.4-1                       amd64        Intel Media SDK -- shared library
ii  libminizip-dev:amd64               1.1-8+deb12u1                  amd64        compression library - minizip development files
ii  libminizip1:amd64                  1.1-8+deb12u1                  amd64        compression library - minizip library
ii  libmount-dev:amd64                 2.38.1-5+deb12u1               amd64        device mounting library - headers
ii  libmount1:amd64                    2.38.1-5+deb12u1               amd64        device mounting library
ii  libmp3lame0:amd64                  3.100-6                        amd64        MP3 encoding library
ii  libmpc3:amd64                      1.3.1-1                        amd64        multiple precision complex floating-point library
ii  libmpfr6:amd64                     4.2.0-1                        amd64        multiple precision floating-point computation
ii  libmpg123-0:amd64                  1.31.2-1                       amd64        MPEG layer 1/2/3 audio decoder (shared library)
ii  libmysofa1:amd64                   1.3.1~dfsg0-1                  amd64        library to read HRTFs stored in the AES69-2015 SOFA format
ii  libncurses-dev:amd64               6.4-4                          amd64        developer's libraries for ncurses
ii  libncurses5-dev:amd64              6.4-4                          amd64        transitional package for libncurses-dev
ii  libncurses6:amd64                  6.4-4                          amd64        shared libraries for terminal handling
ii  libncursesw5-dev:amd64             6.4-4                          amd64        transitional package for libncurses-dev
ii  libncursesw6:amd64                 6.4-4                          amd64        shared libraries for terminal handling (wide character support)
ii  libnet-dbus-perl                   1.2.0-2                        amd64        Perl extension for the DBus bindings
ii  libnet-http-perl                   6.22-1                         all          module providing low-level HTTP connection client
ii  libnet-smtp-ssl-perl               1.04-2                         all          Perl module providing SSL support to Net::SMTP
ii  libnet-ssleay-perl:amd64           1.92-2+b1                      amd64        Perl module for Secure Sockets Layer (SSL)
ii  libnetcdf-dev                      1:4.9.0-3+b1                   amd64        creation, access, and sharing of scientific data
ii  libnetcdf19:amd64                  1:4.9.0-3+b1                   amd64        Interface for scientific data access to large binary data
ii  libnettle8:amd64                   3.8.1-2                        amd64        low level cryptographic library (symmetric and one-way cryptos)
ii  libnghttp2-14:amd64                1.52.0-1+deb12u1               amd64        library implementing HTTP/2 protocol (shared library)
ii  libnorm1:amd64                     1.5.9+dfsg-2                   amd64        NACK-Oriented Reliable Multicast (NORM) library
ii  libnpth0:amd64                     1.6-3                          amd64        replacement for GNU Pth using system threads
ii  libnsl-dev:amd64                   1.3.0-2                        amd64        libnsl development files
ii  libnsl2:amd64                      1.3.0-2                        amd64        Public client interface for NIS(YP) and NIS+
ii  libnspr4:amd64                     2:4.35-1                       amd64        NetScape Portable Runtime Library
ii  libnss-systemd:amd64               252.26-1~deb12u2               amd64        nss module providing dynamic user and group name resolution
ii  libnss3:amd64                      2:3.87.1-1                     amd64        Network Security Service libraries
ii  libnuma1:amd64                     2.0.16-1                       amd64        Libraries for controlling NUMA policy
ii  libodbc2:amd64                     2.3.11-2+deb12u1               amd64        ODBC Driver Manager library for Unix
ii  libodbccr2:amd64                   2.3.11-2+deb12u1               amd64        ODBC Cursor library for Unix
ii  libodbcinst2:amd64                 2.3.11-2+deb12u1               amd64        Support library for accessing ODBC configuration files
ii  libogdi-dev                        4.1.0+ds-6                     amd64        Open Geographic Datastore Interface Library -- development
ii  libogdi4.1                         4.1.0+ds-6                     amd64        Open Geographic Datastore Interface Library -- library
ii  libogg0:amd64                      1.3.5-3                        amd64        Ogg bitstream library
ii  libopenal-data                     1:1.19.1-2                     all          Software implementation of the OpenAL audio API (data files)
ii  libopenal1:amd64                   1:1.19.1-2                     amd64        Software implementation of the OpenAL audio API (shared library)
ii  libopencore-amrnb0:amd64           0.1.6-1                        amd64        Adaptive Multi Rate speech codec - shared library
ii  libopencore-amrwb0:amd64           0.1.6-1                        amd64        Adaptive Multi-Rate - Wideband speech codec - shared library
ii  libopenexr-3-1-30:amd64            3.1.5-5                        amd64        runtime files for the OpenEXR image library
ii  libopenexr-dev                     3.1.5-5                        amd64        development files for the OpenEXR image library
ii  libopenjp2-7:amd64                 2.5.0-2                        amd64        JPEG 2000 image compression/decompression library
ii  libopenjp2-7-dev:amd64             2.5.0-2                        amd64        development files for OpenJPEG, a JPEG 2000 image library
ii  libopenmpt0:amd64                  0.6.9-1                        amd64        module music library based on OpenMPT -- shared library
ii  libopus0:amd64                     1.3.1-3                        amd64        Opus codec runtime library
ii  libp11-kit0:amd64                  0.24.1-2                       amd64        library for loading and coordinating access to PKCS#11 modules - runtime
ii  libpackagekit-glib2-18:amd64       1.2.6-5                        amd64        Library for accessing PackageKit using GLib
ii  libpam-cap:amd64                   1:2.66-4                       amd64        POSIX 1003.1e capabilities (PAM module)
ii  libpam-modules:amd64               1.5.2-6+deb12u1                amd64        Pluggable Authentication Modules for PAM
ii  libpam-modules-bin                 1.5.2-6+deb12u1                amd64        Pluggable Authentication Modules for PAM - helper binaries
ii  libpam-runtime                     1.5.2-6+deb12u1                all          Runtime support for the PAM library
ii  libpam-systemd:amd64               252.26-1~deb12u2               amd64        system and service manager - PAM module
ii  libpam0g:amd64                     1.5.2-6+deb12u1                amd64        Pluggable Authentication Modules library
ii  libpango-1.0-0:amd64               1.50.12+ds-1                   amd64        Layout and rendering of internationalized text
ii  libpangocairo-1.0-0:amd64          1.50.12+ds-1                   amd64        Layout and rendering of internationalized text
ii  libpangoft2-1.0-0:amd64            1.50.12+ds-1                   amd64        Layout and rendering of internationalized text
ii  libpathplan4:amd64                 2.42.2-7+b3                    amd64        rich set of graph drawing tools - pathplan library
ii  libpciaccess0:amd64                0.17-2                         amd64        Generic PCI access library for X
ii  libpcre2-16-0:amd64                10.42-1                        amd64        New Perl Compatible Regular Expression Library - 16 bit runtime files
ii  libpcre2-32-0:amd64                10.42-1                        amd64        New Perl Compatible Regular Expression Library - 32 bit runtime files
ii  libpcre2-8-0:amd64                 10.42-1                        amd64        New Perl Compatible Regular Expression Library- 8 bit runtime files
ii  libpcre2-dev:amd64                 10.42-1                        amd64        New Perl Compatible Regular Expression Library - development files
ii  libpcre2-posix3:amd64              10.42-1                        amd64        New Perl Compatible Regular Expression Library - posix-compatible runtime files
ii  libperl5.36:amd64                  5.36.0-7+deb12u1               amd64        shared Perl library
ii  libpgm-5.3-0:amd64                 5.3.128~dfsg-2                 amd64        OpenPGM shared library
ii  libpixman-1-0:amd64                0.42.2-1                       amd64        pixel-manipulation library for X and cairo
ii  libpixman-1-dev:amd64              0.42.2-1                       amd64        pixel-manipulation library for X and cairo (development files)
ii  libpkgconf3:amd64                  1.8.1-1                        amd64        shared library for pkgconf
ii  libplacebo208:amd64                4.208.0-3                      amd64        GPU-accelerated video/image rendering primitives (shared library)
ii  libpng-dev:amd64                   1.6.39-2                       amd64        PNG library - development (version 1.6)
ii  libpng16-16:amd64                  1.6.39-2                       amd64        PNG library - runtime (version 1.6)
ii  libpocketsphinx3:amd64             0.8+5prealpha+1-15             amd64        Speech recognition tool - front-end library
ii  libpolkit-agent-1-0:amd64          122-3                          amd64        polkit Authentication Agent API
ii  libpolkit-gobject-1-0:amd64        122-3                          amd64        polkit Authorization API
ii  libpoppler-dev:amd64               22.12.0-2+b1                   amd64        PDF rendering library -- development files
ii  libpoppler-private-dev:amd64       22.12.0-2+b1                   amd64        PDF rendering library -- private development files
ii  libpoppler126:amd64                22.12.0-2+b1                   amd64        PDF rendering library
ii  libportaudio2:amd64                19.6.0-1.2                     amd64        Portable audio I/O - shared library
ii  libpostproc56:amd64                7:5.1.5-0+deb12u1              amd64        FFmpeg library for post processing - runtime files
ii  libpq-dev                          15.8-0+deb12u1                 amd64        header files for libpq5 (PostgreSQL library)
ii  libpq5:amd64                       15.8-0+deb12u1                 amd64        PostgreSQL C client library
ii  libproc2-0:amd64                   2:4.0.2-3                      amd64        library for accessing process information from /proc
ii  libproj-dev:amd64                  9.1.1-1+b1                     amd64        Cartographic projection library (development files)
ii  libproj25:amd64                    9.1.1-1+b1                     amd64        Cartographic projection library
ii  libpsl5:amd64                      0.21.2-1                       amd64        Library for Public Suffix List (shared libraries)
ii  libpthread-stubs0-dev:amd64        0.4-1                          amd64        pthread stubs not provided by native libc, development files
ii  libpulse0:amd64                    16.1+dfsg1-2+b1                amd64        PulseAudio client libraries
ii  libpython3-stdlib:amd64            3.11.2-1+b1                    amd64        interactive high-level object-oriented language (default python3 version)
ii  libpython3.11-minimal:amd64        3.11.2-6                       amd64        Minimal subset of the Python language (version 3.11)
ii  libpython3.11-stdlib:amd64         3.11.2-6                       amd64        Interactive high-level object-oriented language (standard library, version 3.11)
ii  libqhull-dev:amd64                 2020.2-5                       amd64        calculate convex hulls and related structures (development files)
ii  libqhull-r8.0:amd64                2020.2-5                       amd64        calculate convex hulls and related structures (reentrant shared library)
ii  libqhull8.0:amd64                  2020.2-5                       amd64        calculate convex hulls and related structures (shared library)
ii  libqhullcpp8.0:amd64               2020.2-5                       amd64        calculate convex hulls and related structures (C++ shared library)
ii  libquadmath0:amd64                 12.2.0-14                      amd64        GCC Quad-Precision Math Library
ii  librabbitmq4:amd64                 0.11.0-1+b1                    amd64        AMQP client library written in C
ii  librav1e0:amd64                    0.5.1-6                        amd64        Fastest and safest AV1 encoder - shared library
ii  libraw1394-11:amd64                2.1.2-2                        amd64        library for direct access to IEEE 1394 bus (aka FireWire)
ii  libreadline-dev:amd64              8.2-1.3                        amd64        GNU readline and history libraries, development files
ii  libreadline8:amd64                 8.2-1.3                        amd64        GNU readline and history libraries, run-time libraries
ii  libregexp-ipv6-perl                0.03-3                         all          Regular expression for IPv6 addresses
ii  librhash0:amd64                    1.4.3-3                        amd64        shared library for hash functions computing
ii  librist4:amd64                     0.2.7+dfsg-1                   amd64        Reliable Internet Stream Transport -- shared library
ii  librsvg2-2:amd64                   2.54.7+dfsg-1~deb12u1          amd64        SAX-based renderer library for SVG files (runtime)
ii  librsvg2-common:amd64              2.54.7+dfsg-1~deb12u1          amd64        SAX-based renderer library for SVG files (extra runtime)
ii  librsvg2-dev:amd64                 2.54.7+dfsg-1~deb12u1          amd64        SAX-based renderer library for SVG files (development)
ii  librtmp1:amd64                     2.4+20151223.gitfa8646d.1-2+b2 amd64        toolkit for RTMP streams (shared library)
ii  librttopo-dev:amd64                1.1.0-3                        amd64        Tuscany Region topology library - Development files
ii  librttopo1:amd64                   1.1.0-3                        amd64        Tuscany Region topology library
ii  librubberband2:amd64               3.1.2+dfsg0-1                  amd64        audio time-stretching and pitch-shifting library
ii  libsamplerate0:amd64               0.2.2-3                        amd64        Audio sample rate conversion library
ii  libsasl2-2:amd64                   2.1.28+dfsg-10                 amd64        Cyrus SASL - authentication abstraction library
ii  libsasl2-modules-db:amd64          2.1.28+dfsg-10                 amd64        Cyrus SASL - pluggable authentication modules (DB)
ii  libsdl2-2.0-0:amd64                2.26.5+dfsg-1                  amd64        Simple DirectMedia Layer
ii  libseccomp2:amd64                  2.5.4-1+b3                     amd64        high level interface to Linux seccomp filter
ii  libselinux1:amd64                  3.4-1+b6                       amd64        SELinux runtime shared libraries
ii  libselinux1-dev:amd64              3.4-1+b6                       amd64        SELinux development headers
ii  libsemanage-common                 3.4-1                          all          Common files for SELinux policy management libraries
ii  libsemanage2:amd64                 3.4-1+b5                       amd64        SELinux policy management library
ii  libsensors-config                  1:3.6.0-7.1                    all          lm-sensors configuration files
ii  libsensors5:amd64                  1:3.6.0-7.1                    amd64        library to read temperature/voltage/fan sensors
ii  libsepol-dev:amd64                 3.4-2.1                        amd64        SELinux binary policy manipulation library and development files
ii  libsepol2:amd64                    3.4-2.1                        amd64        SELinux library for manipulating binary security policies
ii  libserd-0-0:amd64                  0.30.16-1                      amd64        lightweight RDF syntax library
ii  libserf-1-1:amd64                  1.3.9-11                       amd64        high-performance asynchronous HTTP client library
ii  libshine3:amd64                    3.1.1-2                        amd64        Fixed-point MP3 encoding library - runtime files
ii  libslang2:amd64                    2.3.3-3                        amd64        S-Lang programming library - runtime version
ii  libsm-dev:amd64                    2:1.2.3-1                      amd64        X11 Session Management library (development headers)
ii  libsm6:amd64                       2:1.2.3-1                      amd64        X11 Session Management library
ii  libsmartcols1:amd64                2.38.1-5+deb12u1               amd64        smart column output alignment library
ii  libsnappy1v5:amd64                 1.1.9-3                        amd64        fast compression/decompression library
ii  libsndfile1:amd64                  1.2.0-1                        amd64        Library for reading/writing audio files
ii  libsndio7.0:amd64                  1.9.0-0.3+b2                   amd64        Small audio and MIDI framework from OpenBSD, runtime libraries
ii  libsodium23:amd64                  1.0.18-1                       amd64        Network communication, cryptography and signaturing library
ii  libsonic0:amd64                    0.2.0-12                       amd64        Simple library to speed up or slow down speech
ii  libsord-0-0:amd64                  0.16.14+git221008-1            amd64        library for storing RDF data in memory
ii  libsox-fmt-alsa:amd64              14.4.2+git20190427-3.5         amd64        SoX alsa format I/O library
ii  libsox-fmt-base:amd64              14.4.2+git20190427-3.5         amd64        Minimal set of SoX format libraries
ii  libsox-fmt-mp3:amd64               14.4.2+git20190427-3.5         amd64        SoX MP2 and MP3 format library
ii  libsox3:amd64                      14.4.2+git20190427-3.5         amd64        SoX library of audio effects and processing
ii  libsoxr0:amd64                     0.1.3-4                        amd64        High quality 1D sample-rate conversion library
ii  libspatialite-dev:amd64            5.0.1-3                        amd64        Geospatial extension for SQLite - development files
ii  libspatialite7:amd64               5.0.1-3                        amd64        Geospatial extension for SQLite - libraries
ii  libspeex1:amd64                    1.2.1-2                        amd64        The Speex codec runtime library
ii  libsphinxbase3:amd64               0.8+5prealpha+1-16             amd64        Speech recognition tool - shared library
ii  libsqlite3-0:amd64                 3.40.1-2                       amd64        SQLite 3 shared library
ii  libsqlite3-dev:amd64               3.40.1-2                       amd64        SQLite 3 development files
ii  libsratom-0-0:amd64                0.6.14-1                       amd64        library for serialising LV2 atoms to/from Turtle
ii  libsrt1.5-gnutls:amd64             1.5.1-1                        amd64        Secure Reliable Transport UDP streaming library (GnuTLS flavour)
ii  libss2:amd64                       1.47.0-2                       amd64        command-line interface parsing library
ii  libssh-gcrypt-4:amd64              0.10.6-0+deb12u1               amd64        tiny C SSH library (gcrypt flavor)
ii  libssh2-1:amd64                    1.10.0-3+b1                    amd64        SSH2 client-side library
ii  libssl-dev:amd64                   3.0.13-1~deb12u1               amd64        Secure Sockets Layer toolkit - development files
ii  libssl3:amd64                      3.0.13-1~deb12u1               amd64        Secure Sockets Layer toolkit - shared libraries
ii  libstdc++-12-dev:amd64             12.2.0-14                      amd64        GNU Standard C++ Library v3 (development files)
ii  libstdc++6:amd64                   12.2.0-14                      amd64        GNU Standard C++ Library v3
ii  libstemmer0d:amd64                 2.2.0-2                        amd64        Snowball stemming algorithms for use in Information Retrieval
ii  libsuperlu-dev:amd64               5.3.0+dfsg1-2+b1               amd64        Direct solution of large, sparse systems of linear equations
ii  libsuperlu5:amd64                  5.3.0+dfsg1-2+b1               amd64        Direct solution of large, sparse systems of linear equations
ii  libsvn1:amd64                      1.14.2-4+b2                    amd64        Shared libraries used by Apache Subversion
ii  libsvtav1enc1:amd64                1.4.1+dfsg-1                   amd64        Scalable Video Technology for AV1 (libsvtav1enc shared library)
ii  libswresample4:amd64               7:5.1.5-0+deb12u1              amd64        FFmpeg library for audio resampling, rematrixing etc. - runtime files
ii  libswscale6:amd64                  7:5.1.5-0+deb12u1              amd64        FFmpeg library for image scaling and various conversions - runtime files
ii  libsystemd-shared:amd64            252.26-1~deb12u2               amd64        systemd shared private library
ii  libsystemd0:amd64                  252.26-1~deb12u2               amd64        systemd utility library
ii  libsz2:amd64                       1.0.6-1+b1                     amd64        Adaptive Entropy Coding library - SZIP
ii  libtasn1-6:amd64                   4.19.0-2                       amd64        Manage ASN.1 structures (runtime)
ii  libtcl8.6:amd64                    8.6.13+dfsg-2                  amd64        Tcl (the Tool Command Language) v8.6 - run-time library files
ii  libtesseract-dev:amd64             5.3.0-2                        amd64        Development files for the tesseract command line OCR tool
ii  libtesseract5:amd64                5.3.0-2                        amd64        Tesseract OCR library
ii  libtext-iconv-perl:amd64           1.7-8                          amd64        module to convert between character sets in Perl
ii  libthai-data                       0.1.29-1                       all          Data files for Thai language support library
ii  libthai0:amd64                     0.1.29-1                       amd64        Thai language support library
ii  libtheora0:amd64                   1.1.1+dfsg.1-16.1+b1           amd64        Theora Video Compression Codec
ii  libtie-ixhash-perl                 1.23-4                         all          Perl module to order associative arrays
ii  libtiff-dev:amd64                  4.5.0-6+deb12u1                amd64        Tag Image File Format library (TIFF), development files
ii  libtiff6:amd64                     4.5.0-6+deb12u1                amd64        Tag Image File Format (TIFF) library
ii  libtiffxx6:amd64                   4.5.0-6+deb12u1                amd64        Tag Image File Format (TIFF) library -- C++ interface
ii  libtimedate-perl                   2.3300-2                       all          collection of modules to manipulate date/time information
ii  libtinfo6:amd64                    6.4-4                          amd64        shared low-level terminfo library for terminal handling
ii  libtirpc-common                    1.3.3+ds-1                     all          transport-independent RPC library - common files
ii  libtirpc-dev:amd64                 1.3.3+ds-1                     amd64        transport-independent RPC library - development files
ii  libtirpc3:amd64                    1.3.3+ds-1                     amd64        transport-independent RPC library
ii  libtk8.6:amd64                     8.6.13-2                       amd64        Tk toolkit for Tcl and X11 v8.6 - run-time files
ii  libtool                            2.4.7-5                        all          Generic library support script
ii  libtry-tiny-perl                   0.31-2                         all          module providing minimalistic try/catch
ii  libtsan2:amd64                     12.2.0-14                      amd64        ThreadSanitizer -- a Valgrind-based detector of data races (runtime)
ii  libtwolame0:amd64                  0.4.0-2                        amd64        MPEG Audio Layer 2 encoding library
ii  libubsan1:amd64                    12.2.0-14                      amd64        UBSan -- undefined behaviour sanitizer (runtime)
ii  libudev1:amd64                     252.26-1~deb12u2               amd64        libudev shared library
ii  libudfread0:amd64                  1.1.2-1                        amd64        UDF reader library
ii  libunistring2:amd64                1.0-2                          amd64        Unicode string library for C
ii  libunwind8:amd64                   1.6.2-3                        amd64        library to determine the call-chain of a program - runtime
ii  liburi-perl                        5.17-1                         all          module to manipulate and access URI strings
ii  liburiparser-dev                   0.9.7+dfsg-2                   amd64        development files for uriparser
ii  liburiparser1:amd64                0.9.7+dfsg-2                   amd64        URI parsing library compliant with RFC 3986
ii  libusb-1.0-0:amd64                 2:1.0.26-1                     amd64        userspace USB programming library
ii  libutf8proc2:amd64                 2.8.0-1                        amd64        C library for processing UTF-8 Unicode data (shared library)
ii  libuuid1:amd64                     2.38.1-5+deb12u1               amd64        Universally Unique ID library
ii  libuv1:amd64                       1.44.2-1+deb12u1               amd64        asynchronous event notification library - runtime library
ii  libva-drm2:amd64                   2.17.0-1                       amd64        Video Acceleration (VA) API for Linux -- DRM runtime
ii  libva-x11-2:amd64                  2.17.0-1                       amd64        Video Acceleration (VA) API for Linux -- X11 runtime
ii  libva2:amd64                       2.17.0-1                       amd64        Video Acceleration (VA) API for Linux -- runtime
ii  libvdpau-va-gl1:amd64              0.4.2-1+b1                     amd64        VDPAU driver with OpenGL/VAAPI backend
ii  libvdpau1:amd64                    1.5-2                          amd64        Video Decode and Presentation API for Unix (libraries)
ii  libvidstab1.1:amd64                1.1.0-2+b1                     amd64        video stabilization library (shared library)
ii  libvorbis0a:amd64                  1.3.7-1                        amd64        decoder library for Vorbis General Audio Compression Codec
ii  libvorbisenc2:amd64                1.3.7-1                        amd64        encoder library for Vorbis General Audio Compression Codec
ii  libvorbisfile3:amd64               1.3.7-1                        amd64        high-level API for Vorbis General Audio Compression Codec
ii  libvpx7:amd64                      1.12.0-1+deb12u3               amd64        VP8 and VP9 video codec (shared library)
ii  libvulkan1:amd64                   1.3.239.0-1                    amd64        Vulkan loader library
ii  libwavpack1:amd64                  5.6.0-1                        amd64        audio codec (lossy and lossless) - library
ii  libwayland-client0:amd64           1.21.0-1                       amd64        wayland compositor infrastructure - client library
ii  libwayland-cursor0:amd64           1.21.0-1                       amd64        wayland compositor infrastructure - cursor library
ii  libwayland-egl1:amd64              1.21.0-1                       amd64        wayland compositor infrastructure - EGL library
ii  libwayland-server0:amd64           1.21.0-1                       amd64        wayland compositor infrastructure - server library
ii  libwebp-dev:amd64                  1.2.4-0.2+deb12u1              amd64        Lossy compression of digital photographic images
ii  libwebp7:amd64                     1.2.4-0.2+deb12u1              amd64        Lossy compression of digital photographic images
ii  libwebpdemux2:amd64                1.2.4-0.2+deb12u1              amd64        Lossy compression of digital photographic images.
ii  libwebpmux3:amd64                  1.2.4-0.2+deb12u1              amd64        Lossy compression of digital photographic images
ii  libwmf-0.2-7:amd64                 0.2.12-5.1                     amd64        Windows metafile conversion library
ii  libwmf-dev                         0.2.12-5.1                     amd64        Windows metafile conversion development
ii  libwmflite-0.2-7:amd64             0.2.12-5.1                     amd64        Windows metafile conversion lite library
ii  libwww-perl                        6.68-1                         all          simple and consistent interface to the world-wide web
ii  libwww-robotrules-perl             6.02-1                         all          database of robots.txt-derived permissions
ii  libx11-6:amd64                     2:1.8.4-2+deb12u2              amd64        X11 client-side library
ii  libx11-data                        2:1.8.4-2+deb12u2              all          X11 client-side library
ii  libx11-dev:amd64                   2:1.8.4-2+deb12u2              amd64        X11 client-side library (development headers)
ii  libx11-protocol-perl               0.56-9                         all          Perl module for the X Window System Protocol, version 11
ii  libx11-xcb1:amd64                  2:1.8.4-2+deb12u2              amd64        Xlib/XCB interface library
ii  libx264-164:amd64                  2:0.164.3095+gitbaee400-3      amd64        x264 video coding library
ii  libx265-199:amd64                  3.5-2+b1                       amd64        H.265/HEVC video stream encoder (shared library)
ii  libx265-dev:amd64                  3.5-2+b1                       amd64        H.265/HEVC video stream encoder (development files)
ii  libxau-dev:amd64                   1:1.0.9-1                      amd64        X11 authorisation library (development headers)
ii  libxau6:amd64                      1:1.0.9-1                      amd64        X11 authorisation library
ii  libxaw7:amd64                      2:1.0.14-1                     amd64        X11 Athena Widget library
ii  libxcb-dri2-0:amd64                1.15-1                         amd64        X C Binding, dri2 extension
ii  libxcb-dri3-0:amd64                1.15-1                         amd64        X C Binding, dri3 extension
ii  libxcb-glx0:amd64                  1.15-1                         amd64        X C Binding, glx extension
ii  libxcb-present0:amd64              1.15-1                         amd64        X C Binding, present extension
ii  libxcb-randr0:amd64                1.15-1                         amd64        X C Binding, randr extension
ii  libxcb-render0:amd64               1.15-1                         amd64        X C Binding, render extension
ii  libxcb-render0-dev:amd64           1.15-1                         amd64        X C Binding, render extension, development files
ii  libxcb-shape0:amd64                1.15-1                         amd64        X C Binding, shape extension
ii  libxcb-shm0:amd64                  1.15-1                         amd64        X C Binding, shm extension
ii  libxcb-shm0-dev:amd64              1.15-1                         amd64        X C Binding, shm extension, development files
ii  libxcb-sync1:amd64                 1.15-1                         amd64        X C Binding, sync extension
ii  libxcb-xfixes0:amd64               1.15-1                         amd64        X C Binding, xfixes extension
ii  libxcb1:amd64                      1.15-1                         amd64        X C Binding
ii  libxcb1-dev:amd64                  1.15-1                         amd64        X C Binding, development files
ii  libxcomposite1:amd64               1:0.4.5-1                      amd64        X11 Composite extension library
ii  libxcursor1:amd64                  1:1.2.1-1                      amd64        X cursor management library
ii  libxdamage1:amd64                  1:1.1.6-1                      amd64        X11 damaged region extension library
ii  libxdmcp-dev:amd64                 1:1.1.2-3                      amd64        X11 authorisation library (development headers)
ii  libxdmcp6:amd64                    1:1.1.2-3                      amd64        X11 Display Manager Control Protocol library
ii  libxdot4:amd64                     2.42.2-7+b3                    amd64        rich set of graph drawing tools - xdot library
ii  libxerces-c-dev:amd64              3.2.4+debian-1                 amd64        validating XML parser library for C++ (development files)
ii  libxerces-c3.2:amd64               3.2.4+debian-1                 amd64        validating XML parser library for C++
ii  libxext-dev:amd64                  2:1.3.4-1+b1                   amd64        X11 miscellaneous extensions library (development headers)
ii  libxext6:amd64                     2:1.3.4-1+b1                   amd64        X11 miscellaneous extension library
ii  libxfixes3:amd64                   1:6.0.0-2                      amd64        X11 miscellaneous 'fixes' extension library
ii  libxft-dev:amd64                   2.3.6-1                        amd64        FreeType-based font drawing library for X (development files)
ii  libxft2:amd64                      2.3.6-1                        amd64        FreeType-based font drawing library for X
ii  libxi6:amd64                       2:1.8-1+b1                     amd64        X11 Input extension library
ii  libxinerama1:amd64                 2:1.1.4-3                      amd64        X11 Xinerama extension library
ii  libxkbcommon0:amd64                1.5.0-1                        amd64        library interface to the XKB compiler - shared library
ii  libxkbfile1:amd64                  1:1.1.0-1                      amd64        X11 keyboard file manipulation library
ii  libxml-parser-perl                 2.46-4                         amd64        Perl module for parsing XML files
ii  libxml-twig-perl                   1:3.52-2                       all          Perl module for processing huge XML documents in tree mode
ii  libxml-xpathengine-perl            0.14-2                         all          re-usable XPath engine for DOM-like trees
ii  libxml2:amd64                      2.9.14+dfsg-1.3~deb12u1        amd64        GNOME XML library
ii  libxml2-dev:amd64                  2.9.14+dfsg-1.3~deb12u1        amd64        GNOME XML library - development files
ii  libxmlb2:amd64                     0.3.10-2                       amd64        Binary XML library
ii  libxmu6:amd64                      2:1.1.3-3                      amd64        X11 miscellaneous utility library
ii  libxmuu1:amd64                     2:1.1.3-3                      amd64        X11 miscellaneous micro-utility library
ii  libxpm4:amd64                      1:3.5.12-1.1+deb12u1           amd64        X11 pixmap library
ii  libxrandr2:amd64                   2:1.5.2-2+b1                   amd64        X11 RandR extension library
ii  libxrender-dev:amd64               1:0.9.10-1.1                   amd64        X Rendering Extension client library (development files)
ii  libxrender1:amd64                  1:0.9.10-1.1                   amd64        X Rendering Extension client library
ii  libxshmfence1:amd64                1.3-1                          amd64        X shared memory fences - shared library
ii  libxslt1-dev:amd64                 1.1.35-1                       amd64        XSLT 1.0 processing library - development kit
ii  libxslt1.1:amd64                   1.1.35-1                       amd64        XSLT 1.0 processing library - runtime library
ii  libxss-dev:amd64                   1:1.2.3-1                      amd64        X11 Screen Saver extension library (development headers)
ii  libxss1:amd64                      1:1.2.3-1                      amd64        X11 Screen Saver extension library
ii  libxt-dev:amd64                    1:1.2.1-1.1                    amd64        X11 toolkit intrinsics library (development headers)
ii  libxt6:amd64                       1:1.2.1-1.1                    amd64        X11 toolkit intrinsics library
ii  libxtst6:amd64                     2:1.2.3-1.1                    amd64        X11 Testing -- Record extension library
ii  libxv1:amd64                       2:1.0.11-1.1                   amd64        X11 Video extension library
ii  libxvidcore4:amd64                 2:1.3.7-1                      amd64        Open source MPEG-4 video codec (library)
ii  libxxf86dga1:amd64                 2:1.1.5-1                      amd64        X11 Direct Graphics Access extension library
ii  libxxf86vm1:amd64                  1:1.1.4-1+b2                   amd64        X11 XFree86 video mode extension library
ii  libxxhash0:amd64                   0.8.1-1                        amd64        shared library for xxhash
ii  libyaml-0-2:amd64                  0.2.5-1                        amd64        Fast YAML 1.1 parser and emitter library
ii  libyaml-dev:amd64                  0.2.5-1                        amd64        Fast YAML 1.1 parser and emitter library (development)
ii  libyuv0:amd64                      0.0~git20230123.b2528b0-1      amd64        Library for YUV scaling (shared library)
ii  libz3-4:amd64                      4.8.12-3.1                     amd64        theorem prover from Microsoft Research - runtime libraries
ii  libzimg2:amd64                     3.0.4+ds1-1                    amd64        scaling, colorspace, depth conversion library (shared library)
ii  libzmq5:amd64                      4.3.4-6                        amd64        lightweight messaging kernel (shared library)
ii  libzstd-dev:amd64                  1.5.4+dfsg2-5                  amd64        fast lossless compression algorithm -- development files
ii  libzstd1:amd64                     1.5.4+dfsg2-5                  amd64        fast lossless compression algorithm
ii  libzvbi-common                     0.2.41-1                       all          Vertical Blanking Interval decoder (VBI) - common files
ii  libzvbi0:amd64                     0.2.41-1                       amd64        Vertical Blanking Interval decoder (VBI) - runtime files
ii  linux-compiler-gcc-12-x86          6.1.99-1                       amd64        Compiler for Linux on x86 (meta-package)
ii  linux-headers-6.1.0-23-amd64       6.1.99-1                       amd64        Header files for Linux 6.1.0-23-amd64
ii  linux-headers-6.1.0-23-common      6.1.99-1                       all          Common header files for Linux 6.1.0-23
ii  linux-headers-amd64                6.1.99-1                       amd64        Header files for Linux amd64 configuration (meta-package)
ii  linux-kbuild-6.1                   6.1.99-1                       amd64        Kbuild infrastructure for Linux 6.1
ii  linux-libc-dev:amd64               6.1.99-1                       amd64        Linux support headers for userspace development
ii  login                              1:4.13+dfsg1-1+b1              amd64        system login tools
ii  logsave                            1.47.0-2                       amd64        save the output of a command in a log file
ii  lsb-release                        12.0-1                         all          Linux Standard Base version reporting utility (minimal implementation)
ii  m4                                 1.4.19-3                       amd64        macro processing language
ii  make                               4.3-4.1                        amd64        utility for directing compilation
ii  mariadb-common                     1:10.11.6-0+deb12u1            all          MariaDB common configuration files
ii  mawk                               1.3.4.20200120-3.1             amd64        Pattern scanning and text processing language
ii  media-types                        10.0.0                         all          List of standard media types and their usual file extension
ii  mercurial                          6.3.2-1                        amd64        easy-to-use, scalable distributed version control system
ii  mercurial-common                   6.3.2-1                        all          easy-to-use, scalable distributed version control system (common files)
ii  mesa-va-drivers:amd64              22.3.6-1+deb12u1               amd64        Mesa VA-API video acceleration drivers
ii  mesa-vdpau-drivers:amd64           22.3.6-1+deb12u1               amd64        Mesa VDPAU video acceleration drivers
ii  mesa-vulkan-drivers:amd64          22.3.6-1+deb12u1               amd64        Mesa Vulkan graphics drivers
ii  mount                              2.38.1-5+deb12u1               amd64        tools for mounting and manipulating filesystems
ii  mysql-common                       5.8+1.1.0                      all          MySQL database common files, e.g. /etc/mysql/my.cnf
ii  ncurses-base                       6.4-4                          all          basic terminal type definitions
ii  ncurses-bin                        6.4-4                          amd64        terminal-related programs and man pages
ii  netbase                            6.4                            all          Basic TCP/IP networking system
ii  ninja-build                        1.11.1-1                       amd64        small build system closest in spirit to Make
ii  ocl-icd-libopencl1:amd64           2.3.1-1                        amd64        Generic OpenCL ICD Loader
ii  openssh-client                     1:9.2p1-2+deb12u2              amd64        secure shell (SSH) client, for secure access to remote machines
ii  openssl                            3.0.13-1~deb12u1               amd64        Secure Sockets Layer toolkit - cryptographic utility
ii  packagekit                         1.2.6-5                        amd64        Provides a package management service
ii  packagekit-tools                   1.2.6-5                        amd64        Provides PackageKit command-line tools
ii  passwd                             1:4.13+dfsg1-1+b1              amd64        change and administer password and group data
ii  patch                              2.7.6-7                        amd64        Apply a diff file to an original
ii  perl                               5.36.0-7+deb12u1               amd64        Larry Wall's Practical Extraction and Report Language
ii  perl-base                          5.36.0-7+deb12u1               amd64        minimal Perl system
ii  perl-modules-5.36                  5.36.0-7+deb12u1               all          Core Perl modules
ii  perl-openssl-defaults:amd64        7+b1                           amd64        version compatibility baseline for Perl OpenSSL packages
ii  pinentry-curses                    1.2.1-1                        amd64        curses-based PIN or pass-phrase entry dialog for GnuPG
ii  pkg-config:amd64                   1.8.1-1                        amd64        manage compile and link flags for libraries (transitional package)
ii  pkgconf:amd64                      1.8.1-1                        amd64        manage compile and link flags for libraries
ii  pkgconf-bin                        1.8.1-1                        amd64        manage compile and link flags for libraries (binaries)
ii  pocketsphinx-en-us                 0.8+5prealpha+1-15             all          Speech recognition tool - US English language model
ii  polkitd                            122-3                          amd64        framework for managing administrative policies and privileges
ii  poppler-data                       0.4.12-1                       all          encoding data for the poppler PDF rendering library
ii  poppler-utils                      22.12.0-2+b1                   amd64        PDF utilities (based on Poppler)
ii  procps                             2:4.0.2-3                      amd64        /proc file system utilities
ii  proj-bin                           9.1.1-1+b1                     amd64        Cartographic projection library (tools)
ii  proj-data                          9.1.1-1                        all          Cartographic projection filter and library (datum package)
ii  python-apt-common                  2.6.0                          all          Python interface to libapt-pkg (locales)
ii  python-is-python3                  3.11.2-1+deb12u1               all          symlinks /usr/bin/python to python3
ii  python3                            3.11.2-1+b1                    amd64        interactive high-level object-oriented language (default python3 version)
ii  python3-apt                        2.6.0                          amd64        Python 3 interface to libapt-pkg
ii  python3-blinker                    1.5-1                          all          Fast, simple object-to-object and broadcast signaling (Python3)
ii  python3-cffi-backend:amd64         1.15.1-5+b1                    amd64        Foreign Function Interface for Python 3 calling C code - runtime
ii  python3-cryptography               38.0.4-3                       amd64        Python library exposing cryptographic recipes and primitives (Python 3)
ii  python3-dbus                       1.3.2-4+b1                     amd64        simple interprocess messaging system (Python 3 interface)
ii  python3-distro                     1.8.0-1                        all          Linux OS platform information API
ii  python3-distutils                  3.11.2-3                       all          distutils package for Python 3.x
ii  python3-gi                         3.42.2-3+b1                    amd64        Python 3 bindings for gobject-introspection libraries
ii  python3-httplib2                   0.20.4-3                       all          comprehensive HTTP client library written for Python3
ii  python3-jwt                        2.6.0-1                        all          Python 3 implementation of JSON Web Token
ii  python3-lazr.restfulclient         0.14.5-1                       all          client for lazr.restful-based web services (Python 3)
ii  python3-lazr.uri                   1.0.6-3                        all          library for parsing, manipulating, and generating URIs
ii  python3-lib2to3                    3.11.2-3                       all          Interactive high-level object-oriented language (lib2to3)
ii  python3-minimal                    3.11.2-1+b1                    amd64        minimal subset of the Python language (default python3 version)
ii  python3-oauthlib                   3.2.2-1                        all          generic, spec-compliant implementation of OAuth for Python3
ii  python3-pkg-resources              66.1.1-1                       all          Package Discovery and Resource Access using pkg_resources
ii  python3-pyaudio                    0.2.13-1+b1                    amd64        Python3 bindings for PortAudio v19
ii  python3-pyparsing                  3.0.9-1                        all          alternative to creating and executing simple grammars - Python 3.x
ii  python3-six                        1.16.0-4                       all          Python 2 and 3 compatibility library
ii  python3-software-properties        0.99.30-4.1~deb12u1            all          manage the repositories that you install software from
ii  python3-wadllib                    1.3.6-4                        all          Python 3 library for navigating WADL files
ii  python3.11                         3.11.2-6                       amd64        Interactive high-level object-oriented language (version 3.11)
ii  python3.11-minimal                 3.11.2-6                       amd64        Minimal subset of the Python language (version 3.11)
ii  readline-common                    8.2-1.3                        all          GNU readline and history libraries, common files
ii  rpcsvc-proto                       1.4.3-1                        amd64        RPC protocol compiler and definitions
ii  sed                                4.9-1                          amd64        GNU stream editor for filtering/transforming text
ii  sensible-utils                     0.0.17+nmu1                    all          Utilities for sensible alternative selection
ii  sgml-base                          1.31                           all          SGML infrastructure and SGML catalog file support
ii  shared-mime-info                   2.2-1                          amd64        FreeDesktop.org shared MIME database and spec
ii  software-properties-common         0.99.30-4.1~deb12u1            all          manage the repositories that you install software from (common)
ii  sox                                14.4.2+git20190427-3.5         amd64        Swiss army knife of sound processing
ii  sq                                 0.27.0-2+b1                    amd64        OpenPGP command-line tool from Sequoia
ii  subversion                         1.14.2-4+b2                    amd64        Advanced version control system
ii  sudo                               1.9.13p3-1+deb12u1             amd64        Provide limited super user privileges to specific users
ii  swig                               4.1.0-0.2                      all          Generate scripting interfaces to C/C++ code
ii  swig4.0                            4.1.0-0.2                      amd64        Generate scripting interfaces to C/C++ code
ii  systemd                            252.26-1~deb12u2               amd64        system and service manager
ii  systemd-sysv                       252.26-1~deb12u2               amd64        system and service manager - SysV compatibility symlinks
ii  systemd-timesyncd                  252.26-1~deb12u2               amd64        minimalistic service to synchronize local time with NTP servers
ii  sysvinit-utils                     3.06-4                         amd64        System-V-like utilities
ii  tar                                1.34+dfsg-1.2+deb12u1          amd64        GNU version of the tar archiving utility
ii  tcl                                8.6.13                         amd64        Tool Command Language (default version) - shell
ii  tcl-dev:amd64                      8.6.13                         amd64        Tool Command Language (default version) - development files
ii  tcl8.6                             8.6.13+dfsg-2                  amd64        Tcl (the Tool Command Language) v8.6 - shell
ii  tcl8.6-dev:amd64                   8.6.13+dfsg-2                  amd64        Tcl (the Tool Command Language) v8.6 - development files
ii  tesseract-ocr                      5.3.0-2                        amd64        Tesseract command line OCR tool
ii  tesseract-ocr-eng                  1:4.1.0-2                      all          tesseract-ocr language files for English
ii  tesseract-ocr-osd                  1:4.1.0-2                      all          tesseract-ocr language files for script and orientation
ii  tini                               0.19.0-1                       amd64        tiny but valid init for containers
ii  tk                                 8.6.13                         amd64        Toolkit for Tcl and X11 (default version) - windowing shell
ii  tk-dev:amd64                       8.6.13                         amd64        Toolkit for Tcl and X11 (default version) - development files
ii  tk8.6                              8.6.13-2                       amd64        Tk toolkit for Tcl and X11 v8.6 - windowing shell
ii  tk8.6-dev:amd64                    8.6.13-2                       amd64        Tk toolkit for Tcl and X11 v8.6 - development files
ii  tzdata                             2024a-0+deb12u1                all          time zone and daylight-saving time data
ii  ucf                                3.0043+nmu1                    all          Update Configuration File(s): preserve user changes to config files
ii  unixodbc-common                    2.3.11-2+deb12u1               all          Common ODBC configuration files
ii  unixodbc-dev:amd64                 2.3.11-2+deb12u1               amd64        ODBC libraries for Unix (development files)
ii  unrtf                              0.21.10-clean-1                amd64        RTF to other formats converter
ii  unzip                              6.0-28                         amd64        De-archiver for .zip files
ii  usr-is-merged                      37~deb12u1                     all          Transitional package to assert a merged-/usr system
ii  util-linux                         2.38.1-5+deb12u1               amd64        miscellaneous system utilities
ii  util-linux-extra                   2.38.1-5+deb12u1               amd64        interactive login tools
ii  uuid-dev:amd64                     2.38.1-5+deb12u1               amd64        Universally Unique ID library - headers and static libraries
ii  va-driver-all:amd64                2.17.0-1                       amd64        Video Acceleration (VA) API -- driver metapackage
ii  vdpau-driver-all:amd64             1.5-2                          amd64        Video Decode and Presentation API for Unix (driver metapackage)
ii  vim                                2:9.0.1378-2                   amd64        Vi IMproved - enhanced vi editor
ii  vim-common                         2:9.0.1378-2                   all          Vi IMproved - Common files
ii  vim-runtime                        2:9.0.1378-2                   all          Vi IMproved - Runtime files
ii  wget                               1.21.3-1+b2                    amd64        retrieves files from the web
ii  x11-common                         1:7.7+23                       all          X Window System (X.Org) infrastructure
ii  x11-utils                          7.7+5                          amd64        X11 utilities
ii  x11-xserver-utils                  7.7+9+b1                       amd64        X server utilities
ii  x11proto-core-dev                  2022.1-1                       all          transitional dummy package
ii  x11proto-dev                       2022.1-1                       all          X11 extension protocols and auxiliary headers
ii  xdg-utils                          1.1.3-4.1                      all          desktop integration utilities from freedesktop.org
ii  xkb-data                           2.35.1-1                       all          X Keyboard Extension (XKB) configuration data
ii  xml-core                           0.18+nmu1                      all          XML infrastructure and XML catalog file support
ii  xorg-sgml-doctools                 1:1.11-1.1                     all          Common tools for building X.Org SGML documentation
ii  xtrans-dev                         1.4.0-1                        all          X transport library (development files)
ii  xxd                                2:9.0.1378-2                   amd64        tool to make (or reverse) a hex dump
ii  xz-utils                           5.4.1-0.2                      amd64        XZ-format compression utilities
ii  zlib1g:amd64                       1:1.2.13.dfsg-1                amd64        compression library - runtime
ii  zlib1g-dev:amd64                   1:1.2.13.dfsg-1                amd64        compression library - development
ii  zutty                              0.14.0.20230218+dfsg1-1        amd64        Efficient full-featured X11 terminal emulator
```
