import time
import datetime
import requests

from os import system

ARONDIRE_AU_MODULO = lambda x,mod: (x + (mod - (x%mod)) if x%mod!=0 else x)

milliseconde = lambda la: int(la * 1000   )*1
seconde      = lambda la: int(la          )*1000
heure        = lambda la: int(la / (60*60))*1000*60*60

requette_bitget = lambda de, a, SYMBOLE, d: eval(
	requests.get(
		f"https://api.bitget.com/api/mix/v1/market/history-candles?symbol={SYMBOLE}_UMCBL&granularity={d}&startTime={de}&endTime={a}&productType=usdt-futures"
	).text
)

HEURES_PAR_REQUETTE = 100

def DONNEES_BITGET(HEURES, d):
	assert d in ('1H', '1m', '15m')
	print(f"L'intervalle choisie est : {d}")
	assert d == '15m'
	#
	HEURES = ARONDIRE_AU_MODULO(HEURES, HEURES_PAR_REQUETTE)
	#
	la = heure(time.time())
	heures_voulues = [
		la - 15*60*1000*i # <<--- 15= 15mins,  60=60mins=1h
		for i in range(ARONDIRE_AU_MODULO(HEURES, HEURES_PAR_REQUETTE))
	][::-1]

	donnees_BTCUSDT = []

	REQUETTES = int(len(heures_voulues) / HEURES_PAR_REQUETTE)
	print(f"Extraction de {len(heures_voulues)} {d} depuis api.bitget.com ...")
	#
	depart = time.time()
	for i in range(REQUETTES):
		paquet_heures_btc = requette_bitget(
			heures_voulues[ i   *HEURES_PAR_REQUETTE  ],
			heures_voulues[(i+1)*HEURES_PAR_REQUETTE-1],
			"BTCUSDT",
			d
		)
		donnees_BTCUSDT += paquet_heures_btc

		if i % 1 == 0:
			pourcent = i*HEURES_PAR_REQUETTE/len(heures_voulues)
			print(f"[{round(pourcent*100,2)}%],   len(paquet_heures_btc)={len(paquet_heures_btc)}, (btc,)  reste={(round((time.time()-depart)/pourcent*(1-pourcent)/60) if pourcent!=0 else 0)} mins   len(donnees_BTCUSDT)={len(donnees_BTCUSDT)}")

	print(f"HEURES VOULUES = {len(heures_voulues)}, len(donnees_BTCUSDT)={len(donnees_BTCUSDT)}")

	return donnees_BTCUSDT

#	Ancien site : https://www.CryptoDataDownload.com

def faire_un_csv(donnees_BTCUSDT, NOM="bitgetBTCUSDT"):
	csv = """https://www.bitget.com/api-doc/contract/market/Get-History-Candle-Data
Unix,Date,Symbol,Open,High,Low,Close,Volume,Volume Base Asset,tradecount\n"""

	for _,o,h,l,c,vB,vU in donnees_BTCUSDT[::-1]:
		csv += f'0,0,{NOM},{o},{h},{l},{c},{vU},{vB},0\n'

	return csv

if __name__ == "__main__":
	_15m = (2024-2020)*365 * 24 * 4
	donnees = DONNEES_BITGET(_15m, d='15m')
	csv = faire_un_csv(donnees, NOM="BTCUSDT")

	with open("prixs/BTCUSDT_bitget_2020_2024.csv", 'w') as co: co.write(csv)