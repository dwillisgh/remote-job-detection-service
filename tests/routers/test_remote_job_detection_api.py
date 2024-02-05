from fastapi.testclient import TestClient

from app.main import app


def test_remote_job_detect_api():
    ldjson = {
        "description": "This is a remote position",
        "title": "software engineer",
        "jobLocationType": "TELECOMMUTE",
        "jobLocation": {
            "@type": "Place",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Remote",
                "addressCountry": "US"
            }
        }
    }

    with TestClient(app) as client:
        response = client.post("/jobs-remote-job-detection-service/v1/remotejobdetect",
                               json=ldjson)
        print(response.status_code)
        print(response.text)
        assert response.status_code == 200