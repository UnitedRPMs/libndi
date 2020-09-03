%global commit0 c14b40caafb26a02249f062e7f907ceaa53c1b74
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

%define _legacy_common_support 1


Name:           libndi
Version:        0.0.1
Release:        1%{?gver}%{dist}
Summary:        libNDI is a new NDI cross-platform

License:        LGPLv2+
URL:            https://code.videolan.org/jbk/libndi
Source0: 	https://code.videolan.org/jbk/libndi/-/archive/%{commit0}/libndi-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:	ffmpeg-devel
BuildRequires:	pkgconfig(microdns)
BuildRequires:	meson

%description
libNDI is a new NDI cross-platform, open-source library done to interact with NDI streams.


%package devel
Summary:        Libraries/include files for GStreamer streaming media framework
Requires:       %{name} = %{version}-%{release}


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{commit0}  -p1

%build

%meson 

%meson_build 

%install
%meson_install 

%files 
%{_bindir}/ndi
%{_libdir}/libndi.so.*


%files devel
%{_libdir}/libndi.so
%{_includedir}/libndi.h


%changelog

* Tue Sep 01 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.0.1-1.gitc14b40c
- Initial build
