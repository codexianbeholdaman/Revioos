_delimiter = "====="
def list_parser(listing):
    return list(map(lambda x: x.strip().replace("'", ''), listing.split('[')[1].split(']')[0].split(',')))

def create_review(title, **kwargs):
    format_element = lambda key, value: f'{key.upper()}: {value}'
    full_res = _delimiter + '\n'
    full_res += format_element('title', title) + '\n'
    for key in kwargs:
        full_res += format_element(key.upper(), kwargs[key]) + '\n'
    return full_res + _delimiter

def parse_entry(post):
    all_entries = []
    for i, entry in enumerate(post.split(_delimiter)):
        if i%2:
            parsed_entry = {}
            last_part = [None, None]
            for line in entry.split('\n'):
                parts = line.split(':')
                if not parts or (len(parts) == 1 and (not parts[0] or parts[0].isspace())):
                    continue
                if parts[0].isupper():
                    if last_part[0] is not None:
                        parsed_entry[last_part[0]] = last_part[1]
                    last_part[1] = ':'.join(parts[1:]) if len(parts)>1 else ''
                    last_part[0] = parts[0]
                else:
                    last_part[1] += '\n' + line
            if last_part[0]:
                parsed_entry[last_part[0]] = last_part[1]
            all_entries.append(parsed_entry)
    return all_entries

def refine_entry(post_dict):
    boolifier = lambda x: True if x.upper()=='TRUE' else False

    res = {}
    for key in post_dict:
        value = post_dict[key]
        if key != 'REVIEW':
            value = value.lstrip()

        processors = {
            'RATING': float,
            'RPG': boolifier,
            'EXTERNAL': boolifier,
            'TAGS': list_parser
        }
        try:
            if key in processors:
                value = processors[key](value)
        except:
            raise RuntimeError(f"The value for a key {key} is unexpected")
        res[key] = value
    return res

def post_processing(post):
    entries = parse_entry(post)
    valid_entries = []
    for entry in entries:
        valid_entries.append(refine_entry(entry))
    return valid_entries
