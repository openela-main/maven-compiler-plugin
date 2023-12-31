Name:           maven-compiler-plugin
Version:        3.7.0
Release:        2%{?dist}
Summary:        Maven Compiler Plugin
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-compiler-plugin
BuildArch:      noarch

Source0:        http://archive.apache.org/dist/maven/plugins/%{name}-%{version}-source-release.zip

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-incremental)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-javac)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-manager)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-java)


%description
The Compiler Plugin is used to compile the sources of your project.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.7.0-1
- Update to upstream version 3.7.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Michael Simacek <msimacek@redhat.com> - 3.6.1-1
- Update to upstream version 3.6.1

* Tue Nov 08 2016 Michael Simacek <msimacek@redhat.com> - 3.6.0-2
- Add upstream patch for broken test skipping

* Mon Oct 31 2016 Michael Simacek <msimacek@redhat.com> - 3.6.0-1
- Update to upstream version 3.6.0

* Fri Jul 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.5.1-4
- Remove dependency on Maven 2 toolchain

* Fri Jul 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.5.1-3
- Add missing BR on maven-plugin-plugin

* Fri Jul  8 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.5.1-2
- Remove unneeded build-requires

* Tue Feb 16 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.5.1-1
- Update to upstream version 3.5.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.5-1
- Update to upstream version 3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3-1
- Update to upstream version 3.3

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-2
- Remove legacy Obsoletes/Provides for maven2 plugin

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-1
- Update to upstream version 3.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.1-5
- Use Requires: java-headless rebuild (#1067528)

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-4
- Fix unowned directory

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 24 2013 Michal Srb <msrb@redhat.com> - 3.1-2
- Build against proper maven-shared-incremental artifactId

* Wed Apr 24 2013 Michal Srb <msrb@redhat.com> - 3.1-1
- Update to upstream version 3.1

* Tue Mar 05 2013 Michal Srb <msrb@redhat.com> - 3.0-2
- Build against proper plexus-compiler

* Tue Jan 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0-1
- Update to upstream version 3.0
- Build with xmvn
- Install license files, resolves: rhbz#895544

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.5.1-1
- Updated to latest upstream version (2.5.1)

* Wed May 23 2012 Tomas Radej <tradej@redhat.com> - 2.4-1
- Updated to latest upstream version
- Guidelines fixes + Removed RPM workaround

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 27 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.3.2-4
- Add few missing (Build)requires
- Remove post(un) scriptlets with update_maven_depmap
- Use new add_maven_depmap macro

* Fri Jun 3 2011 Alexander Kurtakov <akurtako@redhat.com> 2.3.2-3
- Do not require maven2.
- Guidelines fixes.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 19 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.3.2-1
- Update to latest version (2.3.2)
- Modifications according to new guidelines
- Build with maven 3

* Wed May 12 2010 Alexander Kurtakov <akurtako@redhat.com> 2.0.2-2
- Add missing requires.

* Tue May 11 2010 Alexander Kurtakov <akurtako@redhat.com> 2.0.2-1
- Initial package.
