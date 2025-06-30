import pytest
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InMemoryCategoryRepository
from src.core.category.application.use_cases.list_category import CategoryOutput, ListCategory, ListCategoryRequest, ListCategoryResponse

class TestListCategory:
    @pytest.fixture
    def category_movie(self,scope="module") -> Category:
        return Category(
            name="Filme",
            description="Categoria de filmes",
        )

    @pytest.fixture
    def category_series(self) -> Category:
        return Category(
            name="Séries",
            description="Categoria de séries",
        )


    def test_when_no_categories_then_return_empty_list(self) -> None:
        empty_repository = InMemoryCategoryRepository()
        use_case = ListCategory(repository=empty_repository)
        response = use_case.execute(request=ListCategoryRequest())

        assert response == ListCategoryResponse(data=[])

    def test_when_categories_exist_then_return_mapped_list(
        self,
        category_movie: Category,
        category_series: Category,
    ) -> None:
         
        repository = InMemoryCategoryRepository()
        # repository.save(category=category_movie)
        # repository.save(category=category_series)

        for category in [category_movie, category_series]:
            repository.save(category)


        use_case = ListCategory(repository)
        response = use_case.execute(ListCategoryRequest())

        # assert response == ListCategoryResponse(
        #     data=[
        #         CategoryOutput(
        #             id=category_movie.id,
        #             name=category_movie.name,
        #             description=category_movie.description,
        #             is_active=category_movie.is_active,
        #         ),
        #         CategoryOutput(
        #             id=category_series.id,
        #             name=category_series.name,
        #             description=category_series.description,
        #             is_active=category_series.is_active,
        #         ),
        #     ]
        # )

        assert response ==  ListCategoryResponse(
            data=[ 
                CategoryOutput(**vars(category)) 
                for category in [category_movie, category_series]
            ]
        )



        