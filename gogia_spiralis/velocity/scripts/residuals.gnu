dpi = 300 ## dpi (variable)
width = 160 ## mm (variable)
height = 90 ## mm (variable)

in2mm = 25.4 # mm (fixed)
pt2mm = 0.3528 # mm (fixed)

mm2px = dpi/in2mm
ptscale = pt2mm*mm2px
round(x) = x - floor(x) < 0.5 ? floor(x) : ceil(x)
wpx = round(width * mm2px)
hpx = round(height * mm2px)

set terminal pngcairo size wpx,hpx fontscale ptscale linewidth ptscale pointscale ptscale


#set terminal png size 400,300 enhanced font "Helvetica,8"
set output 'postProcessing/residual_p.png'
set logscale y
plot 'logs/p_0' using 1:2 with lines title 'p_0', 'logs/pFinalRes_0' using 1:2 with lines title 'p_{final}'

set output 'postProcessing/residual_Co.png'
unset logscale
plot 'logs/CourantMax_0' using 1:2 with lines title 'Co

set output 'postProcessing/residual_U.png'
set logscale y
plot 'logs/Ux_0' using 1:2 with lines title 'Ux', 'logs/Uy_0' with lines title 'Uy', 'logs/Uz_0' with lines title 'Uz'

set output 'postProcessing/Cd.png'
unset logscale
plot 'postProcessing/forces/0/forceCoeffs.dat' using 1:3 with lines title 'C_d'
set output 'postProcessing/Cl.png'
plot 'postProcessing/forces/0/forceCoeffs.dat' using 1:4 with lines title 'C_l'