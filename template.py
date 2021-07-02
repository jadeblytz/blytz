def basic():
    return '''<template>
\t
</template>

<script>
export default {{

}}
</script>'''.format()

def withProps(LIST):
    propsStr = ''
    for index, item in enumerate(LIST, start=1):
        if index == 1:
            propsStr += '{}: String,\n'.format(item)
        else:
            propsStr += '    {}: String,\n'.format(item)
    return '''<template>
\t
</template>

<script>
export default {{
  props: {{
    {}
  }}
}}
</script>
'''.format(propsStr[:-2])

