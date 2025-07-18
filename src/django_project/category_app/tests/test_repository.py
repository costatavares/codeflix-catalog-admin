import uuid
import pytest
from django_project.category_app.repository import DjangoORMCategoryRepository
from django_project.category_app.models import Category as CategoryORM
from core.category.domain.category import Category


@pytest.mark.django_db
class TestSave:
    def test_saves_category_in_database(self):
        category = Category(
            name="Movie",
            description="Movie description",
        )
        repository = DjangoORMCategoryRepository()

        assert CategoryORM.objects.count() == 0
        repository.save(category)
        assert CategoryORM.objects.count() == 1
        saved_category = CategoryORM.objects.get()

        assert saved_category.id == category.id
        assert saved_category.name == category.name
        assert saved_category.description == category.description
        assert saved_category.is_active == category.is_active

@pytest.mark.django_db
class TestGet:
    @pytest.fixture
    def category_movie(self,scope="module") -> Category:
        return Category(
            name="Filme",
            description="Categoria de filmes",
        )
    
    def test_get_category_by_id(self, category_movie: Category):
        repository = DjangoORMCategoryRepository()
        assert CategoryORM.objects.count() == 0
        
        repository.save(category_movie)

        category = repository.get_by_id(category_movie.id)
        assert category.id == category_movie.id
        assert category.name == category_movie.name
        assert category.description == category_movie.description
        assert category.is_active == category_movie.is_active


    def test_get_category_by_id_not_found(self):
        repository = DjangoORMCategoryRepository()

        category = repository.get_by_id(uuid.uuid4()) 
           
        assert CategoryORM.objects.count() == 0
        assert category is None  

@pytest.mark.django_db
class TestList:
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
    
    def test_list_category_in_database(
        self, 
        category_movie: Category,
        category_series: Category
    ):
        repository = DjangoORMCategoryRepository()
        assert CategoryORM.objects.count() == 0

        for category in [category_movie, category_series]:
            repository.save(category)

        list_category = CategoryORM.objects.all()
        assert list_category.count() == 2
        

        for result, category in zip(list_category, [category_movie, category_series]):
            # print(category.name, category.description, category.is_active)
            print(f"\nid={category.id}, name={category.name}, active={category.is_active}")
            assert result.name == category.name
            assert result.description == category.description
            assert result.is_active == category.is_active

@pytest.mark.django_db
class TestDelete:
    @pytest.fixture
    def category_movie(self,scope="module") -> Category:
        return Category(
            name="Filme",
            description="Categoria de filmes",
        )
    
    def test_delete_category_by_id(self, category_movie: Category):
        repository = DjangoORMCategoryRepository()
        assert CategoryORM.objects.count() == 0
        
        repository.save(category_movie)
        assert CategoryORM.objects.count() == 1

        repository.delete(category_movie.id)
        assert CategoryORM.objects.count() == 0

    def test_delete_category_by_id_not_found(self):
        repository = DjangoORMCategoryRepository()
        
        repository.delete(uuid.uuid4())
        assert CategoryORM.objects.count() == 0

@pytest.mark.django_db
class TestUpdate:
    @pytest.fixture
    def category_movie(self,scope="module") -> Category:
        return Category(
            name="Filme",
            description="Categoria de filmes",
        )
    
    def test_update_category_with_provided_fields(self, category_movie: Category):
        repository = DjangoORMCategoryRepository()
        assert CategoryORM.objects.count() == 0
        
        repository.save(category_movie)
        saved_category = CategoryORM.objects.get()
        assert CategoryORM.objects.count() == 1
        print(f"\saved_category.name={saved_category.name}")


        category_movie.name = "Filme1"
        response =  repository.update(category_movie)
        update_category = CategoryORM.objects.get()
        assert CategoryORM.objects.count() == 1
        print(f"\nupdate_category.name={update_category.name}")

        assert response is None
        assert update_category.id == category_movie.id
        assert update_category.name == category_movie.name
        assert update_category.description == category_movie.description
        assert update_category.is_active == category_movie.is_active

    def test_update_category_not_provided_fields(self, category_movie: Category):     
        repository = DjangoORMCategoryRepository()
        response =  repository.update(category_movie)
        
        assert response is None

