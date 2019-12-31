from jinja2 import Template
import os
import sys

if len(sys.argv) < 3:
    print('Usage: docker run -e template_var_1=some ooga/cloud-builder-jinja /path/to/template.jinja /destination/path/out.yaml')
    exit(1)

input_path = sys.argv[1]
output_path = sys.argv[2]
template_vars = dict(os.environ)

with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
    template = Template(input_file.read())
    output_file.write(template.render(template_vars))
