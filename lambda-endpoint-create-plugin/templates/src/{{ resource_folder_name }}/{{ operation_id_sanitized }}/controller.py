from fastapi import FastAPI, APIRouter
from mangum import Mangum
from src.{{ resource_folder_name }}.{{ operation_id_sanitized }} import usecase
from src.{{ resource_folder_name }}.{{ operation_id_sanitized }}.models import {{ resource }}

app = FastAPI()
router = APIRouter(tags=["{{resource_folder_name}}"])


@router.{{ method_sanitized }}("{{ uri }}", response_model={{ resource }}, responses={404: {"description": "{{ resource }} not found"}})
def {{ operation_id_sanitized }}({% for parameter in parameters %}{{parameter[0]}}: {{parameter[1]}}{% if loop.index + 1 <= loop.length %}{{', '}}{% endif %}{% endfor %}):
    return usecase.{{ operation_id_sanitized }}({% for parameter in parameters %}{{parameter[0]}}{% if loop.index + 1 <= loop.length %}{{', '}}{% endif %}{% endfor %})


app.include_router(router)
handler = Mangum(app)

