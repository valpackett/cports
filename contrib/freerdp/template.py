pkgname = "freerdp"
pkgver = "3.0.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DWITH_JPEG=ON",
    "-DWITH_SOXR=ON",
    "-DWITH_FFMPEG=ON",
    "-DWITH_SWSCALE=ON",
    "-DWITH_DSP_FFMPEG=ON",
    "-DWITH_SERVER=ON",
    "-DWITH_SAMPLE=OFF",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "xsltproc", "docbook-xsl"]
makedepends = [
    "zlib-devel",
    "openssl-devel",
    "wayland-devel",
    "libxkbcommon-devel",
    "ffmpeg-devel",
    "libjpeg-turbo-devel",
    "cjson-devel-static",
    "pkcs11-helper-devel",
    "heimdal-devel",
    "soxr-devel",
    "libx11-devel",
    "cups-devel",
    "fuse-devel",
    "sdl-devel",
    "sdl_ttf-devel",
    "webkitgtk-devel",
    "libpulse-devel",
]
pkgdesc = "RDP protocol implementation"
maintainer = "Val Packett <val@packett.cool>"
license = "Apache-2.0"
url = "https://www.freerdp.com"
source = f"https://github.com/FreeRDP/FreeRDP/releases/download/3.0.0-rc0/{pkgname}-3.0.0-rc0.tar.gz"
sha256 = "14a5c77994a1a749542c72ce1fc952682b14a4c81aa6b82c50a43796aa7ce9ac"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libwinpr")
def _libwinpr(self):
    self.pkgdesc = "Windows Portable Runtime library"

    return ["usr/lib/libwinpr*3.so.*"]


@subpackage("libwinpr-devel")
def _libwinpr_devel(self):
    self.pkgdesc = "Windows Portable Runtime library"

    return [
        "usr/lib/cmake/WinPR*3",
        "usr/lib/pkgconfig/winpr*3.pc",
        "usr/include/winpr3",
    ]


@subpackage("libwinpr-progs")
def _libwinpr_progs(self):
    self.pkgdesc = "Windows Portable Runtime library"

    return ["usr/bin/winpr-*"]


@subpackage("freerdp-progs")
def _progs(self):
    return self.default_progs()


@subpackage("freerdp-devel")
def _devel(self):
    return self.default_devel()
