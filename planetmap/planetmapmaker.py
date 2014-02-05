import PIL
from PIL import Image

#print 'A'
#universe = Image.new('RGB',(128000,256000),(0,0,0))
#print 'B'
#stars =Image.open('stars7.png')

#uX,uY = universe.size

#for yit in range(uX/800):
#	print yit
#	for vapp in range(uY/800):
#		print yit, vapp
#		universe.paste(stars,(yit*800,vapp*800))

stars = Image.open('stars7.png')

for yit in range(160):
	for vapp in range(320):
		stars.save(str(yit)+'x'+str(vapp)+'.png')

#universe.save('planetmap.png')