# .PHONY: download_all

SHELL = bash

run:
	# python3 main.py  > nom_valex_telny_comp.tsv
	python3 main.py suffix=ný vallex_path=./data_sources/vallex/Vendula_3.tsv \
	compounding=yes filter_suffixes=[telný,ený,aný]\
	> nom_vallex_telny_comp.tsv

unpack_derinet:
	gzip -dkf ./data_sources/derinet-2-3.tsv.gz

compress_derinet:
	gzip -kf ./data_sources/derinet-2-3.tsv


#use it like: python3 main.py suffix=ný vallex_path=./data_sources/vallex/Vendula_3.tsv compounding=no filter_suffixes=[telný,ený,aný] > nom_vallex_telny_comp.tsv