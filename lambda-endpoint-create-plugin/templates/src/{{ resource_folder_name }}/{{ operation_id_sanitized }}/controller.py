from fastapi import FastAPI, APIRouter, status{% if not should_response_data %}, Response{% endif %}
{{"\n"}}from mangum import Mangum
{% if should_response_as_list %}from typing import List{{"\n"}}{% endif %}
from src.{{ resource_folder_name }}.{{ operation_id_sanitized }} import usecase
{% if should_response_data %}
from src.{{ resource_folder_name }}.{{ operation_id_sanitized }}.models import {% if contain_resource_parameter %}{{ resource_request }}, {% endif %}{{ resource_response }}
{% endif %}


app = FastAPI()
router = APIRouter(tags=["{{ resource_folder_name }}"])


# Route: {{ uri_sanitized }}
@router.{{ method_sanitized }}("{{ uri_sanitized_without_query_parms }}", {% if not should_response_data %}response_class=Response, status_code=status.HTTP_204_NO_CONTENT{% else %}response_model={{ resource_response_full_sanitized }}, {% if method == 'POST' %}status_code=status.HTTP_201_CREATED{% else %}status_code=status.HTTP_200_OK{% endif %}{% endif %})
def {{ operation_id_sanitized }}({% for parameter in parameters %}{{ parameter[0]}}: {{ parameter[1]}}{% if loop.index + 1 <= loop.length %}{{', '}}{% endif %}{% endfor %}):
    {% if should_response_data %}
    return usecase.{{ operation_id_sanitized }}({% for parameter in parameters %}{{ parameter[0]}}{% if loop.index + 1 <= loop.length %}{{', '}}{% endif %}{% endfor %})
    {% else %}
    usecase.{{ operation_id_sanitized }}({% for parameter in parameters %}{{ parameter[0]}}{% if loop.index + 1 <= loop.length %}{{', '}}{% endif %}{% endfor %})
    {% endif %}


app.include_router(router)
handler = Mangum(app)
