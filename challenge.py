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


class SeparatedDropdown(Dropdown):

  @classmethod
  def get_top_elements(cls):
    return []

  @classmethod
  def get_ordered_items(cls):
    list_as_dir = dict(sorted(cls.as_list()))
    top_items = cls.get_top_elements()
    top_elements_values = []
    rest_of_langs_dic = {}
    for key, value in list_as_dir.items():
      if key in top_items:
        top_elements_values.insert(top_items.index(key),(key,value))
      else:
        rest_of_langs_dic[key] = value
    result = top_elements_values+[("-","---")]+list(rest_of_langs_dic.items())
    return result




  @classmethod
  def get_disableds(cls):
    return []


  @classmethod
  def render(cls):
    print (f"{cls.INPUT_NAME}:")
    for key, value in cls.get_ordered_items():
      if key in cls.get_disableds():
        print (f"        {value}")
      else:
        print (f"  {key} => {value}")


#--DATA-COMPONENTS/------------------------------
class ExampleTitle(PageTitle):
  TEXT = "--- Demo Page ---"

class GenderDropdown(Dropdown):
  INPUT_NAME = 'Gender'

  @classmethod
  def as_list(cls):
    return [('M', 'Male'), ('F', 'Female')]

class LangDropdown(Dropdown):
  INPUT_NAME = 'Language'

  @classmethod
  def get_disableds(cls):
    return ["-"]

  @classmethod
  def get_ordered_items(cls):
    list_as_dir = dict(sorted(cls.as_list()))
    top_items = cls.get_top_elements()
    top_elements_values = []
    rest_of_langs_dic = {}
    for key, value in list_as_dir.items():
      if key in top_items:
        top_elements_values.insert(top_items.index(key),(key,value))
      else:
        rest_of_langs_dic[key] = value
    result = top_elements_values+[("-","---")]+list(rest_of_langs_dic.items())
    return result

  @classmethod
  def as_list(cls):
    # return SettingsImporter.LANGUAGES
    return cls.get_ordered_lang_items()






class LangDropdownSeparated(SeparatedDropdown):
  INPUT_NAME = 'Language1'

  @classmethod
  def as_list(cls):
    return SettingsImporter.LANGUAGES


  @classmethod
  def get_top_elements(cls):
    return ['en', 'sp', 'fr']

  @classmethod
  def get_disableds(cls):
    return ["-"]





class LangDropdownSeparated2(SeparatedDropdown):
  INPUT_NAME = 'Language2'

  @classmethod
  def as_list(cls):
    return SettingsImporter.LANGUAGES

  @classmethod
  def get_top_elements(cls):
    return ['de','fr']

  @classmethod
  def get_disableds(cls):
    return ["-"]




#--MAIN---------------------------------

components = [ExampleTitle, GenderDropdown, LangDropdownSeparated, LangDropdownSeparated2]
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


