#!/usr/bin/env python3
import json, sys
sys.path.insert(0, '/workspace/regbuild')
from common import build
import content_a, content_b

cities = set(json.load(open('/tmp/cities.json')))
META = {**content_a.META, **content_b.META}
CONTENT = {**content_a.CONTENT, **content_b.CONTENT}
for key in META:
    r = dict(META[key]); r.update(CONTENT[key])
    build(key, r, cities)
