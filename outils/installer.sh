#!/bin/bash
# Télécharge les moteurs hors ligne (voix française + transcription) dans .outils/ (non versionné).
set -e
cd "$(dirname "$0")/.." && mkdir -p .outils && cd .outils
V=v1.13.8
[ -d sherpa ] || { curl -sSL -o b.tar.bz2 "https://github.com/k2-fsa/sherpa-onnx/releases/download/$V/sherpa-onnx-$V-linux-x64-shared.tar.bz2" && tar xjf b.tar.bz2 && mv sherpa-onnx-$V-linux-x64-shared sherpa && rm b.tar.bz2; }
[ -d voix-fr ] || { curl -sSL -o v.tar.bz2 https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-fr_FR-siwis-medium.tar.bz2 && tar xjf v.tar.bz2 && mv vits-piper-fr_FR-siwis-medium voix-fr && rm v.tar.bz2; }
[ -d whisper ] || { curl -sSL -o w.tar.bz2 https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-whisper-small.tar.bz2 && tar xjf w.tar.bz2 && mv sherpa-onnx-whisper-small whisper && rm w.tar.bz2; }
echo "Outils prêts dans .outils/"
