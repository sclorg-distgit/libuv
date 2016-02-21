%{?scl:%scl_package libuv}
%{!?scl:%global pkg_name %{name}}

Name: %{?scl_prefix}libuv
Epoch:   1
Version: 1.7.5
Release: 3%{?dist}
Summary: Platform layer for node.js

Group: System Environment/Libraries
# the licensing breakdown is described in detail in the LICENSE file
License: MIT and BSD and ISC

%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}

URL: http://libuv.org/
Source0: http://libuv.org/dist/v%{version}/%{pkg_name}-v%{version}.tar.gz
Source2: libuv.pc.in

BuildRequires: autoconf automake libtool

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

# Bundling exception request:
# https://fedorahosted.org/fpc/ticket/231
Provides: %{?scl_prefix}bundled(libev) = 4.04

%description
libuv is a new platform layer for Node. Its purpose is to abstract IOCP on
Windows and libev on Unix systems. We intend to eventually contain all platform
differences in this library.

%package devel
Summary: Development libraries for libuv
Group: Development/Libraries
Requires: %{?scl_prefix}%{pkg_name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: pkgconfig
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description devel
Development libraries for libuv

%package static
Summary: Platform layer for node.js - static library
Group:   Development/Libraries
Requires:   %{?scl_prefix}%{pkg_name}-devel = %{epoch}:%{version}-%{release}

%description static
Static library (.a) version of libuv.

%prep
%setup -q -n %{pkg_name}-v%{version}

%build
./autogen.sh
%{?scl:scl enable %{scl} - << \EOF}
%configure
%{?scl:EOF}
%{?scl:scl enable %{scl} - << \EOF}
make %{?_smp_mflags}
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << \EOF}
make DESTDIR=%{buildroot} install
%{?scl:EOF}
rm -f %{buildroot}%{_libdir}/libuv.la

%check
# Tests are currently disabled because some require network access
# Working with upstream to split these out
#./run-tests
#./run-benchmarks

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md AUTHORS LICENSE
%{_libdir}/libuv.so.*

%files devel
%doc README.md AUTHORS LICENSE
%{_libdir}/libuv.so
%{_libdir}/pkgconfig/libuv.pc
%{_includedir}/uv*.h

%files static
%{_libdir}/libuv.a

%changelog
* Wed Feb 10 2016 Tomas Hrcka <thrcka@redhat.com> - 1:1.7.5-4
- New upstream release 

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 01 2015 Stephen Gallagher <sgallagh@redhat.com> 1.7.5-1
- Rebase to 1.7.5 to support Node.js 4.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 19 2015 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:1.4.0-1
- rebase to 1.4.0

* Thu Feb 19 2015 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.33-2
- add missing %%{_?isa} to devel requires of main package
- fix some issues with the pkgconfig file and Group reported by Michael Schwendt

* Thu Feb 19 2015 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.33-1
- new upstream release 0.10.33
  https://github.com/joyent/libuv/blob/v0.10.33/ChangeLog
- update URL to point to the new libuv.org

* Wed Jan 07 2015 Tomas Hrcka <thrcka@redhat.com> - 1:0.10.30-1
- new upstream release 0.10.30

* Wed Nov 19 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.29-1
- new upstream release 0.10.29
  https://github.com/joyent/libuv/blob/v0.10.29/ChangeLog

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.10.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.28-1
- new upstream release 0.10.28
  https://github.com/joyent/libuv/blob/v0.10.28/ChangeLog

* Thu Jul 03 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.27-3
- build static library for rust (RHBZ#1115975)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.10.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 02 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.27-1
- new upstream release 0.10.27
  https://github.com/joyent/libuv/blob/v0.10.27/ChangeLog

* Thu Feb 20 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.25-1
- new upstream release 0.10.25
  https://github.com/joyent/libuv/blob/v0.10.25/ChangeLog

* Fri Jan 31 2014 Tomas Hrcka <thrcka@redhat.com> - 1:0.10.23-2
- new upstream release

* Mon Jan 27 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.23-1
- new upstream release 0.10.23
  https://github.com/joyent/libuv/blob/v0.10.23/ChangeLog

* Thu Dec 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.21-1
- new upstream release 0.10.21
  https://github.com/joyent/libuv/blob/v0.10.21/ChangeLog

* Thu Dec 12 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.20-1
- new upstream release 0.10.20
  https://github.com/joyent/libuv/blob/v0.10.20/ChangeLog

* Thu Dec 05 2013 Tomas Hrcka <thrcka@redhat.com> - 1:0.10.19-1.1
- rebuilt with gyp from v8collection
- build requires scl-runtime

* Tue Nov 12 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.19-1
- new upstream release 0.10.19
  https://github.com/joyent/libuv/blob/v0.10.19/ChangeLog

* Fri Oct 18 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.18-1
- new upstream release 0.10.18
  https://github.com/joyent/libuv/blob/v0.10.18/ChangeLog

* Wed Sep 25 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.17-1
- new upstream release 0.10.17
  https://github.com/joyent/libuv/blob/v0.10.17/ChangeLog

* Fri Sep 06 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.15-1
- new upstream release 0.10.15
  https://github.com/joyent/libuv/blob/v0.10.15/ChangeLog

* Tue Aug 27 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.14-1
- new upstream release 0.10.14
  https://github.com/joyent/libuv/blob/v0.10.14/ChangeLog

* Thu Jul 25 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.13-1
- new upstream release 0.10.13
  https://github.com/joyent/libuv/blob/v0.10.13/ChangeLog

* Wed Jul 10 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.12-1
- new upstream release 0.10.12

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.11-1
- new upstream release 0.10.11

* Fri May 31 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.9-1
- new upstream release 0.10.9

* Wed May 29 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.8-2
- fix License tag (RHBZ#968226)

* Wed May 29 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.8-1
- new upstream release 0.10.8

* Wed May 29 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.7-1
- new upstream release 0.10.7
- drop upstreamed patch from 0.10.5-2

* Wed May 15 2013 Tomas Hrcka <thrcka@redhat.com> - 1:0.10.5-1.1
- updated to upstream stable version

* Mon May 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.5-3
- don't sed the soname in the spec anymore; the patch takes care of it now
- drop leftover global define for git revision

* Mon May 13 2013 Stephen Gallagher <sgallagh@redhat.com> - 1:0.10.5-2
- Add patch to properly report soname version information
  This patch will be included upstream in 0.10.6 and can be dropped then.
- Remove Bundles(ev) as this has not been true since 0.9.5

* Wed Apr 24 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.5-1
- new upstream release 0.10.5

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.4-1
- new upstream release 0.10.4
- drop upstreamed patch

* Fri Apr 05 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:0.10.3-3
- Add support for software collections

* Thu Apr 04 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.3-2
- backport patch that fixes FTBFS in nodejs-0.10.3

* Sun Mar 31 2013 tchollingsworth@gmail.com - 1:0.10.3-1
- rebase to 0.10.3
- upstream now does proper releases

* Tue Mar 12 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1:0.10.0-2.git5462dab
- drop the patchlevel from the SONAME since libuv will retain binary
  compatibility for the life of the 0.10.x series

* Mon Mar 11 2013 Stephen Gallagher <sgallagh@redhat.com> - 1:0.10.0-1.git5462dab
- Upgrade to 0.10.0 release to match stable Node.js release

* Thu Feb 28 2013 Stephen Gallagher <sgallagh@redhat.com> - 1:0.9.4-4.gitdc559a5
- Bump epoch for the version downgrade
- The 0.9.7 version hit the Rawhide repo due to the mass rebuild, we need a
  clean upgrade path.

* Thu Feb 21 2013 Stephen Gallagher <sgallagh@redhat.com> - 0.9.4-3.gitdc559a5
- Revert to version 0.9.4 (since 0.9.7 is breaking builds)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-2.git4ba03dd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Stephen Gallagher <sgallagh@redhat.com> - 0.9.7-1.git4ba03dd
- Bump to version included with Node.js 0.9.7

* Wed Dec 26 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.9.4-0.1.gitdc559a5
- bump to version included with node 0.9.4
- drop upstreamed patch
- respect optflags

* Thu Nov 15 2012 Stephen Gallagher <sgallagh@redhat.com> - 0.9.3-0.3.git09b0222
- Add patch to export uv_inet_*

* Wed Nov 14 2012 Stephen Gallagher <sgallagh@redhat.com> - 0.9.3-0.2.git09b0222
- Fixes from package review
- Removed doubly-listed include directory
- Update git tarball to the latest upstream code

* Thu Nov 08 2012 Stephen Gallagher <sgallagh@redhat.com> - 0.9.3-0.1.gitd56434a
- Initial package
