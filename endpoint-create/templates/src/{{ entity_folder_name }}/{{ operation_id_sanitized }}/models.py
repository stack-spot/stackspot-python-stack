from pydantic import BaseModel, Field


class {{entity}}(BaseModel):
    id_: int = Field(..., gt=0, title='Id of the {{entity_sanitized}}.', description='Must be greater than zero')

    class Config:
        schema_extra = {
            "example": {
                "id_": 1
            }
        }

