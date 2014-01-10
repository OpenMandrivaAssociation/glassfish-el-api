%{?_javapackages_macros:%_javapackages_macros}

%global artifactId javax.el-api

Name:           glassfish-el-api
Version:        2.2.4
Release:        3.0%{?dist}
Summary:        Expression Language API 2.2.4
# Part of implementation files contain ASL 2.0 copyright
License:        CDDL and ASL 2.0
URL:            http://uel.java.net
# svn export https://svn.java.net/svn/uel~svn/tags/javax.el-api-2.2.4 javax.el-api-2.2.4
# tar cvJf javax.el-api-2.2.4.tar.xz javax.el-api-2.2.4/
Source0:        %{artifactId}-%{version}.tar.xz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  java-devel >= 1:1.6.0

BuildRequires:  jvnet-parent
BuildRequires:  maven-local
BuildRequires:  maven-source-plugin

%description
This project provides an implementation of the Expression Language (EL). 
The main goals are:
 * Improves current implementation: bug fixes and performance improvements
 * Provides API for use by other tools, such as Netbeans

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{artifactId}-%{version}
cp -p %{SOURCE1} .

%build

%mvn_file :%{artifactId} %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Thu Aug 08 2013 gil cattaneo <puntogil@libero.it> 2.2.4-3
- fix rhbz#992386
- switch to XMvn
- minor changes to adapt to current guideline

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jan 31 2013 David Xie <david.scriptfan@gmail.com> - 2.2.4-1
- Initial version of package
