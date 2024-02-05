from fastapi import Query
from pydantic import BaseModel, Field
from typing import Optional, List


class RemoteJobDetectionResponse(BaseModel):
    descriptionmatches: Optional[List[str]] = Field(
                                                    description='all phrases found in description that indicate job '
                                                                'is a remote job',
                                                    default=None
                                                    )
    descriptionremotematches: Optional[List[str]] = Field(
                                                    description='remote terms found in description',
                                                    default=None
                                                    )
    addresslocalitymatches: Optional[List[str]] = Field(
                                                    description='all phrases found in addressLocality that indicate '
                                                                'job is a remote job',
                                                    default=None
                                                    )
    titlematches: Optional[List[str]] = Field(
                                                    description='all phrases found in title that indicate '
                                                                'job is a remote job',
                                                    default=None
                                                    )
    descriptionfalsepositiveremotematches: Optional[List[str]] = Field(
                                                    description='all phrases found in description that are '
                                                                'false positives',
                                                    default=None
                                                    )
    descriptionnonremotematches: Optional[List[str]] = Field(
                                                    description='all phrases found in description that indicate '
                                                                'the job is not a remote job',
                                                    default=None
                                                    )
    descriptionhybridmatches: Optional[List[str]] = Field(
                                                    description='all phrases found in description that indicate '
                                                                'the job is a hybrid job',
                                                    default=None
                                                    )
    jobLocationType: Optional[str] = None
