#!/usr/bin/env python3
"""Repère les pauses d'un enregistrement et transcrit chaque phrase, pour savoir où couper.
Usage : python3 outils/transcrire.py enregistrement.aac
Affiche : numéro de segment, début-fin, texte reconnu (approximatif)."""
import subprocess,sys,re,os
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); T=os.path.join(R,'.outils')
src=sys.argv[1]
def pauses(src):
    o=subprocess.run(['ffmpeg','-i',src,'-af','silencedetect=noise=-30dB:d=0.45','-f','null','-'],capture_output=True,text=True).stderr
    st=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',o)]; en=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',o)]
    dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src],capture_output=True,text=True).stdout)
    S=list(zip(st,en))
    if not S or S[0][0]>0.3: S.insert(0,(0,0))
    if S[-1][1]<dur-0.3: S.append((dur,dur))
    return S,dur
if __name__=='__main__':
    S,dur=pauses(src); print('durée',round(dur,2))
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',src,'-ar','16000','-ac','1','/tmp/tr.wav'])
    for i in range(len(S)-1):
        a=max(0,S[i][1]-0.1); b=S[i+1][0]+0.1
        subprocess.run(['ffmpeg','-y','-loglevel','error','-i','/tmp/tr.wav','-ss',str(a),'-to',str(b),'/tmp/seg.wav'])
        o=subprocess.run([f'{T}/sherpa/bin/sherpa-onnx-offline',f'--whisper-encoder={T}/whisper/small-encoder.int8.onnx',f'--whisper-decoder={T}/whisper/small-decoder.int8.onnx','--whisper-language=fr',f'--tokens={T}/whisper/small-tokens.txt','/tmp/seg.wav'],capture_output=True,text=True)
        t=re.findall(r'"text": *"([^"]*)"',o.stdout+o.stderr)
        print(i,f'{a:.2f}-{b:.2f}',t[0] if t else '?')
