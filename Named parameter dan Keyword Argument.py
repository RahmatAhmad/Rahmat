
def pangkat(angka, pangkat = 2):
  hasil = 1
  for i in range(0,pangkat):
    hasil = hasil * angka
  return hasil;
 
print( pangkat(5) )      # 25
print( pangkat(5,4) )    # 625
print( pangkat(6,6) )    # 46656
