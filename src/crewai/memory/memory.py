from pathlib import Path
from typing import Any, Dict, Optional

from crewai.memory.storage.interface import Storage
from crewai.utilities.paths import db_storage_path


def get_memory_paths(memory_path: Path | None = None) -> tuple[Path, Path, Path]:
    if not memory_path:
        memory_path = db_storage_path()

    long_term_memory_path = memory_path / "long_term_memory_storage.db"
    short_term_memory_path = memory_path
    entity_memory_path = memory_path
    return long_term_memory_path, short_term_memory_path, entity_memory_path


class Memory:
    """
    Base class for memory, now supporting agent tags and generic metadata.
    """

    def __init__(self, storage: Storage):
        self.storage = storage

    def save(
        self,
        value: Any,
        metadata: Optional[Dict[str, Any]] = None,
        agent: Optional[str] = None,
    ) -> None:
        metadata = metadata or {}
        if agent:
            metadata["agent"] = agent

        self.storage.save(value, metadata)  # type: ignore # Maybe BUG? Should be self.storage.save(key, value, metadata)

    def search(self, query: str) -> Dict[str, Any]:
        return self.storage.search(query)
