pkgname = "pkcs11-helper"
pkgver = "1.29.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["openssl-devel"]
pkgdesc = "Helper library for PKCS#11"
maintainer = "Val Packett <val@packett.cool>"
license = "GPL-2.0-or-later OR BSD-3-Clause"
url = "https://github.com/OpenSC/pkcs11-helper"
source = f"https://github.com/OpenSC/{pkgname}/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "996846a3c8395e03d8c0515111dc84d82e6e3648d44ba28cb2dbbbca2d4db7d6"


def post_install(self):
    self.install_license("COPYING")
    self.install_license("COPYING.BSD")
    self.install_license("COPYING.GPL")


@subpackage("pkcs11-helper-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
