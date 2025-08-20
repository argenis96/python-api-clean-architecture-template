
class AnimalQuery:
    GET_ALL_ANIMALS:str="""
        SELECT
        id,
        name,
        category
        FROM PUBLIC.ANIMALS
        """
    GET_ANIMAL_BY_ID:str="""
        SELECT
        id,
        name,
        category
        FROM PUBLIC.ANIMALS
        where id = ?AnimalId?
        """
    UPDATE_ANIMAL_BY_ID:str="""
    UPDATE PUBLIC.ANIMALS
    SET
    name=?name?,
    category=?category?
    where id = ?id?
    """
    INSERT="""
    INSERT INTO PUBLIC.ANIMALS(name, category)
    VALUES(?name?,?category?)
    RETURNING id
    """