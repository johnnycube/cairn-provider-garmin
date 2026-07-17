"""Put the worker package on sys.path so `import cairn_garmin` resolves in tests.
cairn_garmin/__init__.py then bootstraps the generated proto stubs.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
