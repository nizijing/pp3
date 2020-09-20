```html
<father>
	<brother>Mike</brother>
  <sister>Alice</sister>
	<brother>Tom</brother>
  <sister>Juli</sister>
</father>
```

目标：找到Tom下面的sister
```python
for line in bs.xpath('father/brother'):
	if line.xpath('./text()')[0] == 'Tom':
		print(line.xpath('following-sibling::sister/./text()')[0])
```