import os
input = input("Enter ip to ping the host =")
oscommand = 'ping -c 2'
os.system(oscommand +' '+ input)


