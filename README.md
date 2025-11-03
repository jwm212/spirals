## starting a new CFD project
- created folder
- `git init` to create new local git repository
- created folder for taxon e.g. *Stromatocystites* and copy generic `base_case` folder from other taxon - *Helicoplacus*

### Adapting `base_case` to new taxon
1. Find dimensions of organism:

    e.g. *Stomatocystites*: 
    using scale bar in screenshot of Zamora et al. 2013 Fig 1.3 (https://doi.org/10.1016/j.geobios.2015.07.004) $= 32$ mm. In the description, "Theca ranges from $20$ mm to $60$ mm wide".

2. Check dimensions of model in paraview: Original *Stromatocystites* model measures $3$ m so needs rescaling. Rescale using Blender. Check orientation/location of model and edit if necessary.

3. Replace `Helicoplacus.stl` with taxon `.stl` file in:
    
    - `constant/trisurface`
    - `system/snappyHexMeshDict>geometry`

4. Update `domain` in `system/blockMeshDict` based on characteristic length.

    e.g. *Stromatocystites*: $L = 30$ mm, so
    
    $\Delta (+x) = 10L = 300$ mm 

    $\Delta (-x) = 4L = 120$ mm

    $=> (-0.12 \leq x \leq 0.3)$ m

    $\Delta(\pm y) = 4L = 120$ mm
    
    $=> (-0.12 \leq y \leq 0.12)$ m

    $\Delta(+z) = 4L = 120$ mm

    $=> (0 \leq z \leq 0.12)$ m

5. update `system/blockMeshDict` cell numbers to match n280 resolution:
    
    n280 resolution: for $\Delta x$ of 600 mm, assign 280 cells (see `../Helicoplacus_CFD`).

    $\Delta x = 420$ mm $=> n_x = 196$ cells

    $\Delta y = 240$ mm $=> n_y = 112$ cells
    
    $\Delta z = 120$ mm $=> n_z = 56$ cells

6. run `blockMesh` and visualise in Paraview alongside the model to check domain size is correct.

7. run `snappyHexMesh` and `checkMesh`. Check minimum mesh quality parameters.

    e.g. *Stromatocystites*:

    ```
    Overall domain bounding box (-0.0477782 -0.03543318 0) (0.04784281 0.05260949 0.06071247)
    Mesh has 3 geometric (non-empty/wedge) directions (1 1 1)
    Mesh has 3 solution (non-empty) directions (1 1 1)
    Max cell openness = 3.689203e-16 OK.
    Max aspect ratio = 4.711672 OK.
    Minimum face area = 4.486088e-08. Maximum face area = 4.591988e-06.  Face area magnitudes OK.
    Min volume = 2.168883e-11. Max volume = 9.839979e-09.  Total volume = 0.0002131412.  Cell volumes OK.
    Mesh non-orthogonality Max: 43.36838 average: 9.031391
    Non-orthogonality check OK.
    Face pyramids OK.
    Max skewness = 2.778041 OK.
    Coupled point location match (average 0) OK.
    ```
    
    Open `controlDict` in paraview (using OpenFOAM reader) to visualise mesh. If the mesh seems to only mesh inside the model instead of outside, re-define `locationInMesh`.

## Orientation sensitivity study:
Varying orientation of *Stromatocystites* from $0^{\circ}$ to $180^{\circ}$ in $45^{\circ}$ increments. orientations above $180^{\circ}$ not needed because of the 2-1-2 symmetry of the organism and the symmetrical fluid flow. 

## Velocity sensitivity study:
Varying current velocity from $0.05-0.5$ m/s to test sensitivity of flow. 
### `/scripts`:
#### `postprocessing.sh`:
This shell script runs python scripts (using `pvpython`) on the `gpu` queue to produce figures. The python scripts:
 - `xz_profiles.py`
    This produces a 2D colormap of velocity in the x-z coordinate plane at $y = 0$ overlayed with velocity vector glyphs. Saved in `*case*/postProcessing`.
 - `xy_profiles.py`
    This produces a 2D colormap of velocity in the x-y coordinate plane at an z-coordinate appropraite for each taxon, overlayed with velocity vector glyphs. Saved in `*case*/postProcessing`.


# TODO:

[ ] fix issue in _extract.py scripts where they don't extract the last timestep, due to different timesteps being used - find way to specify largest number in the filename.

[ ] Set up U_profiles extract and plot velocity scaled by L of each taxon.

[x] Set up Gogia palmeri case and run velocity study.

[ ] Re-run orientation.

[ ] Automate x-y profile figure creation.

[ ] create time-averaged colormap profiles.