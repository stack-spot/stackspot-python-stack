from fastapi import HTTPException
from src.{{resource_folder_name}}.{{operation_id_sanitized}}.models import {{resource}}


def {{ operation_id_sanitized }}({% for parameter in parameters %}{{parameter[0]}}: {{parameter[1]}}{% if loop.index + 1 <= loop.length %}{{', '}}{% endif %}{% endfor %}):
    pass

