import numpy as np

# greek letters and other symbols (Ctrl+Shift+u):
# Γ = u0393
# Δ = u0394
# Ω = u03a9

# α = u03b1
# β = u03b2
# γ = u03b3, 𝛾 = u1D6FE
# δ = u03b4
# ε = u03b5

# λ = u03bb

# σ = u03c3
# τ = u03c4

# ψ = u03c8
# ω = u03c9

# √ = u221a
# × = u00d7


### CONSTANTS and PARAMETERS

### general physics
ε0 = 8.85418782e-12  # [F/m] vacuum permittivity epsilon_0
c0 = 299792458       # [m/s] speed of light in vacuum c_0
ħ  = 1.05457180e-34  # [J*s] Planck constant

### geometrical parameters
R    = 4.5e-6        # [m ] radius
w    = 500e-9        # [m ] width
h    = 200e-9        # [m ] height
wga  = w*h           # [m²] waveguide (core) area

L    = 2*np.pi*R     # [m ] core length
V    = L*wga         # [m³] ~ core volume

ρSi = 2.3290e3       # [kg/m³]
#Mring = ρSi*V        # [kg] mass of the microring
Cp = 0.7e3           # [J/kg/K]
MCpV = ρSi*Cp        # [J/K/m³]

### standard wavelength
λ0 = 1.550e-6        # [m]
ω0 = c0/λ0           # ~ 193.1 e12 [Hz] or 0.1931 [PHz]

𝛾TH = 300e6          # [Hz] or 300 µs-¹
𝛾FC =  12e6          # [Hz] or 250 µs-¹

### refractive index
nSi = 3.48           # Silicon refractive index
n0 = nSi             # standard refractive index
n2 = 4.5e-18         # [1/(W/m²)]  intensity-dependent refractive index
dndT = 1.86e-4       # [1/K]
dndN = -4.2e-27      # [m³]
dαdN =  1.45e-15     # [m²]
βtpa =  0.79e-11     # [m/W]

κ	= 0.10           # [1]
𝛾	= 0.9			 # [1]

### RENORMALIZED CONSTANTS and PARAMETERS

### normalization parameters
# length: µm
L0 = 1e-6 # [m]
# frenq. & time: PHz & fs
f0 = 1e15 # [Hz]
# Power: P0 = 1 mW
P0 = 1e-3 # [mw]
# hence energy J = Ws = 1e12 mW fs = 1e12 P0/
# Temperature: K
T0 = 1 # [K]
# Mass: Kg
M0 = 1 # [Kg]

### general physics
#ε0 = 8.85418782e-12  # [F/m] vacuum permittivity epsilon_0
ñc0 = c0/L0/f0        # [m/s] speed of light in vacuum c_0
ñħ  = ħ/P0*f0**2      # [W/Hz²/P0*f0²] Planck constant

### geometrical parameters
ñR    = R/L0         # [m /L0 ]=[1] radius
ñw    = w/L0         # [m /L0 ]=[1] width
ñh    = h/L0         # [m /L0 ]=[1] height
ñwga  = ñw*ñh        # [m²/L0²]=[1] core area

ñL    = 2*np.pi*ñR   # [m /L0 ]=[1] core length
ñV    = ñL*ñwga      # [m³/L0³]=[1] ~ core volume

ñMCpV = MCpV*T0*L0**3/(P0/f0)	# [J/K/m³]

### standard wavelength
ñλ0 = λ0/L0       	# [m]
ñω0 = c0/λ0/f0      # ~ 193.1 e12 [Hz] or 0.1931 [PHz]

ñ𝛾TH = 𝛾TH/f0        # [Hz/PHz]=[1]
ñ𝛾FC = 𝛾FC/f0        # [Hz/PHz]=[1]

### refractive index
ñn0 = n0             # standard refractive index
ñn2 = n2*P0/L0**2    # [m²/W*P0/L0²)]=[1]  intensity-dependent refractive index
ñdndT = dndT*T0      # [T0/K]=[1]
ñdndN = dndN/L0**3   # [m³/λ0³]=[1]
ñdαdN = dαdN/L0**2   # [m²/λ0²]=[1]
ñβtpa = βtpa*P0/L0   # [m/W*P0/λ0]=[1]

#ω, ωp, ω0, Ep, Es, τa, τb, τ0, 𝛾TH, 𝛾FC, Mring, Cp, n0, n2, dndT, dndN, dαdN, βtpa, Γ, V, Veff = par
