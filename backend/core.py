from nodeBlueprints import nodeBlueprints


nodes=[]
inputs=[]
outputs=[]
forms=[]

class Plug:
	def __init__(self,label,parent):
		self.label=label
		self.connected=False
		self.connectedTo=None
		print('created Plug: {0}'.format(id(self)))

	def evaluate(self,evaluationData):
		if self.connected:
			self.connectedTo.evaluate(evaluationData)
		else:
			evaluationData.status='failed'
			evaluationData.traceBack.append('Plug {0} has no connection'.format(id(self)))


class FormElem:
	def __init__(self,label,elemType,parent):
		self.label=label
		self.elemType=elemType
		self.parent=parent
		print('created FormElem: {0}'.format(id(self)))

	def evaluate(self,evaluationData):
		pass


class Node:
	def __init__(self,blueprint):
		self.label=blueprint['label']
		self.inputs=[]
		for input in blueprint['inputs']:
			self.inputs.append(Plug(input['label'],self))
		self.outputs=[]
		for output in blueprint['outputs']:
			self.outputs.append(Plug(output['label'],self))
		self.form=[]
		for elem in blueprint['form']:
			self.form.append(FormElem(elem['label'],elem['type'],self))
		self.evaluated=False
		self.evaluation=False
		print('created Node: {0}'.format(id(self)))

	def evaluate_item(item,evaluationData):
		item.evaluate(evaluationData);

	def evaluate(self,evaluationData):
		if self.evaluated:
			return self.evaluation
		else:
			map(evaluate_item,self.inputs)
			map(evaluate_item,self.outputs)
			map(evaluate_item,self.form)


class EvaluationData:
	def __init__(self):
		self.status='OK'
		self.traceBack=[]

def create_node(name):
	nodes.append(Node(nodeBlueprints[name]))