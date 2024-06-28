#include "btcusdt.cuh"

#include "../impl_template/tmpl_etc.cu"

static __global__ void k__f_btcusdt__moyenneK(
	float * moyenneK,
	float * y, float * p1p0,
	uint * ts__d,
	uint P, uint Y,
	uint T)
{
	uint t      = threadIdx.x + blockIdx.x * blockDim.x;
	uint mega_t = threadIdx.y + blockIdx.y * blockDim.y;
	//
	if (t < GRAND_T && mega_t < MEGA_T) {
		uint ty        = t_MODE(t, mega_t);
		uint t_btcusdt = ts__d[t] + mega_t;
		assert(t_btcusdt < T);
		//
		FOR(0, p, P) {
			float _y = y[ty*Y + 1+p];
			assert(_y >= -1 && _y <= +1);
			//
			float _p1p0 = p1p0[t_btcusdt*P + p];
			//
			float _k = K(_y, _p1p0) / (GRAND_T*MEGA_T);
			//
			atomicAdd(&moyenneK[p], _k);
		}
	}
};

static __global__ void k__f_btcusdt(
	float * somme_score,
	float * moyenneK,
	float * y, float * p1p0,
	uint * ts__d,
	uint P, uint Y,
	uint T)
{
	uint t      = threadIdx.x + blockIdx.x * blockDim.x;
	uint mega_t = threadIdx.y + blockIdx.y * blockDim.y;
	//
	if (t < GRAND_T && mega_t < MEGA_T) {
		uint ty        = t_MODE(t, mega_t);
		uint t_btcusdt = ts__d[t] + mega_t;
		assert(t_btcusdt < T);
		//
		float A = y[ty*Y + 0];
		assert(A >= -1 && A <= +1);
		//
		FOR(0, p, P) {
			float _y = y[ty*Y + 1+p];
			assert(_y >= -1 && _y <= +1);
			//
			float _p1p0 = p1p0[t_btcusdt*P + p];
			//
			float _S = S(A, _y, _p1p0);
			assert(_S >= 0);
			//
			atomicAdd(&somme_score[0], _S / moyenneK[p]);
		}
	}
};

float f_btcusdt(BTCUSDT_t * btcusdt, float * y__d, uint * ts__d) {
	uint P = btcusdt->P;
	uint Y = btcusdt->P + btcusdt->A;
	//
	//
	float * moyenneK__d = cudalloc<float>(P);
	k__f_btcusdt__moyenneK<<<dim3(KERD(GRAND_T, 16), KERD(MEGA_T, 8)), dim3(16,8)>>>(
		moyenneK__d,
		y__d, btcusdt->sorties__d,
		ts__d,
		P, Y,
		btcusdt->T
	);
	ATTENDRE_CUDA();
	//
	//
	float * somme__d = cudalloc<float>(1);
	k__f_btcusdt<<<dim3(KERD(GRAND_T, 16), KERD(MEGA_T, 8)), dim3(16,8)>>>(
		somme__d,
		moyenneK__d,
		y__d, btcusdt->sorties__d,
		ts__d,
		P, Y,
		btcusdt->T
	);
	ATTENDRE_CUDA();
	//
	//
	float * somme = gpu_vers_cpu<float>(somme__d, 1);
	//
	float score = somme[0] / ((float)(P * GRAND_T * MEGA_T));
	//
	//
	cudafree<float>(somme__d   );
	cudafree<float>(moyenneK__d);
	    free       (somme      );
	//
	return score;
};