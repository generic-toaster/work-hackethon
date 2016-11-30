import tw2.forms as twf

from myproj.model.charClass import CharClass
from myproj.model.race import Race
import logging

log = logging.getLogger(__name__)

class CharacterForm(twf.FormPage):
    title = 'DnD Character Form'

    def prepopulate(self, charac):
        log.debug("setting name for " + charac.name)


    class child(twf.TableForm):
        action = "/characters"
        method = "POST"
        id = twf.HiddenField(size=50)
        name = twf.TextField('name', size=30)
        character_class = twf.SingleSelectField(options=['', str(CharClass.Fighter), str(CharClass.Cleric), str(CharClass.Wizard), str(CharClass.Thief)])
        race = twf.SingleSelectField(options=['', str(Race.human), str(Race.dwarf), str(Race.elf), str(Race.halfElf)])

        class strength(twf.GridLayout):
            extra_reps = 1
            attr_options = [str(x) for x in range(3, 19)]
            strength = twf.SingleSelectField(options=attr_options)
            strength_modifier = twf.TextField(size=5)
            roll = twf.Button(id="strengthButton", value='Roll', attrs={'onclick': 'var val = roll(); document.getElementById("characterform:strength:0:strength").selectedIndex = (val - 2);document.getElementById("characterform:strength:0:strength_modifier").value = Math.ceil((val - 11) / 2)'})
        class dexterity(twf.GridLayout):
            extra_reps = 1
            attr_options = [str(x) for x in range(3, 19)]
            dexterity = twf.SingleSelectField(options=attr_options)
            dexterity_modifier = twf.TextField(size=5)
            droll = twf.Button(id="dexterityButton", value='Roll', attrs={
                'onclick': 'var val = roll(); document.getElementById("characterform:dexterity:0:dexterity").selectedIndex = (val - 2);document.getElementById("characterform:dexterity:0:dexterity_modifier").value = Math.ceil((val - 11) / 2);document.getElementById("characterform:armor_class").value = 10+Math.ceil((val - 11) / 2)'})
        class constitution(twf.GridLayout):
            extra_reps = 1
            attr_options = [str(x) for x in range(3, 19)]
            constitution = twf.SingleSelectField(options=attr_options)
            constitution_modifier = twf.TextField(size=5)
            croll = twf.Button(id="constitutionButton", value='Roll', attrs={
                'onclick': 'var val = roll(); document.getElementById("characterform:constitution:0:constitution").selectedIndex = (val - 2);document.getElementById("characterform:constitution:0:constitution_modifier").value = Math.ceil((val - 11) / 2)'})

        class intelligence(twf.GridLayout):
            extra_reps = 1
            attr_options = [str(x) for x in range(3, 19)]
            intelligence = twf.SingleSelectField(options=attr_options)
            intelligence_modifier = twf.TextField(size=5)
            iroll = twf.Button(id="intelligenceButton", value='Roll', attrs={
                'onclick': 'var val = roll(); document.getElementById("characterform:intelligence:0:intelligence").selectedIndex = (val - 2);document.getElementById("characterform:intelligence:0:intelligence_modifier").value = Math.ceil((val - 11) / 2)'})
        class wisdom(twf.GridLayout):
            extra_reps = 1
            attr_options = [str(x) for x in range(3, 19)]
            wisdom = twf.SingleSelectField(options=attr_options)
            wisdom_modifier = twf.TextField(size=5)
            wroll = twf.Button(id="wisdomButton", value='Roll', attrs={
                'onclick': 'var val = roll(); document.getElementById("characterform:wisdom:0:wisdom").selectedIndex = (val - 2);document.getElementById("characterform:wisdom:0:wisdom_modifier").value = Math.ceil((val - 11) / 2)'})
        class charisma(twf.GridLayout):
            extra_reps = 1
            attr_options = [str(x) for x in range(3, 19)]
            charisma = twf.SingleSelectField(options=attr_options)
            charisma_modifier = twf.TextField(size=5)
            chroll = twf.Button(id="charismaButton", value='Roll', attrs={
                'onclick': 'var val = roll(); document.getElementById("characterform:charisma:0:charisma").selectedIndex = (val - 2);document.getElementById("characterform:charisma:0:charisma_modifier").value = Math.ceil((val - 11) / 2)'})
        armor_class = twf.TextField(size=5)

    #submit = twf.SubmitButton(value = 'Save')