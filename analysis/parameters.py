class Taxon(object):
    def __init__(self, name, label, A_frontal, V, L, h, r, R, cfd):
        self.name = name # taxon name
        self.label = label # label for plotting purposes
        self.A_frontal = A_frontal # frontal area w.r.t incoming flow (m^2)
        self.V = V # Body volume (m^3)
        self.L = L # Characteristic length (m)
        self.h = h # Height (m)
        self.r = r # Magnitude of position vector of centre of mass (m)
        self.R = R # Radius of base (m)
        self.cfd = cfd

class Environment(object):
    def __init__(self, rho_w, rho_calcite, g, nu):
        self.rho_w = rho_w # Density of water (kg/m^3) 
        self.rho_calcite = rho_calcite # Density of calcite (kg/m^3)
        self.g = g # Acceleration due to gravity (ms^-2)
        self.nu = nu # Kinematic viscosity of water (m^2/s)

# Define environment:
Env1 = Environment(
    rho_w = 1025,
    rho_calcite = 2710,
    g = 9.81,
    nu = 1.04E-6
)

# Define taxa:
Stromatocystites = Taxon(
    name = "stromatocystites",
    label = r"$\it{Stromatocystites}$", 
    A_frontal = 0.00114, 
    V = 2.66E-5, 
    L = 0.03, 
    h = 0.03,
    r = 7.27E-3,
    R = 0.005,
    cfd = {
        "Re100": {
            "time_range": [64, 321],
            "write_interval": 2,
            "flow_through_time": 129
        },
        "Re500": {
            "time_range": [52, 257],
            "write_interval": 0.5,
            "flow_through_time": 25.8
        },
        "Re1000": {
            "time_range": [65, 324],
            "write_interval": 0.2,
            "flow_through_time": 12.9
        },
        "Re5000": {
            "time_range": [52, 259],
            "write_interval": 0.05,
            "flow_through_time": 2.58
        },
        "Re10000": {
            "time_range": [65, 324],
            "write_interval": 0.02,
            "flow_through_time": 1.29
        }

    }
)

Kailidiscus = Taxon(
    name = "kailidiscus",
    label = r"$\it{Kailidiscus}$",
    A_frontal = 0.00106,
    V = 3.01E-5,
    L = 0.03,
    h = 0.03,
    r = 0.0167405,
    R = 0.012,
    cfd = {
        "Re100": {
            "time_range": [64, 321],
            "write_interval": 2,
            "flow_through_time": 129
        },
        "Re500": {
            "time_range": [52, 257],
            "write_interval": 0.5,
            "flow_through_time": 25.8
        },
        "Re1000": {
            "time_range": [65, 324],
            "write_interval": 0.2,
            "flow_through_time": 12.9
        },
        "Re5000": {
            "time_range": [52, 259],
            "write_interval": 0.05,
            "flow_through_time": 2.58
        },
        "Re10000": {
            "time_range": [65, 324],
            "write_interval": 0.02,
            "flow_through_time": 1.29
        }
    }
)

Helicocystis_straight = Taxon(
    name = "helicocystis_straight",
    label = r"$\it{Helicocystis}$ (straight)",
    A_frontal = 0.0000288031,
    V = 6.5E-8,
    L = 0.003,
    h = 0.012,
    r = 0.00738148,
    R = 1E-4,
    cfd = {
        "Re100": {
            "time_range": [108, 540],
            "write_interval": 0.05,
            "flow_through_time": 5.4
        },
        "Re500": {
            "time_range": [108, 540],
            "write_interval": 0.01,
            "flow_through_time": 1.08
        },
        "Re1000": {
            "time_range": [108, 540],
            "write_interval": 0.005,
            "flow_through_time": 0.54
        },
        "Re5000": {
            "time_range": [108, 540],
            "write_interval": 0.001,
            "flow_through_time": 0.108
        },
        "Re10000": {
            "time_range": [108, 540],
            "write_interval": 0.0005,
            "flow_through_time": 0.054
        }
    }
)

Helicocystis = Taxon(
    name = "helicocystis",
    label = r"$\it{Helicocystis}$",
    A_frontal = 0.0000331,
    V = 6.2E-8,
    L = 0.003,
    h = 0.012,
    r = 0.00738148,
    R = 1E-4,
    cfd={
        "Re100": {
            "time_range": [108, 540],
            "write_interval": 0.05,
            "flow_through_time": 5.4
        },
        "Re500": {
            "time_range": [108, 540],
            "write_interval": 0.01,
            "flow_through_time": 1.08
        },
        "Re1000": {
            "time_range": [108, 464],
            "write_interval": 0.005,
            "flow_through_time": 0.54
        },
        "Re5000": {
            "time_range": [108, 540],
            "write_interval": 0.001,
            "flow_through_time": 0.108
        },
        "Re10000": {
            "time_range": [108, 540],
            "write_interval": 0.0005,
            "flow_through_time": 0.054
        }
    }
)

Gogia_palmeri = Taxon(
    name = "gogia_palmeri",
    label = r"$\it{Gogia}$ $\it{palmeri}$",
    A_frontal = 0.000792,
    V = 9E-6,
    L = 0.02,
    h = 0.13,
    r = 0.0335649,
    R = 9E-4,
    cfd={
        "Re100": {
            "time_range": [73, 364],
            "write_interval": 5,
            "flow_through_time": 364
        },
        "Re500": {
            "time_range": [73, 364],
            "write_interval": 1,
            "flow_through_time": 72.8
        },
        "Re1000": {
            "time_range": [73, 364],
            "write_interval": 0.5,
            "flow_through_time": 36.4
        },
        "Re5000": {
            "time_range": [73, 364],
            "write_interval": 0.1,
            "flow_through_time": 7.28
        },
        "Re10000": {
            "time_range": [73, 364],
            "write_interval": 0.05,
            "flow_through_time": 3.64
        }
    }
)

Gogia_spiralis = Taxon(
    name = "gogia_spiralis",
    label = r"$\it{Gogia}$ $\it{spiralis}$",
    A_frontal = 0.000284,
    V = 1.1E-6,
    L = 0.01,
    h = 0.065,
    r = 0.02354967,
    R = 2E-3,
    cfd={
        "Re100": {
            "time_range": [91, 455],
            "write_interval": 1,
            "flow_through_time": 91
        },
        "Re500": {
            "time_range": [73, 360],
            "write_interval": 0.25,
            "flow_through_time": 18.2
        },
        "Re1000": {
            "time_range": [91, 455],
            "write_interval": 0.1,
            "flow_through_time": 9.1
        },
        "Re5000": {
            "time_range": [73, 360],
            "write_interval": 0.025,
            "flow_through_time": 1.82
        },
        "Re10000": {
            "time_range": [91, 455],
            "write_interval": 0.01,
            "flow_through_time": 0.91
        }
    }
)

#Helicoplacus = Taxon(
#    name = "helicoplacus",
#    label = r"$\it{Helicoplacus}$",
#    A_frontal = 0.000443,
#    V = 3.92E-6,
#    L = 0.04,
#    r = 0.02393894,
#    R = 0.0025
#)
