const CACHE='pistache-v4';
const FICHIERS=['./','index.html','manifest.webmanifest','icons/icon-192.png','icons/icon-512.png','icons/apple-touch-icon.png','audio/chaton-0.mp3','audio/chaton-1.mp3','audio/chaton-2.mp3','audio/chaton-3.mp3','audio/chaton-4.mp3','audio/chaton-5.mp3','audio/chaton-6.mp3','audio/chaton-7.mp3','audio/chaton-8.mp3','audio/chaton-9.mp3','audio/dodo-0.mp3','audio/dodo-1.mp3','audio/dodo-2.mp3','audio/dodo-3.mp3','audio/dodo-4.mp3','audio/dodo-5.mp3','audio/dodo-6.mp3','audio/dodo-7.mp3','audio/dodo-8.mp3','audio/dodo-9.mp3','audio/fin.mp3','audio/gateau-0.mp3','audio/gateau-1.mp3','audio/gateau-2.mp3','audio/gateau-3.mp3','audio/gateau-4.mp3','audio/gateau-5.mp3','audio/gateau-6.mp3','audio/gateau-7.mp3','audio/gateau-8.mp3','audio/gateau-9.mp3','audio/hoquet-0.mp3','audio/hoquet-1.mp3','audio/hoquet-10.mp3','audio/hoquet-2.mp3','audio/hoquet-3.mp3','audio/hoquet-4.mp3','audio/hoquet-5.mp3','audio/hoquet-6.mp3','audio/hoquet-7.mp3','audio/hoquet-8.mp3','audio/hoquet-9.mp3','audio/noa-0.mp3','audio/noa-1.mp3','audio/noa-10.mp3','audio/noa-2.mp3','audio/noa-3.mp3','audio/noa-4.mp3','audio/noa-5.mp3','audio/noa-6.mp3','audio/noa-7.mp3','audio/noa-8.mp3','audio/noa-9.mp3'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(FICHIERS)));self.skipWaiting();});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(n=>n!==CACHE).map(n=>caches.delete(n)))));self.clients.claim();});
self.addEventListener('fetch',e=>{
  if(e.request.method!=='GET') return;
  e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request).then(res=>{
    const copie=res.clone(); caches.open(CACHE).then(c=>c.put(e.request,copie)); return res;
  }).catch(()=>caches.match('index.html'))));
});
