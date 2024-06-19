from tkinter_cree_dossier.modules._etc import *

from tkinter_cree_dossier.modules.dot1d import DOT1D__CHAINE

class RESEAU(Module_Mdl):
	bg = 'cyan'
	fg = 'black'
	nom = "RESEAU"
	X, Y = [0], [0]
	X_noms, Y_noms = ["X"], ["Y"] # LSTM [X], [H]
	params = {
		'H' : 1,
		'N' : 0,
		'activ cachée' : 0,
		'activ sortie' : 0,
	}
	def cree_ix(self):
		#	Params
		N = self.params['N']
		H = self.params['H']

		ac_ca = self.params['activ cachée']
		ac_so = self.params['activ sortie']

		X = self.X[0]
		Y = self.Y[0]

		assert N > 1
		assert H > 1

		#	------------------

		self.elements = {
			'reseau'     : DOT1D__CHAINE      (X=[X], Y=[Y], params={'N':N, 'H':H, 'C0':1, 'activ':ac_ca}).cree_ix(),
			'activation' : MODULE_i_Activation(X=[Y], Y=[Y], params={'activ':ac_so}).cree_ix()
		}
		self.connections = {
			'reseau'     : {0:None},
			'activation' : {0:('reseau', 0)}
		}

		self.cree_elements_connections()
		return self.ix