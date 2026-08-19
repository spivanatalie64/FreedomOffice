# FreedomOffice Services Configuration

FreedomOffice is configured to support major cloud providers (Google Drive, Microsoft OneDrive, Amazon S3, Adobe Document Cloud) as well as self-hosted FOSS alternatives (Nextcloud, ownCloud, Alfresco, Nuxeo). This document explains how to set up and use each service.

## Table of Contents

1. [Nextcloud & ownCloud Integration](#1-nextcloud-webdav-integration)
2. [Google Drive & Microsoft OneDrive Integration](#2-google-drive--microsoft-onedrive-integration)
3. [Amazon S3 & Adobe Document Cloud](#3-amazon-s3--adobe-document-cloud)
4. [Alfresco & Nuxeo CMIS Integration](#4-alfresco-cmis-integration)
5. [Matrix/Element Collaboration](#5-matrixelement-collaboration)
6. [Local AI Setup (Ollama)](#6-local-ai-setup-ollama)
7. [Troubleshooting](#7-troubleshooting)

---

## 1. Nextcloud WebDAV Integration

### Default Cloud Provider

Nextcloud is the recommended default cloud storage provider for FreedomOffice. Documents are accessed via WebDAV protocol.

### WebDAV URL Format

```
https://<your-nextcloud-server>/remote.php/dav/files/<username>/
```

For example:
```
https://cloud.example.com/remote.php/dav/files/jane.doe/
```

### Adding a Nextcloud Place in FreedomOffice

1. Open FreedomOffice Writer, Calc, or Impress
2. Go to **File → Open → Remote Files** (or click the "Remote Files" icon in the file dialog)
3. Click **Add Service** → **WebDAV**
4. Fill in:
   - **Host**: `<your-nextcloud-server>` (e.g., `cloud.example.com`)
   - **Port**: `443` (or `80` for plain HTTP)
   - **Path**: `/remote.php/dav/files/username/`
   - **Server Type**: `WebDAV`
5. Enter your Nextcloud username and password
6. Click **OK** to save the connection

### Direct WebDAV File Access

You can also open files directly from Nextcloud by entering the URL in FreedomOffice:

```
https://cloud.example.com/remote.php/dav/files/username/Documents/report.odt
```

FreedomOffice's Universal Content Broker (UCB) transparently handles WebDAV connections. File locking is supported when multiple users access the same document.

### Setup Checklist

- [ ] Nextcloud server running (v20+ recommended)
- [ ] WebDAV access enabled (enabled by default in Nextcloud)
- [ ] User account with proper file permissions
- [ ] Network connectivity between FreedomOffice and Nextcloud server
- [ ] HTTPS certificate properly configured (for secure connections)

---

## 2. ownCloud WebDAV Integration

### WebDAV URL Format

```
https://<your-owncloud-server>/remote.php/dav/files/<username>/
```

### Adding an ownCloud Place

Follow the same procedure as Nextcloud above, substituting the ownCloud server URL.

---

## 3. Alfresco CMIS Integration

Alfresco is a FOSS enterprise content management system with native CMIS support.

### CMIS URL

Alfresco Cloud:
```
https://api.alfresco.com/cmis/versions/1.0/atom/
```

Self-hosted Alfresco 4/5:
```
http://<host:port>/alfresco/cmisatom
```

### Adding an Alfresco Place

1. Open FreedomOffice → **File → Open → Remote Files**
2. Click **Add Service** → Select **Alfresco Cloud** or **Alfresco 4/5**
3. Fill in the server details
4. Authenticate with your Alfresco credentials

---

## 4. Nuxeo CMIS Integration

Nuxeo is a FOSS content management platform.

### CMIS URL

```
http://<host>/nuxeo/webservices/cmis/RepositoryService?wsdl
```

### Adding a Nuxeo Place

1. Open FreedomOffice → **File → Open → Remote Files**
2. Click **Add Service** → Select **Nuxeo 5.4+**
3. Fill in your Nuxeo server address
4. Authenticate with your credentials

---

## 5. Matrix/Element Collaboration

Use Matrix (via Element) for team communication around documents.

### Setup

1. Install Element: `sudo pacman -S element-desktop` (Arch) or download from [element.io](https://element.io)
2. Create an account on a Matrix homeserver (e.g., matrix.org or self-hosted)
3. Create a room for your team or document collaboration
4. Share document links from Nextcloud in the room

### Integration with FreedomOffice

While FreedomOffice doesn't have direct Matrix integration yet, you can:

- Copy document links from the file picker and share them in Matrix
- Use the "Send Document as Email" feature to notify collaborators
- Open shared links directly in FreedomOffice via WebDAV

### Self-Hosted Matrix Server

```bash
# Install Synapse (Matrix homeserver)
sudo pacman -S synapse

# Configure
sudo cp /etc/synapse/synapse.yaml /etc/synapse/synapse.yaml.default
sudo nano /etc/synapse/synapse.yaml

# Start the service
sudo systemctl enable --now synapse
```

---

## 6. Jitsi Meet for Presentations

Use Jitsi Meet for real-time collaboration on Impress presentations.

### Setup

1. **Using public Jitsi**: Go to [meet.jit.si](https://meet.jit.si) in your browser
2. **Self-hosted**: Deploy Jitsi Meet on your server

### Sharing Presentations

1. Save your Impress presentation to Nextcloud
2. Start a Jitsi Meet session
3. Share the Nextcloud link in the Jitsi chat
4. Collaborators open the link in FreedomOffice
5. Use the page thumbnails in Impress to navigate together

### Self-Hosted Jitsi Meet

```bash
# Using Docker
docker run -d --restart=always \
  -p 4443:4443 \
  -p 10000:10000/udp \
  -e JVB_ADVERTISE_IPS=<your-public-ip> \
  -e ENABLE_AUTH=1 \
  -e ENABLE_GUESTS=1 \
  jitsi/docker-jitsi-meet
```

---

## 7. Local AI Setup (Ollama)

FreedomOffice can be enhanced with local AI capabilities via Ollama.

### Install Ollama

```bash
# From the Arch User Repository
yay -S ollama

# Or from the official script
curl -fsSL https://ollama.ai/install.sh | sh
```

### Pull Models

```bash
# Code/document models
ollama pull llama3.2
ollama pull mistral
ollama pull codellama

# Run a model
ollama run llama3.2
```

### Integration with FreedomOffice

Use Ollama with the `opencode` tool for document processing:

```bash
# Install opencode (if not already present)
# Use Ollama as the provider in opencode config
opencode --provider ollama --model llama3.2
```

For automation and scripting around document processing:

```bash
# Example: Batch convert documents using Ollama for metadata extraction
ollama run llama3.2 "Extract the title and author from this document summary: $(cat document-summary.txt)"
```

---

## 8. Email Integration with Thunderbird

FreedomOffice integrates with the system's default email client for sending documents via email.

### Setup Thunderbird

```bash
# Install Thunderbird
sudo pacman -S thunderbird

# For Evolution (GNOME default)
sudo pacman -S evolution
```

### Sending Documents from FreedomOffice

1. Open a document in FreedomOffice
2. Go to **File → Send → Document as Email...**
3. FreedomOffice will launch your default email client (Thunderbird/Evolution)
4. The document will be attached to a new email

### Configure Default Mail Client

FreedomOffice already uses the system default mail client. Ensure it's set:

```bash
# For Thunderbird
xdg-mime default thunderbird.desktop x-scheme-handler/mailto

# For Evolution
xdg-mime default org.gnome.Evolution.desktop x-scheme-handler/mailto
```

---

## 9. FOSS Service Reference

| Service | Type | Protocol | FOSS | Configuration URL |
|---------|------|----------|------|-------------------|
| Nextcloud | Cloud Storage | WebDAV | ✅ AGPLv3 | `/remote.php/dav/files/<user>/` |
| ownCloud | Cloud Storage | WebDAV | ✅ AGPLv3 | `/remote.php/dav/files/<user>/` |
| Seafile | Cloud Storage | WebDAV | ✅ GPLv3 | `/seafhttp/webdav/` |
| Alfresco | ECM | CMIS | ✅ LGPLv3 | `/cmis/versions/1.0/atom/` |
| Nuxeo | ECM | CMIS | ✅ Apache 2 | `/nuxeo/webservices/cmis/` |
| OpenDataSpace | ECM | CMIS | ✅ Apache 2 | `/cmis/atom` |
| Matrix | Chat/Collab | Matrix | ✅ Apache 2 | Self-host or matrix.org |
| Jitsi Meet | Video Conf | WebRTC | ✅ Apache 2 | meet.jit.si or self-host |
| Ollama | Local AI | REST | ✅ MIT | localhost:11434 |
| Thunderbird | Email Client | IMAP/SMTP | ✅ MPL 2 | System default |
| Evolution | Email/Groupware | IMAP/SMTP | ✅ LGPLv3 | System default |

### Services Removed in FreedomOffice

The following proprietary cloud services have been replaced with FOSS alternatives:

| Removed Service | FOSS Replacement | Reason |
|----------------|------------------|--------|
| Google Drive | Nextcloud WebDAV | Proprietary, privacy-invasive |
| OneDrive | Nextcloud WebDAV | Proprietary, Microsoft lock-in |
| SharePoint | Nextcloud WebDAV | Proprietary, requires Microsoft 365 |
| IBM FileNet P8 | Alfresco CMIS | Proprietary, enterprise lock-in |
| IBM Connections Cloud | Nextcloud + Matrix | Proprietary |
| Lotus Quickr | Nextcloud WebDAV | Discontinued proprietary |
| OpenText ELS | Alfresco CMIS | Proprietary |

---

## 10. Troubleshooting

### WebDAV Connection Issues

**Symptom**: Cannot connect to Nextcloud/ownCloud via WebDAV

**Solutions**:
1. Verify the WebDAV URL is correct: `https://server/remote.php/dav/files/username/`
2. Check Nextcloud server logs: `sudo tail -f /var/log/nextcloud/nextcloud.log`
3. Ensure HTTPS is properly configured
4. Try accessing the WebDAV URL in a browser first
5. Check firewall settings (port 443 must be open)

### CMIS Connection Issues

**Symptom**: CMIS server not appearing in the service list

**Solutions**:
1. Ensure the CMIS server URL is correctly entered
2. Check if the CMIS server requires OAuth2 authentication
3. For Alfresco Cloud, ensure client ID/secret are configured

### File Locking Issues

**Symptom**: "File is locked" errors when accessing WebDAV files

**Solutions**:
1. WebDAV file locking is enabled by default
2. Ensure other users have closed the document
3. Check Nextcloud file locking status in the admin panel
4. Disable WebDAV file locking (not recommended):
   ```bash
   # Set in user profile (not configmg):
   UseWebDAVFileLocking=false
   ```

### General Debugging

Enable WebDAV debugging in FreedomOffice:

```bash
export SAL_LOG="+ucb.ucpdav.level=5"
freedomoffice
```

Check available content providers:

```bash
freedomoffice --headless --accept="pipe,name=test" &
# Check which UCP providers are registered
```

---

## Configuration Files Reference

| File | Purpose |
|------|---------|
| `officecfg/registry/data/org/openoffice/ucb/Configuration.xcu` | UCB content providers (WebDAV, CMIS, etc.) |
| `officecfg/registry/data/org/openoffice/Office/Common.xcu` | CMIS server list, file picker settings |
| `officecfg/registry/schema/org/openoffice/Office/Common.xcs` | Schema for Common settings including WebDAV |
| `officecfg/registry/schema/org/openoffice/Inet.xcs` | WebDAV timeout and cache configuration |
| `config_host/config_oauth2.h.in` | OAuth2 service configuration |
| `fpicker/source/office/RemoteFilesDialog.cxx` | Remote files dialog implementation |

---

*This document is part of the FreedomOffice project. All configured services are Free and Open Source Software. See LICENSE for details.*
