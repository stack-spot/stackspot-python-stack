{% if should_response_data %}
from src.{{ resource_folder_name }}.{{ operation_id_sanitized }}.models import {% if contain_resource_parameter %}{{ resource_request }}, {% endif %}{{ resource_response }}
{% if should_response_as_list %}from typing import List{{ "\n"}}{% endif %}


{% endif %}
def {{ operation_id_sanitized }}({% for parameter in parameters %}{{ parameter[0]}}: {{ parameter[1]}}{% if loop.index + 1 <= loop.length %}{{', '}}{% endif %}{% endfor %}){% if should_response_data %} -> {{ resource_response_full_sanitized }}{% endif %}:
    {% if not should_response_data %}
    # TODO: implement the logic here
    pass
    {% elif should_response_as_list %}
    {{ resource_response_sanitized }}s = [
        {{ resource_response }}(id_=1),
        {{ resource_response }}(id_=100)
    ]

    return {{ resource_response_sanitized }}s
    {% else %}
    {{ resource_response_sanitized }} = {{ resource_response }}(id_=20)

    return {{ resource_response_sanitized }}
{% endif %}