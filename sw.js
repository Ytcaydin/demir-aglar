const CACHE='demir-aglar-v4';
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
/* hatırlatma bildirimi: oyun kurulu bir uygulamaysa tarayıcı bunu birkaç saatte bir çalıştırır */
const STATE_URL=new URL('./__state',self.location).href;
async function remind(){const c=await caches.open('da-state');const r=await c.match(STATE_URL);if(!r)return;let s;try{s=await r.json()}catch(e){return}
  if(!s.on||!s.lastSeen||Notification.permission!=='granted')return;const now=Date.now(),el=now-s.lastSeen;if(el<8*3600e3)return;if(s.nAt&&s.nAt>s.lastSeen&&now-s.nAt<24*3600e3)return;
  const g=Math.round((s.net||0)*Math.min(el/300000,96)*0.8),d=new Date(),today=`${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;
  const en=s.lang==='en';
  const body=en?(g>0?`Your trains kept running while you were away: +${g.toLocaleString('en-US')}k ₺ is waiting in your cash.`:'Your trains are waiting. Keep growing your network!')+(s.day!==today?' Your daily reward is ready too.':'')
    :(g>0?`Sen yokken trenler çalıştı: kasada +${g.toLocaleString('tr-TR')} bin ₺ seni bekliyor.`:'Trenlerin seni bekliyor. Ağını büyütmeye devam et!')+(s.day!==today?' Günlük ödülün de hazır.':'');
  await self.registration.showNotification('Demir Ağlar',{body,icon:'icons/icon-192.png',badge:'icons/icon-192.png',tag:'da-remind',lang:en?'en':'tr'});
  s.nAt=now;await c.put(STATE_URL,new Response(JSON.stringify(s),{headers:{'Content-Type':'application/json'}}))}
self.addEventListener('periodicsync',e=>{if(e.tag==='da-remind')e.waitUntil(remind().catch(()=>{}))});
self.addEventListener('notificationclick',e=>{e.notification.close();e.waitUntil(self.clients.matchAll({type:'window',includeUncontrolled:true}).then(L=>{for(const w of L)if('focus' in w)return w.focus();return self.clients.openWindow('./')}))});
