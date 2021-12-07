'''
Test attribute module
'''

from package import attributes

# Attribute
def test_attribute_constructor():
    '''
    Test Attribute constructor
    '''
    hero_attribute = attributes.Attribute(22, 2.8, 1)
    assert hero_attribute.get_attribute() == 24.8

def test_attribute_default_primary():
    '''
    Test default value for primary attribute
    '''
    hero_attribute = attributes.Attribute(22, 2.8, 1)
    assert hero_attribute.is_primary_attribute() is False

def test_attribute_primary():
    '''
    Test set value for primary attribute
    '''
    hero_attribute = attributes.Attribute(22, 2.8, 1, True)
    assert hero_attribute.is_primary_attribute() is True

def test_attribute_bonus_attack():
    '''
    Test bonus attack for primary attribute
    '''
    hero_attribute = attributes.Attribute(22, 2.8, 1, True)
    assert hero_attribute.get_bonus_attack_damage() == 24

def test_strengh_constructor():
    '''
    Test Strengh constructor
    '''
    hero_attribute = attributes.Strengh(22, 2.8, 1)
    assert hero_attribute.get_attribute() == 24.8
    assert hero_attribute.is_primary_attribute() is False
    assert hero_attribute.get_bonus_attack_damage() == 24

# Strengh
def test_strengh_maximum_hp():
    '''
    Test Strengh maximum health point
    '''
    hero_attribute = attributes.Strengh(22, 2.8, 20)
    assert hero_attribute.get_maximum_health_point() == 1760

def test_strengh_hp_regeneration():
    '''
    Test Strengh health regeneration
    '''
    hero_attribute = attributes.Strengh(22, 2.8, 20)
    assert hero_attribute.get_health_regeneration() == 7.8

# Agility
def test_agility_armor():
    '''
    Test Agility armor
    '''
    hero_attribute = attributes.Agility(24, 2.8, 1)
    assert hero_attribute.get_armor() == 4.47

def test_agility_attack_speed():
    '''
    Test Agility attack speed
    '''
    hero_attribute = attributes.Agility(24, 2.8, 1)
    assert hero_attribute.get_attack_speed() == 26.8

#Intelligence
def test_intelligence_mana():
    '''
    Test Intelligence Mana
    '''
    hero_attribute = attributes.Intelligence(23, 3.4, 1)
    assert hero_attribute.get_mana() == 316

def test_intelligence_mana_regeneration():
    '''
    Test Intelligence Mana Regeneration
    '''
    hero_attribute = attributes.Intelligence(23, 3.4, 1)
    assert hero_attribute.get_mana_regeneration() == 1.32
