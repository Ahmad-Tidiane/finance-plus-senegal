"""Build the static site from CMS content using only the Python standard library."""
from pathlib import Path
import html,json,re
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parent

def read(name):return json.loads((ROOT/'content'/name).read_text())
def text(value):
 if not isinstance(value,str):raise ValueError('Un champ texte doit contenir du texte')
 return html.escape(value,quote=True).replace('`','&#96;').replace('$','&#36;').replace('\\','&#92;')
def image(value):
 if not isinstance(value,str):raise ValueError('Image invalide')
 if not (value.startswith('/finance-plus-senegal/media/') or (urlparse(value).scheme=='https' and urlparse(value).netloc)):
  raise ValueError('Les images doivent être en HTTPS ou dans /finance-plus-senegal/media/')
 return text(value)
def required(obj,keys):
 for k in keys:
  if not isinstance(obj.get(k),str) or not obj[k].strip():raise ValueError('Champ obligatoire manquant : '+k)

def build():
 s=(ROOT/'src/template.html').read_text()
 for section in ['accueil','apropos','contact','general','agences']:
  data=read(section+'.json')
  for key in re.findall(r'@@'+section+r'\.([a-z0-9_]+)@@',s):
   if key not in data:raise ValueError('Champ manquant : '+section+'.'+key)
   # Tokens occur inside both HTML and JavaScript strings. Encode special characters
   # as HTML entities and escape newlines for JavaScript string syntax.
   s=s.replace('@@'+section+'.'+key+'@@',text(data[key]).replace('\r','').replace('\n','\\n'))
 pics=read('images.json');pics={k:image(pics[k]) for k in ['hero','team','business','plant','mobile']}
 products=read('produits.json')
 details=[]
 for p in products['items']:
  required(p,['title','category','description'])
  if p['category'] not in ['Comptes','Crédits','Digital']:raise ValueError('Catégorie produit invalide')
  details.append([text(p[k]) for k in ['title','category','description']])
 featured=[]
 for p in products['featured']:
  required(p,['icon','title','description','category'])
  featured.append([text(p[k]) for k in ['icon','title','description','category']])
 articles=[]
 for path in sorted((ROOT/'content/actualites').glob('*.json')):
  a=json.loads(path.read_text())
  if a.get('published') is not True:continue
  required(a,['title','category','image','body'])
  articles.append((float(a.get('order',10)),path.name,[text(a['category']),text(a['title']),image(a['image']),text(a['body']),a.get('demo') is True]))
 articles=[x[2] for x in sorted(articles,key=lambda x:(x[0],x[1]))]
 agencies=[]
 for a in read('agences.json')['items']:
  required(a,['name','city','address','phone','hours','mapquery'])
  agencies.append({**{k:text(a[k]) for k in ['name','city','address','phone','hours','mapquery']},'demo':a.get('demo') is True})
 for token,value in [('PICS',pics),('PRODUCTS',featured),('DETAILS',details),('ARTICLES',articles),('AGENCIES',agencies)]:
  s=s.replace('__'+token+'__',json.dumps(value,ensure_ascii=False).replace('<','\\u003c').replace('\u2028','\\u2028').replace('\u2029','\\u2029'))
 if '@@' in s:raise ValueError('Un champ de contenu n’a pas été remplacé')
 (ROOT/'dist').mkdir(exist_ok=True)
 (ROOT/'dist/index.html').write_text(s)
 print('Site généré :',len(details),'produits,',len(agencies),'agences,',len(articles),'actualités publiées.')
if __name__=='__main__':build()
