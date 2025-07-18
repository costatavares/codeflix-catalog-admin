import pytest
from unittest.mock import create_autospec
from src.core.category.domain.category import Category
from src.core.category.domain.category_repository import CategoryRepository
from src.core.category.application.use_cases.update_category import UpdateCategory, UpdateCategoryRequest


class TestUpdateCategory:
    @pytest.fixture
    def category(self) -> Category:
        return Category(
            name="Filme",
            description="Categoria de filmes",
        )

    @pytest.fixture
    def mock_repository(self, category: Category) -> CategoryRepository:
        repository = create_autospec(CategoryRepository, instance=True)
        repository.get_by_id.return_value = category
        return repository

    def test_update_category_name(
        self,
        mock_repository: CategoryRepository,
        category: Category,
    ):
        use_case = UpdateCategory(mock_repository)
        use_case.execute(UpdateCategoryRequest(
            id=category.id,
            name="Séries",
        ))

        assert category.name == "Séries"
        mock_repository.update.assert_called_once_with(category) 