def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note >= 40 and (note % 5 >= 3):
            note = note + (5 - note % 5)
        notes_arrondies.append(note)
    return notes_arrondies

# Exemple d'utilisation
notes = [84, 82, 38, 47, 63,59,48,98]
print(arrondir_notes(notes))  