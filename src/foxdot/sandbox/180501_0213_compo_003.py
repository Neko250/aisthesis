Scale.default = Scale.minor
Root.default = 0
Clock.bpm = 120

p1 >> sitar(P[0,1,2,3],)
p1 >> sitar(P[0,1,2,3],dur=PDur(3,8)*2,)
p1 >> sitar(P[0,1,2,3],dur=PDur(3,8)*2,) + var([0,2])
p1 >> sitar(P[0,1,2,[3,5]],dur=PDur(3,8)*2,) + var([0,2])
p1 >> sitar(P[0,1,2,[3,(5,7)]],dur=PDur(3,8)*2,) + var([0,2])
p1 >> sitar(P[0,[1,3],2,[3,(5,7)]],dur=PDur(3,8)*2,) + var([0,2])
p1 >> sitar(P[0,[1,3],2,[3,(5,7)]],dur=PDur(3,8)*2,) + var([0,2,-1,3])
p1 >> sitar(P[0,[1,3],2,[3,(5,7)]],dur=PDur(3,8)*2,echo=(0,0.25),) + var([0,2,-1,3])
p1 >> sitar(P[0,[1,3],2,[3,(5,7)]],dur=PDur(3,8)*2,echo=(0,0.25),pan=(-1,1),) + var([0,2,-1,3])
p1 >> sitar(P[0,[1,3],2,[3,(5,7)]],dur=PDur(3,8)*2,echo=(0,0.25),pan=linvar([0,-1,0,1]),) + var([0,2,-1,3])
p1 >> sitar(P[0,[1,3],2,[3,(5,7)]],dur=PDur(3,8)*2,echo=(0,0.25),pan=linvar([0,-1,0,1]),chop=256,) + var([0,2,-1,3])
p1 >> sitar(P[0,[1,3],2,[3,(5,7)]],dur=PDur(3,8)*2,echo=(0,0.25),pan=linvar([0,-1,0,1]),chop=256,coarse=1,) + var([0,2,-1,3])
p1 >> sitar(P[0,[1,3],2,[3,(5,7)]],dur=PDur(3,8)*2,echo=(0,0.25),pan=linvar([0,-1,0,1]),chop=256,coarse=1,amp=PWhite(1),) + var([0,2,-1,3])

b1 >> bass(oct=4,).spread()
b1 >> bass(oct=PRand([4,5]),).spread()
b1 >> bass(oct=PRand([4,5]),lpf=800,).spread()
b1 >> bass(oct=PRand([4,5]),lpf=800,).spread().follow(p1)
b1 >> bass(oct=PRand([4,5]),lpf=800,).spread().follow(p1).every(5,"offadd",3)
b1 >> bass(oct=PRand([4,5]),lpf=800,chop=2,).spread().follow(p1).every(5,"offadd",3)
b1 >> bass(oct=PRand([4,5]),lpf=800,chop=1,).spread().follow(p1).every(5,"offadd",3)
b1 >> bass(oct=PRand([4,5]),lpf=800,chop=1,).spread().follow(p1).every(5,"offadd",3).every(3,"stutter",4,dur=3)
b1 >> bass(oct=PRand([4,5]),lpf=400,lpr=linvar([0.1,1],8),chop=1,).spread().follow(p1).every(5,"offadd",3).every(3,"stutter",4,dur=3)

p2 >> star(p1.degree,dur=8,)
p2 >> star(p1.degree,dur=8,hpf=2500,)
p2 >> star(p1.degree,dur=8,hpf=0,coarse=12,formant=1,)
p2 >> star(p1.degree,dur=8,hpf=0,coarse=12,formant=1,shape=0.25,)
p2 >> star(p1.degree,dur=8,hpf=0,coarse=12,formant=1,shape=0.5,)
p2 >> star(p1.degree,dur=8,hpf=0,coarse=12,formant=1,shape=0.75,)
p2 >> star(p1.degree,dur=8,hpf=0,coarse=12,formant=1,shape=1,)
p2 >> star(p1.degree,dur=8,hpf=0,coarse=12,formant=1,shape=0.75,)
p2 >> star(p1.degree,dur=8,hpf=0,coarse=12,formant=1,shape=0.5,)
p2 >> star(p1.degree,dur=8,hpf=0,coarse=12,formant=1,shape=0.5,pan=PWhite(-0.5,0.5),)

Group(p1,p2).only()

p3 >> piano(p1.degree,dur=8,sus=p3.dur-1.5,)
p3 >> piano(p1.degree,dur=8,sus=p3.dur-1.5,).every(4,"offadd",[P*(2,4),P*(2,4,7)])
p3 >> piano(p1.degree,dur=8,sus=p3.dur-1.5,).every(4,"offadd",[P*(2,4),P*(2,4,7)]).spread()
p3 >> piano(p1.degree,dur=8,sus=p3.dur-1.5,shape=2,).every(4,"offadd",[P*(2,4),P*(2,4,7)]).spread()
p3 >> piano(p1.degree,dur=8,sus=p3.dur-1.5,shape=2,delay=(0,0.5),).every(4,"offadd",[P*(2,4),P*(2,4,7)]).spread()
p3 >> piano(p1.degree,dur=8,sus=p3.dur-1.5,shape=2,delay=(0,0.25),).every(4,"offadd",[P*(2,4),P*(2,4,7)]).spread()
p3 >> piano(p1.degree,dur=8,sus=p3.dur-1.5,shape=2,delay=0,).every(4,"offadd",[P*(2,4),P*(2,4,7)]).spread()
p3 >> piano(p1.degree,dur=8,sus=p3.dur-1.5,shape=2,delay=0,dist=0.0125,).every(4,"offadd",[P*(2,4),P*(2,4,7)]).spread()
p3 >> piano(p1.degree,dur=8,sus=p3.dur-1.5,shape=2,delay=0,dist=0.0125,).every(4,"offadd",[P*(2,4),P*(2,4,7)]).spread()

c2 >> play("p",sample=PRand(5),)
c2 >> play("{ppP[pp]}",sample=PRand(5),)
c2 >> play("{ppP[pp]}",sample=PRand(5),pan=PWhite(-1,1),)
c2 >> play("{ppP[pp]}",sample=PRand(5),pan=PWhite(-1,1),rate=PRand([1,.8,1.2]),)
c2 >> play("{ppP[pp]}",sample=PRand(5),pan=PWhite(-1,1),rate=PRand([1,.8,1.2]),room=0.5,)
c2 >> play("{ppP[pp]}",sample=PRand(5),pan=PWhite(-1,1),rate=PRand([1,.8,1.2]),room=0.5,verb=0.2,)
c2 >> play("{ppP[pp]}",sample=PRand(5),pan=PWhite(-1,1),rate=PRand([1,.8,1.2]),room=0.5,verb=linvar([0,1],8),)
c2 >> play("{ppP[pp]}",sample=PRand(5),pan=PWhite(-1,1),rate=PRand([1,.8,1.2]),room=linvar([0,1],16),verb=linvar([0,1],8),)
c2 >> play("{ppP[pp]}",sample=PRand(5),pan=PWhite(-1,1),rate=PRand([1,.8,1.2]),room=linvar([0,1],12),verb=linvar([0,1],8),)
c2 >> play("{ppP[pp]}",sample=PRand(5),pan=PWhite(-1,1),rate=PRand([1,.8,1.2]),room=linvar([0,1],12),verb=linvar([0,1],8),hpf=linvar([0,4000],12),hpr=linvar([0.1,1],17),)
c2.solo()
c2 >> play("{ppP[pp]}",sample=PRand(5),pan=PWhite(-1,1),rate=PRand([1,.8,1.2]),room=linvar([0,1],12),verb=linvar([0,1],8),hpf=PWhite(0,5000),hpr=linvar([0.1,1],17),)
c2 >> play("{ppP[pp]}",sample=PRand(5),pan=PWhite(-1,1),rate=PRand([1,.8,1.2])*PRand([1,1,2,1/2]),room=linvar([0,1],12),verb=linvar([0,1],8),hpf=PWhite(0,5000),hpr=linvar([0.1,1],17),)
c2 >> play("{ppP[pp]}",sample=PRand(5),pan=PWhite(-1,1),rate=PRand([1,.8,1.2])*PRand([1,1,2,1/2,-1]),room=linvar([0,1],12),verb=linvar([0,1],8),hpf=PWhite(0,5000),hpr=linvar([0.1,1],17),)
c2 >> play("{ppP[pp]}",sample=PRand(5),pan=PWhite(-1,1),rate=PRand([1,.8,1.2])*PRand([1,1,2,1/2,-1]),room=linvar([0,1],12),verb=linvar([0,1],8),hpf=PWhite(0,5000),hpr=linvar([0.1,1],17),lpf=4000,)
c2 >> play("{ppP[pp]}",sample=PRand(5),pan=PWhite(-1,1),rate=PRand([1,.8,1.2])*PRand([1,1,2,1/2,-1]),room=linvar([0,1],12),verb=linvar([0,1],8),hpf=PWhite(0,5000),hpr=linvar([0.1,1],17),lpf=PRand([0,400,4000]),)