class Module_Mdl:
	bg  = None
	fg  = None
	img = None
	def __init__(self, X=None, Y=None, params=None):
		if X != None:
			assert len(X) == len(self.X)
			self.X = X
		if Y != None:
			assert len(Y) == len(self.Y)
			self.Y = Y
		if params != None:
			assert len(list(params.keys())) == len(list(self.params.keys()))
			self.params = params

	def cree_elements_connections(self):
		self.ix = []
		
		assert sum(int(elm==None) for l,d in self.connections.items() for _,elm in d.items()) == len(self.X)

		for k,v in self.connections.items():
			noniques = []
			for i,inst in enumerate(self.elements[k]):
				for e,entree in enumerate(inst['x']):
					if entree == None:
						noniques += [(i,e)]
			#
			for nn, (i,e) in enumerate(noniques):
				if v[nn] != None:
					x, t = v[nn]
					self.elements[k][i]['x' ][e] = self.elements[x][-1]
					self.elements[k][i]['xt'][e] = abs(t)


					if not self.elements[k][i]['X'][e] == self.elements[x][-1]['y']:
						print("FAUX : self.elements[k][i]['X'][e] == self.elements[x][-1]['y']")
						print(f"k={k} i={i}, e={e} x={x}")
						print(f"{self.elements[k][i]['X'][e]} != {self.elements[x][-1]['y']}")
						raise Exception("Erreur")

		for e,_ix in self.elements.items():
			self.ix += _ix

		#	======================

		for i in self.ix: i['sortie'] = False
		self.ix[-1]['sortie'] = True