class Inst:
	def __init__(self, X=[], Y=0, params=[], do=0, dc=0):
		self.X      = X
		self.Y      = Y
		self.params = params

		self.do = do
		self.dc = dc

		assert len(self.params) == len(self.params_str)

	def assert_coherance(self):
		raise Exception("Doit etre implémenté")

############################################ 

class i__Entree(Inst):
	nom = "_entrée"
	params = []
	params_str = []
	X = [0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 1
		assert self.X[0] == self.Y

		#	Params
		assert len(self.params) == 0

############################################

class i_Activation(Inst):
	nom = "activ(x)"
	params = [0]
	params_str = ['activ']
	X = [0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 1
		assert self.X[0] == self.Y

		#	Params
		assert len(self.params) == 1
		#       tanh, logistic, gauss, relu
		#activs = (0,     1,       2,     3)
		#assert self.params[0] in activs

class i_Biais(Inst):
	nom = "+b"
	params = []
	params_str = []
	X = []
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 0
		assert self.Y > 0

		#	Params
		assert len(self.params) == 0

class i_Cadrans_Pondérés(Inst):
	nom = "Cadrans Pondérés"
	params = [0,1,1]
	params_str = ['Cx', 'C0', 'C1']
	X = [0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 1
		assert self.Y > 0
		assert self.X[0] > 0

		#	Params
		assert len(self.params) == 3

		Cx = self.params[0]
		C0 = self.params[1]
		C1 = self.params[2]

		assert self.Y == Cx*C1
		assert self.X[0] == Cx*C0

class i_Const(Inst):
	nom = "cst"
	params = ['const']
	params_str = [1]
	X = []
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 0
		assert self.Y > 0

		#	Params
		assert len(self.params) == 1

############################################

class i_Dot1d_X(Inst):
	nom = "Dot1d X"
	params = [0,0]
	params_str = ['C0', 'activ']
	X = [0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 1
		#assert self.X[0] == self.Y

		#	Params
		assert len(self.params) == 2
		C0 = self.params[0]
		assert self.X[0] % C0 == 0
		assert self.Y    % C0 == 0
		#       tanh, logistic, gauss, relu
		#activs = (0,     1,       2,     3)
		#assert self.params[1] in activs

class i_Dot1d_XY(Inst):
	nom = "Dot1d XY"
	params = [0,0]
	params_str = ['C0', 'activ']
	X = [0,0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 2
		#assert self.X[0] == self.Y == self.X[1]

		#	Params
		assert len(self.params) == 2
		C0 = self.params[0]
		assert self.X[0] % C0 == 0
		assert self.X[1] % C0 == 0
		assert self.Y    % C0 == 0
		#       tanh, logistic, gauss, relu
		#activs = (0,     1,       2,     3)
		#assert self.params[1] in activs

############################################

class i_Kconvl1d(Inst):
	nom = "Kconvl1d"
	params = [0,0,0,0,0]
	params_str = ['K', 'C0', 'C1', 'im_X', 'im_Y']
	X = [0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 1
		assert self.Y > 0

		#	Params
		assert len(self.params) == 5
		K, C0, C1, im_X, im_Y = self.params

		N = (K-1)/2

		assert N > 0
		assert C0 > 0
		assert C1 > 0
		assert im_X > 0
		assert im_Y > 0

		assert im_Y == im_X-N-N

		assert self.X[0] == C0*im_X
		assert self.Y    == C1*im_Y #(im_X-2*N)*(im_Y-2*N)

class i_Kconvl1d_stricte(Inst):
	nom = "Kconvl1d stricte"
	params = [0,0,0,0]
	params_str = ['K', 'C0', 'C1', 'im_X']
	X = [0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 1
		assert self.Y > 0

		#	Params
		assert len(self.params) == 4
		K, C0, C1, im_X = self.params

		N = (K-1)/2

		assert N > 0
		assert C0 > 0
		assert C1 > 0
		assert im_X > 0

		assert self.X[0] == C0*im_X
		assert self.Y    == C1*im_X #(im_X-2*N)*(im_Y-2*N)

class i_Kconvl2d_stricte(Inst):
	nom = "Kconvl2d stricte"
	params = [0,0,0,0,0]
	params_str = ['K', 'C0', 'C1', 'im_X', 'im_Y']
	X = [0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 1
		assert self.Y > 0

		#	Params
		assert len(self.params) == 5
		K, C0, C1, im_X, im_Y = self.params

		N = (K-1)/2

		assert N > 0
		assert C0 > 0
		assert C1 > 0
		assert im_X > 0
		assert im_Y > 0

		assert self.X[0] == C0*im_X*im_Y
		assert self.Y    == C1*im_X*im_Y #(im_X-2*N)*(im_Y-2*N)

############################################

class i_MatMul(Inst):
	nom = "x@P"
	params = []
	params_str = []
	X = [0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 1
		assert self.Y > 0

		#	Params
		assert len(self.params) == 0

class i_MatMul_Canal(Inst):
	nom = "x@P Canal"
	params = [1,1,1]
	params_str = ['C0', 'C1', 'M']
	X = [0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 1
		assert self.Y > 0

		#	Params
		assert len(self.params) == 3

		C0, C1, M = self.params

		assert all(i>0 for i in self.params)

		assert self.X[0] % C0 == 0
		assert self.Y    % C1 == 0

		assert C0 % M == 0
		assert C1 % M == 0

class i_Matmul2d_Sans_Poids(Inst):
	nom = "A@B 2D"
	params = [1,1,1,1]
	params_str = ['Ax', 'Ay', 'Bx', 'C0']
	X = [0,0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 2
		assert self.Y > 0
		assert self.X[0] > 0
		assert self.X[1] > 0

		#	Params
		assert len(self.params) == 4

		Ax, Ay, Bx, C0 = self.params

		assert all(i>0 for i in self.params)

		assert self.X[0] == C0*Ax*Ay
		assert self.X[1] == C0*Ax*Bx

		assert self.Y == C0*Ay*Bx

############################################

class i_Mul2(Inst):
	nom = "A*B"
	params = []
	params_str = []
	X = [0,0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 2
		assert self.Y == self.X[0] == self.X[1]

		#	Params
		assert len(self.params) == 0

class i_Mul3(Inst):
	nom = "A*B*C"
	params = []
	params_str = []
	X = [0,0,0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 3
		assert self.Y == self.X[0] == self.X[1] == self.X[2]

		#	Params
		assert len(self.params) == 0

############################################

class i_Pool2_1d(Inst):
	nom = "pool2x1 1d"
	params = [0,0]
	params_str = ["C0", "X"]
	X = [0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 1

		#	Params
		assert len(self.params) == 2
		C0, _X = self.params
		assert C0 > 0
		assert _X > 0
		
		assert self.X[0] == (C0 * _X)
		assert _X % 2 == 0
		assert self.Y == int(C0 * _X/2)

class i_Pool2x2_2d(Inst):
	nom = "pool2x2 2d"
	params = [0,0,0]
	params_str = ["C0", "X", "Y"]
	X = [0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 1

		#	Params
		assert len(self.params) == 3
		C0, _X, _Y = self.params
		assert C0 > 0
		assert _X > 0
		assert _Y > 0
		
		assert self.X[0] == (C0 * _X * _Y)
		assert _X % 2 == 0
		assert _Y % 2 == 0
		assert self.Y == int(C0 * _X/2 * _Y/2)

############################################

class i_Somme(Inst):
	nom = "Somme"
	params = [1]
	params_str = ['C0']
	X = [0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 1
		assert self.Y == self.params[0]

		#	Params
		assert len(self.params) == 1

		assert self.params[0] > 0 #i_Somme C0>0

############################################

class i_Somme2(Inst):
	nom = "A+B"
	params = []
	params_str = []
	X = [0,0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 2
		assert self.Y == self.X[0] == self.X[1]

		#	Params
		assert len(self.params) == 0

class i_Somme3(Inst):
	nom = "A+B+C"
	params = []
	params_str = []
	X = [0,0,0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 3
		assert self.Y == self.X[0] == self.X[1] == self.X[2]

		#	Params
		assert len(self.params) == 0

class i_Somme4(Inst):
	nom = "A+B+C+D"
	params = []
	params_str = []
	X = [0,0,0,0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 4
		assert self.Y == self.X[0] == self.X[1] == self.X[2] == self.X[3]

		#	Params
		assert len(self.params) == 0

##########################################

class i_Sub2(Inst):
	nom = "A-B"
	params = []
	params_str = []
	X = [0,0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 2
		assert self.Y == self.X[0] == self.X[1]

		#	Params
		assert len(self.params) == 0

##########################################

class i_Vect_Div_Unitair(Inst):
	nom = "x0/x1[0]"
	params = [1]
	params_str = ['C0']
	X = [0,0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 2
		assert self.Y == self.X[0]
		assert self.X[1] == self.params[0]

		#	Params
		assert len(self.params) == 1
		assert self.params[0] > 0 #C0 de Vect_Div_Unitair

##########################################

class i_Y(Inst):
	nom = "Y"
	params = []
	params_str = []
	X = [0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 1
		assert self.Y == self.X[0]

		#	Params
		assert len(self.params) == 0

class i_Y_canalisation(Inst):
	nom = "Y canalisation"
	params = [0]
	params_str = ['C0']
	X = [0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 1
		#assert self.Y == self.X[0]

		#	Params
		assert len(self.params) == 1
		C0 = self.params[0]
		assert self.Y == self.X[0] * C0

class i_Y_union_2(Inst):
	nom = "Y_union_2"
	params = []
	params_str = []
	X = [0,0]
	Y =  0

	def assert_coherance(self):
		assert len(self.X) == 2
		assert self.Y == (self.X[0]+self.X[1])

		#	Params
		assert len(self.params) == 0

##########################################
liste_insts = [
	i__Entree,
	#
	i_Activation,
	i_Biais,
	i_Cadrans_Pondérés,
	i_Const,
	#
	i_Dot1d_X,
	i_Dot1d_XY,
	#
	i_Kconvl1d,
	i_Kconvl1d_stricte,
	i_Kconvl2d_stricte,
	#
	i_MatMul,
	i_MatMul_Canal,
	#
	i_Matmul2d_Sans_Poids,
	#
	i_Mul2,
	i_Mul3,
	#
	i_Pool2_1d,
	i_Pool2x2_2d,
	#
	i_Somme,
	#
	i_Somme2,
	i_Somme3,
	i_Somme4,
	#
	i_Sub2,
	#
	i_Vect_Div_Unitair,
	#
	i_Y,
	i_Y_canalisation,
	i_Y_union_2
]