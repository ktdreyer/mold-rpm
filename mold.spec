%global forgeurl https://github.com/rui314/mold
Version:        1.0.1
%forgemeta

Name:           mold
Release:        1%{dist}
Summary:        mold: A Modern Linker
License:        AGPLv3
URL:            %{forgeurl}
Source:         %{forgesource}

%global toolchain clang
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(zlib)

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
  STRIP=/usr/bin/echo \
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir}

%install
make install %{?_smp_mflags} \
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
