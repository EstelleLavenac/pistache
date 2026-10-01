#!/usr/bin/env python3
"""Génère la voix de synthèse (audio/<id>-<page>.mp3) pour les histoires indiquées.
Usage : python3 outils/voix_synthese.py noa lia   (sans argument : aucune, par sécurité)
Attention : écrase les fichiers. Ne pas l'utiliser sur une histoire lue par Estelle."""
import re,subprocess,sys,os
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); T=os.path.join(R,'.outils'); A=os.path.join(R,'audio')
ids=sys.argv[1:]
if not ids: sys.exit(__doc__)
src=open(os.path.join(R,'index.html')).read()
for blk in re.finditer(r"\{id:'(\w+)'.*?pages:\[(.*?)\n  \]\}",src,re.S):
    if blk.group(1) not in ids: continue
    for i,t in enumerate(re.findall(r"\['(.*?)',\(\)=>",blk.group(2))):
        n=f"{blk.group(1)}-{i}"; t=t.replace('«','').replace('»','').replace('’',"'")
        subprocess.run([f'{T}/sherpa/bin/sherpa-onnx-offline-tts',f'--vits-model={T}/voix-fr/fr_FR-siwis-medium.onnx',f'--vits-tokens={T}/voix-fr/tokens.txt',f'--vits-data-dir={T}/voix-fr/espeak-ng-data','--vits-length-scale=1.2','--vits-noise-scale=0.6',f'--output-filename=/tmp/{n}.wav',t],capture_output=True,check=True)
        subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'/tmp/{n}.wav','-af','apad=pad_dur=0.3','-ac','1','-b:a','64k',f'{A}/{n}.mp3'],check=True)
        print(n)
