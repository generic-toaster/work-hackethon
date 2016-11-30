# -*- coding: utf-8 -*-
"""{{target.capitalize()}} controller module"""

from tg import expose, redirect, validate, flash, url
import logging
# from tg.i18n import ugettext as _
# from tg import predicates

from myproj.lib.base import BaseController
# from myproj.model import DBSession
from bson.objectid import ObjectId
from myproj.model.character import Character
from myproj.model.characterForm import CharacterForm
from myproj.model.attributes import Attributes
from myproj.model.race import Race
from myproj.model.charClass import CharClass
from tg import RestController, redirect

log = logging.getLogger(__name__)

class CharactersController(RestController):
    # Uncomment this line if your controller requires an authenticated user
    # allow_only = predicates.not_anonymous()
    #def _lookup(self, id, *remainder):
    #    log.debug("really I'm here dammit!")
    #    cont = CharactersController(id)
    #    return cont, remainder

    #def __init__(self, id):
    #    self.thing = 1
    #    #self.character = Character.query.find({'id': id}).first()
    
    @expose('myproj.templates.characters.index')
    def home(self, **kw):
        log.debug("loser I'm here ")
        characs = Character.query.find({})
        return dict(page='list_characters', characters=characs)

    #get the form to create a character, ie return the template
    @expose("myproj.templates.characters.characterForm")
    def form(self, ch_id, **kw):
        log.debug("In the other form method!!")
        charac = Character.query.find({'_id': ObjectId(ch_id)}).first()
        form = CharacterForm()
        log.debug(charac.convertToForm())

        return dict(page = 'chacterform', form = form.req(), values = charac.convertToForm())

    @expose("myproj.templates.characters.characterForm")
    def new(self, **kw):
        log.debug("In the form method!!")
        return dict(page='chacterform', form=CharacterForm().req(), values=dict())

    def doitnow(self, **kw):
        Character.query.remove({})
        redirect('/characters/')

    @expose('json')
    def get_all(self):
        characs = Character.query.find({}).all()
        log.debug("found " + str(len(characs)) + " characters")
        return dict(characters=characs)

    @expose('json')
    def get_one(self, ch_id):
        log.debug("id = " + ch_id)
        charac = Character.query.find({'_id': ObjectId(ch_id)}).first()

        if charac:
            log.debug("character found")

        return dict(character=charac)

    #create new character
    @expose()
    def post(self, **kw):
        log.debug("POSTING NEW CHARACTER!!")
        attrs = []
        attrs_mod = []

        attrs.insert(Attributes.Strength.value, int(kw['characterform:strength:0:strength']))
        attrs_mod.insert(Attributes.Strength.value, int(kw['characterform:strength:0:strength_modifier']))
        attrs.insert(Attributes.Dexterity.value, int(kw['characterform:dexterity:0:dexterity']))
        attrs_mod.insert(Attributes.Dexterity.value, int(kw['characterform:dexterity:0:dexterity_modifier']))
        attrs.insert(Attributes.Constitution.value, int(kw['characterform:constitution:0:constitution']))
        attrs_mod.insert(Attributes.Constitution.value, int(kw['characterform:constitution:0:constitution_modifier']))
        attrs.insert(Attributes.Intellect.value, int(kw['characterform:intelligence:0:intelligence']))
        attrs_mod.insert(Attributes.Intellect.value, int(kw['characterform:intelligence:0:intelligence_modifier']))
        attrs.insert(Attributes.Wisdom.value, int(kw['characterform:wisdom:0:wisdom']))
        attrs_mod.insert(Attributes.Wisdom.value, int(kw['characterform:wisdom:0:wisdom_modifier']))
        attrs.insert(Attributes.Charisma.value, int(kw['characterform:charisma:0:charisma']))
        attrs_mod.insert(Attributes.Charisma.value, int(kw['characterform:charisma:0:charisma_modifier']))

        raceStr = kw['characterform:race']
        chClass = kw['characterform:character_class']

        if 'Human' in raceStr:
            race = Race.human
        elif 'HalfElf' in raceStr:
            race = Race.halfElf
        elif 'Dwarf' in raceStr:
            race = Race.dwarf
        else:
            race = Race.elf

        if 'Fighter' in chClass:
            charac_class = CharClass.Fighter
        elif 'Cleric' in chClass:
            charac_class = CharClass.Cleric
        elif 'Wizard' in chClass:
            charac_class = CharClass.Wizard
        else:
            charac_class = CharClass.Thief


        log.debug('name = ' + str(kw))

        if not kw['characterform:id']:
            charac = Character(kw['characterform:name'], str(charac_class), str(race), int(kw['characterform:armor_class']),
                           attrs, attrs_mod)
        else:
            existingChar = Character.query.find({'_id': ObjectId(kw['characterform:id'])}).first()
            existingChar.name = kw['characterform:name']
            existingChar.charClass = str(charac_class)
            existingChar.race = str(race)
            existingChar.armorClass = int(kw['characterform:armor_class'])
            existingChar.attributes = attrs
            existingChar.attributeModifiers = attrs_mod

        redirect('/characters/home')

    #@expose('json')
    #def put(self, id, **kw):
     #   return

    @expose()
    def deleteit(self, ch_id, **kw):
        log.debug("delete that sucker! " + ch_id)
        existingChar = Character.query.find({'_id': ObjectId(ch_id)}).first()
        existingChar.delete()

        return redirect('characters/home')

 #   @expose('sometemplate')
  #  def edit(self, **kw):
   #     return dict(character=self.character)

    #@expose('sometemplate')
    #def html(self, **kw):
    #    return dict(character=self.character)

    @expose('json')
    def json(self, id, **kw):
        existingChar = Character.query.find({'_id': ObjectId(kw['characterform:id'])}).first()

        return existingChar
