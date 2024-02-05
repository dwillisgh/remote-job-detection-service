nlp service to detect whether a job is a remote job
accepts a JobPosting json 
returns matches for these JobPosting fields

description
addresslocality
title

Response
{
    "descriptionmatches": [
        "opportunities to work remotely"
    ],
    "descriptionremotematches": null,
    "addresslocalitymatches": [
        "Remote"
    ],
    "titlematches": null,
    "descriptionfalsepositiveremotematches": null,
    "descriptionnonremotematches": null,
    "descriptionhybridmatches": null,
    "jobLocationType": "TELECOMMUTE"
}
