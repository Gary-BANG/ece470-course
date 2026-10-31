from pathlib import Path
import json,shutil
root=Path(__file__).resolve().parents[1]
m=json.loads((root/'content/manifest.json').read_text())
for l in m['lessons']:
 l['body']=(root/'content'/f'{l["id"]}.md').read_text()
 l['minutes']=max(5,round(len(l['body'])/220))
(root/'dist/course.js').write_text('const COURSE = '+json.dumps(m,ensure_ascii=False)+';\n')
for name in ['README.md','COURSE_MAP.md','UPDATE_COURSE_PROMPT.md']:
 if (root/name).exists():shutil.copy(root/name,root/'dist'/name)
print(f'Built {len(m["lessons"])} lessons, {sum(len(l["body"]) for l in m["lessons"])} characters')
