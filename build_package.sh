#!/bin/bash

set -e

TOPDIR=$(rpm --eval '%{_topdir}')
SPEC=python-sfmanager.spec

[ -d "${TOPDIR}"/SOURCES ] || rpmdev-setuptree

echo "[+] Fetch sources..."
spectool -g ${SPEC} -C ${TOPDIR}/SOURCES/

echo "[+] Building package..."
exec rpmbuild -v -ba ${SPEC}
