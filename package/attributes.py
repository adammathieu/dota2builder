'''
Module attributes define the main statistic of dota2 heroes
'''

from math import floor

class Attribute:
    '''
    Class Attribute define the main characteristic of dota 2 heroes.
    '''
    def __init__(self, base, growth, level, primary=False):
        self.base_value = base
        self.growth_value = growth
        self.level = level
        self.primary = primary

    def get_attribute(self):
        '''
        Get attribute value base on hero level
        '''
        return round(self.base_value + (self.level * self.growth_value), 2)

    def is_primary_attribute(self):
        '''
        Indicate if it is a primary attribute
        '''
        return self.primary

    def get_bonus_attack_damage(self):
        '''
        Get bonus attack damage based on primary attribute
        '''
        return floor(self.base_value + (self.level * self.growth_value))

class Strengh(Attribute):
    '''
    Class Strengh is an attribute that is a measure of a hero's toughness and endurance.
    It grants health and health regeneration.
    '''
    base_hp = 200

    def get_maximum_health_point(self):
        '''
        Get the maximum hp based on strengh attribute
        '''
        return Strengh.base_hp + floor(20*self.get_attribute())

    def get_health_regeneration(self):
        '''
        Get the health regeneration based on strengh attribute
        '''
        return 0.1*self.get_attribute() // 0.01 * 0.01 #round down with 2 decimals: /0.01*0.01

class Agility(Attribute):
    '''
    Class Agility is an attribute that is a measure of a hero's swiftness and dexterity.
    It grants attack speed and armor.
    '''
    base_armor = 0.167

    def get_armor(self):
        '''
        Get armor
        '''
        return Agility.base_armor*self.get_attribute() // 0.01 * 0.01 #round down with 2 decimals: /0.01*0.01

    def get_attack_speed(self):
        '''
        Get Attack Speed
        '''
        return self.get_attribute() // 0.01 * 0.01 #round down with 2 decimals: /0.01*0.01

class Intelligence(Attribute):
    """
    Class Intelligence is an attribute that is a measure of a hero's wit and wisdom.
    It grants mana and mana regeneration.
    """
    base_mana = 12
    base_mana_regen = 0.05

    def get_mana(self):
        '''
        Get Mana
        '''
        return floor(Intelligence.base_mana * self.get_attribute())

    def get_mana_regeneration(self):
        '''
        Get Mana Regeneration
        '''
        return Intelligence.base_mana_regen * self.get_attribute() // 0.01 * 0.01 #round down with 2 decimals: /0.01*0.01
