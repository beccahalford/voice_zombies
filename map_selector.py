from random import randint

from facts import der_reise, five


def select_map_fact(map_id):
    i = randint(1,5)

    if map_id == 'nacht':
        return nacht[i]
    elif map_id == 'verruckt':
        return verruckt[i]
    elif map_id == 'shi_no_numa':
        return shi_no_numa[i]
    elif map_id == 'der_reise':
        return der_reise[i]
    elif map_id == 'kino':
        return kino[i]
    elif map_id == 'five':
        return five[i]
    elif map_id == 'ascension':
        return ascension[i]
    elif map_id == 'call_of_the_dead':
        return call_of_the_dead[i]
    elif map_id == 'shangri_la':
        return shangri_la[i]
    elif map_id == 'moon':
        return moon[i]
    elif map_id == 'town':
        return town[i]
    elif map_id == 'nuketown':
        return nuketown[i]
    elif map_id == 'die_rise':
        return die_rise[i]
    elif map_id == 'mob':
        return mob[i]
    elif map_id == 'buried':
        return buried[i]
    elif map_id == 'origins':
        return origins[i]
    elif map_id == 'shadows':
        return shadows[i]
    elif map_id == 'the_giant':
        return the_giant[i]
    elif map_id == 'der_eisendrache':
        return der_eisendrache[i]
    elif map_id == 'zetsubou':
        return zetsubou[i]
    elif map_id == 'gorod_krovi':
        return gorod_krovi[i]
    elif map_id == 'revelations':
        return revelations[i]
    elif map_id == 'spaceland':
        return spaceland[i]
    elif map_id == 'redwoods':
        return redwoods[i]
    elif map_id == 'shaolin':
        return shaolin[i]
    elif map_id == 'radioactive':
        return radioactive[i]
    elif map_id == 'beast':
        return beast[i]
    elif map_id == 'prologue':
        return prologue[i]
    elif map_id == 'final_reich':
        return final_reich[i]
    elif map_id == 'haus':
        return haus[i]
    elif map_id == 'darkest_shore':
        return darkest_shore[i]
    elif map_id == 'shadowed_throne':
        return shadowed_throne[i]
    return "No facts available for {}" + format()
