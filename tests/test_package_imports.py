import importlib
import unittest


class PackageImportsTest(unittest.TestCase):
    def test_agent_and_shared_packages_import(self):
        modules = [
            "bas.agents.a1_onboarding",
            "bas.agents.a2_ledger",
            "bas.agents.a3_bas_preparation",
            "bas.agents.a4_compliance",
            "bas.agents.a5_lodgment",
            "bas.shared",
            "bas.supervisor",
        ]
        for module in modules:
            with self.subTest(module=module):
                importlib.import_module(module)


if __name__ == "__main__":
    unittest.main()
