# Maintainer: Natalie Spiva <natalie@acreetionos.org>
# Contributor: Arch Linux packagers (original LibreOffice PKGBUILD)

# FreedomOffice - A free, open-source office suite with Microsoft Office-compatible UI.
# Based on LibreOffice with MS Office Ribbon UI, zero telemetry, and full .docx/.xlsx/.pptx support.

pkgname=freedomoffice
pkgver=27.2.0.0
pkgrel=1
pkgdesc="A free, open-source office suite with Microsoft Office-compatible Ribbon UI - based on LibreOffice"
arch=('x86_64')
url="https://github.com/spivanatalie64/FreedomOffice"
license=('MPL' 'LGPL' 'GPL' 'CC')
depends=(
  'bash' 'libcups' 'curl' 'neon' 'openssl' 'libxml2' 'libxslt'
  'libxinerama' 'libxrandr' 'libxfixes' 'cairo' 'harfbuzz' 'icu'
  'zlib' 'bzip2' 'lz4' 'xz' 'zstd'
  'nss' 'nspr' 'redland' 'rasqal'
  'hunspell' 'hyphen' 'libmspack'
  'lcms2' 'poppler' 'glu' 'libgl'
  'libpagemaker' 'libabw' 'libwpd' 'libwpg' 'libwps'
  'libcdr' 'libvisio' 'libmspub' 'libodfgen'
  'libetonyek' 'librevenge' 'libfreehand'
  'libnumbertext' 'libmwaw' 'libe-book'
  'libzmf' 'libqxp' 'libstaroffice' 'libpagemaker'
  'liborcus' 'liblangtag'
  'clucene' 'gconf' 'gtk3' 'gtk4' 'qt6-base'
  'dbus-glib' 'fontconfig' 'freetype2' 'graphite'
  'pango' 'gdk-pixbuf2' 'cairo'
  'libxext' 'libxdamage' 'libxcomposite' 'libxrender'
  'libxslt' 'libatomic_ops' 'lpsolve'
  'unixodbc' 'libsecret' 'liboauth'
  'pcsclite' 'libtommath' 'mdds'
)
makedepends=(
  'git' 'base-devel' 'java-environment>=17' 'python' 'python-pip'
  'perl' 'perl-archive-zip' 'perl-compress-bzip2'
  'ant' 'apache-ant' 'doxygen' 'graphviz'
  'gperf' 'flex' 'bison' 'patchelf' 'rsync'
  'mesa' 'libglvnd' 'vlc'
  'ruby' 'nodejs' 'npm' 'typescript'
  'zip' 'unzip' 'pkg-config'
  'ccache' 'gcc' 'llvm' 'clang'
  'firebird' 'mariadb-libs' 'postgresql-libs'
  'jfreerdp' 'libtrace' 'libwebp'
  'box2d' 'dragon' 'libepubgen'
)
optdepends=(
  'java-runtime: for additional functionality'
  'postgresql-libs: for PostgreSQL database connectivity'
  'mariadb-libs: for MySQL/MariaDB database connectivity'
  'firebird: for Firebird database connectivity'
  'libmythes: for thesaurus'
  'libgltf: for GLTF model support'
)
provides=("${pkgname}")
conflicts=('libreoffice-fresh' 'libreoffice-still' 'libreoffice')
replaces=()
backup=()
options=('!strip' '!emptydirs')
install=
changelog=

# Source is the git repo at the tagged release version
source=("${pkgname}::git+https://github.com/spivanatalie64/FreedomOffice.git#tag=v${pkgver}")
sha256sums=('SKIP')
validpgpkeys=()

prepare() {
  cd "${srcdir}/${pkgname}"
  # Apply any FreedomOffice-specific patches if needed
}

build() {
  cd "${srcdir}/${pkgname}"
  
  # Configure with FreedomOffice settings
  ./autogen.sh \
    --prefix=/usr \
    --libdir=/usr/lib \
    --sysconfdir=/etc \
    --with-system-dicts \
    --with-system-libs \
    --with-system-curl \
    --with-system-neon \
    --with-system-openssl \
    --with-system-nss \
    --with-system-libxml \
    --with-system-libxslt \
    --with-system-cairo \
    --with-system-harfbuzz \
    --with-system-icu \
    --with-system-zlib \
    --with-system-bzip2 \
    --with-system-lz4 \
    --with-system-zstd \
    --with-system-liblangtag \
    --with-system-liborcus \
    --with-system-mdds \
    --with-system-librevenge \
    --with-system-libodfgen \
    --with-system-libepubgen \
    --with-system-libcdr \
    --with-system-libmspub \
    --with-system-libwpd \
    --with-system-libwpg \
    --with-system-libwps \
    --with-system-libvisio \
    --with-system-libetonyek \
    --with-system-libfreehand \
    --with-system-libnumbertext \
    --with-system-libmwaw \
    --with-system-libe-book \
    --with-system-libzmf \
    --with-system-libqxp \
    --with-system-libstaroffice \
    --with-system-libpagemaker \
    --with-system-libtommath \
    --with-system-lpsolve \
    --with-system-box2d \
    --with-system-libmspack \
    --with-system-poppler \
    --with-system-lcms2 \
    --with-system-glm \
    --with-system-dragon \
    --with-system-epubgen \
    --enable-qt6 \
    --enable-gtk3 \
    --enable-introspection=no \
    --without-java \
    --without-help \
    --without-myspell-dicts \
    --disable-breakpad \
    --disable-online-update \
    --disable-report-builder \
    --disable-odk \
    --disable-dependency-tracking \
    --disable-fetch-external
  
  make -j$(nproc)
}

package() {
  cd "${srcdir}/${pkgname}"
  make DESTDIR="${pkgdir}" install
  
  # Create symlinks for the Microsoft Office-compatible binary names
  mkdir -p "${pkgdir}/usr/bin"
  ln -sf /usr/lib/freedomoffice/program/FREEDOMWRITER "${pkgdir}/usr/bin/freedomwriter"
  ln -sf /usr/lib/freedomoffice/program/FREEDOMSHEET "${pkgdir}/usr/bin/freedomsheet"
  ln -sf /usr/lib/freedomoffice/program/FREEDOMSHOW "${pkgdir}/usr/bin/freedomshow"
  ln -sf /usr/lib/freedomoffice/program/FREEDOMBASE "${pkgdir}/usr/bin/freedombase"
  ln -sf /usr/lib/freedomoffice/program/FREEDOMDRAW "${pkgdir}/usr/bin/freedomdraw"
  ln -sf /usr/lib/freedomoffice/program/FREEDOMEQUATION "${pkgdir}/usr/bin/freedomequation"
  
  # Desktop files
  mkdir -p "${pkgdir}/usr/share/applications"
  cat > "${pkgdir}/usr/share/applications/freedomoffice-writer.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=FreedomWriter
GenericName=Word Processor
Comment=Create and edit word processing documents (Microsoft Word-compatible)
Exec=freedomwriter %F
Icon=freedomoffice-writer
StartupNotify=true
Terminal=false
Categories=Office;WordProcessor;
MimeType=application/msword;application/vnd.openxmlformats-officedocument.wordprocessingml.document;application/vnd.oasis.opendocument.text;application/rtf;text/plain;
EOF
  
  cat > "${pkgdir}/usr/share/applications/freedomoffice-sheet.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=FreedomSheet
GenericName=Spreadsheet
Comment=Create and edit spreadsheets (Microsoft Excel-compatible)
Exec=freedomsheet %F
Icon=freedomoffice-sheet
StartupNotify=true
Terminal=false
Categories=Office;Spreadsheet;
MimeType=application/vnd.ms-excel;application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;application/vnd.oasis.opendocument.spreadsheet;text/csv;
EOF
  
  cat > "${pkgdir}/usr/share/applications/freedomoffice-show.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=FreedomShow
GenericName=Presentation
Comment=Create and edit presentations (Microsoft PowerPoint-compatible)
Exec=freedomshow %F
Icon=freedomoffice-show
StartupNotify=true
Terminal=false
Categories=Office;Presentation;
MimeType=application/vnd.ms-powerpoint;application/vnd.openxmlformats-officedocument.presentationml.presentation;application/vnd.oasis.opendocument.presentation;
EOF
  
  cat > "${pkgdir}/usr/share/applications/freedomoffice-base.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=FreedomBase
GenericName=Database
Comment=Create and manage databases (Microsoft Access-compatible)
Exec=freedombase %F
Icon=freedomoffice-base
StartupNotify=true
Terminal=false
Categories=Office;Database;
MimeType=application/vnd.ms-access;
EOF
  
  cat > "${pkgdir}/usr/share/applications/freedomoffice-draw.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=FreedomDraw
GenericName=Diagram
Comment=Create diagrams and vector graphics (Microsoft Visio-compatible)
Exec=freedomdraw %F
Icon=freedomoffice-draw
StartupNotify=true
Terminal=false
Categories=Office;Graphics;
MimeType=application/vnd.ms-visio;application/vnd.oasis.opendocument.graphics;
EOF
  
  # Install icons
  mkdir -p "${pkgdir}/usr/share/icons/hicolor/scalable/apps"
  for app in writer sheet show base draw equation; do
    cp "${srcdir}/${pkgname}/icon-themes/freedomoffice/brand/logo.svg" \
      "${pkgdir}/usr/share/icons/hicolor/scalable/apps/freedomoffice-${app}.svg"
  done
  
  echo "FreedomOffice has been installed!"
  echo "Run 'freedomwriter', 'freedomsheet', 'freedomshow', or just 'FREEDOMOFFICE' from terminal."
  echo "Go to View > User Interface > FreedomOffice Ribbon for the MS Office-style UI."
}
