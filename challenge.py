from platform import architecture
#-- Lemys Lopez General Comments--
#
# After inspection fo the challenge class layers i can fell a subset of the  django arhitecute style
# knowing tha django is MVT (model, view, template), i ve found similary with the view layer of MVT, also we have here
# the data componetns layer that smeels like the template side of mvt.
#
# Being said so and also knowing that there is always ad new way to obtimize a system, for this hypothetical constrained
# case i ve impleted the best SOLID principles techniques to improve the code to adapt to the new requirements.
#
# Q1: WHY DID YOU CREATE A NEW COMPONENT IN THE VISUAL LAYER FOR SEPARATED DROPDOWN? :
#
# A: Well as the new requirement state that top elements are need in the language dropdown. IF this requirement where
# unique only for one drop down (as a not replated behaviur in othe dorp downs) i considre ok that the functionality and
# logic for top elments hapens in a single component of the DTATA COMPONENTS LAYER.
#
# But situations is that the behaviur need to be replicated ind a secound laguage dropdown with diferent elements at the
# top.
#
# So i ve created a new component that inherits from the Dropdown class (DropDownWithTopOptions) and any component that
# extends form it will inherit the top elements functionality
#
# Q2: THEM WHY DIDNT YOU MODIFIED THE ALREADY EXISTAND ONE (Dropdown)?:
#
# A2: As the way ive implemented the new top elements functionality, required to modify the component rendering logic
# and also as this new component rendering logic dependes of other methods data returns as input, In my experience the
# safest way to keep the BACKWARDS COMPAITBILTY with odther components that might be extending the Dropdown is to create
# a new class (DropDownWithTopOptions) extending from Dropdown, Overwriting the redering logic with everithing else.
#
# Q3: WHY DropDownWithTopOptions HVE DISABLED ITEMS FUNCTIOANLITY WHEN IT WAS NOT EXPLICIT REQUIRED ?
#
# A3: In the interview a susgestion form intervierwr was to handle the separator was to treat it as a disabled item, with
# my last improovemnt at the render method of the DropDownWithTopOptions does not need that childrens specify the
# separator as disabled item EVENTHOUG is a nice feature so i decided to keep it






#--CONFIG/------------------------
# NOTE: Settings are loaded from an external secret manager when deployed.
#       Values here are only for testing.
class SettingsImporter ():

  LANGUAGES = [
    ('ar', 'Arabic'),
    ('de', 'German'),
    ('el', 'Greek'),
    ('fr', 'French'),
    ('en', 'English'),
    ('sp', 'Spanish'),
    ('pt', 'Portuguese'),
    ('it', 'Italian'),
    ('tr', 'Turkish'),
    ('ja', 'Japanese'),
  ]


#--HELPER-CLASSES/------------------------
class Component():
  @classmethod
  def render(cls):
    print ("Component")

class TemplateRenderer():
  def __init__(self, components: [Component]):
    self.components = components

  def render_page(self):
    for c in self.components:
      c.render()


#--VISUAL-COMPONENTS/------------------------------
class PageTitle(Component):
  TEXT = ""

  @classmethod
  def render(cls):
    print (cls.TEXT)

class Dropdown(Component):
  INPUT_NAME = "Dropdown"


  @classmethod
  def as_list(cls):
    return []

  @classmethod
  def render(cls):
    print (f"{cls.INPUT_NAME}:")
    for key, value in cls.as_list():
      print (f"  {key} => {value}")


#class DropdownWithTopOptions(Dropdown):
#  TOP_OPTIONS = []
#  DISABLED_KEYS = []
#
#  @class_method
#  def as_list(cls):
#    list =
#    return top_list + divider + rest


class DropDownWithTopOptions(Dropdown):

  @classmethod
  def get_top_elements_keys(cls):
    return []

  @classmethod
  def get_disabled_keys(cls):
    return []

  @classmethod
  def get_sorted_items_list(cls,items):
    return dict(sorted(items))

  @classmethod
  def get_split_items(cls):
    top_items = cls.get_top_elements_keys()
    top_elements_items = []
    rest_of_elements_items = []
    for key, value in cls.get_sorted_items_list(cls.as_list()).items():
      if key in top_items:
        top_elements_items.insert(top_items.index(key),(key,value))
      else:
        rest_of_elements_items.append((key,value))

    return top_elements_items,rest_of_elements_items

  @classmethod
  def format_item(cls,item,disabled=False):
    if disabled:
      return f"        {item[1]}"
    else:
      return f"  {item[0]} => {item[1]}"


  @classmethod
  def render_formated_items(cls,items):
    for item in items:
      print(cls.format_item(item,item[0] in cls.get_disabled_keys()))

  @classmethod
  def render(cls):
    print (f"{cls.INPUT_NAME}:")
    top_elements_items,rest_of_elements_items = cls.get_split_items()
    if len(top_elements_items) > 0:
      cls.render_formated_items(top_elements_items)
      print ("         ----")
    cls.render_formated_items(rest_of_elements_items)

#--DATA-COMPONENTS/------------------------------
class ExampleTitle(PageTitle):
  TEXT = "--- Demo Page ---"

class GenderDropdown(Dropdown):
  INPUT_NAME = 'Gender'

  @classmethod
  def as_list(cls):
    return [('M', 'Male'), ('F', 'Female')]


class LangDropdownSeparated(DropDownWithTopOptions):
  INPUT_NAME = 'Languages DropDown with top elements '

  @classmethod
  def as_list(cls):
    return SettingsImporter.LANGUAGES


  @classmethod
  def get_top_elements_keys(cls):
    return ['en', 'sp', 'fr']


class LangDropdownSeparated2(DropDownWithTopOptions):
  INPUT_NAME = 'Languages DropDown with others top elements'

  @classmethod
  def as_list(cls):
    return SettingsImporter.LANGUAGES

  @classmethod
  def get_top_elements_keys(cls):
    return ['de','fr']



class LangDropdownSeparated3(DropDownWithTopOptions):
  INPUT_NAME = 'Language With Disabled elemets'

  @classmethod
  def as_list(cls):
    return SettingsImporter.LANGUAGES

  @classmethod
  def get_top_elements_keys(cls):
    return ['de','fr']


  @classmethod
  def get_disabled_keys(cls):
    return ["sp"]

#--MAIN---------------------------------

components = [ExampleTitle, GenderDropdown, LangDropdownSeparated, LangDropdownSeparated2, LangDropdownSeparated3]
TemplateRenderer(components).render_page()




## TODO:
## Show the langueges in dropdown in this order:
##   English
##   Spanish
##   French
##   ---------
##   Remaining languages sorted alphabeticaly





## TODO:
## Show dropdown #2 with common languages French and German at the top
## followed by remaining languages sorted alphabetically.


