import spacy
from spacy.matcher import Matcher

description_nlp = spacy.load('en_core_web_sm')
description_matcher = Matcher(description_nlp.vocab)

description_patterns = [
    [
        {'LOWER': 'position'},
        {'LEMMA': "be"},
        {'LOWER': 'fully'},
        {'LOWER': 'remote'}
    ],  # position is fully remote
    [{'LOWER': 'employee'},
     {'LOWER': 'choice'},
     {'LOWER': 'to'},
     {'LOWER': 'work'},
     {'LOWER': 'remote'}
     ],  # Employee choice to work remote
    [{'LOWER': 'work'},
     {'LOWER': 'remote'}
     ],  # work remote
    [{'LOWER': 'remote'},
     {'LOWER': 'opportunity'}
     ],  # remote opportunity
    [{'LOWER': 'position'},
     {'LEMMA': "be", "OP": "?"},
     {'SHAPE': 'ddd'},
     {'ORTH': '%'},
     {'LOWER': 'remote'}
     ],  # position is 100% remote || position 100% remote
    [{'LOWER': 'position'},
     {'LEMMA': "be"},
     {'LOWER': 'remote'}
     ],  # position is remote
    [{'LOWER': 'fully'},
     {'LOWER': 'remote'}
     ],  # fully remote
    [{'POS': 'PRON'},
     {'LEMMA': "be"},
     {'POS': 'DET'},
     {'LOWER': 'remote'},
     {'LOWER': 'position'}
     ],  # This is a remote position
    [{'LOWER': 'work'},
     {'LOWER': 'location'},
     {'IS_PUNCT': True, "OP": "*"},
     {'LOWER': 'remote'}
     ],  # Work Location: Remote
    [{'LOWER': 'job'},
     {'LOWER': 'location'},
     {'IS_PUNCT': True, "OP": "*"},
     {'LOWER': 'remote'}
     ],  # job Location: Remote
    [{'POS': 'PRON'},
     {'LEMMA': "be"},
     {'POS': 'DET'},
     {'SHAPE': 'ddd'},
     {'ORTH': '%'},
     {'LOWER': 'remote'},
     {'LOWER': 'position'}
     ],  # This is a 100% remote position
    [{'LOWER': 'opportunities'},
     {'LEMMA': "to"},
     {'LOWER': 'work'},
     {'LOWER': 'remotely'}
     ],  # opportunities to work remotely
    [
        {"POS": "PROPN", "OP": "?"},
        {"POS": "NOUN", "OP": "?"},
        {'LEMMA': "be"},
        {'LEMMA': "seek"},
        {"POS": 'DET', "OP": "?"},
        {"LOWER": 'highly', "OP": "?"},
        {"LOWER": 'skilled', "OP": "?"},
        {"LOWER": 'and', "OP": "?"},
        {"LOWER": 'experienced', "OP": "?"},
        {'LOWER': 'remote'},
        {'LOWER': 'based'},
        {"POS": "PROPN", "OP": "?"},
        {"POS": "NOUN", "OP": "?"},

    ]  # <PROPN>?<NOUN>? is seeking [a highly skilled and experienced] remote based <PROPN>?<NOUN>?

]

for pattern in description_patterns:
    description_matcher.add('REMOTEDESCRIPTION', patterns=[pattern])


def run_match():
    phrase = ("ADT Solar is seeking a highly skilled and experienced remote based Senior Director of Performance-Based "
              "Marketing to lead our marketing team and drive the success of our performance marketing initiatives.")
    doc = description_nlp(phrase)
    for token in doc:
        # Get the token text, part-of-speech tag and dependency label
        token_text = token.text
        token_pos = token.pos_
        token_dep = token.dep_
        # This is for formatting only
        print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")

    matches = description_matcher(doc)

    descriptionmatches = []
    for match_id, start, end in matches:
        span = doc[start:end]
        descriptionmatches.append(span.text)
        print(span.text)


if __name__ == "__main__":
    run_match()
