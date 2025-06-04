"""Test configuration and fixtures."""
import pytest
from typing import List, Any

from src.report_generators.base_generator import BaseGenerator
from src.report_generators.utils.types import COLUMNS_TYPE


class MockGenerator(BaseGenerator):
    """Mock implementation of BaseGenerator for testing."""

    def get_columns(self) -> List[COLUMNS_TYPE]:
        return [
            ("Name", 20),
            ("Age", 10),
            ("Email", 30)
        ]

    def generate_row_fn(self, item: Any) -> list:
        return [item["name"], item["age"], item["email"]]


@pytest.fixture
def mock_data():
    """Sample data for testing."""
    return [
        {"name": "John Doe", "age": 30, "email": "john@example.com"},
        {"name": "Jane Smith", "age": 25, "email": "jane@example.com"},
    ]


@pytest.fixture
def base_generator():
    """Fixture providing a mock generator instance."""
    return MockGenerator()
