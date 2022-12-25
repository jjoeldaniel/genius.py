import json

def format_json(json_object):
    """Formats JSON object to be more readable
    
    Keyword arguments:
        json_object -- The JSON object to format

    Returns:
        JSON object
    """
    return json.dumps(json_object, indent=2)