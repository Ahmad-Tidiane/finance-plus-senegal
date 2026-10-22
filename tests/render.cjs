const fs=require('node:fs'), vm=require('node:vm'), assert=require('node:assert/strict');
const html=fs.readFileSync('dist/index.html','utf8');
const code=html.match(/<script>([\s\S]*)<\/script>/)[1];
function render(route,override='') {
 const elements=new Map();
 const stub=()=>({innerHTML:'',classList:{remove(){},toggle(){}},setAttribute(){},close(){},showModal(){}});
 for(const key of ['#nav','.menu','#main','.close','#modal'])elements.set(key,stub());
 const context={document:{querySelector:s=>elements.get(s)||null,querySelectorAll:()=>[],title:''},location:{hash:'#'+route},window:{scrollTo(){}},addEventListener(){},URL,setTimeout};
 vm.createContext(context);vm.runInContext(code,context);
 if(override)vm.runInContext(override+';render()',context);
 return elements.get('#main').innerHTML;
}
for(const route of ['accueil','apropos','produits','agences','actualites','credit','contact','documents','confidentialite','article-0'])assert.ok(render(route).length>200,route);
assert.ok(render('agences').includes('Agence de Dakar'));
const long=render('article-11','while(articles.length<12)articles.push(["Test","Douzième actualité","https://example.org/photo.jpg","Texte",false])');
assert.ok(long.includes('Douzième actualité'));
assert.ok(render('actualites','articles.length=0').includes('Aucune actualité publiée'));
assert.ok(!render('article-100').includes('undefined'));
assert.ok(!html.includes('@@'));
console.log('Rendu vérifié : pages, nouvelles agences, 12e article, liste vide et lien absent.');
