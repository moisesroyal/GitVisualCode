countries = {'mex','col','arg','usa'}
northAm = {'usa','canada'}
centralAm = {'mex','gt','bz'}
southAm = {'col','bz','arg'}

new_set = set()
new_set = countries | northAm | centralAm | southAm
print(new_set)