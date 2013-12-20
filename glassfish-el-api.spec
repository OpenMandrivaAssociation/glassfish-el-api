%_javapackages_macros
%global artifactId javax.el-api

Name:           glassfish-el-api
Version:        3.0.0
Release:        1.0%{?dist}
Summary:        Expression Language API 2.2.4
# Part of implementation files contain ASL 2.0 copyright
License:        (CDDL or GPLv2 with exceptions) and ASL 2.0
URL:            http://uel.java.net
# ./generate_tarball.sh
Source0:        %{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        generate_tarball.sh
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(net.java:jvnet-parent)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)

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
%setup -q
cp -p %{SOURCE1} .

%mvn_file :%{artifactId} %{name}

# missing (unneeded) dep org.glassfish:legal
%pom_remove_plugin :maven-remote-resources-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt LICENSE-2.0.txt
