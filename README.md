# cloud-builder-jinja
Simple jinja step for google cloud builder

## example
```yaml
steps:
  - name: 'ooga/cloud-builder-jinja'
  env:
    - template_var_1=some
  args: ['/workspace/template.jinja', '/workspace/out.yaml']
```
