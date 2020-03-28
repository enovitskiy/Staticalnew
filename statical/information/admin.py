from django.contrib import admin
from .models import \
    Subnavigator,Navconstruct,Subsubnav,\
    Social,Footer,Text,Footercont,Page,Slider,\
    Pagenext, Projects, Example, Pictures, \
    Short, Pageproject,Faqblock, Faq,Contact, Contdecr,Pictslider, Textslider, Mpage, Values, Etapy

class Pagenext(admin.StackedInline):
    model = Pagenext
    extra = 0


class Page(admin.StackedInline):
    model = Page
    extra = 0

class Project(admin.StackedInline):
    model = Projects
    extra = 0

class Menu(admin.StackedInline):
    model = Subnavigator
    extra = 0

@admin.register(Navconstruct)
class Panel(admin.ModelAdmin):
    inlines = [Menu, Page,Project,Pagenext]

class Submenu(admin.StackedInline):
    model = Subsubnav
    extra = 0

class Slider(admin.StackedInline):
    model = Slider
    extra = 0

@admin.register(Subnavigator)
class Subpanel(admin.ModelAdmin):
    inlines = [Submenu,Page,Slider, Project,Pagenext]


class Pictures(admin.StackedInline):
    model = Pictures
    extra = 0

class Short(admin.StackedInline):
    model = Short
    extra = 0
class Pageproject(admin.StackedInline):
    model = Pageproject
    extra = 0

@admin.register(Example)
class Example(admin.ModelAdmin):
    inlines = [Pictures, Short, Pageproject]

class Faq(admin.StackedInline):
    model = Faq
    extra = 0

@admin.register(Faqblock)
class Faqblock(admin.ModelAdmin):
    inlines = [Faq]

class Textslider(admin.StackedInline):
    model = Textslider
    extra = 0

@admin.register(Pictslider)
class Pictslider(admin.ModelAdmin):
    inlines = [Textslider]


admin.site.register(Social)

admin.site.register(Footer)
admin.site.register(Text)
admin.site.register(Footercont)


admin.site.register(Contact)
admin.site.register(Contdecr)



admin.site.register(Mpage)
admin.site.register(Values)

admin.site.register(Etapy)