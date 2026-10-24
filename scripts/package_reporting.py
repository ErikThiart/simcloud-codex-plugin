#!/usr/bin/env python3
"""Validate and package the public reporting plugin, without runtime credentials."""
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'plugins/simcloud-reporting'
FILES = ['plugin.json', 'mcp.json', 'assets/simcloud.svg', 'skills/simcloud-reporting/SKILL.md']
manifest = json.loads((PLUGIN / 'plugin.json').read_text())
settings = manifest['extensions']['com.openai']
interface = settings['interface']
for field, limit in [('displayName', 30), ('shortDescription', 30), ('longDescription', 4000), ('developerName', 80)]:
    assert 0 < len(interface[field]) <= limit, field + ' is missing or too long'
for field in ['websiteURL', 'supportURL', 'privacyPolicyURL', 'termsOfServiceURL']:
    assert interface[field].startswith('https://simcloud.co.za/'), field
for prompt in interface['defaultPrompt']:
    assert 0 < len(prompt) <= 128
assert len(interface['defaultPrompt']) <= 3
for field in ['logo', 'composerIcon']:
    asset = interface[field]
    assert asset.startswith('./') and asset[2:] in FILES
    svg = ET.fromstring((PLUGIN / asset[2:]).read_text())
    _, _, width, height = map(float, svg.attrib['viewBox'].split())
    assert width == height and width >= 48
review = settings['review']
assert review['commerce'] is False
assert len(review['test_cases']['positive']) == 5
assert len(review['test_cases']['negative']) == 3
for case in review['test_cases']['positive']:
    assert all(case.get(field) for field in ['description', 'prompt', 'tools_triggered', 'expected_behavior'])
mcp = json.loads((PLUGIN / 'mcp.json').read_text())
assert len(mcp['mcpServers']) == 1
server = mcp['mcpServers']['simcloud-reporting']
assert server['type'] == 'streamable-http'
assert server['url'] == 'https://simcloud.co.za/api/reporting-mcp.php'
auth = server['extensions']['com.openai']['auth']
assert auth['type'] == 'oauth' and auth['client'] == {'mode': 'dcr'}
assert auth['resource'] == server['url']
assert auth['baseScopes'] == auth['defaultScopes'] == ['reports:read']
assert not any(key in json.dumps(mcp).lower() for key in ['clientsecret', 'authorization:', 'bearer '])
for file in FILES:
    assert (PLUGIN / file).is_file() and not (PLUGIN / file).is_symlink(), file
    assert not re.search(r'\[TODO|\[TBD|YOUR_API_TOKEN', (PLUGIN / file).read_text()), file
output = ROOT / 'dist' / ('simcloud-reporting-' + manifest['version'] + '.zip')
output.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
    for file in FILES:
        archive.write(PLUGIN / file, file)
with zipfile.ZipFile(output) as archive:
    assert sorted(archive.namelist()) == sorted(FILES)
    assert archive.testzip() is None
print('Package checks passed. Review account, live ChatGPT tests, video and portal review are separate requirements.')
print(output)
