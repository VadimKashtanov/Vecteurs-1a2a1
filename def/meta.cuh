#pragma once

#include "etc.cuh"

#define GRAND_T (1 *  16 )
#define  MEGA_T (1 * 7 * (24))

//	Les Parantèses sont fondamentales !

//Reseaux tanachiques
//	16*16*N
//		  1

//Petits Reseaux Recurrents
//		8*8
//		 24

//Grands Reseaux Recurents
//		 16
//   7*24*2

//	verif_mdl()
//GRAND_T = 64 ou 16*16
// MEGA_T = 4 ou 8

#define t_MODE(t, mega_t) ((t)*MEGA_T + (mega_t))