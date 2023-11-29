pkgname = "sdl_ttf"
pkgver = "2.20.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DSDL2TTF_HARFBUZZ=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "harfbuzz-devel",
    "freetype-devel",
    "sdl-devel",
]
pkgdesc = "SDL TrueType font support library"
maintainer = "Val Packett <val@packett.cool>"
license = "Zlib"
url = "https://github.com/libsdl-org/SDL_ttf"
source = f"{url}/releases/download/release-{pkgver}/SDL2_ttf-{pkgver}.tar.gz"
sha256 = "9dc71ed93487521b107a2c4a9ca6bf43fb62f6bddd5c26b055e6b91418a22053"
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("sdl_ttf-devel")
def _devel(self):
    return self.default_devel()
