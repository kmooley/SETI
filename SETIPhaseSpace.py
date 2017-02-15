########## Define the dictionary of individual searches to be plotted

seti_dict = \
{0:{'ref'  : 'Drake+1960',  # Reference
    'tel'  : 'NRAO-300ft',  # Telescope
    'freq' : 1.420,         # Approx. observing frequency (GHz)
    'dist' : [10.5,12],     # distance (ly)
    'sens' : 1e-22,         # Sensitivity (W/m^2)
    'res'  : 100,           # Spectral resolution (Hz)
    'hours': 200,           # Obseving time (hr)
    'xytxt': [92000,20,0],  # [x,y] Location of the label on the plot
    'comment': '2 stars - epsilon eridani and tau ceti'}, # Title of the entry on 
 1:{'ref'  : 'Cohen+1980',
    'tel'  : 'Haystack,Arecibo,Parkes',
    'freq' : 1.67,
    'dist' : array([4.6,50,50,16.7,13,8.8,14,6.7,7.2,6.3,14.3,17,3.3,5,4.4,8.9,3.1,34,9.8,50,50,8.3,21])*1e3*3.26,
    'sens' : array([6.6e17,1.2e20,2.4e20,1.8e18,3.4e18,5e17,2.6e18,2.8e17,2.5e18,3.7e17,8.1e18,3e18,\
                5.2e17,5e17,3e17,6.9e17,6.7e16,8.6e18,5.4e17,1.2e20,2.4e20,1.1e18,\
                2.5e18])/(4*pi*(array([4.6,50,50,16.7,13,8.8,14,6.7,7.2,6.3,14.3,17,3.3,5,4.4,8.9,3.1,34,9.8,50,50,8.3,21])*1e3*pc)**2),
    'res'  : 9500,
    'hours': 40,
    'xytxt': [10,2500,0],
    'comment': '25 Globular Clusters'},
 2:{'ref'  : 'Cole+1979', 
    'tel'  : 'Parkes',
    'freq' : 5,
    'dist' : 6*3.26,
    'sens' : 4e-18,
    'res'  : 10**7,
    'hours': 50,
    'xytxt': [0,0,0],
    'comment': 'Nearby F, G and K stars'},
 3:{'ref'  : 'Valdes+1986', 
    'tel'  : 'HCRO',
    'freq' : 1.5,
    'dist' : array([760000.0,790000.0,900000.0,187.0,2.6,3.5,3.6,27.8,250.0,3.2,140.0,200.0,5.0,200.0,90.9,13.2,5.6,412.3,5.8,200.0,\
                    5.6,125.0,6.0,3500000.0,17000000.0,1400.0,1.8,333.3,5500.0,500000.0,5.1,166.7,595.2,3125.0,166.0,65000000.0])*3.26,
    'sens' : array([7.9,7.4,4.1,7.9,7.4,7.4,5.9,7.9,7.4,7.4,13.6,7.4,7.9,7.4,6.4,7.9,7.4,7.4,7.4,7.4,6.9,11.8,7.4,7.4,7.4,7.9,7.4,7.4,\
                    7.4,11.8,7.9,7.9,7.4,7.9,7.9,7.4])*1e-24,
    'res'  : 4.883e3,
    'hours': 100,
    'xytxt': [80,280000,0],
    'comment': '80 STARS & 12 NEARBY STARS'},
 4:{'ref'  : 'Biraud+1997', 
    'tel'  : 'NANCAY',
    'freq' : 1.420,
    'dist' : array([15.6,14.1, 18.0, 5.8])*3.26,
    'sens' : 1e-24,
    'res'  : 50,
    'hours': 40,
    'xytxt': [550,80,0],
    'comment': ' 4 stars with giant planets (51 Peg, 47 UMa, 70 Vir, Gl 229)'},
 5:{'ref'  : 'Shirai+2002', 
    'tel'  : 'VLA',
    'freq' : 22,
    'dist' : array([30,35.9,22.4,3.22,33,42.4,33.4,16.7,17,20,21.3,14.7,19.7])*3.26,
    'sens' : array([3,5.2,9.5,7.1,8.9,2.2,2.4,3.4,6.7,6.2,2.4,6.3,2.4])*1e-3*1e-26*6.1e3,
    'res'  : 6.1e3,
    'hours': 4,
    'xytxt': [4,200,0],
    'comment': '13 exoplanetary systems'},
 6:{'ref'  : 'Shostak+1996', 
    'tel'  : 'Parkes',
    'freq' : 1.5,
    'dist' : 158000.0,
    'sens' : 1.9e-25,
    'res'  : 1,
    'hours': 24,
    'xytxt': [9000,50000,0],
    'comment': '3 fields in the SMC'},
 7:{'ref'  : 'Zadnik+1996', 
    'tel'  : 'Parkes',
    'freq' : [4.462, 4.532, 8.295, 8.393, 8.666],
    'dist' : array([4.5,7.2,6.4,6.9,6.7,8.4,3.6,11.1,8.3,10.7,11.4,9.3,6.3,3.3,4.8,8,3.9,7.8,8.8,2.6,6.9,\
                    10.4,9.3,4.5,9.4,4.6,10.3,9.6,8.7,1.3,1.3,6.4,5.8,6.1,10.8,10.8,5.3,7.1,7.6,5.7,5.7,5.6,\
                    6.1,8.1,3.9,9,4.7,3.5,3.5])*3.26,
    'sens' : 3.5*1e-26,
    'res'  : 1,
    'hours': 48,
    'xytxt': [4500,2,0],
    'comment': '49 stars closer than 11.5 pc - http://www.atnf.csiro.au/people/Ray.Norris/papers/n139.html'},
 8:{'ref'  : 'Verschuur1973', 
    'tel'  : 'NRAO-140',
    'freq' : 1.42,
    'dist' : array([1.8,2.4,2.4,2.5,2.8,3.2,3.3,3.4,3.7,5.0])*3.26,
    'sens' : array([0.665,1.407,2.909,1.577,4.035,1.984,5.426,2.871,6.986,2.944])*4*1e-23/0.665,
    'res'  : 7e3,
    'hours': 13,
    'xytxt': [420,1.3,0],
    'comment': '9 stars'},
 9:{'ref'  : 'GM16', 
    'tel'  : 'VLA',
    'freq' : 1.42,
    'dist' : array([3.3e6,3.3e6])*3.26,
    'sens' : array([30,190])*1e-26*122*1e-3,
    'res'  : 122,
    'hours': 20,
    'xytxt': [0,0,0],
    'comment': 'Gray & Mooley 2016'},
10:{'ref'  : 'SERENDIP III', 
    'tel'  : 'Arecibo',
    'freq' : 0.43,
    'dist' : 0,
    'sens' : 3e-25,
    'res'  : 0.6,
    'hours': 35000,
    'xytxt': [0,0,0],
    'comment': '93% of the observable sky at least once and 44% of the sky at least five times SERENDIP III'},
11:{'ref'  : 'Southern SERENDIP', 
    'tel'  : 'Parkes',
    'freq' : 1.42,
    'dist' : 0,
    'sens' : 4e-24,
    'res'  : 0.6,
    'hours': 0,
    'xytxt': [0,0,0],
    'comment': 'Southern Sky survey; Stootman+00'},
12:{'ref'  : 'SERENDIP IV', 
    'tel'  : 'Parkes',
    'freq' : 1.42,
    'dist' : 0,
    'sens' : 4e-24,
    'res'  : 0.6,
    'hours': 0,
    'xytxt': [0,0,0],
    'comment': 'Data taken from SERENDIP IV - 90 % of the sky visible from Arecibo --- ; Korpela+04'},
13:{'ref'  : 'SERENDIP V', 
    'tel'  : 'Arecibo',
    'freq' : 1.42,
    'dist' : 0,
    'sens' : 1e-24,
    'res'  : 1.6,
    'hours': 43800,
    'xytxt': [0,0,0],
    'comment': 'Sky survey --- 30% of the sky covered three times; Korpela+09'},
}


########## Plotting and Annotation
from matplotlib.patches import Rectangle
from matplotlib import plot,text,quiver,xlabel,ylabel,legend,axis,show,gca,subplots_adjust

#### Plot the lines of constant isotropic power in signals having a 1 Hz bandwidth
clf()
S_mJy = array([0.1,1e7])
freq_Hz = 1 # 1.4e9
Wlist = [1e3,1e6,1e9,1e12,1e15,1e18,1e21,1e24] 
for W in Wlist:
    distance_ly = sqrt( W / (S_mJy * 1e-3 * 1e-26 * 4*pi* freq_Hz) ) / (c * 86400 * 365)
    plot(S_mJy, distance_ly, 'k--')

myangle=-15
x = 1.7
text(x,x/2.2*10,r'10$^{3}$ W',rotation=myangle,fontsize=14) # ref: http://homepages.rpi.edu/~sofkam/papers/fermi.pdf
text(x,x/2.2*300,r'10$^{6}$ W',rotation=myangle,fontsize=14)
text(x,x/2.2*1e4,r'10$^{9}$ W',rotation=myangle,fontsize=14)
text(x,x/2.2*3e5,r'10$^{12}$ W',rotation=myangle,fontsize=14)
text(x,x/2.2*1e7,r'10$^{15}$ W',rotation=myangle,fontsize=14)


#### Plot the distances to famous astrophysical objects

x = 0.1

plot([x,2*x],[4.3]*2,'k-',lw=2)
text(1.1*x,4.3*1.25,r'$\alpha$ Centauri',fontsize=14,color='k')

plot([x,2*x],[412*3.26]*2,'k-',lw=2)
text(1.1*x,412*3.26*1.25,'Orion Neb.',fontsize=14,color='k')

plot([x,2*x],[140*3.26]*2,'k-',lw=2)
text(1.1*x,140*3.26*1.25,'Taurus M. Cloud',fontsize=14,color='k')

#plot([1e3,2e3],[8.4e3*3.26]*2,'k-',lw=2)
#text(1000,8.4e3*3.26/1.8,'Sgr A*',fontsize=12,color='k')

plot([x,2*x],[3e4]*2,'k-',lw=2)
text(1.1*x,3.e4*1.25,'M80 Glob. / Sgr A*',fontsize=14,color='k')

plot([x,2*x],[178e3]*2,'k-',lw=2)
text(1.1*x,178e3*1.25,'SMC / LMC',fontsize=14,color='k')

plot([x,2*x],[2.537e6]*2,'k-',lw=2)
text(1.1*x,2.538e6*1.25,'M31/M33',fontsize=14,color='k')

plot([x,2*x],[53.49e6]*2,'k-',lw=2)
text(1.1*x,53.49e6*1.25,'M87',fontsize=14,color='k')


#### Plot the individual SETI surveys

for item in seti_dict.values():
    if item['ref'] in ['Cole+1979'] or 'SERENDIP' in item['ref']: continue
    y = item['dist']
    x = item['sens']/item['res'] * 1e26 * 1e3 if ( ('float' not in str(type(item['sens']))) | ('float' in str(type(y))) ) else [item['sens']/item['res'] * 1e26 * 1e3]*len(y)
    mymark,myms = ('s',8) if item['res']<3 else ('o',10) if item['res']<300 else ('^',12) if item['res']<30000 else ('v',14)
    aa=plot(x,y,mymark,ms=myms,mew=2,alpha=0.8)
    if aa[0].get_mfc()=='y': aa[0].set_mfc([0.28,  0.19,  0.11])
    freq_str = '%.1f GHz'%item['freq'] if 'list' not in str(type(item['freq'])) else '%.1f-%.1f GHz'%(item['freq'][0],item['freq'][-1])
    freq_str = '22 GHz' if freq_str=='22.0 GHz' else freq_str
    text(item['xytxt'][0],item['xytxt'][1],item['ref']+'\n'+freq_str+' ('+str(item['hours'])+'h)',color=aa[0].get_mfc(),rotation=item['xytxt'][2],horizontalalignment='left',verticalalignment='bottom',fontsize=14)

text(25,3.5e6,'Gray+Mooley2016\n1.4 GHz (2h)',fontsize=14,color='g',weight='bold')


#### Plot the blind searches

# ATA - Exoplanets
myrec = Rectangle([18e3/0.7,10], 40e3, 2e4, linestyle='--',color=[0.2]*3,fill=False,lw=4)
ax.add_artist(myrec)
text(29000,13,'Exopl. ATA 1-9 GHz @0.7 Hz\nHarp+2016, 9k stars (19kh)',color=[0.2]*3,rotation=90,horizontalalignment='left',verticalalignment='bottom',fontsize=14)

# SERENDIP III-V
myrec2 = Rectangle([3e-25/0.6*1e26*1e3,1], 6.16e5, 1e9, hatch='///',color=[0.6]*3,fill=False,zorder=-2,linewidth=0)
ax.add_artist(myrec2)
text(95e3,2e3,'SERENDIP III-V/Southern, Harvard SENTINEL\n0.4-1.4 GHz @0.03-1.6 Hz\nKorpela+2004,2009, Bowyer+1992, Stootman+2000,\nHorowitz+1985  (~100kh)',fontsize=14,rotation=90,horizontalalignment='left',verticalalignment='bottom')

# Phoenix
myrec3 = Rectangle([1.4e-26/1*1e26*1e3,10], 17000, 2e4, linestyle='--',color=[0.2]*3,fill=False,lw=4)
ax.add_artist(myrec3)
text(4800,18,'Phoenix, 1-3 GHz @1 Hz\nBackus+1998, Shostak+1999 \n850 stars (6800h)',color=[0.2]*3,rotation=90,horizontalalignment='left',verticalalignment='bottom',fontsize=14)

#  All sky survey
myrec4 = Rectangle([1.15e-22/1000*1e26*1e3,1], 1e4, 1e9, hatch='///',color=[0.6]*3,fill=False,zorder=-2,linewidth=0)
ax.add_artist(myrec4)
text(11000,2.5e5,'All-Sky Survey\n0.9-5 GHz @1 kHz\n Bowyer+1983',fontsize=14,rotation=90,horizontalalignment='left',verticalalignment='bottom')

#  NASA HRMS Sky Survey X-Band
myrec5 = Rectangle([1,1], 0.5, 1e9, hatch='///',color=[0.6]*3,fill=False,zorder=-2,linewidth=0)
ax.add_artist(myrec5)
text(1,2.5e5,'NASA HRMS Sky Survey X-Band\n8.3 GHz @40 MHz, Levin+1995',fontsize=14,rotation=90,horizontalalignment='left',verticalalignment='bottom')

# Other All-sky
myrec6 = Rectangle([1.1e6,1], 2e6, 1e9, hatch='///',color=[0.6]*3,fill=False,zorder=-2,linewidth=0)
ax.add_artist(myrec6)
text(95e4,1e2,'Harvard META/BETA, SETI-ARGUS, Ohio Sky Surveys, etc.\n1.4-4 GHz @0.5-1 Hz\nColomb+1995, Leigh+2000, Gray+1994',fontsize=14,rotation=90,horizontalalignment='left',verticalalignment='bottom')
quiver(1.1e6,50,95e4*0.01,0,headlength=4.5,headwidth=2,color='k',alpha=0.9)
plot([1.1e6]*2,[50/1.4,50*1.35],'k',lw=4,alpha=0.9)
# META, BETA,  ALL SKY SEARCH The Ohio Sky Surveys

# Galactic Center Surveys
plot([60,5000],[3e4]*2,'b',lw=8,alpha=0.9)
quiver(5000,3e4,60*0.01,0,headlength=4.5,headwidth=2,color='b',alpha=0.9)
quiver(60,3e4,0,3e4*-0.01,headlength=4.5,headwidth=2,color='b',alpha=0.9)

text(58,40e3,'Galactic Center Surveys**\n0.02-200 GHz @0.7 Hz-0.2 GHz (>300h)',color='b',fontsize=14)
text(200,3500,'**Shostak+1982, Vallee+1985,\n   Marx+1991, Steffes+1994,\n   Mauersberger+1996, Sullivan+1996,\n   Backus+2005, Harp+2010,\n   Williams+2013, Tingay+2016',color='b',fontsize=10)


########## More annotation and scaling

# Axes labels
xlabel('Channel RMS Sensitivity (mJy)')
ylabel('Distance (ly)')

# Axes scaling
ax = gca()
ax.set_xscale('log')
ax.set_yscale('log')
axis([0.1,3e6,1,3e8])
subplots_adjust(top=0.98,left=0.08,right=0.98,bottom=0.08)

# Set ticklabel size
labelsize=18
ticksize=8
linewidth=1.5
for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontsize(labelsize)
for tick in ax.yaxis.get_major_ticks():
    tick.label1.set_fontsize(labelsize)

# Set label size
ax.xaxis.label.set_fontsize(labelsize+4)
ax.yaxis.label.set_fontsize(labelsize+4)
ax.title.set_fontsize(labelsize+4)

for lines in ax.get_xticklines() + ax.get_yticklines(): 
    lines.set_markersize(8)
    lines.set_markeredgewidth(linewidth)    

# Increase the border linewidth
[i.set_linewidth(linewidth) for i in ax.spines.itervalues()]
show()

# Legend
p1 = plot(0,0,'s',ms=8,mfc='none',mew=2)
p2 = plot(0,0,'o',ms=10,mfc='none',mew=2)
p3 = plot(0,0,'^',ms=12,mfc='none',mew=2)
p4 = plot(0,0,'v',ms=14,mfc='none',mew=2)
legend([p1[0],p2[0],p3[0],p4[0]],['<3 Hz','<300 Hz','<30 kHz'],numpoints=1)


"""

Notes:

 1. 
 
-----------------------------------
Valdes+86   80 STARS & 12 NEARBY STARS -- http://ezproxy-prd.bodleian.ox.ac.uk:2054/science/article/pii/0019103586900692
-----------------------------------
4883 Hz/chan
-----------------------------------
Source      Dist_pc    Pow_10^24 x W/m^2/chan
-----------------------------------
m31         760,000.0       7.9
m32         790,000.0       7.4
m33         900,000.0       4.1
m44         187.0           7.9
sirius      2.6             7.4
procyon     3.5             7.4
tau ceti    3.6             5.9
algol       27.8            7.9
53 arieti   250.0           7.4
eps eri     3.2             7.4
pleiades    140.0           13.6
rw tau      200.0           7.4
40 eri      5.0             7.9
t tau       200.0           7.4
mira        90.9            6.4
capella     13.2            7.9
hd 36395    5.6             7.4
orion nebula 412.3          7.4
ross 47     5.8             7.4
xi ori      200.0           7.4
wolf 294    5.6             6.9
z cam       125.0           11.8
ross 882    6.0             7.4
m82         3,500,000.0     7.4
m87         17,000,000.0    7.4
r cor bor   1,400.0         7.9
barnard star  1.8           7.4
beta lyra   333.3           7.4
ss 433      5,500.0         7.4
ngc 6822    500,000.0       11.8
altair      5.1             7.9
chi cyg     166.7           7.9
cyg x1      595.2           7.4
p cygni     3,125.0         7.9
ss cyg      166.0           7.9
ngc 7252    65,000,000.0    7.4
jupiter     1.91e-5         11.8
saturn      3.89e-5         11.8
-----------------------------------


 2. More surveys which could be included:

 # 4 square degree region of galaxy in constellation Cygnus - 100 Jy, Harp+10, 0.7 Hz , 1.4-1.7 GHz
 X-band survey - 5 x 10^-22 W/m^2 , Levin+95, 40 MHz, 8300 to 8600 MHz = 1.2 mJy
 # SKY SURVEY OF SOUTHERN SKIES AND 90 TARGET STARS, AND OH MASERS = 1420.4, 1667, 3300 MHz, Resolution: 0.05 Hz, Flux: 1 x 10^-23 TO 7 x 10^-25 W/m^2 , Colomb+95 =1.4e6 
 # SKY SURVEY & -27 degrees (declination) = 1 x 10^-22 W/m^2, 1419.5 - 1421.5 MHz, 40 TO 1 Hz , Gray+86 = 
 Partial southern sky = Frequency: 8 GHz & 2380 5 MHz, Resolution: 40 kHz, Flux: 2 x 10^-22 W/m^2 , Kuiper+83 = 500 mJy
 NORTH GALACTIC ROTATION AXIS b = 5° -> 90° = Frequency: 115000 MHz, Resolution: 20000, 125000, 4 x 10^8 Hz, Flux: 1 x 10^-21 W/m^2, Total Hours: 50.0 , Tarter+85 = 0.25-5000 mJy


 3. List of GC surveys considered in this plot:
 
 Galactic Center - 100 Jy, 0.7 Hz, 1.42 to 1.72 GHz, Williams+13
 Around 40 billion stars in 20 square degrees of Waterhole = " " ", Harp+10
 GALACTIC CENTER = 1.3 x 10^-25 W/m^2, 1200 to 3000 MHz, 1 Hz, no reference
 GALACTIC CENTER = 1.2-3 GHz, 1.3 x 10^-25 W/m^2 , 1 Hz
 Galactic Center and Plane = 1420 MHz, 1.9 x 10^-25 W/m^2 , 48.0 h, Sullivan+96, 1 Hz
 23 square degrees around galactic center for narrowband signals (Waterhole)     = 10^-23 W/m^2, 20 MHz, 1 Hz, Backus+05
 16 stars + Galactic Center = Mauersberger+96, 5h, 203 GHz, 0.2 - 20 x 10^15 W EIRP, 1 MHz and 9.7 kHz 
 40 STARS + 3 LOCATIONS NEAR GALACTIC CENTER = Steffes+94,  2.3 x 10^-19 W/m^2 , 203 GHz, 32 Hz, 25 h
 GALACTIC CENTER MERIDIAN  = 1 x 10^-19 W/m^2 , 72 h, 185 MHz, 10.5 GHz, Vallee+85
 GALACTIC CENTER = 1 x 10^-24 W/m^2, 1200 Hz, 1.4 GHz, Shostak+82, 4h
 GALACTIC CENTER & 33 NEARBY STARS = Marx+91, 6 x 10^-25 to 10^-24 W/m^2 , 144 h, 76 Hz, 4829.620 - 4829.776 MHz
 Tingay+16, 400 mJy, 103/133 MHz, 2 h, 10 kHz

 
 4. http://setiquest.org/wiki/index.php/Seti_programs is the central reference for the surveys considered here

"""

