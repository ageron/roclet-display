import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('update_examples', Path(__file__).parents[1] / 'tools/update-examples.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class UpdateTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        module.ROOT = Path(temp.name)
        (module.ROOT / 'examples').mkdir()
        self.old = 'https://github.com/ageron/roclet-display/releases/download/0.4.0/Abc.tar.zst'
        self.paths = [module.ROOT / name for name in ['package-url.txt', 'README.md', 'examples/one.roc', 'examples/two.roc']]
        for path in self.paths:
            path.write_text(self.old + '\n')

    def test_complete_and_idempotent(self):
        expected = module.update('0.5.0', 'Def.tar.zst')
        for path in self.paths:
            self.assertEqual(path.read_text().strip(), expected)
        self.assertEqual(module.update('0.5.0', 'Def.tar.zst'), expected)

    def test_missing_pin_does_not_partially_update(self):
        self.paths[-1].write_text('no pin')
        before = [path.read_bytes() for path in self.paths]
        with self.assertRaises(ValueError):
            module.update('0.5.0', 'Def.tar.zst')
        self.assertEqual([path.read_bytes() for path in self.paths], before)

    def test_rejects_invalid_metadata(self):
        for version, archive in [('latest', 'Abc.tar.zst'), ('0.5.0', '../Abc.tar.zst')]:
            with self.assertRaises(ValueError):
                module.update(version, archive)


if __name__ == '__main__':
    unittest.main()
