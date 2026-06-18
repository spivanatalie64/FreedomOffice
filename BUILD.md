# Building FreedomOffice

FreedomOffice is built on the LibreOffice codebase. The build process is the same as LibreOffice's.

## Prerequisites

### Arch Linux
```bash
sudo pacman -S --needed \
  base-devel git java-environment=17 \
  python python-pip python-setuptools python-virtualenv \
  perl perl-archive-zip perl-compress-bzip2 \
  libxslt libxml2 libpng libtiff libmspack \
  lcms2 poppler cups glu \
  mesa mesa-libgl libglvnd \
  harfbuzz icu graphite \
  dbus-glib gtk3 gtk4 \
  qt5-base qt6-base \
  libsecret liboauth libwpd libwpg libwps \
  libcdr libvisio libmspub libodfgen \
  libetonyek librevenge \
  libnumbertext libmwaw libe-book \
  libzmf libqxp libstaroffice \
  cairo pango gdk-pixbuf2 \
  libatomic_ops lpsolve \
  mdds box2d \
  clucene hunspell \
  zlib bzip2 lz4 xz zstd \
  curl neon openssl \
  xmlsec libxslt \
  firebird mariadb-libs postgresql-libs \
  unixodbc \
  fontconfig freetype2 \
  nss nspr \
  redland rasqal \
  jfreerdp \
  libpagemaker libabw \
  liborcus \
  liblangtag \
  libgltf
```

### Install build dependencies automatically
```bash
cd /home/natalie/Projects/FreedomOffice/freedomoffice-core
sudo ./autogen.sh --with-distro=ArchLinux
```

## Build

### Quick build (minimal features)
```bash
cd /home/natalie/Projects/FreedomOffice/freedomoffice-core
./autogen.sh --disable-breakpad --disable-online-update \
  --without-java --disable-report-builder \
  --enable-qt6 --enable-gtk3 \
  --prefix=/opt/freedomoffice
```

### Full build
```bash
cd /home/natalie/Projects/FreedomOffice/freedomoffice-core
./autogen.sh --enable-all-languages \
  --prefix=/opt/freedomoffice
```

### After configure
```bash
make -j$(nproc)
```

This will take 1-4 hours depending on your machine.

## Install
```bash
sudo make install
```

## Run
```bash
/opt/freedomoffice/bin/FREEDOMOFFICE
```

Or launch individual apps:
```bash
/opt/freedomoffice/bin/FREEDOMWRITER    # Word-compatible
/opt/freedomoffice/bin/FREEDOMSHEET     # Excel-compatible
/opt/freedomoffice/bin/FREEDOMSHOW      # PowerPoint-compatible
/opt/freedomoffice/bin/FREEDOMBASE      # Access-compatible
/opt/freedomoffice/bin/FREEDOMDRAW      # Visio-compatible
/opt/freedomoffice/bin/FREEDOMEQUATION  # Equation Editor
```

## Enable the FreedomOffice Ribbon
Once running, go to:
**View → User Interface → FreedomOffice Ribbon**

The FreedomOffice Ribbon will be the default in future builds.
