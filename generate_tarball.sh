#!/bin/bash

aid="javax.el-api"
version=`grep Version: *spec | sed -e 's/Version:\s*\(.*\)/\1/'`
filename="${aid}-${version}-sources.jar"
tempdir="glassfish-el-api-${version}"
url="http://central.maven.org/maven2/javax/el/${aid}/${version}/${aid}-${version}-sources.jar"

echo $version

rm -Rf ${tempdir}
mkdir ${tempdir}

pushd ${tempdir}
  wget ${url}
  unzip ${filename}
  mv META-INF/LICENSE.txt .
  rm -Rf ${filename} META-INF/
  mkdir -p src/main/java
  mv javax/ src/main/java
popd

tar czvf glassfish-el-api-${version}.tar.gz ${tempdir}

rm -Rf ${tempdir}

