from pydantic import BaseModel, Field

{% if contain_resource_parameter %}

class {{ resource_request }}(BaseModel):
    id_: int = Field(..., gt=0, title='Id of the {{resource_request }}.', description='Must be greater than zero')

    class Config:
        schema_extra = {
            "example": {
                "id_": 1
            }
        }

{% endif %}

class {{ resource_response }}(BaseModel):
    id_: int = Field(..., gt=0, title='Id of the {{resource_response }}.', description='Must be greater than zero')

    class Config:
        schema_extra = {
            "example": {
                "id_": 1
            }
        }
