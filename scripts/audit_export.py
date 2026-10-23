"""Audit the explicit source-only export; write a portable manifest under out/.
No Git repository is needed. Ignored outputs never enter the source manifest.
"""
from pathlib import Path
import argparse, hashlib, json, re
ROOT=Path(__file__).resolve().parents[1]
SOURCE_PATHS='.gitignore\n.env.example\nAGENTS.md\nREADME.md\nCONTRIBUTING.md\nLICENSE\nLICENSE-RECOMMENDATION.md\nTHIRD_PARTY_NOTICES.md\nVALIDATION.md\nRELEASE-READINESS.md\nconfig.example.json\npackage.json\npackage-lock.json\nrequirements.txt\nrequirements-tts.txt\ntsconfig.json\n.agents/skills/content-production/SKILL.md\nsrc/index.ts\nsrc/Root.tsx\nscripts/content.py\nscripts/render_video.mjs\nscripts/audit_export.py\ntests/smoke.py\nexamples/synthetic-demo.json\npublic/README.md\npublic/fonts/Vera.ttf\npublic/fonts/VeraBd.ttf\npublic/fonts/bitstream-vera-license.txt\ndocs/dependency-licenses.json'.splitlines()
SKIP={'out','node_modules','.venv','.local','__pycache__','.git','content','research','models'}

def audit(extra_patterns=()):
    findings=[];rows=[];allowed=set(SOURCE_PATHS)
    patterns=[('personal_absolute_path',r'(?i)(?:\b[A-Z]:[\\/](?!/)[A-Za-z0-9_-]+[\\/]|/(?:Users|home)/[A-Za-z0-9_.-]+/)'),('private_key',r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),('service_secret',r'\b(?:sk-[A-Za-z0-9]{24,}|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|AKIA[A-Z0-9]{16})\b'),('personal_social_profile',r'https?://(?:www\.)?linkedin\.com/in/[^\s)]+')]
    for rel in SOURCE_PATHS:
        p=ROOT/rel
        if not p.is_file():findings.append({'check':'missing_source','path':rel});continue
        data=p.read_bytes()
        if p.suffix!='.ttf':
            t=data.decode('utf-8')
            for label,pattern in patterns:
                if re.search(pattern,t):findings.append({'check':label,'path':rel})
            for term in extra_patterns:
                if term and term.casefold() in t.casefold():findings.append({'check':'private_material_match','path':rel})
        rows.append({'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
    for p in ROOT.rglob('*'):
        rel=p.relative_to(ROOT)
        if any(part in SKIP or part.startswith('.venv-') for part in rel.parts):continue
        if p.is_file() and rel.as_posix() not in allowed:findings.append({'check':'unlisted_file_not_exported','path':rel.as_posix()})
    ignores=(ROOT/'.gitignore').read_text().splitlines()
    for required in ['out/','node_modules/','.env','content/','models/','.local/']:
        if required not in ignores:findings.append({'check':'missing_ignore','path':required})
    pkg=json.loads((ROOT/'package.json').read_text())
    return {'result':'PASS' if not findings else 'FAIL','package_license':pkg.get('license','UNSPECIFIED'),'git_directory_present_but_never_exported':(ROOT/'.git').exists(),'source_files':rows,'total_source_bytes':sum(x['bytes'] for x in rows),'findings':findings,'excluded':'All out/, content, dependency trees, caches, models and private configuration are outside this explicit export list','limitations':'Pattern scans are heuristic; review code provenance, content and legal rights before any public release'}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--private-patterns-file',help='Optional local JSON array; contents never copied into reports');args=p.parse_args()
    terms=json.loads(Path(args.private_patterns_file).read_text(encoding='utf-8')) if args.private_patterns_file else []
    result=audit(terms);(ROOT/'out').mkdir(exist_ok=True);(ROOT/'out/source-manifest.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='source_files'},indent=2))
    raise SystemExit(0 if result['result']=='PASS' else 1)
