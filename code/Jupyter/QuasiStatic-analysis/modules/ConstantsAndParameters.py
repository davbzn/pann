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
R    = 9.0e-6        # [m ] radius
w    = 500e-9        # [m ] width
h    = 200e-9        # [m ] height
wga  = w*h           # [m²] core area

L    = 2*np.pi*R     # [m ] core length
V    = L*wga         # [m³] ~ core volume
Veff = V             # [m³] effective mode volume
Γ    = 0.9

ρSi = 2.3290e3       # [kg/m³]
Mring = ρSi*V        # [kg] mass of the microring
Cp = 0.7e3           # [J/kg/K]
MCp = Mring*Cp       # [J/K] 

### parameters
λ0 = 1.550e-6        # [m]
ω0 = c0/λ0           # ~ 193.1 e12 [Hz] or e0 [THz]
λp = 1.5505e-6       # [m]
ωp = c0/λp           # ~ 193.1 e12 [Hz] or e0 [THz]

𝛾TH = 7.5e6          # [Hz]
𝛾FC = 250e6          # [Hz] or 250 µs-¹

### refractive index
nSi = 3.48           # Silicon refractive index
n0 = nSi             # standard refractive index
n2 = 5e-14           # [1/(W/cm²)] intensity-dependent refractive index
n2 = 4.5e-18         # [1/(W/m²)]  intensity-dependent refractive index
dndT = 1.86e-4       # [1/K]
#dndT = 1e6*1.86e-4  # [1/K] !!!!!!!!!!! USER DEFINED
dndN = -1.73e-27     # [m³]
dαdN =  1.1e-15      # [m²]
βtpa =  0.79e-11      # [m/W]
vg = c0/4.0          # [m/s]

κa = 0.15               # [1]
κb = κa                 # [1]
τa = 2*L / (κa**2 * vg) # [s]
τb = τa                 # [s]
τ0 = 3.0e-9             # [s] ~ 1 / (α * vg)

σ = np.sqrt(0.5*c0*ε0*n0*wga)  # [ √W / (V/m) ]
Ep =  np.power( 1.0e-0, 0.5)      # [ σ * (V/m) ] ~ [√W]
Es =  np.power( 1.0e-4, 0.5)      # [ σ * (V/m) ] ~ [√W]

#ω, ωp, ω0, Ep, Es, τa, τb, τ0, 𝛾TH, 𝛾FC, Mring, Cp, n0, n2, dndT, dndN, dαdN, βtpa, Γ, V, Veff = par


### RENORMALIZED CONSTANTS and PARAMETERS

### normalization parameters
# length: λ0
# frenq. & time: ω0
# Power: P0 = 1 mW
P0 = 1e-3            # [mW]
# temperature: T0
T0 = 1               # [K]

### geometrical parameters
ñR    = R/λ0         # [m /λ0 ]=[1] radius
ñw    = w/λ0         # [m /λ0 ]=[1] width
ñh    = h/λ0         # [m /λ0 ]=[1] height
ñwga  = ñw*ñh        # [m²/λ0²]=[1] core area

ñL    = 2*np.pi*ñR   # [m /λ0 ]=[1] core length
ñV    = ñL*ñwga      # [m³/λ0³]=[1] ~ core volume
ñVeff = ñV           # [m³/λ0³]=[1] effective mode volume
Γ     = 0.9

ρSi = 2.3290e3       # [kg/m³]
ñMring = ρSi*V       # [kg] mass of the microring
ñCp = Cp*T0*ω0/P0    # [J/kg/K*T0*ω0/P0]=[1/kg]
ñMCp = ñMring*ñCp    # [J/K*T0*ω0/P0]=[1]

### parameters
ñλ0 = 1              # ~ 1.55 e-6 [m] or 1.55 [µm]
ñω0 = 1              # ~ 193.1 e12 [Hz] or [THz]
ñλp = λp/λ0          # [m/λp]=[1]
ñωp = ωp/ω0          # [Hz/ωp]=[1]

ñ𝛾TH = 𝛾TH/ω0        # [Hz/ω0]=[1]
ñ𝛾FC = 𝛾FC/ω0        # [Hz/ω0]=[1]

### refractive index
ñn0 = n0             # standard refractive index
ñn2 = n2*P0/λ0**2    # [m²/W*P0/λ0²)]=[1]  intensity-dependent refractive index
ñdndT = dndT*T0      # [T0/K]=[1]
ñdndN = dndN/λ0**3   # [m³/λ0³]=[1]
ñdαdN = dαdN/λ0**2   # [m²/λ0²]=[1]
ñβtpa = βtpa*P0/λ0   # [m/W*P0/λ0]=[1]
ñvg = vg/(ω0*λ0)      # [m/s*ω0/λ0]=[1]

κa = 0.15            # [1]
κb = κa              # [1]
ñτa = τa*ω0          # [s*ω0]=[1]
ñτb = ñτa            # [s*ω0]=[1]
ñτ0 = τ0*ω0          # [s*ω0]=[1]

ñEp = Ep/np.sqrt(P0) # [√W/√mW]=[1]
ñEs = Es/np.sqrt(P0) # [√W/√mW]=[1]

#ω, ωp, ω0, Ep, Es, τa, τb, τ0, 𝛾TH, 𝛾FC, Mring, Cp, n0, n2, dndT, dndN, dαdN, βtpa, Γ, V, Veff = par