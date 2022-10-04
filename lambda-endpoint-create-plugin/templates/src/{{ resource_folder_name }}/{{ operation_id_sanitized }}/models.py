from pydantic import BaseModel, Field


class {{resource}}(BaseModel):
    id_: int = Field(..., gt=0, title='Id of the {{resource_sanitized}}.', description='Must be greater than zero')

    class Config:
        schema_extra = {
            "example": {
                "id_": 1
            }
        }

