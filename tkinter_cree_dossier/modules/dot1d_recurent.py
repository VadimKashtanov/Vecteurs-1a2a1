from tkinter_cree_dossier.modules._etc import *

from tkinter_cree_dossier.modules.dot1d import *

class RECURENT_DOT1D(Module_Mdl):
	bg, fg = 'light yellow', 'black'
	nom = "[RECURENT_DOT1D]"
	X, Y = [0], [0]
	X_noms, Y_noms = ["X"], ["Y"]
	params = {
		'N f(y[-1])' : 1,
		'N f(x    )' : 1,
		'C0' : 1
	}
	def cree_ix(self):
		#	Params
		N_y   = self.params['N f(y[-1])']
		N_x   = self.params['N f(x    )']
		C0    = self.params[ 'C0'  ]

		#	X, Y
		X = self.X[0]
		Y = self.Y[0]

		#	------------------

		self.elements = {
			'f(x)' : DOT1D__CHAINE    (X=[X],   Y=[Y], params={'H':Y, 'N':N_y, 'C0':C0, 'activ':0}, do=self.do,dc=self.dc).cree_ix(),
			'f(y)' : DOT1D__CHAINE    (X=[Y],   Y=[Y], params={'H':Y, 'N':N_x, 'C0':C0, 'activ':0}, do=self.do,dc=self.dc).cree_ix(),
			'y'    : MODULE_i_Dot1d_XY(X=[Y,Y], Y=[Y], params={                'C0':C0, 'activ':0}, do=self.do,dc=self.dc).cree_ix()
		}

		self.connections = {
			'f(x)' : {0:None},
			'f(y)' : {0:('y', -1)},
			'y'    : {
				0 : ('f(x)', 0),
				1 : ('f(y)', 0),
			}
		}

		self.cree_elements_connections()
		return self.ix

class RECURENT_DOT1D__CHAINE(CHAINE):
	img = img_chaine
	bg, fg = 'light yellow', 'black'
	nom = "[RECURENT_DOT1D] CHAINE"
	X, Y = [0], [0]
	X_noms, Y_noms = ["X"], ["Y"]
	params = {
		'H' : 0,
		'N' : 1,
		'N f(y[-1])' : 1,
		'N f(x    )' : 1,
		'C0' : 1
	}
	#	--------------------------
	H       = 'H'
	N       = 'N'
	ELEMENT = RECURENT_DOT1D

class RECURENT_DOT1D__CHAINE__RESIDUELLE(RESIDUE):
	img = img_chaine_residue
	bg, fg = 'light yellow', 'black'
	nom = "[RECURENT_DOT1D Chaine] Res"
	X, Y = [0], [0]
	X_noms, Y_noms = ["X"], ["Y"] # LSTM [X], [H]
	params = {
		'H' : 0,
		'N' : 1,
		'N f(y[-1])' : 1,
		'N f(x    )' : 1,
		'C0' : 1
	}
	#	--------------------------
	ELEMENT = RECURENT_DOT1D__CHAINE