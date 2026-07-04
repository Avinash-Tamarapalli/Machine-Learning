from pathlib import Path
from dataclasses import dataclass


def _find_root(marker: str = "pyproject.toml") -> Path:
    """Walk up from this file until a directory containing `marker` is found."""
    for parent in Path(__file__).resolve().parents:
        if (parent / marker).exists():
            return parent
    raise RuntimeError(f"Project root (containing {marker}) not found")


# Project root — holds pyproject.toml and the data/ folder (resolved via marker search).
PROJECT_ROOT_PATH = _find_root()

# Package root — src/bank_marketing/, holds the bundled conf/ folder.
PACKAGE_ROOT_PATH = Path(__file__).resolve().parent.parent


@dataclass
class EntityDetails:
    path: str | Path
    format: str
    sep: str