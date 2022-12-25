import json

def format_json(json_object):
    """Formats JSON object to be more readable"""
    return json.dumps(json_object, indent=2)