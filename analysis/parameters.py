class Taxon(object):
    def __init__(self, name, label, A_frontal, V, L, r, R):
        self.name = name # taxon name
        self.label = label # label for plotting purposes
        self.A_frontal = A_frontal # frontal area w.r.t incoming flow (m^2)
        self.V = V # Body volume (m^3)
        self.L = L # Characteristic length (m)
        self.r = r # Magnitude of position vector of centre of mass (m)
        self.R = R # Radius of base (m)

class Environment(object):
    def __init__(self, rho_w, rho_calcite, g):
        self.rho_w = rho_w # Density of water (kg/m^3) 
        self.rho_calcite = rho_calcite # Density of calcite (kg/m^3)
        self.g = g # Acceleration due to gravity (ms^-2)

# Define environment:
Env1 = Environment(
    rho_w = 1025,
    rho_calcite = 2710,
    g = 9.81
)

# Define taxa:
Stromatocystites = Taxon(
    name = "stromatocystites",
    label = r"$\it{Stromatocystites}$", 
    A_frontal = 0.00114, 
    V = 2.66E-5, 
    L = 0.03, 
    r = 7.27E-3,
    R = 0.005
)

Kailidiscus = Taxon(
    name = "kailidiscus",
    label = r"$\it{Kailidiscus}$",
    A_frontal = 0.00106,
    V = 3.01E-5,
    L = 0.03,
    r = 0.0167405,
    R = 0.012
)

Helicocystis_straight = Taxon(
    name = "helicocystis_straight",
    label = r"$\it{Helicocystis}$ (straight)",
    A_frontal = 0.00024,
    V = 6.5E-8,
    L = 0.012,
    r = 0.00738148,
    R = 1E-4
)

Helicocystis = Taxon(
    name = "helicocystis",
    label = r"$\it{Helicocystis}$",
    A_frontal = 0.0000331,
    V = 6.2E-8,
    L = 0.012,
    r = 0.00738148,
    R = 1E-4
)

Gogia_palmeri = Taxon(
    name = "gogia_palmeri",
    label = r"$\it{Gogia}$ $\it{palmeri}$",
    A_frontal = 0.000792,
    V = 9E-6,
    L = 0.13,
    r = 0.0335649,
    R = 9E-4
)

Gogia_spiralis = Taxon(
    name = "gogia_spiralis",
    label = r"$\it{Gogia}$ $\it{spiralis}$",
    A_frontal = 0.000284,
    V = 1.1E-6,
    L = 0.065,
    r = 0.02354967,
    R = 2E-3
)

Helicoplacus = Taxon(
    name = "helicoplacus",
    label = r"$\it{Helicoplacus}$",
    A_frontal = 0.000443,
    V = 3.92E-6,
    L = 0.04,
    r = 0.02393894,
    R = 0.0025
)