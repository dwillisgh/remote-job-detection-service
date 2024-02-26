import re

import spacy
from spacy.matcher import Matcher
from bs4 import BeautifulSoup
import json
from loguru import logger
import os

from app.api.errors import GenericException

description_nlp = None
description_matcher = None
title_nlp = None
title_matcher = None
address_locality_nlp = None
address_locality_matcher = None
description_remote_nlp = None
description_remote_matcher = None
description_false_positive_remote_nlp = None
description_false_positive_remote_matcher = None
description_non_remote_nlp = None
description_non_remote_matcher = None
description_hybrid_nlp = None
description_hybrid_matcher = None

# use regex to detect remote
remote_regex = re.compile(r"\bremote\b", re.IGNORECASE)


# returns phrase patterns from the patterns_json_file
# used to load all nlp models with patterns for each field
def load_patterns_from_file(patterns_json_file):
    pattern_file_root_dir = "etc"
    # to support tests
    if not os.path.exists(pattern_file_root_dir):
        pattern_file_root_dir = "../../etc"

    pattern_file_path = pattern_file_root_dir + "/" + patterns_json_file

    with open(pattern_file_path) as f:
        ldjson = f.read()

    # Parse JSON into an object with attributes corresponding to dict keys.
    # strict False gets rid of encoding issues
    load_field_patterns = json.loads(ldjson, strict=False)

    field_patterns = []
    for fieldPattern in load_field_patterns:
        field_patterns.append(fieldPattern['phrasePatterns'])

    return field_patterns


# used to support the remotepatterns endpoint
# returns entire json patterns and terms for each field pattern
def load_term_patterns_from_file(patterns_json_file):
    pattern_file_root_dir = "etc"
    # to support tests
    if not os.path.exists(pattern_file_root_dir):
        pattern_file_root_dir = "../../etc"

    pattern_file_path = pattern_file_root_dir + "/" + patterns_json_file
    with open(pattern_file_path) as f:
        ldjson = f.read()

    # Parse JSON into an object with attributes corresponding to dict keys.
    # strict False gets rid of encoding issues
    load_field_patterns = json.loads(ldjson, strict=False)

    return load_field_patterns


def load_description_nlp_matcher():
    logger.info("reloading description_nlp")

    global description_nlp
    global description_matcher
    # description nlp/matcher
    description_nlp = spacy.load('en_core_web_sm', disable=["ner", "lemmatizer"])
    description_matcher = Matcher(description_nlp.vocab)

    description_patterns = load_patterns_from_file("descriptionPatterns.json")

    for pattern in description_patterns:
        description_matcher.add('REMOTEDESCRIPTION', patterns=[pattern])


def load_description_remote_nlp_matcher():
    logger.info("reloading description_remote_nlp")

    global description_remote_nlp
    global description_remote_matcher

    # description_remote nlp/matcher
    description_remote_nlp = spacy.load('en_core_web_sm', disable=["ner", "lemmatizer"])
    description_remote_matcher = Matcher(description_remote_nlp.vocab)

    description_remote_term_patterns = load_patterns_from_file("descriptionRemoteTermPatterns.json")

    for pattern in description_remote_term_patterns:
        description_remote_matcher.add('DESCRIPTIONREMOTE', patterns=[pattern])


def load_description_false_positive_remote_nlp_matcher():
    logger.info("reloading description_false_positive_remote_nlp")

    global description_false_positive_remote_nlp
    global description_false_positive_remote_matcher

    # description_false_positive_remote nlp/matcher
    description_false_positive_remote_nlp = spacy.load('en_core_web_sm', disable=["ner", "lemmatizer"])
    description_false_positive_remote_matcher = Matcher(description_false_positive_remote_nlp.vocab)

    description_false_positive_patterns = load_patterns_from_file("descriptionFalsePositivePatterns.json")

    for pattern in description_false_positive_patterns:
        description_false_positive_remote_matcher.add('DESCRIPTIONFALSEPOSITIVEREMOTE', patterns=[pattern])


def load_description_non_remote_nlp_matcher():
    logger.info("reloading description_non_remote_nlp")

    global description_non_remote_nlp
    global description_non_remote_matcher

    # description_non_remote nlp/matcher
    description_non_remote_nlp = spacy.load('en_core_web_sm', disable=["ner", "lemmatizer"])
    description_non_remote_matcher = Matcher(description_non_remote_nlp.vocab)

    description_non_remote_patterns = load_patterns_from_file("descriptionNonRemotePatterns.json")

    for pattern in description_non_remote_patterns:
        description_non_remote_matcher.add('DESCRIPTIONNONREMOTE', patterns=[pattern])


def load_description_hybrid_nlp_matcher():
    logger.info("reloading description_hybrid_nlp")

    global description_hybrid_nlp
    global description_hybrid_matcher
    # description nlp/matcher
    description_hybrid_nlp = spacy.load('en_core_web_sm', disable=["ner", "lemmatizer"])
    description_hybrid_matcher = Matcher(description_hybrid_nlp.vocab)

    description_hybrid_patterns = load_patterns_from_file("descriptionHybridPatterns.json")

    for pattern in description_hybrid_patterns:
        description_hybrid_matcher.add('HYBRIDDDESCRIPTION', patterns=[pattern])


load_description_nlp_matcher()
load_description_non_remote_nlp_matcher()


async def load_field_remote_patterns():
    field_patterns = []
    field_pattern = {
        "fieldName": "descriptionPatterns",
        "fieldPatterns": load_term_patterns_from_file("descriptionPatterns.json")
    }
    field_patterns.append(field_pattern)
    field_pattern = {
        "fieldName": "addressLocalityPatterns",
        "fieldPatterns": load_term_patterns_from_file("addressLocalityPatterns.json")
    }
    field_patterns.append(field_pattern)
    field_pattern = {
        "fieldName": "titlePatterns",
        "fieldPatterns": load_term_patterns_from_file("titlePatterns.json")
    }
    field_patterns.append(field_pattern)
    field_pattern = {
        "fieldName": "descriptionFalsePositivePatterns",
        "fieldPatterns": load_term_patterns_from_file("descriptionFalsePositivePatterns.json")
    }
    field_patterns.append(field_pattern)
    field_pattern = {
        "fieldName": "descriptionNonRemotePatterns",
        "fieldPatterns": load_term_patterns_from_file("descriptionNonRemotePatterns.json")
    }
    field_patterns.append(field_pattern)
    field_pattern = {
        "fieldName": "descriptionHybridPatterns",
        "fieldPatterns": load_term_patterns_from_file("descriptionHybridPatterns.json")
    }
    field_patterns.append(field_pattern)
    field_pattern = {
        "fieldName": "descriptionRemoteTermPatterns",
        "fieldPatterns": load_term_patterns_from_file("descriptionRemoteTermPatterns.json")
    }
    field_patterns.append(field_pattern)
    return field_patterns


async def load_json_detect_remote_patterns():
    with open("/Users/dwillis/Documents/remoteLdJson") as f:
        ldjson = f.read()

    # Parse JSON into an object with attributes corresponding to dict keys.
    # strict False gets rid of encoding issues
    jobposting = json.loads(ldjson, strict=False)

    return await extract_remote_patterns(jobposting)


# Function to remove tags
async def remove_tags(html):
    # parse html content
    soup = BeautifulSoup(html, "html.parser")

    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)


async def extract_remote_patterns(job_posting, research_patterns):
    try:
        if job_posting.description is not None:
            description_text = await remove_tags(job_posting.description)

            # change non-breaking spaces to space
            non_break_space = u'\xa0'
            description_text = description_text.replace(non_break_space, ' ')

            # the replace parameter changes non utf-8 chars to ? and the byte str is decoded back to a string
            job_posting.description = description_text.encode('utf-8', 'replace').decode('utf-8')

        description_remote_matches = None
        description_false_positive_remote_matches = None
        description_hybrid_matches = None

        description_matches = await extract_remote_patterns_description(job_posting)

        # print(descriptionmatches)

        title_matches = await extract_remote_patterns_title_no_nlp(job_posting)

        # print(titlematches)

        address_locality_matches = await extract_remote_patterns_address_locality_no_nlp(job_posting)
        # print(addresslocalitymatches)

        description_non_remote_matches = await extract_description_non_remote_patterns(job_posting)
        # print(descriptionnonremotematches)

        if research_patterns:
            description_remote_matches = await extract_remote_patterns_description_remote(job_posting)
            # print(descriptionremotematches)

            description_false_positive_remote_matches = await extract_description_false_positive_patterns(job_posting)
            # print(descriptionfalsepositiveremotematches)

            description_hybrid_matches = await extract_hybrid_patterns_description(job_posting)
            # print(descriptionnonremotematches)

        identifier_str = None
        if job_posting.identifier is not None:
            identifier_str = '|'.join(filter(None, [job_posting.identifier.name, job_posting.identifier.value]))

        results = {"descriptionmatches": description_matches,
                   "titlematches": title_matches,
                   "addresslocalitymatches": address_locality_matches,
                   "descriptionnonremotematches": description_non_remote_matches,
                   "jobLocationType": job_posting.jobLocationType,
                   "identifier": identifier_str}

        if research_patterns:
            results["descriptionfalsepositiveremotematches"] = description_false_positive_remote_matches
            results["descriptionremotematches"] = description_remote_matches
            results["descriptionhybridmatches"] = description_hybrid_matches

        return results
    except Exception as error:
        raise GenericException(400, repr(error))


async def extract_remote_patterns_description_remote(job_posting):
    if job_posting.description is None:
        return None

    global description_remote_nlp
    if description_remote_nlp is None:
        load_description_remote_nlp_matcher()

    doc = description_remote_nlp(job_posting.description)

    matches = description_remote_matcher(doc)

    description_remote_matches = []
    for match_id, start, end in matches:
        span = doc[start:end]
        description_remote_matches.append(span.text)
        # print(span.text)

    if len(description_remote_matches) > 0:
        return description_remote_matches

    # print("found 0 matches in description")
    return None


async def extract_hybrid_patterns_description(job_posting):
    if job_posting.description is None:
        return None

    global description_hybrid_nlp
    if description_hybrid_nlp is None:
        load_description_hybrid_nlp_matcher()

    doc = description_hybrid_nlp(job_posting.description)

    matches = description_hybrid_matcher(doc)

    description_hybrid_matches = []
    for match_id, start, end in matches:
        span = doc[start:end]
        description_hybrid_matches.append(span.text)
        # print(span.text)

    if len(description_hybrid_matches) > 0:
        return description_hybrid_matches

    # print("found 0 matches in description")
    return None


async def extract_description_false_positive_patterns(job_posting):
    if job_posting.description is None:
        return None

    global description_false_positive_remote_nlp

    if description_false_positive_remote_nlp is None:
        load_description_false_positive_remote_nlp_matcher()

    doc = description_false_positive_remote_nlp(job_posting.description)

    matches = description_false_positive_remote_matcher(doc)

    description_false_positive_remote_matches = []
    for match_id, start, end in matches:
        span = doc[start:end]
        description_false_positive_remote_matches.append(span.text)

    if len(description_false_positive_remote_matches) > 0:
        return description_false_positive_remote_matches

    return None


async def extract_description_non_remote_patterns(job_posting):
    if job_posting.description is None:
        return None
    doc = description_non_remote_nlp(job_posting.description)

    matches = description_non_remote_matcher(doc)

    description_non_remote_matches = []
    for match_id, start, end in matches:
        span = doc[start:end]
        description_non_remote_matches.append(span.text)

    if len(description_non_remote_matches) > 0:
        return description_non_remote_matches

    return None


async def extract_remote_patterns_description(job_posting):
    if job_posting.description is None:
        return None

    doc = description_nlp(job_posting.description)

    matches = description_matcher(doc)

    descriptionmatches = []
    for match_id, start, end in matches:
        span = doc[start:end]
        descriptionmatches.append(span.text)

    if len(descriptionmatches) > 0:
        return descriptionmatches

    # print("found 0 matches in description")
    return None


async def extract_remote_patterns_title_no_nlp(job_posting):
    if job_posting.title is None:
        return None

    title_matches_with_remote = remote_regex.findall(job_posting.title)

    if len(title_matches_with_remote) > 0:
        return title_matches_with_remote

    # print("found 0 matches in title")
    return None


async def extract_remote_patterns_address_locality_no_nlp(job_posting):
    if job_posting.jobLocation is None:
        return None
    locality = None
    if type(job_posting.jobLocation).__name__ == "list":
        if len(job_posting.jobLocation) == 0:
            return None
        if job_posting.jobLocation[0].address is None:
            return None
        if job_posting.jobLocation[0].address.addressLocality is None:
            return None
        locality = job_posting.jobLocation[0].address.addressLocality
    else:
        if job_posting.jobLocation.address is None:
            return None
        if job_posting.jobLocation.address.addressLocality is None:
            return None
        locality = job_posting.jobLocation.address.addressLocality

    address_locality_matches = remote_regex.findall(locality)

    if len(address_locality_matches) > 0:
        return address_locality_matches

    # print("found 0 matches in address locality matches")
    return None
