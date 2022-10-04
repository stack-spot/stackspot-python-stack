from fastapi import FastAPI, APIRouter{% if method == 'POST' %}, status{{"\n"}}{% else %}{{"\n"}}{% endif %}
from mangum import Mangum
{% if should_response_as_list %}from typing import List{{"\n"}}{% endif %}
from src.{{ resource_folder_name }}.{{ operation_id_sanitized }} import usecase
from src.{{ resource_folder_name }}.{{ operation_id_sanitized }}.models import {% if contain_resource_parameter %}{{ resource_request }}, {% endif %}{{ resource_response }}


app = FastAPI()
router = APIRouter(tags=["{{resource_folder_name}}"])


@router.{{ method_sanitized }}("{{ uri }}", response_model={{ resource_response_full_sanitized }}{% if method == 'POST' %}, status_code=status.HTTP_201_CREATED{% endif %})
def {{ operation_id_sanitized }}({% for parameter in parameters %}{{parameter[0]}}: {{parameter[1]}}{% if loop.index + 1 <= loop.length %}{{', '}}{% endif %}{% endfor %}):
    return usecase.{{ operation_id_sanitized }}({% for parameter in parameters %}{{parameter[0]}}{% if loop.index + 1 <= loop.length %}{{', '}}{% endif %}{% endfor %})


app.include_router(router)
handler = Mangum(app)
