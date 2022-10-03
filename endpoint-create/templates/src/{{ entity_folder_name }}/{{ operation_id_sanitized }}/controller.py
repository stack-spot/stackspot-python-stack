from fastapi import FastAPI, APIRouter
from mangum import Mangum
from src.{{ entity_folder_name }}.{{ operation_id_sanitized }} import usecase
from src.{{ entity_folder_name }}.{{ operation_id_sanitized }}.models import {{ entity }}

app = FastAPI()
router = APIRouter(tags=["{{entity_folder_name}}"])


@router.{{ method_sanitized }}("{{ uri }}", response_model={{ entity }}, responses={404: {"description": "{{ entity }} not found"}})
def {{ operation_id_sanitized }}({% for parameter in parameters %}{{parameter[0]}}: {{parameter[1]}}{% if loop.index + 1 <= loop.length %}{{', '}}{% endif %}{% endfor %}):
    return usecase.{{ operation_id_sanitized }}({% for parameter in parameters %}{{parameter[0]}}{% if loop.index + 1 <= loop.length %}{{', '}}{% endif %}{% endfor %})


app.include_router(router)
handler = Mangum(app)

