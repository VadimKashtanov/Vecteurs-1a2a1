#pragma once

#include "mdl.cuh"

#define L2_regularisation 0.0
#define ADAM 0
#define ADAM_HISTOIRE 2

void adam(
	Mdl_t   *  mdl,
	float *** hist,	//[hist][inst][p]
	uint         i,
	float    alpha
);

void opti(
	Mdl_t     *     mdl,
	BTCUSDT_t * btcusdt,
	uint      *   ts__d,
	uint              I,
	uint       tous_les,
	uint        methode,
	float         alpha
);