# Les histoires de Pistache

Appli d'histoires illustrées et racontées pour **Noa, 3 ans**, le neveu d'Estelle Lavenac (designer graphique, autrice du projet).
Elle est installable sur téléphone (PWA), fonctionne hors connexion et est publiée sur GitHub Pages :

- En ligne : https://estellelavenac.github.io/pistache/
- Dépôt : github.com/EstelleLavenac/pistache (branche `main`, publiée automatiquement à chaque push)
- Une copie existe aussi en artifact Claude (« Les histoires de Pistache »). Elle reprend les mêmes histoires mais lit avec la voix du navigateur. La version de référence est ce dépôt.

## Pour qui, et le ton

- Un enfant de 3 ans : phrases courtes, mots simples, onomatopées (HIC !, Flap, Miam), répétitions, fin douce et rassurante.
- Environ 10 à 11 pages par histoire, une ou deux phrases par page.
- Noa adore les dragons et les chiens sauveteurs.
- **Ne jamais utiliser de personnages protégés** (Pat' Patrouille, Disney, Pixar…), ni leurs noms ou signes distinctifs. On peut s'inspirer d'un *style* de rendu, jamais d'un personnage.

## Personnages (tous originaux)

| Personnage | Qui | Dessin (fonction dans `index.html`) |
|---|---|---|
| Pistache | petit dragon vert, gentil, crache des étincelles ou des bulles | `dragon(x,y,échelle,{yeux:'fermes',flamme,ailes,hoquet})` |
| Biscotte | chienne sauveteuse, casque rouge | `chienne(x,y,é,{casque})` |
| Le chaton | petit chat gris | `chaton(x,y,é)` |
| Noa | 3 ans, cheveux bruns, t-shirt jaune, cartable rouge | `garcon(x,y,é,{cartable,bras,content})` |
| Lia | 6 ans, cousine de Noa, fille d'Estelle, couettes, robe rose | `fille(x,y,é,{bras,fraise})` |
| Tata Estelle | cheveux longs châtains, haut turquoise, dessine | `tata(x,y,é,{carnet,bras})` |

Décors disponibles : `fond(ciel,sol)`, `soleil()`, `couchant(x)`, `lune()`, `etoiles()`, `nuage()`, `arbre()`, `maison()`, `ecole()`, `classe()`, `table()`, `cabane()`, `piquenique()`, `gateau(x,y,bougies)`, `ballon()`, `lit()`, `couverture()`, `flaque()`, `bulles()`.

## Style visuel

C'est un rendu « film d'animation », dessiné en SVG. Les dégradés (`DEFS`) donnent du volume, le filtre `volume` ajoute une ombre portée et `gRim` une lumière de contour. Les yeux, dessinés par `oeil()`, ont de grands iris, un reflet et des sourcils. Pistache a des écailles (`ecailles`). La scène fait 640×400 et le sol se situe vers y=300–330.
Après toute modification des dessins, vérifie le rendu avec `outils/apercu.py`.

## Les histoires (ordre de l'appli)

`noa` Noa va à l'école · `lia` La journée chez tata Estelle · `hoquet` Pistache a le hoquet · `chaton` Au secours, petit chaton ! · `gateau` Le gâteau de Biscotte · `dodo` Bonne nuit, Pistache.

Elles sont définies dans `HISTOIRES` (dans `index.html`), sous la forme `[texte, ()=>scène]` pour chaque page.

## Voix

- **Toutes les histoires sont lues par Estelle** (fichiers `audio/<id>-<page>.mp3`). Ne jamais les écraser par la voix de synthèse.
- Phrases de fin : `audio/fin.mp3`, `noa-fin.mp3` et `dodo-fin.mp3` (« Fin, bravo ! Tu as écouté toute l'histoire, Noa ! »).
- Si le fichier audio manque, l'appli se rabat sur la voix du navigateur.
- Le clonage de voix n'est pas possible ici. Estelle s'enregistre elle-même : un fichier par histoire, au dictaphone de son téléphone.

## Marches à suivre

Commence par préparer les outils : `bash outils/installer.sh`, qui télécharge les voix et la transcription dans `.outils/`.

**Ajouter ou modifier une histoire**
1. Écris ou modifie l'entrée dans `HISTOIRES`, en réutilisant les personnages et les décors existants.
2. Vérifie le rendu avec `python3 outils/apercu.py <id> /tmp/apercu.png`, puis regarde l'image.
3. En attendant l'enregistrement d'Estelle, génère une voix provisoire avec `python3 outils/voix_synthese.py <id>`.
4. Mets en ligne (voir plus bas).

**Intégrer un enregistrement d'Estelle**
1. Lance `python3 outils/transcrire.py fichier.aac`, qui liste les segments avec leur texte. La transcription est approximative : fie-toi au sens.
2. Repère le dernier segment de chaque page. Les bruits isolés, souvent des onomatopées, se rattachent à la page voisine.
3. Lance `python3 outils/decouper.py fichier.aac <id> "[seg_fin_p0, seg_fin_p1, …]" fin`. Le dernier argument est facultatif : il sert à remplacer la phrase de fin.
4. Vérifie quelques pages en retranscrivant les mp3 produits, puis mets en ligne.

**Mettre en ligne**
1. Lance `python3 outils/maj_cache.py`, qui liste les audios et change la version du cache, sinon les téléphones gardent l'ancienne version.
2. Lance `git add -A && git commit && git push`.
3. GitHub Pages republie en 1 à 2 minutes. Sur le téléphone, il suffit de fermer et rouvrir l'appli.
4. Si l'artifact Claude existe, applique-lui les mêmes modifications d'histoires et de dessins.

Pour régénérer l'icône après un changement de Pistache : `python3 outils/icones.py`.
