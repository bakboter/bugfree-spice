def tip_en_vloei_wiet (tip, vloei ,wiet):
	print "je hebt %d tips, je hebt %d tips, en je hebt %d wiet" % (tip, vloei ,wiet)
	

print "huppa kijke of jhe jonko kan rolle j ehebt %d tips %d Vloei $d wiet"
tip_en_vloei_wiet (3, 3, 13)

# voor bereiding van funcit bouw voor gedraaiden 
#vloei
print " hoeveel vloei heb je bruine , witte , brede"
bruine_vloei ,witte_vloei = raw_input()
# = raw_input()
brede_vloei = raw_input()
vloei_totaal = bruine_vloei + witte_vloei + brede_vloei
print "hoeveel tips heb je ?"
#tips 
tips_groen = raw_input()
tips_geel = raw_input()
tips_rood = raw_input()
tips_totaal = tips_groen + tips_geel + tips_rood
print " hoeveel wiet heb je "
#wiet 
og_kush  = raw_input()
merry_kush = raw_input()
high_rise = raw_input()
wiet_totaal = og_kush + merry_kush + high_rise
print "hoeveel hasj heb je "
# hashjies 
pollen = raw_input()
nepal = raw_input()
afgaan = raw_input()
hash_totaal = pollen + nepal + afgaan 

print """
Dus je hebt bruine_vloei %r, witte_vloei %r, brede_vloei %r.
je hebt dus tips_groen %r tips_geel %r tips_rood %r
en je hebt og_kush %r merry_kush %r high_rise %raise
en hasj pollen %r nepal %r afgaan %r
""" % (bruine_vloei ,witte_vloei , brede_vloei , tips_groen ,tips_geel ,
	tips_rood ,og_kush ,merry_kush ,high_rise ,pollen ,nepal ,afgaan)