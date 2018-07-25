#!/usr/bin/env python2.7

import pythoncyc

# Todos los PGDBs
	# pythoncyc.all_orgids()
	
def PGDB_select(name):
	meta = pythoncyc.select_organism(name)
	return(meta)

def All_pathways(PGDB):
	all_pathways_list=PGDB.all_pathways(selector='all', base=False)
	# Transformo de unicode a ascii
	all_pathways_list=[x.encode('ascii')[1:-1] for x in all_pathways_list]
	return(all_pathways_list)

def All_reactions(PGDB):
	all_reactions_list=PGDB.all_reactions(type='metab-smm')
	# Transformo de unicode a ascii
	all_reactions_list=[x.encode('ascii')[1:-1] for x in all_reactions_list]
	return(all_reactions_list)
