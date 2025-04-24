# .PHONY: download_all

SHELL = bash

run:
	python3 main.py  > nom_valex_telny.tsv

unpack_derinet:
	gzip -dkf ./data_sources/derinet-2-3.tsv.gz

compress_derinet:
	gzip -kf ./data_sources/derinet-2-3.tsv


#use it like: python3 main.py suffix=icí vallex_path=./data_sources/vallex/Vendula_3.tsv > nom_vallex_ici2.tsv