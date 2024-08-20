from django import forms
from .models import Character, ShadowSlaveCharacter, LotmCharacter

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'novel', 'description']

class ShadowSlaveCharacterForm(forms.ModelForm):
    class Meta:
        model = ShadowSlaveCharacter
        fields = ['rank', 'aspect', 'aspect_rank']
    
class LotmCharacterForm(forms.ModelForm):
    class Meta:
        model = LotmCharacter
        fields = ['pathway', 'sequence']