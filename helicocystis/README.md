# Helicocystis
base_case proportions based on Helicoplacus, but rescaled to charactersitic length of Helicocystis, 12mm.

Number of refienment layers increased from 2 to 4 to fully resolve ambulacra.

CFL condition: 
$\Delta T = \frac{4\times 10^{-5}}{0.5} = 8\times 10&{-5}$ s. Set `controlDict/deltaT` to `0.0001`.

EDIT: reduced `deltaT` to `0.00005` for `v0.4` and `v0.5`.