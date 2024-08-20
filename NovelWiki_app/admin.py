from django.contrib import admin
from .models import Novel, Character, ShadowSlaveCharacter, LotmCharacter

# Register your models here.
@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'novel', 'description')
    search_fields = ('name',)
    list_filter = ('novel',)

@admin.register(ShadowSlaveCharacter)
class ShadowSlaveCharacterAdmin(admin.ModelAdmin):
    list_display = ('character', 'rank', 'aspect_rank', 'aspect')
    search_fields = ('character__name',)

@admin.register(LotmCharacter)
class LotmCharacterAdmin(admin.ModelAdmin):
    list_display = ('character', 'pathway', 'sequence')
    search_fields = ('character__name', 'pathway')
