nodeBlueprints = [
	{
		'label': 'Sum',
		'inputs':[
			{
				'label':'A'
			},
			{
				'label':'B'
			}
		],
		'outputs':[
			{
				'label':'O'
			}
		],
		'form':[]
	},
	{
		'label': 'Merge',
		'inputs':[
			{
				'label':'A'
			},
			{
				'label':'B'
			}
		],
		'outputs':[
			{
				'label':'O'
			}
		],
		'form':[
			{
				'label':'Column to merge from A',
				'type':'Slct'
			},
			{
				'label':'Column to merge from B',
				'type':'Slct'
			}
		]
	}
]