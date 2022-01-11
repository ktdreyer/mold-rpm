%bcond_with system_libs

%global forgeurl https://github.com/rui314/mold
%global commit b6316ef085b3416d9e5af273c2e1abf724c9561c
Version:        1.0.1
%forgemeta

Name:           mold
Release:        1%{dist}
Summary:        mold: A Modern Linker
License:        AGPLv3
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
%if 0%{with system_libs}
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(tbb)
%endif

%description
mold is a faster drop-in replacement for existing Unix linkers. It is several
times faster than LLVM lld linker. mold is created for increasing developer
productivity by reducing build time, especially in rapid debug-edit-rebuild
cycles.

%prep
%forgesetup

%build
%{set_build_flags}
make %{?_smp_mflags} \
%if 0%{with system_libs}
  SYSTEM_TBB=1 SYSTEM_XXHASH=1 \
%endif
  STRIP=/usr/bin/echo \
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir}

%install
make install %{?_smp_mflags} \
%if 0%{with system_libs}
  SYSTEM_TBB=1 SYSTEM_XXHASH=1 \
%endif
  STRIP=/usr/bin/echo \
  DESTDIR=%{buildroot} \
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir}

%files
%license LICENSE
%{_bindir}/mold
%{_bindir}/ld.mold
%{_bindir}/ld64.mold
%{_libdir}/mold/mold-wrapper.so
%{_libexecdir}/mold
%{_mandir}/man1/mold.1*

%changelog
* Thu Jan 06 2022 Ken Dreyer <kdreyer@redhat.com> - 1.0.1-1
- initial package
