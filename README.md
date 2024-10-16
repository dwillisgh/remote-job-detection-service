nlp service to detect whether a job is a remote job
accepts a JobPosting json 
returns matches for these JobPosting fields

description
addresslocality
title



running locally you call

post http://0.0.0.0:8000/jobs-remote-job-detection-service/v1/remotejobdetect

Request
Any job posting json object

Response
{
    "descriptionmatches": [
        "remote position",
        "This is a remote position",
        "This is a remote position.",
        "remote position"
    ],
    "descriptionnonremotematches": [
        "this is not a remote position"
    ]
}
