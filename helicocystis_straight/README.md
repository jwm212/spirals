# Helicocystis
base_case copied from ../helicocystis

## Meshing:
Initially:
```
nCellsBetweenLevels 5;

refinementSurfaces
{
    HH
    {
            
        level (2 4);
    }
}
```
Output:
```
   *Number of severely non-orthogonal (> 70 degrees) faces: 1.
 ***Number of non-orthogonality errors: 5.
 ***Error in face pyramids: 22 faces are incorrectly oriented.
 ***Max skewness = 6.525563, 15 highly skew faces detected which may impair the quality of the results
    Coupled point location match (average 0) OK.

Failed 3 mesh checks.
```

Extra refinement:
```
nCellsBetweenLevels 10;

refinementSurfaces
{
    HH
    {
            
        level (3 5);
    }
}
```
Result:
```
 ***Number of non-orthogonality errors: 7.
    Face pyramids OK.
 ***Max skewness = 8.675081, 20 highly skew faces detected which may impair the quality of the results
    Coupled point location match (average 0) OK.

Failed 2 mesh checks.
```


CFL condition: 
$\Delta T = \frac{2\times 10^{-5}}{0.5} = 4\times 10^{-5}$ s. Set `controlDict/deltaT` to `0.00005`.

writeInterval:


mpi:
40 cpus, 10x2x2 gives ~82000 cells per cpu.


