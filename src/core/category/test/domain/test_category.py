import pytest
import unittest
from uuid import UUID 
from src.core.category.domain.category import Category

# class TestCategory(unittest.TestCase):
class TestCategory:
    def test_name_is_requerid(self):
        with pytest.raises(TypeError,match="missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_less_than_255_characteres(self):
        with pytest.raises(ValueError,match="name cannot be longer than 255"):
            Category(name="a" * 256)

    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name="Filme")
        # self.assertEqual(type(category.id),UUID)
        assert isinstance(category.id,UUID)

    def test_created_category_with_default_values(self):
        category = Category(name="Filme")
        # self.assertEqual(category.name,"Filme")
        # self.assertEqual(category.description,"") 
        # self.assertEqual(category.is_active,True)
        assert category.name == "Filme"
        assert category.description == "" 
        assert category.is_active == True 
     
    def test_cannot_create_category_with_empty_name(self):
        with pytest.raises(ValueError,match="name cannot be empty"):
            Category(name="")
                
# if __name__ == "__main__":
#     unittest.main()

class TestUpdateCategory:
    def test_update_category_with_name_and_description(self):
        category = Category(name="Filme",description="Filmes em geral")

        category.update_category(name="Série",description="Séries em geral")

        assert category.name == "Série"
        assert category.description == "Séries em geral"

    def test_update_category_with_invalid_name(self):
        category = Category(name="Filme",description="Filmes em geral")

        with pytest.raises(ValueError,match="name cannot be longer than 255"):
            category.update_category(name= "a" * 256,description="Séries em geral")

class TestActive:
    def test_activate_inactive_category(self):
        category = Category(
            name="Filme",
            description="Filmes em geral",
            is_active=False
        )
        
        category.active()
        
        assert category.is_active is True 

    def test_activate_active_category(self):
        category = Category(
            name="Filme",
            description="Filmes em geral",
            is_active=True
        )
        
        category.active()
        
        assert category.is_active is True     