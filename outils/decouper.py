#!/usr/bin/env python3
"""Découpe un enregistrement d'Estelle en un fichier par page.
Usage : python3 outils/decouper.py enregistrement.aac <id> "[fin_page0, fin_page1, ...]" [nom_fin]
La liste donne, pour chaque page, le numéro du DERNIER segment de cette page (voir transcrire.py).
Tout ce qui suit la dernière page devient la phrase de fin (nom_fin, par défaut : pas de fichier de fin)."""
import subprocess,sys,json,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from transcrire import pauses
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); A=os.path.join(R,'audio')
src,ident,fins=sys.argv[1],sys.argv[2],json.loads(sys.argv[3]); nom_fin=sys.argv[4] if len(sys.argv)>4 else None
S,dur=pauses(src); mid=lambda k:(S[k][0]+S[k][1])/2
pts=[max(0,S[0][1]-0.25)]+[mid(k+1) for k in fins]+[dur]
noms=[f'{ident}-{i}' for i in range(len(fins))]+([nom_fin] if nom_fin else [])
FILTRE='highpass=f=80,loudnorm=I=-16:TP=-1.5:LRA=11,afade=t=in:d=0.05,areverse,silenceremove=start_periods=1:start_threshold=-45dB,afade=t=in:d=0.08,areverse,apad=pad_dur=0.3'
for i,n in enumerate(noms):
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',src,'-ss',f'{pts[i]:.2f}','-to',f'{pts[i+1]:.2f}','-af',FILTRE,'-ac','1','-ar','44100','-b:a','96k',f'{A}/{n}.mp3'],check=True)
    print(n,f'{pts[i]:.2f}-{pts[i+1]:.2f}')
