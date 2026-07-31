#!/usr/bin/env python3
"""
check_links.py — verificador de integridade do site Recanto das Seriemas.

Dois modos:

  --repo   (padrao) Confere se TODO caminho local referenciado no HTML
           existe de fato no repositorio. Roda em segundos, sem rede.
           E o modo que teria pego o commit a9d931e ANTES do deploy.

  --live   Bate HTTP no site publicado e confere status 200.
           Roda apos o deploy e semanalmente.

Saida: relatorio legivel + exit code 1 se houver qualquer quebra.
"""

import argparse
import os
import re
import sys
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "https://recantodasseriemas.com.br"
TIMEOUT = 25
UA = "Mozilla/5.0 (compatible; RecantoLinkCheck/1.0)"

ATTR_RE = re.compile(r'(?:src|href|content|data-src)\s*=\s*"([^"]+)"', re.I)
SRCSET_RE = re.compile(r'srcset\s*=\s*"([^"]+)"', re.I)
CSSURL_RE = re.compile(r'url\(\s*[\'"]?([^\'")]+)[\'"]?\s*\)', re.I)
META_REFRESH_RE = re.compile(r'^\s*\d+\s*;\s*url\s*=\s*(.+)$', re.I)
EXT_RE = re.compile(r"\.(html|jpe?g|png|webp|gif|svg|ico|css|js|mp4|pdf|xml|txt)$", re.I)

SKIP_PREFIX = ("http://", "https://", "//", "mailto:", "tel:", "#",
               "data:", "javascript:", "whatsapp:")


def html_files(root):
    return sorted(
        os.path.join(dp, f)
        for dp, _, fs in os.walk(root)
        for f in fs
        if f.endswith(".html") and ".git" not in dp
    )


def extract_refs(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        html = fh.read()

    refs = set(ATTR_RE.findall(html))
    refs |= set(CSSURL_RE.findall(html))
    for ss in SRCSET_RE.findall(html):
        for part in ss.split(","):
            cand = part.strip().split(" ")[0]
            if cand:
                refs.add(cand)

    out = set()
    for r in refs:
        r = r.strip()
        m = META_REFRESH_RE.match(r)          # <meta http-equiv=refresh content="0; url=x.html">
        if m:
            r = m.group(1).strip().strip('\'"')
        if not r or r.lower().startswith(SKIP_PREFIX):
            continue
        if not EXT_RE.search(r):
            continue
        out.add(r.split("?")[0].split("#")[0].lstrip("/"))
    return out


def check_repo(root):
    problems = []
    total = 0

    on_disk = set()
    for dp, _, fs in os.walk(root):
        if ".git" in dp:
            continue
        for f in fs:
            on_disk.add(os.path.relpath(os.path.join(dp, f), root))
    lower_index = {p.lower(): p for p in on_disk}

    for page in html_files(root):
        rel_page = os.path.relpath(page, root)
        for ref in sorted(extract_refs(page)):
            total += 1
            if ref in on_disk:
                continue
            match = lower_index.get(ref.lower())
            if match:
                problems.append((rel_page, ref, f"CAIXA ERRADA -> arquivo real e '{match}'"))
            else:
                problems.append((rel_page, ref, "ARQUIVO NAO EXISTE NO REPO"))
    return total, problems


def head(url):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return f"ERRO: {type(e).__name__}"


def check_live(root):
    urls = {f"{BASE_URL}/", f"{BASE_URL}/robots.txt", f"{BASE_URL}/sitemap.xml"}
    for page in html_files(root):
        urls.add(f"{BASE_URL}/{os.path.relpath(page, root)}")
        for ref in extract_refs(page):
            urls.add(f"{BASE_URL}/{ref}")

    urls = sorted(urls)
    with ThreadPoolExecutor(max_workers=12) as ex:
        codes = list(ex.map(head, urls))
    return len(urls), [(u, c) for u, c in zip(urls, codes) if c != 200]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="checar o site publicado")
    ap.add_argument("--root", default=".", help="raiz do repositorio")
    args = ap.parse_args()
    root = os.path.abspath(args.root)

    if args.live:
        total, problems = check_live(root)
        print(f"MODO LIVE — {total} URLs verificadas em {BASE_URL}\n")
        if not problems:
            print("OK: nenhuma URL quebrada.")
            return 0
        print(f"FALHA: {len(problems)} URL(s) fora do ar:\n")
        for u, c in problems:
            print(f"  [{c}]  {u}")
        return 1

    total, problems = check_repo(root)
    print(f"MODO REPO — {total} referencias locais verificadas\n")
    if not problems:
        print("OK: todo arquivo referenciado existe no repositorio.")
        return 0
    print(f"FALHA: {len(problems)} referencia(s) quebrada(s):\n")
    for page, ref, why in problems:
        print(f"  {page}\n      -> {ref}\n         {why}")
    print("\nNao faca deploy com essas quebras. Restaure os arquivos ou corrija o caminho.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
