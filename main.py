c = box(texture =     "https://i.postimg.cc/1X1wWLt6/geulim1.png",size=vec(1,2,1), pos=vec(0,-28,0))
for i in range(50) : 
    for j in range(50) : 
        for k in range(50) :
             box(color=vec(1,i,j), size=vec(30,60,0.5), pos=vec(0,0,0))
      
s1 = box(pos=vec(-4,0,0),size=vec(2,1,2))
s2 = box(pos=vec(-9,-27,0),size=vec(2,1,2))
s3 = box(pos=vec(-6.5,-25.5,0),size=vec(2,1,2))
s4 = box(pos=vec(-4,-24,0),size=vec(2,1,2))
s5 = box(pos=vec(-1.5,-22.5,0),size=vec(2,1,2))
s6 = box(pos=vec(1,-21,0),size=vec(2,1,2))
s7 = box(pos=vec(3.5,-19.5,0),size=vec(2,1,2))
s8 = box(pos=vec(6,-18,0),size=vec(2,1,2))
s9 = box(pos=vec(8.5,-16.5,0),size=vec(2,1,2),color=color.red)
s10 = box(pos=vec(6,-12.5,0),size=vec(2,1,2))
s11 = box(pos=vec(3.5,-11,0),size=vec(2,1,2))
s12 = box(pos=vec(1,-9.5,0),size=vec(2,1,2))
s13 = box(pos=vec(-1.5,-8,0),size=vec(2,1,2))
s14 = box(pos=vec(-4,-6.5,0),size=vec(2,1,2))
s15 = box(pos=vec(-6.5,-5,0),size=vec(2,1,2),color=color.red)
s16 = box(pos=vec(-6.5,5,0),size=vec(2,1,2), color = color.green)
s17 = box(pos=vec(-4,9,0),size=vec(2,1,2),color=color.red)
s18 = box(pos=vec(-4,0,0),size=vec(2,1,2))
s19 = box(pos=vec(-9,-27,0),size=vec(2,1,2))
s20 = box(pos=vec(-6.5,-25.5,0),size=vec(2,1,2))
s21 = box(pos=vec(-4,-24,0),size=vec(2,1,2))
s22 = box(pos=vec(-1.5,-22.5,0),size=vec(2,1,2))
s23 = box(pos=vec(1,-21,0),size=vec(2,1,2))
s24 = box(pos=vec(3.5,-19.5,0),size=vec(2,1,2))
s25 =  box(pos=vec(6,-18,0),size=vec(2,1,2))
s26 = box(pos=vec(8.5,-16.5,0),size=vec(2,1,2),color=color.red)

while True  :
    rate(100)
    k = keysdown()
    if 'w' in k :
        c.pos.y += 0.1
    if 'a' in k :
        c.pos.x -= 0.1
    if 's' in k :
        c.pos.y -= 0.1
    if 'd' in k :
        c.pos.x += 0.1

A = sphere(pos = vec(0,0,0), color = vec(153/255,204/255,1), radius = 3, axis  = vec(0,1,0))
B = ring(pos = vec(0,0,0), color = vec(0,128/255,1), radius = 5, axis  = vec(0,1,0))
C = cone(pos = vec(0,-7,0), color = vec(1,1,0), size = vec(5,5,5), axis = vec(0,1,0) , opacity = 0.2)
 
UFO = compound ([A,B,C])
for part in UFO :
    part. =
