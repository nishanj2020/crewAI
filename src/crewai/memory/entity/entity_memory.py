from pathlib import Path

from crewai.memory.entity.entity_memory_item import EntityMemoryItem
from crewai.memory.memory import Memory
from crewai.memory.storage.rag_storage import RAGStorage


class EntityMemory(Memory):
    """
    EntityMemory class for managing structured information about entities
    and their relationships using SQLite storage.
    Inherits from the Memory class.
    """

    def __init__(
        self,
        crew=None,
        db_storage_path: Path | None = None,
        embedder_config: dict | None = None,
    ):
        storage = RAGStorage(
            type="entities",
            db_storage_path=db_storage_path,
            allow_reset=False,
            embedder_config=embedder_config,
            crew=crew,
        )
        super().__init__(storage)

    def save(self, item: EntityMemoryItem) -> None:  # type: ignore # BUG?: Signature of "save" incompatible with supertype "Memory"
        """Saves an entity item into the SQLite storage."""
        data = f"{item.name}({item.type}): {item.description}"
        super().save(data, item.metadata)
