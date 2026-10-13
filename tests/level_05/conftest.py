import pytest

from dungeon.shop import Listing, Shop
from dungeon.inventory import Inventory, Item
from dungeon.hero import Hero


@pytest.fixture
def hero():
    return Hero("Ada", gold=20)

@pytest.fixture
def backpack():
    return Inventory()

@pytest.fixture
def shop():
    bow = Item("bow", 6.1, 5)
    potion = Item("potion", 5.5 , 10)
    sword = Item("sword", 9.5, 40)
    return Shop([Listing(bow, 5, 3), Listing(potion, 10, 0), Listing(sword, 40, 2)]) 

@pytest.fixture
def hero_ada_rich(hero):
    hero.gold = 100
    return hero 




