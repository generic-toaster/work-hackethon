from ming import schema
from ming.odm import FieldProperty
from ming.odm import MappedClass

from myproj.model import DBSession
from myproj.model.attributes import Attributes


class Character(MappedClass):
    class __mongometa__:
        session = DBSession
        name = 'character'

    def __init__(self, name, characClass, race, armor_class, attrs, attrsMods):
        self.name = name
        self.charClass = characClass
        self.race = race
        self.armorClass = armor_class
        self.attributes = attrs
        self.attributeModifiers = attrsMods

    def convertToForm(self):
        attrs = {'id': self._id,'name': self.name, 'character_class': self.charClass, 'race': self.race, 'armor_class': self.armorClass,
                 'strength_val': str(self.attributes[Attributes.Strength.value]),
                 'strength_modifier': str(self.attributeModifiers[Attributes.Strength.value]),
                 'dexterity_val': str(self.attributes[Attributes.Dexterity.value]),
                 'dexterity_modifier': str(self.attributeModifiers[Attributes.Dexterity.value]),
                 'const_val': str(self.attributes[Attributes.Constitution.value]),
                 'const_modifier': str(self.attributeModifiers[Attributes.Constitution.value]),
                 'intell_val': str(self.attributes[Attributes.Intellect.value]),
                 'intell_modifier': str(self.attributeModifiers[Attributes.Intellect.value]),
                 'wisdom_val': str(self.attributes[Attributes.Wisdom.value]),
                 'wisdom_modifier': str(self.attributeModifiers[Attributes.Wisdom.value]),
                 'charisma_val': str(self.attributes[Attributes.Charisma.value]),
                 'charisma_modifier': str(self.attributeModifiers[Attributes.Charisma.value])}

        return attrs

    _id = FieldProperty(schema.ObjectId)
    name = FieldProperty(schema.String(required=True))
    charClass = FieldProperty(schema.String)
    race = FieldProperty(schema.String)
    armorClass = FieldProperty(schema.Int)
    attributes = FieldProperty(schema.Array(int))
    attributeModifiers = FieldProperty(schema.Array(int))
