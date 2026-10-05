#!/usr/bin/env node
/* Demir Ağlar dil kontrolü.
   Kullanım:  npm i --no-save acorn acorn-walk && node tools/i18n-check.js
   1) _t('…') ve _t`…` ile sarılmış ama İngilizce sözlükte (EN_DICT) olmayan metinleri listeler.
   2) Türkçe görünen ama _t ile sarılmamış metinleri listeler (yeni eklenen metni sarmayı unutma).
   Yeni metin eklerken: metni _t ile sar, sonra EN_DICT'e "Türkçe": "English" çiftini ekle. */
const fs=require('fs'),path=require('path');
const acorn=require('acorn'),walk=require('acorn-walk');
const html=fs.readFileSync(path.join(__dirname,'..','index.html'),'utf8');
const D=JSON.parse(html.match(/const EN_DICT=(\{.*?\});\n/)[1]);
const scripts=[...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m=>m[1]);
const main=scripts.reduce((a,b)=>b.length>a.length?b:a);
const ast=acorn.parse(main,{ecmaVersion:2022});
const tkey=q=>q.quasis.map((x,i)=>x.value.cooked+(i<q.expressions.length?'{'+i+'}':'')).join('');
const missing=new Set(),unwrapped=new Set(),wrapped=new Set();
walk.full(ast,n=>{
  if(n.type==='TaggedTemplateExpression'&&n.tag.name==='_t'){wrapped.add(n.quasi.start);const k=tkey(n.quasi);if(!(k in D))missing.add(k)}
  if(n.type==='CallExpression'&&n.callee.name==='_t'&&n.arguments[0]&&n.arguments[0].type==='Literal'){wrapped.add(n.arguments[0].start);const k=n.arguments[0].value;if(!(k in D))missing.add(k)}});
const TR=/[çğıöşüÇĞİÖŞÜ]/,IGNORE=new Set(['DİL: TR','Türkçe için dokun']);
walk.full(ast,n=>{let k=null;if(n.type==='Literal'&&typeof n.value==='string')k=n.value;if(n.type==='TemplateLiteral')k=tkey(n);
  if(k==null||wrapped.has(n.start)||IGNORE.has(k))return;const v=k.replace(/<[^>]*>/g,' ');if(TR.test(v)&&/\s/.test(v.trim()))unwrapped.add(k.slice(0,140))});
const same=[...missing].filter(k=>!/[A-Za-zçğıöşüÇĞİÖŞÜ]{2}/.test(k.replace(/<[^>]*>/g,'')));
for(const k of same)missing.delete(k);
console.log(`Sözlükte ${Object.keys(D).length} metin.`);
console.log(`\nSözlükte olmayan sarılı metin: ${missing.size}`);for(const k of missing)console.log('  '+JSON.stringify(k));
console.log(`\nSarılmamış Türkçe metin: ${unwrapped.size}`);for(const k of unwrapped)console.log('  '+JSON.stringify(k));
process.exit(missing.size||unwrapped.size?1:0);
