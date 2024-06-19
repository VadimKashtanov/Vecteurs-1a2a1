#pragma once

#include "insts.cuh"
#include "btcusdt.cuh"

typedef struct {
	//	Insts
	uint      insts;
	Inst_t ** inst ;

	uint la_sortie;
	
	//	Optimisation
	uint         BLOQUES;
	uint *      elements;
	uint ** instructions;
} Mdl_t;

//	Fichiez
Mdl_t * cree_mdl_depuis_st_bin(char * file);
Mdl_t *            ouvrire_mdl(char * file);
void                ecrire_mdl(char * file, Mdl_t * mdl);

//	Mem
void liberer_mdl(Mdl_t * mdl);

//	Plume
void plumer_model  (Mdl_t * mdl);
void mdl_plume_poid(Mdl_t * mdl);
void mdl_plume_grad(Mdl_t * mdl, BTCUSDT_t * btcusdt, uint * ts__d);

//	Optimisation
void mdl_optimisation(Mdl_t * mdl);	// Parraleliser les instructions non inter-dépendantes
void mdl_desoptimiser(Mdl_t * mdl);	// Calculer une apres l'autre

//	Verification
void       mdl_verif(Mdl_t * mdl, BTCUSDT_t * btcusdt);
void tester_le_model(Mdl_t * mdl, BTCUSDT_t * btcusdt);

//	Controle
void  mdl_dy_zero(Mdl_t * mdl);
float mdl_max_abs_grad(Mdl_t * mdl);

//	F(x) & dF(x)
void mdl_f (Mdl_t * mdl, BTCUSDT_t * btcusdt, uint * ts__d);
void mdl_df(Mdl_t * mdl, BTCUSDT_t * btcusdt, uint * ts__d);
//
float* mdl_f__temps(Mdl_t * mdl, BTCUSDT_t * btcusdt, uint * ts__d);
float* mdl_df_temps(Mdl_t * mdl, BTCUSDT_t * btcusdt, uint * ts__d);

//	Scores
float   mdl_S           (Mdl_t * mdl, BTCUSDT_t * btcusdt, uint * ts__d);
float * mdl_pourcent    (Mdl_t * mdl, BTCUSDT_t * btcusdt, uint * ts__d, float coef_puissance);
void    mdl_allez_retour(Mdl_t * mdl, BTCUSDT_t * btcusdt, uint * ts__d);
//
float* mdl_allez_retour_temps(Mdl_t * mdl, BTCUSDT_t * btcusdt, uint * ts__d);