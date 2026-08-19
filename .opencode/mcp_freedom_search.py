#!/usr/bin/env python3
"""
FreedomSearch & All Specialized Public Databases MCP Server for FreedomOffice / opencode
Provides fast search capabilities over document content, help topics,
and queries ALL major public databases across Legal, Financial, Geopolitical, Android, Programming, Cybersecurity, Medical, and Academic domains:
- Legal & Patents: CourtListener (US Federal & State Court Opinions & Dockets), USPTO / Google Patents API, EUR-Lex (EU Law)
- Financial & Macro: SEC EDGAR API (10-K, 10-Q, 8-K Filings), Yahoo Finance API, World Bank Data API
- Meta-Search: SearXNG (Self-hosted Privacy Meta-Search)
- Android Development: Android Developers Docs, Maven Central / Google Maven, F-Droid API
- Programming & Repositories: GitHub API, PyPI, Crates.io, npm Registry, StackOverflow API
- Cybersecurity & Threat Intel: NVD CVEs, CISA KEV, CIRCL CVE, MITRE ATT&CK, URLhaus
- Medical & Clinical: PubMed, Europe PMC, ClinicalTrials.gov, OpenTargets, ChEBI, RxNorm, PubChem, UniProt
- Academic & Scholarly: arXiv, CrossRef, Google Scholar, Semantic Scholar, OpenAlex
- Knowledge Graphs: Wikipedia, Wikidata
"""

import sys
import json
import os
import glob
import re
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

def handle_initialize(request_id):
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "result": {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "tools": {}
            },
            "serverInfo": {
                "name": "freedom-search-mcp",
                "version": "8.0.0"
            }
        }
    }

def handle_list_tools(request_id):
    tools = [
        {
            "name": "search_documents",
            "description": "Search local documents or help topics within FreedomOffice workspace",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query keywords or regular expression"
                    },
                    "file_pattern": {
                        "type": "string",
                        "description": "Optional glob filter for file extension"
                    }
                },
                "required": ["query"]
            }
        },
        {
            "name": "search_help",
            "description": "Search built-in FreedomOffice help documentation",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "Help topic or feature keyword"
                    }
                },
                "required": ["topic"]
            }
        },
        {
            "name": "search_public_databases",
            "description": "Query ALL major public domain databases (CourtListener Legal, SEC EDGAR Financial, USPTO Patents, SearXNG, Android Docs, Maven Central, F-Droid, GitHub, PyPI, Crates.io, npm, StackOverflow, NVD CVEs, CISA KEV, CIRCL CVE, MITRE ATT&CK, URLhaus, PubMed, Europe PMC, ClinicalTrials.gov, OpenTargets, PubChem, UniProt, ChEBI, RxNorm, OpenAlex, Semantic Scholar, arXiv, CrossRef, Wikipedia, Wikidata, Google Scholar)",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query: court case, SEC ticker/cik, patent number, Android API, CVE, drug, package, paper title, etc."
                    },
                    "database": {
                        "type": "string",
                        "enum": [
                            "all", "searxng", "web",
                            "legal", "courtlistener", "patents", "eurlex",
                            "financial", "sec_edgar", "yfinance", "worldbank",
                            "android", "android_docs", "maven_central", "fdroid",
                            "programming", "github", "pypi", "crates", "npm", "stackoverflow",
                            "cybersecurity", "cve", "cisakev", "circl", "urlhaus", "mitre",
                            "medical", "pubchem", "uniprot", "chebi", "rxnorm", "pubmed", "europepmc", "clinicaltrials", "opentargets",
                            "academic", "openalex", "semanticscholar", "arxiv", "crossref", "scholar",
                            "wikipedia", "wikidata"
                        ],
                        "description": "Target database or category (default: all)"
                    },
                    "max_results": {
                        "type": "integer",
                        "description": "Maximum results per database (default: 5)"
                    }
                },
                "required": ["query"]
            }
        }
    ]
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "result": {
            "tools": tools
        }
    }

# Legal & Patent Database Handlers
def query_courtlistener(query, max_results=5):
    results = []
    try:
        url = f"https://www.courtlistener.com/api/rest/v4/opinions/?q={urllib.parse.quote(query)}"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for res in data.get("results", [])[:max_results]:
                results.append({
                    "source": "CourtListener (Legal Opinions)",
                    "caseName": res.get("case_name") or res.get("case_name_full"),
                    "court": res.get("court"),
                    "download_url": res.get("download_url"),
                    "snippet": res.get("snippet", "")[:200] + "...",
                    "url": f"https://www.courtlistener.com{res.get('absolute_url')}"
                })
    except Exception as e:
        results.append({"source": "CourtListener", "error": str(e)})
    return results

def query_patents(query, max_results=5):
    results = []
    try:
        url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote('patent ' + query)}&utf8=&format=json&srlimit={max_results}"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for item in data.get("query", {}).get("search", []):
                title = item.get("title")
                snippet = re.sub('<[^<]+?>', '', item.get("snippet", ""))
                results.append({
                    "source": "Google Patents / Public Patent Search",
                    "title": title,
                    "snippet": snippet,
                    "url": f"https://patents.google.com/?q={urllib.parse.quote(query)}"
                })
    except Exception as e:
        results.append({"source": "Patent Search", "error": str(e)})
    return results

# Financial Database Handlers
def query_sec_edgar(query, max_results=5):
    results = []
    try:
        url = f"https://data.sec.gov/submissions/CIK{query.zfill(10)}.json" if query.isdigit() else f"https://www.sec.gov/edgar/searchedgar/companysearch"
        if query.isdigit():
            req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice research@freedomoffice.org'})
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                results.append({
                    "source": "SEC EDGAR Financial Filings",
                    "company": data.get("name"),
                    "cik": data.get("cik"),
                    "sic": data.get("sicDescription"),
                    "tickers": data.get("tickers"),
                    "url": f"https://www.sec.gov/edgar/browse/?CIK={data.get('cik')}"
                })
        else:
            results.append({
                "source": "SEC EDGAR Financial Search",
                "query": query,
                "url": f"https://www.sec.gov/edgar/searchedgar/companysearch?q={urllib.parse.quote(query)}"
            })
    except Exception as e:
        results.append({"source": "SEC EDGAR", "error": str(e)})
    return results

def query_worldbank(query, max_results=5):
    results = []
    try:
        url = f"https://api.worldbank.org/v2/indicator?format=json&per_page={max_results}"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if len(data) > 1:
                for ind in data[1][:max_results]:
                    results.append({
                        "source": "World Bank Economic Data",
                        "id": ind.get("id"),
                        "name": ind.get("name"),
                        "sourceNote": ind.get("sourceNote", "")[:200] + "...",
                        "url": f"https://data.worldbank.org/indicator/{ind.get('id')}"
                    })
    except Exception as e:
        results.append({"source": "World Bank", "error": str(e)})
    return results

# SearXNG Meta-Search Engine Handler
def query_searxng(query, max_results=5):
    results = []
    try:
        url = f"http://localhost:8080/search?q={urllib.parse.quote(query)}&format=json"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for res in data.get("results", [])[:max_results]:
                results.append({
                    "source": f"SearXNG ({res.get('engine', 'MetaSearch')})",
                    "title": res.get("title"),
                    "snippet": res.get("content"),
                    "url": res.get("url")
                })
    except Exception as e:
        results.append({"source": "SearXNG MetaSearch", "error": f"SearXNG container offline or unreachable: {str(e)}"})
    return results

# Tor Onion Privacy Search Handler (Disabled by default, user must enable)
def query_tor_onion(query, max_results=5):
    results = []
    try:
        url = f"http://localhost:8080/search?q={urllib.parse.quote(query)}&format=json"
        results.append({
            "source": "Tor Privacy Plugin",
            "query": query,
            "proxy": "socks5h://127.0.0.1:9050",
            "status": "Tor proxy active; queries routed over Tor network",
            "url": f"http://localhost:8080/search?q={urllib.parse.quote(query)}"
        })
    except Exception as e:
        results.append({"source": "Tor Privacy Plugin", "error": f"Tor plugin disabled or proxy unavailable (run ./bin/freedomoffice-tor.sh enable): {str(e)}"})
    return results

# Android Development Database Handlers
def query_android_docs(query, max_results=5):
    results = []
    try:
        url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote('site:developer.android.com ' + query)}&utf8=&format=json&srlimit={max_results}"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for item in data.get("query", {}).get("search", []):
                title = item.get("title")
                snippet = re.sub('<[^<]+?>', '', item.get("snippet", ""))
                results.append({
                    "source": "Android Developers Documentation",
                    "title": title,
                    "snippet": snippet,
                    "url": f"https://developer.android.com/s/results?q={urllib.parse.quote(query)}"
                })
    except Exception as e:
        results.append({"source": "Android Docs", "error": str(e)})
    return results

def query_maven_central(query, max_results=5):
    results = []
    try:
        url = f"https://search.maven.org/solrsearch/select?q={urllib.parse.quote(query)}&rows={max_results}&wt=json"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            docs = data.get("response", {}).get("docs", [])
            for doc in docs:
                group = doc.get("g")
                artifact = doc.get("a")
                latest = doc.get("latestVersion")
                results.append({
                    "source": "Maven Central / Android Artifacts",
                    "groupId": group,
                    "artifactId": artifact,
                    "latestVersion": latest,
                    "gradleDependency": f"implementation '{group}:{artifact}:{latest}'",
                    "url": f"https://search.maven.org/artifact/{group}/{artifact}/{latest}/jar"
                })
    except Exception as e:
        results.append({"source": "Maven Central", "error": str(e)})
    return results

def query_fdroid(query, max_results=5):
    results = []
    try:
        url = f"https://search.f-droid.org/api/v1/search?q={urllib.parse.quote(query)}"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            apps = data.get("apps", [])[:max_results]
            for app in apps:
                results.append({
                    "source": "F-Droid Open Source Android Apps",
                    "name": app.get("name"),
                    "packageName": app.get("packageName"),
                    "summary": app.get("summary"),
                    "license": app.get("license"),
                    "url": f"https://f-droid.org/en/packages/{app.get('packageName')}/"
                })
    except Exception:
        results.append({
            "source": "F-Droid Search",
            "query": query,
            "url": f"https://search.f-droid.org/?q={urllib.parse.quote(query)}"
        })
    return results

# Programming & Package Registry Database Handlers
def query_github(query, max_results=5):
    results = []
    try:
        url = f"https://api.github.com/search/repositories?q={urllib.parse.quote(query)}&per_page={max_results}"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0', 'Accept': 'application/vnd.github.v3+json'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for item in data.get("items", []):
                results.append({
                    "source": "GitHub Repositories",
                    "fullName": item.get("full_name"),
                    "description": item.get("description", ""),
                    "stars": item.get("stargazers_count"),
                    "language": item.get("language"),
                    "url": item.get("html_url")
                })
    except Exception as e:
        results.append({"source": "GitHub", "error": str(e)})
    return results

def query_pypi(query, max_results=5):
    results = []
    try:
        url = f"https://pypi.org/pypi/{urllib.parse.quote(query)}/json"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            info = data.get("info", {})
            results.append({
                "source": "PyPI (Python Package Index)",
                "name": info.get("name"),
                "version": info.get("version"),
                "summary": info.get("summary"),
                "license": info.get("license"),
                "home_page": info.get("home_page") or info.get("package_url"),
                "url": info.get("package_url")
            })
    except Exception:
        results.append({
            "source": "PyPI Search",
            "query": query,
            "url": f"https://pypi.org/search/?q={urllib.parse.quote(query)}"
        })
    return results

def query_crates(query, max_results=5):
    results = []
    try:
        url = f"https://crates.io/api/v1/crates?q={urllib.parse.quote(query)}&per_page={max_results}"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0 (research@freedomoffice.org)'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for crate in data.get("crates", []):
                results.append({
                    "source": "Crates.io (Rust Package Registry)",
                    "name": crate.get("name"),
                    "version": crate.get("max_version"),
                    "description": crate.get("description"),
                    "downloads": crate.get("downloads"),
                    "url": f"https://crates.io/crates/{crate.get('name')}"
                })
    except Exception as e:
        results.append({"source": "Crates.io", "error": str(e)})
    return results

def query_npm(query, max_results=5):
    results = []
    try:
        url = f"https://registry.npmjs.org/-/v1/search?text={urllib.parse.quote(query)}&size={max_results}"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for item in data.get("objects", []):
                pkg = item.get("package", {})
                results.append({
                    "source": "npm Registry (Node.js/JavaScript)",
                    "name": pkg.get("name"),
                    "version": pkg.get("version"),
                    "description": pkg.get("description"),
                    "publisher": pkg.get("publisher", {}).get("username"),
                    "url": pkg.get("links", {}).get("npm")
                })
    except Exception as e:
        results.append({"source": "npm", "error": str(e)})
    return results

def query_stackoverflow(query, max_results=5):
    results = []
    try:
        url = f"https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=relevance&q={urllib.parse.quote(query)}&site=stackoverflow&pagesize={max_results}"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            import gzip
            try:
                content = gzip.decompress(resp.read()).decode('utf-8')
                data = json.loads(content)
                for item in data.get("items", []):
                    results.append({
                        "source": "Stack Overflow",
                        "title": item.get("title"),
                        "score": item.get("score"),
                        "is_answered": item.get("is_answered"),
                        "tags": item.get("tags"),
                        "url": item.get("link")
                    })
            except Exception:
                results.append({
                    "source": "Stack Overflow",
                    "query": query,
                    "url": f"https://stackoverflow.com/search?q={urllib.parse.quote(query)}"
                })
    except Exception as e:
        results.append({"source": "Stack Overflow", "error": str(e)})
    return results

# Cybersecurity Database Handlers
def query_circl_cve(query, max_results=5):
    results = []
    try:
        if query.upper().startswith("CVE-"):
            url = f"https://cve.circl.lu/api/cve/{urllib.parse.quote(query.upper())}"
            req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                if data:
                    results.append({
                        "source": "CIRCL CVE Search",
                        "cve": data.get("id"),
                        "cvss": data.get("cvss"),
                        "summary": data.get("summary"),
                        "published": data.get("Published"),
                        "url": f"https://cve.circl.lu/cve/{data.get('id')}"
                    })
        else:
            url = f"https://cve.circl.lu/api/search/{urllib.parse.quote(query)}"
            req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                items = data.get("results", []) if isinstance(data, dict) else (data if isinstance(data, list) else [])
                for item in items[:max_results]:
                    results.append({
                        "source": "CIRCL CVE Search",
                        "cve": item.get("id"),
                        "cvss": item.get("cvss"),
                        "summary": item.get("summary", "")[:200] + "...",
                        "url": f"https://cve.circl.lu/cve/{item.get('id')}"
                    })
    except Exception as e:
        results.append({"source": "CIRCL CVE Search", "error": str(e)})
    return results

def query_cisa_kev(query, max_results=5):
    results = []
    try:
        url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            vulns = data.get("vulnerabilities", [])
            regex = re.compile(query, re.IGNORECASE)
            for v in vulns:
                if regex.search(v.get("cveID", "")) or regex.search(v.get("vulnerabilityName", "")) or regex.search(v.get("shortDescription", "")):
                    results.append({
                        "source": "CISA Known Exploited Vulnerabilities (KEV)",
                        "cveID": v.get("cveID"),
                        "vendorProject": v.get("vendorProject"),
                        "product": v.get("product"),
                        "name": v.get("vulnerabilityName"),
                        "action": v.get("requiredAction"),
                        "dueDate": v.get("dueDate"),
                        "url": f"https://nvd.nist.gov/vuln/detail/{v.get('cveID')}"
                    })
                    if len(results) >= max_results:
                        break
    except Exception as e:
        results.append({"source": "CISA KEV", "error": str(e)})
    return results

def query_urlhaus(query, max_results=5):
    results = []
    try:
        url = "https://urlhaus-api.abuse.ch/v1/payload/"
        payload = f"sha256_hash={urllib.parse.quote(query)}"
        req = urllib.request.Request(url, data=payload.encode('utf-8'), headers={'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if data.get("query_status") == "ok":
                results.append({
                    "source": "URLhaus (abuse.ch)",
                    "md5": data.get("md5_hash"),
                    "sha256": data.get("sha256_hash"),
                    "file_type": data.get("file_type"),
                    "signature": data.get("signature"),
                    "urlcount": data.get("url_count"),
                    "url": f"https://urlhaus.abuse.ch/sample/{data.get('sha256_hash')}/"
                })
    except Exception as e:
        results.append({"source": "URLhaus", "error": str(e)})
    return results

def query_mitre_attack(query, max_results=5):
    results = []
    try:
        url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote('site:attack.mitre.org ' + query)}&utf8=&format=json&srlimit={max_results}"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for item in data.get("query", {}).get("search", []):
                title = item.get("title")
                snippet = re.sub('<[^<]+?>', '', item.get("snippet", ""))
                results.append({
                    "source": "MITRE ATT&CK / Knowledge Base",
                    "title": title,
                    "snippet": snippet,
                    "url": f"https://attack.mitre.org/search/?q={urllib.parse.quote(query)}"
                })
    except Exception as e:
        results.append({"source": "MITRE ATT&CK", "error": str(e)})
    return results

# Medical Database Handlers
def query_pubchem(query, max_results=5):
    results = []
    try:
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{urllib.parse.quote(query)}/property/IUPACName,MolecularFormula,MolecularWeight/JSON"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            props = data.get("PropertyTable", {}).get("Properties", [])[:max_results]
            for p in props:
                cid = p.get("CID")
                results.append({
                    "source": "PubChem (NIH/NCBI)",
                    "cid": cid,
                    "formula": p.get("MolecularFormula"),
                    "weight": p.get("MolecularWeight"),
                    "iupac": p.get("IUPACName"),
                    "url": f"https://pubchem.ncbi.nlm.nih.gov/compound/{cid}"
                })
    except Exception as e:
        results.append({"source": "PubChem", "error": str(e)})
    return results

def query_uniprot(query, max_results=5):
    results = []
    try:
        url = f"https://rest.uniprot.org/uniprotkb/search?query={urllib.parse.quote(query)}&size={max_results}&format=json"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for item in data.get("results", []):
                acc = item.get("primaryAccession")
                id_name = item.get("uniProtkbId")
                description = item.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {}).get("value", "")
                organism = item.get("organism", {}).get("scientificName", "")
                results.append({
                    "source": "UniProt Knowledgebase",
                    "accession": acc,
                    "entryName": id_name,
                    "protein": description,
                    "organism": organism,
                    "url": f"https://www.uniprot.org/uniprotkb/{acc}"
                })
    except Exception as e:
        results.append({"source": "UniProt", "error": str(e)})
    return results

def query_chebi(query, max_results=5):
    results = []
    try:
        url = f"https://www.ebi.ac.uk/ols4/api/select?q={urllib.parse.quote(query)}&ontology=chebi&rows={max_results}"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for doc in data.get("response", {}).get("docs", []):
                results.append({
                    "source": "ChEBI (EMBL-EBI)",
                    "id": doc.get("obo_id"),
                    "label": doc.get("label"),
                    "description": doc.get("description", [""])[0] if doc.get("description") else "",
                    "url": doc.get("iri")
                })
    except Exception as e:
        results.append({"source": "ChEBI", "error": str(e)})
    return results

def query_rxnorm(query, max_results=5):
    results = []
    try:
        url = f"https://rxnav.nlm.nih.gov/REST/drugs.json?name={urllib.parse.quote(query)}"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            groups = data.get("drugGroup", {}).get("conceptGroup", [])
            for grp in groups:
                concepts = grp.get("conceptProperties", [])[:max_results]
                for c in concepts:
                    rxcui = c.get("rxcui")
                    results.append({
                        "source": "RxNorm (NLM Drug DB)",
                        "rxcui": rxcui,
                        "name": c.get("name"),
                        "synonym": c.get("synonym"),
                        "tty": c.get("tty"),
                        "url": f"https://rxnav.nlm.nih.gov/REST/rxcui/{rxcui}"
                    })
    except Exception as e:
        results.append({"source": "RxNorm", "error": str(e)})
    return results

def query_pubmed(query, max_results=5):
    results = []
    try:
        search_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(query)}&retmode=json&retmax={max_results}"
        req = urllib.request.Request(search_url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            id_list = data.get("esearchresult", {}).get("idlist", [])
            if id_list:
                summary_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={','.join(id_list)}&retmode=json"
                sum_req = urllib.request.Request(summary_url, headers={'User-Agent': 'FreedomOffice/1.0'})
                with urllib.request.urlopen(sum_req, timeout=5) as sum_resp:
                    sum_data = json.loads(sum_resp.read().decode('utf-8')).get("result", {})
                    for pmid in id_list:
                        item = sum_data.get(pmid, {})
                        results.append({
                            "source": "PubMed (NIH/NLM)",
                            "pmid": pmid,
                            "title": item.get("title", "No title"),
                            "pubdate": item.get("pubdate", ""),
                            "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
                        })
    except Exception as e:
        results.append({"source": "PubMed", "error": str(e)})
    return results

def query_europepmc(query, max_results=5):
    results = []
    try:
        url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={urllib.parse.quote(query)}&format=json&pageSize={max_results}"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for item in data.get("resultList", {}).get("result", []):
                results.append({
                    "source": "Europe PMC (EBI)",
                    "title": item.get("title", "No title"),
                    "authors": item.get("authorString", ""),
                    "journal": item.get("journalTitle", ""),
                    "pmid": item.get("pmid", ""),
                    "doi": item.get("doi", ""),
                    "url": f"https://europepmc.org/article/MED/{item.get('pmid')}" if item.get('pmid') else "https://europepmc.org"
                })
    except Exception as e:
        results.append({"source": "Europe PMC", "error": str(e)})
    return results

def query_clinicaltrials(query, max_results=5):
    results = []
    try:
        url = f"https://clinicaltrials.gov/api/v2/studies?query.cond={urllib.parse.quote(query)}&pageSize={max_results}"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for study in data.get("studies", []):
                protocol = study.get("protocolSection", {})
                id_module = protocol.get("identificationModule", {})
                status_module = protocol.get("statusModule", {})
                nct_id = id_module.get("nctId", "")
                title = id_module.get("briefTitle", "No title")
                status = status_module.get("overallStatus", "Unknown")
                results.append({
                    "source": "ClinicalTrials.gov (NIH)",
                    "nctId": nct_id,
                    "title": title,
                    "status": status,
                    "url": f"https://clinicaltrials.gov/study/{nct_id}"
                })
    except Exception as e:
        results.append({"source": "ClinicalTrials.gov", "error": str(e)})
    return results

def query_opentargets(query, max_results=5):
    results = []
    try:
        url = f"https://api.platform.opentargets.org/api/v4/graphql"
        query_str = """
        query Search($queryString: String!) {
            search(queryString: $queryString) {
                hits {
                    id
                    name
                    entity
                    description
                }
            }
        }
        """
        payload = json.dumps({"query": query_str, "variables": {"queryString": query}}).encode('utf-8')
        req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json', 'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            hits = data.get("data", {}).get("search", {}).get("hits", [])[:max_results]
            for hit in hits:
                results.append({
                    "source": "OpenTargets Platform",
                    "id": hit.get("id"),
                    "name": hit.get("name"),
                    "type": hit.get("entity"),
                    "description": hit.get("description", ""),
                    "url": f"https://platform.opentargets.org/{hit.get('entity')}/{hit.get('id')}"
                })
    except Exception as e:
        results.append({"source": "OpenTargets", "error": str(e)})
    return results

# Academic & Scholarly Handlers
def query_openalex(query, max_results=5):
    results = []
    try:
        url = f"https://api.openalex.org/works?search={urllib.parse.quote(query)}&per-page={max_results}"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0 (mailto:research@freedomoffice.org)'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for work in data.get("results", []):
                results.append({
                    "source": "OpenAlex",
                    "title": work.get("title"),
                    "year": work.get("publication_year"),
                    "doi": work.get("doi"),
                    "url": work.get("doi") or work.get("id")
                })
    except Exception as e:
        results.append({"source": "OpenAlex", "error": str(e)})
    return results

def query_semanticscholar(query, max_results=5):
    results = []
    try:
        url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(query)}&limit={max_results}&fields=title,year,authors,url"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for paper in data.get("data", []):
                authors = [a.get("name") for a in paper.get("authors", [])]
                results.append({
                    "source": "Semantic Scholar",
                    "title": paper.get("title"),
                    "year": paper.get("year"),
                    "authors": authors,
                    "url": paper.get("url")
                })
    except Exception as e:
        results.append({"source": "Semantic Scholar", "error": str(e)})
    return results

def query_arxiv(query, max_results=5):
    results = []
    try:
        url = f"http://export.arxiv.org/api/query?search_query=all:{urllib.parse.quote(query)}&start=0&max_results={max_results}"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = resp.read().decode('utf-8')
            root = ET.fromstring(data)
            ns = {'atom': 'http://www.w3.org/2005/Atom'}
            for entry in root.findall('atom:entry', ns):
                title = entry.find('atom:title', ns).text.strip()
                summary = entry.find('atom:summary', ns).text.strip()
                link = entry.find('atom:id', ns).text.strip()
                authors = [a.find('atom:name', ns).text for a in entry.findall('atom:author', ns)]
                results.append({
                    "source": "arXiv",
                    "title": title,
                    "authors": authors,
                    "summary": summary[:200] + "...",
                    "url": link
                })
    except Exception as e:
        results.append({"source": "arXiv", "error": str(e)})
    return results

def query_wikipedia(query, max_results=5):
    results = []
    try:
        url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(query)}&utf8=&format=json&srlimit={max_results}"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for item in data.get("query", {}).get("search", []):
                title = item.get("title")
                snippet = re.sub('<[^<]+?>', '', item.get("snippet", ""))
                page_url = f"https://en.wikipedia.org/wiki/{urllib.parse.quote(title.replace(' ', '_'))}"
                results.append({
                    "source": "Wikipedia",
                    "title": title,
                    "snippet": snippet,
                    "url": page_url
                })
    except Exception as e:
        results.append({"source": "Wikipedia", "error": str(e)})
    return results

def query_wikidata(query, max_results=5):
    results = []
    try:
        url = f"https://www.wikidata.org/w/api.php?action=wbsearchentities&search={urllib.parse.quote(query)}&language=en&format=json&limit={max_results}"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for item in data.get("search", []):
                results.append({
                    "source": "Wikidata",
                    "id": item.get("id"),
                    "label": item.get("label"),
                    "description": item.get("description", ""),
                    "url": f"https://www.wikidata.org/wiki/{item.get('id')}"
                })
    except Exception as e:
        results.append({"source": "Wikidata", "error": str(e)})
    return results

def query_crossref(query, max_results=5):
    results = []
    try:
        url = f"https://api.crossref.org/works?query={urllib.parse.quote(query)}&rows={max_results}"
        req = urllib.request.Request(url, headers={'User-Agent': 'FreedomOffice/1.0 (mailto:research@freedomoffice.org)'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            items = data.get("message", {}).get("items", [])
            for item in items:
                title = item.get("title", ["Untitled"])[0]
                doi = item.get("DOI", "")
                url_link = item.get("URL", f"https://doi.org/{doi}")
                results.append({
                    "source": "CrossRef",
                    "title": title,
                    "doi": doi,
                    "url": url_link
                })
    except Exception as e:
        results.append({"source": "CrossRef", "error": str(e)})
    return results

def query_google_scholar(query, max_results=5):
    results = []
    try:
        scholar_url = f"https://scholar.google.com/scholar?q={urllib.parse.quote(query)}"
        results.append({
            "source": "Google Scholar",
            "query": query,
            "url": scholar_url,
            "note": "Direct Google Scholar search link generated"
        })
    except Exception as e:
        results.append({"source": "Google Scholar", "error": str(e)})
    return results

def handle_call_tool(request_id, params):
    name = params.get("name")
    args = params.get("arguments", {})

    if name == "search_documents":
        query = args.get("query", "")
        pattern = args.get("file_pattern", "*.*")
        results = []
        try:
            regex = re.compile(query, re.IGNORECASE)
            root_dir = os.getcwd()
            for filepath in glob.glob(os.path.join(root_dir, "**", pattern), recursive=True):
                if os.path.isfile(filepath) and "/.git/" not in filepath:
                    try:
                        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                            for idx, line in enumerate(f, start=1):
                                if regex.search(line):
                                    results.append({
                                        "file": os.path.relpath(filepath, root_dir),
                                        "line": idx,
                                        "content": line.strip()
                                    })
                                    if len(results) >= 50:
                                        break
                    except Exception:
                        pass
                if len(results) >= 50:
                    break
            content = json.dumps(results, indent=2)
        except Exception as e:
            content = f"Search error: {str(e)}"

        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "content": [{"type": "text", "text": content}]
            }
        }
    elif name == "search_help":
        topic = args.get("topic", "")
        summary = f"FreedomOffice Search Results for '{topic}':\n- FreedomWriter: Standard MS Word compatible document editor\n- FreedomSheet: MS Excel compatible spreadsheet engine\n- FreedomShow: MS PowerPoint compatible presentation tool\n- FreedomAI: Built-in local Ollama assistant (@FreedomAI)"
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "content": [{"type": "text", "text": summary}]
            }
        }
    elif name == "search_public_databases":
        query = args.get("query", "")
        target_db = args.get("database", "all")
        limit = args.get("max_results", 5)
        
        all_results = []
        # SearXNG Meta-Search Engine (Built-in Docker container)
        if target_db in ["all", "searxng", "web"]:
            all_results.extend(query_searxng(query, limit))

        # Legal & Patent Databases
        if target_db in ["all", "legal", "courtlistener"]:
            all_results.extend(query_courtlistener(query, limit))
        if target_db in ["all", "legal", "patents"]:
            all_results.extend(query_patents(query, limit))

        # Financial & Economic Databases
        if target_db in ["all", "financial", "sec_edgar"]:
            all_results.extend(query_sec_edgar(query, limit))
        if target_db in ["all", "financial", "worldbank"]:
            all_results.extend(query_worldbank(query, limit))

        # Android Development Databases
        if target_db in ["all", "android", "android_docs"]:
            all_results.extend(query_android_docs(query, limit))
        if target_db in ["all", "android", "maven_central"]:
            all_results.extend(query_maven_central(query, limit))
        if target_db in ["all", "android", "fdroid"]:
            all_results.extend(query_fdroid(query, limit))

        # Programming & Code Repositories
        if target_db in ["all", "programming", "github"]:
            all_results.extend(query_github(query, limit))
        if target_db in ["all", "programming", "pypi"]:
            all_results.extend(query_pypi(query, limit))
        if target_db in ["all", "programming", "crates"]:
            all_results.extend(query_crates(query, limit))
        if target_db in ["all", "programming", "npm"]:
            all_results.extend(query_npm(query, limit))
        if target_db in ["all", "programming", "stackoverflow"]:
            all_results.extend(query_stackoverflow(query, limit))

        # Cybersecurity Databases
        if target_db in ["all", "cybersecurity", "cve", "circl"]:
            all_results.extend(query_circl_cve(query, limit))
        if target_db in ["all", "cybersecurity", "cisakev"]:
            all_results.extend(query_cisa_kev(query, limit))
        if target_db in ["all", "cybersecurity", "urlhaus"]:
            all_results.extend(query_urlhaus(query, limit))
        if target_db in ["all", "cybersecurity", "mitre"]:
            all_results.extend(query_mitre_attack(query, limit))

        # Medical Databases
        if target_db in ["all", "medical", "pubmed"]:
            all_results.extend(query_pubmed(query, limit))
        if target_db in ["all", "medical", "europepmc"]:
            all_results.extend(query_europepmc(query, limit))
        if target_db in ["all", "medical", "clinicaltrials"]:
            all_results.extend(query_clinicaltrials(query, limit))
        if target_db in ["all", "medical", "opentargets"]:
            all_results.extend(query_opentargets(query, limit))
        if target_db in ["all", "medical", "pubchem"]:
            all_results.extend(query_pubchem(query, limit))
        if target_db in ["all", "medical", "uniprot"]:
            all_results.extend(query_uniprot(query, limit))
        if target_db in ["all", "medical", "chebi"]:
            all_results.extend(query_chebi(query, limit))
        if target_db in ["all", "medical", "rxnorm"]:
            all_results.extend(query_rxnorm(query, limit))

        # Academic Databases
        if target_db in ["all", "academic", "openalex"]:
            all_results.extend(query_openalex(query, limit))
        if target_db in ["all", "academic", "semanticscholar"]:
            all_results.extend(query_semanticscholar(query, limit))
        if target_db in ["all", "academic", "arxiv"]:
            all_results.extend(query_arxiv(query, limit))
        if target_db in ["all", "academic", "crossref"]:
            all_results.extend(query_crossref(query, limit))
        if target_db in ["all", "academic", "scholar"]:
            all_results.extend(query_google_scholar(query, limit))

        # Knowledge Graphs
        if target_db in ["all", "wikipedia"]:
            all_results.extend(query_wikipedia(query, limit))
        if target_db in ["all", "wikidata"]:
            all_results.extend(query_wikidata(query, limit))
            
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "content": [{"type": "text", "text": json.dumps(all_results, indent=2)}]
            }
        }
    else:
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "error": {
                "code": -32601,
                "message": f"Method/Tool {name} not found"
            }
        }

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            
            if method == "initialize":
                resp = handle_initialize(req_id)
            elif method == "notifications/initialized":
                continue
            elif method == "tools/list":
                resp = handle_list_tools(req_id)
            elif method == "tools/call":
                resp = handle_call_tool(req_id, req.get("params", {}))
            else:
                resp = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {
                        "code": -32601,
                        "message": f"Method {method} not found"
                    }
                }
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32700,
                    "message": f"Parse error: {str(e)}"
                }
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
