#!/bin/bash

set -e

TOPDIR=$(rpm --eval '%{_topdir}')
SPEC=python-sfmanager.spec

which rpmdev-setuptree &> /dev/null || sudo yum install -y rpmdevtools
[ -d "${TOPDIR}"/SOURCES ] || rpmdev-setuptree

echo "[+] Fetch sources..."
spectool -g ${SPEC} -C ${TOPDIR}/SOURCES/

echo "[+] Building package..."
exec rpmbuild -v -ba ${SPEC}
