# Implement function createTemplate which takes string with tags wrapped in {{brackets}} as input and returns closure, which can fill string with data (flat object, where keys are tag names).
#
# template = create_template("{{name}} likes {{animalType}}")
# template(name="John", animalType="dogs") # John likes dogs
# When key doesn't exist in the map, put there empty string.

import re


def create_template(template):
    def fill_template(**data):
        def replace_match(match):
            tag_name = match.group(1).strip()
            return data.get(tag_name, '')

        return re.sub(r'{{(.*?)}}', replace_match, template)

    return fill_template