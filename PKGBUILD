# Maintainer: AcreetionOS Core Team <dev@acreetionos.org>
pkgname=freedomoffice
pkgver=27.2.0
pkgrel=1
pkgdesc="Microsoft Office visual & workflow clone backed by complete LibreOffice engine compatibility, custom dark theme, and 100% local FreedomAI."
arch=('x86_64')
url="https://acreetionos.org"
license=('MPL-2.0' 'LGPL-3.0-or-later')
depends=(
    'cairo'
    'clucene'
    'curl'
    'dbus'
    'fontconfig'
    'freetype2'
    'glib2'
    'gpgme'
    'gtk3'
    'libepoxy'
    'libpng'
    'libx11'
    'libxext'
    'libxinerama'
    'libxml2'
    'libxslt'
    'neon'
    'nss'
    'poppler'
    'python'
    'python-lxml'
    'redland'
    'shared-mime-info'
    'zlib'
)
optdepends=(
    'docker: for built-in SearXNG meta-search and optional Tor search plugins'
    'ollama: for 100% local FreedomAI assistant support'
    'clamav: for email attachment scanning security'
    'rspamd: for anti-phishing in Thunderbird companion'
    'joplin: for digital note taking and local RAG search'
    'thunderbird: for mail, calendar, and task management'
    'element-desktop: for real-time team chat collaboration'
    'nextcloud-client: for local cloud storage synchronization'
)
options=('!emptydirs' '!makeflags')
source=("freedomoffice-${pkgver}.tar.gz::https://github.com/AcreetionOS-Code/freedomoffice/archive/v${pkgver}.tar.gz")
sha256sums=('SKIP')

build() {
    cd "${srcdir}"
    if [ -d "${pkgname}-${pkgver}" ]; then
        cd "${pkgname}-${pkgver}"
    else
        cd "${startdir:-.}"
    fi
    
    ./autogen.sh \
        --prefix=/usr \
        --sysconfdir=/etc \
        --with-vendor="AcreetionOS" \
        --without-java \
        --disable-report-builder \
        --enable-gtk3 \
        --enable-release-build
        
    make
}

package() {
    cd "${srcdir}"
    if [ -d "${pkgname}-${pkgver}" ]; then
        cd "${pkgname}-${pkgver}"
    else
        cd "${startdir:-.}"
    fi
    make DESTDIR="${pkgdir}" install
    
    # Install FreedomOffice Desktop entries & scripts
    install -Dm755 bin/freedomoffice-searxng.sh "${pkgdir}/usr/bin/freedomoffice-searxng"
    install -Dm755 bin/freedomoffice-tor.sh "${pkgdir}/usr/bin/freedomoffice-tor"
    install -Dm755 .opencode/mcp_freedom_search.py "${pkgdir}/usr/lib/freedomoffice/mcp_freedom_search.py"
}
