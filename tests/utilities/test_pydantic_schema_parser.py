import unittest
from pydantic import BaseModel
from typing import List, Optional

from crewai.utilities.pydantic_schema_parser import PydanticSchemaParser


# Define test models
class InnerModel(BaseModel):
    inner_field: int


class TestModel(BaseModel):
    simple_field: str
    list_field: List[int]
    optional_field: Optional[str]
    nested_model: InnerModel


# Test cases
class TestPydanticSchemaParser(unittest.TestCase):
    def test_simple_model(self):
        class SimpleModel(BaseModel):
            field1: int
            field2: str

        parser = PydanticSchemaParser(model=SimpleModel)
        expected_schema = "- field1: int\n- field2: str"
        self.assertEqual(parser.get_schema(), expected_schema)

    def test_model_with_list(self):
        class ListModel(BaseModel):
            field1: List[int]

        parser = PydanticSchemaParser(model=ListModel)
        expected_schema = "- field1: List[int]"
        self.assertEqual(parser.get_schema(), expected_schema)

    def test_model_with_optional(self):
        class OptionalModel(BaseModel):
            field1: Optional[int]

        parser = PydanticSchemaParser(model=OptionalModel)
        expected_schema = "- field1: Optional[int]"
        self.assertEqual(parser.get_schema(), expected_schema)

    def test_nested_model(self):
        parser = PydanticSchemaParser(model=TestModel)
        expected_schema = (
            "- simple_field: str\n"
            "- list_field: List[int]\n"
            "- optional_field: Optional[str]\n"
            "- nested_model: InnerModel[\n"
            "    - inner_field: int\n"
            "]"
        )
        self.assertEqual(parser.get_schema(), expected_schema)


if __name__ == "__main__":
    unittest.main()
