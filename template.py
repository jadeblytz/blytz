def basic():
    return '''<template>
\t
</template>

<script>
	export default {{

	}}
</script>'''

def withProps(LIST):
    propsStr = ''
    for index, item in enumerate(LIST, start=1):
        if index == 1:
            print("i did it!")
            propsStr += '{}: String,\n'.format(item)
        else:
            propsStr += '\t\t{}: String,\n'.format(item)
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

