#!/usr/bin/env python3
"""Planche d'aperçu des pages d'une histoire (PNG), pour vérifier les dessins.
Usage : python3 outils/apercu.py <id> sortie.png"""
import sys,pathlib
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parent.parent
ident,out=sys.argv[1],sys.argv[2]
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(); err=[]; pg.on('pageerror',lambda e:err.append(str(e)))
    pg.goto((R/'index.html').as_uri())
    k=pg.evaluate(f"HISTOIRES.findIndex(h=>h.id==='{ident}')"); n=pg.evaluate(f"HISTOIRES[{k}].pages.length")
    html='<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:3px">'+''.join(pg.evaluate(f"svg(HISTOIRES[{k}].pages[{i}][1]())") for i in range(n))+pg.evaluate(f"HISTOIRES[{k}].couverture()")+'</div>'
    p2=b.new_page(viewport={'width':1200,'height':800}); p2.set_content('<body style="margin:0">'+html); p2.screenshot(path=out,full_page=True)
    print('erreurs JS :',err or 'aucune'); b.close()
