"""Make backend imports and temporary test databases work from the repository root."""
import shutil
import sys
import uuid
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO_ROOT / "backend"))


@pytest.fixture
def tmp_path():
    """Use a unique workspace-local directory in restricted Windows environments."""
    path = _REPO_ROOT / ".test-tmp" / uuid.uuid4().hex
    path.mkdir(parents=True)
    try:
        yield path
    finally:
        shutil.rmtree(path, ignore_errors=True)
