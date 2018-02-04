import re


def fuzzy_finder(user_input, collection):
        suggestions = []
        pattern = '.*'.join(user_input)  # Converts 'djm' to 'd.*j.*m'
        regex = re.compile(pattern)      # Compiles a regex.
        for item in collection:
            match = regex.search(item.title+item.original_title)  # Checks if the current item matches the regex.
            if match:
                suggestions.append((len(match.group()), match.start(), item))
        return [x for _, _, x in suggestions]
