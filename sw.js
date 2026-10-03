const CACHE='demir-aglar-v2';
const CORE=['./','./index.html','./vitrin-2026.html','./manifest.json','./icons/icon-192.png','./icons/icon-512.png',
 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js',
 'https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>Promise.all(CORE.map(u=>c.add(new Request(u,{mode:u.startsWith('http')?'cors':'same-origin'})).catch(()=>{})))).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k.startsWith('demir-aglar-')&&k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
const OK=u=>u.origin===self.location.origin||/cdnjs\.cloudflare\.com|cdn\.jsdelivr\.net|fonts\.(googleapis|gstatic)\.com/.test(u.host);
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET')return;const u=new URL(r.url);if(!OK(u))return;
  const net=fetch(r).then(res=>{if(res&&res.status===200){const cp=res.clone();return caches.open(CACHE).then(c=>c.put(r,cp)).then(()=>res)}return res});
  e.respondWith(caches.match(r).then(hit=>hit||net).catch(()=>r.mode==='navigate'?caches.match('./index.html'):Response.error()));
  e.waitUntil(net.catch(()=>{}))});
