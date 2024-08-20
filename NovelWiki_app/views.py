from django.shortcuts import render, redirect
from .forms import CharacterForm, ShadowSlaveCharacterForm, LotmCharacterForm
from .models import Character

# Create your views here.
def create_character(request):
    if request.method == 'POST':
        character_form = CharacterForm(request.POST, request.FILES)
        if character_form.is_valid():
            character = character_form.save()
            if character.novel.title == 'Shadow Slave':
                return redirect('create_shadow_slave', character_id=character.id)
            elif character.novel.title == 'Lord of the Mysteries':
                return redirect('create_lotm', character_id=character.id)
    else:
        character_form = CharacterForm()
    return render(request, 'create_character.html', {'form': character_form})

def create_shadow_slave(request, character_id):
    character = Character.objects.get(id=character_id)
    if request.method == 'POST':
        form = ShadowSlaveCharacterForm(request.POST)
        if form.is_valid():
            shadow_slave_character = form.save(commit=False)
            shadow_slave_character.character = character
            shadow_slave_character.save()
            return redirect('character_detail', character_id=character.id)
    else:
        form = ShadowSlaveCharacterForm()
    return render(request, 'create_shadow_slave.html', {'form': form, 'character': character})

def create_lotm(request, character_id):
    character = Character.objects.get(id=character_id)
    if request.method == 'POST':
        form = LotmCharacterForm(request.POST)
        if form.is_valid():
            lotm_character = form.save(commit=False)
            lotm_character.character = character
            lotm_character.save()
            return redirect('character_detail', character_id=character.id)
    else:
        form = LotmCharacterForm()
    return render(request, 'create_lotm.html', {'form': form, 'character': character})

def edit_character(request):
    pass

def delete_character(request):
    pass

