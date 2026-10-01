#!/usr/bin/env python3
"""À lancer avant chaque mise en ligne : liste tous les audios dans sw.js et change la version du cache,
pour que les téléphones récupèrent la nouvelle version."""
import os,re
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(R,'sw.js'); w=open(p).read(); aud=sorted(os.listdir(os.path.join(R,'audio')))
v=int(re.search(r"pistache-v(\d+)",w).group(1))+1
w=re.sub(r"pistache-v\d+",f"pistache-v{v}",w)
w=re.sub(r"'icons/apple-touch-icon.png',.*?\];","'icons/apple-touch-icon.png',"+",".join(f"'audio/{a}'" for a in aud)+"];",w,flags=re.S)
open(p,'w').write(w); print('cache',v,'-',len(aud),'audios')
