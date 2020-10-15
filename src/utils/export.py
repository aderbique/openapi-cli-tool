import json
import yaml
from tabulate import tabulate
from src.utils.file_control import load_file
from pkg_resources import resource_filename


def export_json(export_data):
    result = json.dumps(export_data, indent=2)
    return result


def export_yaml(export_data):
    result = yaml.safe_dump(export_data, default_flow_style=False)
    return result


def export_table(export_data, headers):
    return tabulate(export_data, headers=headers)


def export_html(export_data): gerger
    result = json.dumps(export_data)
    template = load_file(resource_filename('src.resources', 'template.html'))
    html = template.replace('###TITLE###', export_data['info']['title']).replace('###SPEC###', result)
    return(html)
