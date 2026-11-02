import json
import tempfile
import unittest
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class WebsiteRegistryTests(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads((ROOT / 'capability-manifest.json').read_text())
        self.skill = next(c for c in self.manifest['capabilities'] if c['id'] == 'website-bauen')

    def test_unique_external_reference_and_status_boundaries(self):
        ids = [c['id'] for c in self.manifest['capabilities']]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(self.skill['source']['upstream_commit']), 40)
        self.assertEqual(len(self.skill['source']['skill_sha256']), 64)
        self.assertFalse((ROOT / 'skills/website-bauen').exists())
        for host in ('claude_local', 'claude_cloud'):
            self.assertEqual(self.skill['platforms'][host]['status'], 'unverified')
        self.assertEqual(self.skill['platforms']['chatgpt']['status'], 'available-session-verified')
        for host in self.skill['platforms'].values():
            self.assertIn(host['status'], self.manifest['status_definitions'])

    def test_build_preserves_existing_packages_without_duplicate_install(self):
        with tempfile.TemporaryDirectory() as output:
            subprocess.run(['python', str(ROOT / 'scripts/build_skill_packages.py'),
                            '--target', 'all', '--output', output], check=True)
            for host in ('claude', 'chatgpt'):
                names = {p.name for p in (Path(output) / host).iterdir()}
                self.assertEqual(names, {'ppao-candidate', 'token-optimization'})
            ppao = (Path(output) / 'claude/ppao-candidate/SKILL.md').read_text()
            self.assertIn('disable-model-invocation: true', ppao)

    def test_rule_and_runtime_cases_remain_linked(self):
        rule = (ROOT.parent / self.skill['integration']['rule']).read_text()
        self.assertIn('skills: [website-bauen]', rule)
        self.assertIn('Blocker', rule)
        matrix = (ROOT.parent / self.skill['integration']['verification']).read_text()
        for case in ('Explizit', 'Automatisch', 'Änderung', 'Optimierung',
                     'Negativ', 'Agent', 'Fehlt', 'Persistenz'):
            self.assertIn('| ' + case + ' |', matrix)


if __name__ == '__main__':
    unittest.main()
