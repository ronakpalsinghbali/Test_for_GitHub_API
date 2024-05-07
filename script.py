# from jinja2 import Template
# import yaml

# # Read the YAML template from the file
# with open('temp.yaml', 'r') as file:
#     yaml_template = file.read()

# # Define your variables
# variables = {
#     'variable1': 'us-central1',
#     'variable2': 'ceq-autopark'
# }

# # Render the template with your variables
# template = Template(yaml_template)
# rendered_yaml = template.render(variables)

# print(rendered_yaml)
# # Now you can use rendered_yaml as your YAML configuration


from jinja2 import Template
import os

# Read the YAML template from the file
with open('temp.yaml', 'r') as file:
    yaml_template = file.read()

# Fetch values from GitHub inputs
variable1 = os.getenv('INPUT_VARIABLE1')
variable2 = os.getenv('INPUT_VARIABLE2')

# Define your variables
variables = {
    'variable1': variable1,
    'variable2': variable2
}

# Render the template with your variables
template = Template(yaml_template)
rendered_yaml = template.render(variables)

print(rendered_yaml)
# Write the rendered YAML output to a new file named new.yaml
with open('new.yaml', 'w') as file:
    file.write(rendered_yaml)
