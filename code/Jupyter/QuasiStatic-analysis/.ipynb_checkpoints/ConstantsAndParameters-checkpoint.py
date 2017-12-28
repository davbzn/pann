{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# numpy (math) libary\n",
    "import numpy as np \n",
    "\n",
    "# greek letters and other symbols (Ctrl+Shift+u):\n",
    "# Γ = u0393\n",
    "# Δ = u0394\n",
    "# Ω = u03a9\n",
    "\n",
    "# α = u03b1\n",
    "# β = u03b2\n",
    "# γ = u03b3, 𝛾 = u1D6FE\n",
    "# δ = u03b4\n",
    "# ε = u03b5\n",
    "\n",
    "# λ = u03bb\n",
    "\n",
    "# σ = u03c3\n",
    "# τ = u03c4\n",
    "\n",
    "# ψ = u03c8\n",
    "# ω = u03c9\n",
    "\n",
    "# √ = u221a\n",
    "# × = u00d7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pump:\n",
      "\twavelength λ_P =   1.5505 µm\n",
      "\tfrequency  ω_P = 193.3521 THz\n"
     ]
    }
   ],
   "source": [
    "# CONSTANTS and PARAMETERS\n",
    "\n",
    "# general physics\n",
    "ε0 = 8.85418782e-12  # [F/m] vacuum permittivity epsilon_0\n",
    "c0 = 299792458       # [m/s] speed of light in vacuum c_0\n",
    "ħ  = 1.05457180e-34  # [J*s] Planck constant\n",
    "\n",
    "# geometrical parameters\n",
    "R    = 9.0e-6        # [m ] radius\n",
    "w    = 500e-9        # [m ] width\n",
    "h    = 200e-9        # [m ] height\n",
    "wga  = w*h           # [m²] core area\n",
    "\n",
    "L    = 2*np.pi*R     # [m ] core length\n",
    "V    = L*wga         # [m³] ~ core volume\n",
    "Veff = V             # [m³] effective mode volume\n",
    "Γ    = 0.9\n",
    "\n",
    "ρSi = 2.3290e3       # [kg/m³]\n",
    "Mring = ρSi*V        # [kg] mass of the microring\n",
    "Cp = 0.7e3           # [J/kg/K]\n",
    "MCp = Mring*Cp       # [J/K] \n",
    "\n",
    "# parameters\n",
    "λ0 = 1.550e-6        # [m]\n",
    "ω0 = c0/λ0           # ~ 193.1 e12 [Hz] or e0 [THz]\n",
    "λp = 1.5505e-6       # [m]\n",
    "ωp = c0/λp           # ~ 193.1 e12 [Hz] or e0 [THz]\n",
    "print('pump:')\n",
    "print('\\twavelength λ_P =   %.4f' % (λp*1.0e06), 'µm')\n",
    "print('\\tfrequency  ω_P = %.4f' % (ωp/1.0e12), 'THz')\n",
    "\n",
    "𝛾TH = 7.5e6          # [Hz]\n",
    "𝛾FC = 250e6          # [Hz] or 250 µs-¹\n",
    "\n",
    "# refractive index\n",
    "nSi = 3.48           # Silicon refractive index\n",
    "n0 = nSi             # standard refractive index\n",
    "n2 = 5e-14           # [1/(W/cm²)] intensity-dependent refractive index\n",
    "n2 = 4.5e-18         # [1/(W/m²)]  intensity-dependent refractive index\n",
    "dndT = 1.86e-4       # [1/K]\n",
    "#dndT = 1e6*1.86e-4  # [1/K] !!!!!!!!!!! USER DEFINED\n",
    "dndN = -1.73e-27     # [m³]\n",
    "dαdN =  1.1e-15      # [m²]\n",
    "βtpa =  0.79e-11      # [m/W]\n",
    "vg = c0/4.0          # [m/s]\n",
    "\n",
    "κa = 0.15               # [1]\n",
    "κb = κa                 # [1]\n",
    "τa = 2*L / (κa**2 * vg) # [s]\n",
    "τb = τa                 # [s]\n",
    "τ0 = 3.0e-9             # [s] ~ 1 / (α * vg)\n",
    "\n",
    "σ = np.sqrt(0.5*c0*ε0*n0*wga)  # [ √W / (V/m) ]\n",
    "Ep =  np.power( 1.0e-0, 0.5)      # [ σ * (V/m) ] ~ [√W]\n",
    "Es =  np.power( 1.0e-4, 0.5)      # [ σ * (V/m) ] ~ [√W]\n",
    "\n",
    "#ω, ωp, ω0, Ep, Es, τa, τb, τ0, 𝛾TH, 𝛾FC, Mring, Cp, n0, n2, dndT, dndN, dαdN, βtpa, Γ, V, Veff = par"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# RENORMALIZED CONSTANTS and PARAMETERS\n",
    "\n",
    "# general physics\n",
    "ε0 = 8.85418782e-12  # [F/m] vacuum permittivity epsilon_0\n",
    "c0 = 299792458       # [m/s] speed of light in vacuum c_0\n",
    "ħ  = 1.05457180e-34  # [J*s] Planck constant\n",
    "\n",
    "# normalization parameters\n",
    "# length: λ0\n",
    "# frenq. & time: ω0\n",
    "# Power: P0 = 1 mW\n",
    "P0 = 1e-3            # [mW]\n",
    "# temperature: T0\n",
    "T0 = 1               # [K]\n",
    "\n",
    "# geometrical parameters\n",
    "ñR    = R/λ0         # [m /λ0 ]=[1] radius\n",
    "ñw    = w/λ0         # [m /λ0 ]=[1] width\n",
    "ñh    = h/λ0         # [m /λ0 ]=[1] height\n",
    "ñwga  = ñw*ñh        # [m²/λ0²]=[1] core area\n",
    "\n",
    "ñL    = 2*np.pi*ñR   # [m /λ0 ]=[1] core length\n",
    "ñV    = ñL*ñwga      # [m³/λ0³]=[1] ~ core volume\n",
    "ñVeff = ñV           # [m³/λ0³]=[1] effective mode volume\n",
    "Γ     = 0.9\n",
    "\n",
    "ρSi = 2.3290e3       # [kg/m³]\n",
    "ñMring = ρSi*V       # [kg] mass of the microring\n",
    "ñCp = Cp*T0*ω0/P0    # [J/kg/K*T0*ω0/P0]=[1/kg]\n",
    "ñMCp = ñMring*ñCp    # [J/K*T0*ω0/P0]=[1]\n",
    "\n",
    "# parameters\n",
    "ñλ0 = 1              # ~ 1.55 e-6 [m] or 1.55 [µm]\n",
    "ñω0 = 1              # ~ 193.1 e12 [Hz] or [THz]\n",
    "ñλp = λp/λ0          # [m/λp]=[1]\n",
    "ñωp = ωp/ω0          # [Hz/ωp]=[1]\n",
    "\n",
    "ñ𝛾TH = 𝛾TH/ω0        # [Hz/ω0]=[1]\n",
    "ñ𝛾FC = 𝛾FC/ω0        # [Hz/ω0]=[1]\n",
    "\n",
    "# refractive index\n",
    "ñn0 = n0             # standard refractive index\n",
    "ñn2 = n2*P0/λ0**2    # [m²/W*P0/λ0²)]=[1]  intensity-dependent refractive index\n",
    "ñdndT = dndT*T0      # [T0/K]=[1]\n",
    "ñdndN = dndN/λ0**3   # [m³/λ0³]=[1]\n",
    "ñdαdN = dαdN/λ0**2   # [m²/λ0²]=[1]\n",
    "ñβtpa = βtpa*P0/λ0   # [m/W*P0/λ0]=[1]\n",
    "ñvg = vg/(ω0*λ0)      # [m/s*ω0/λ0]=[1]\n",
    "\n",
    "κa = 0.15            # [1]\n",
    "κb = κa              # [1]\n",
    "ñτa = τa*ω0          # [s*ω0]=[1]\n",
    "ñτb = ñτa            # [s*ω0]=[1]\n",
    "ñτ0 = τ0*ω0          # [s*ω0]=[1]\n",
    "\n",
    "ñEp = Ep/np.sqrt(P0) # [√W/√mW]=[1]\n",
    "ñEs = Es/np.sqrt(P0) # [√W/√mW]=[1]\n",
    "\n",
    "#ω, ωp, ω0, Ep, Es, τa, τb, τ0, 𝛾TH, 𝛾FC, Mring, Cp, n0, n2, dndT, dndN, dαdN, βtpa, Γ, V, Veff = par"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# useful functions\n",
    "def wlen_to_freq(wlen):\n",
    "    return c0/wlen # returns the frequency [Hz] \\tfrom the wavelength [m]\n",
    "\n",
    "def freq_to_wlen(freq):\n",
    "    return c0/freq # returns the wavelength [m] \\tfrom the frequency [Hz]\n",
    "\n",
    "def print_const(normalized = False):\n",
    "    if not normalized:\n",
    "        print(\"CONSTANTS and PARAMETERS\")\n",
    "        print()\n",
    "        print(\"general physics constants\")\n",
    "        print(\"ε0\\t= %.8e\"%ε0, \"[F/m] \\tvacuum permittivity\")\n",
    "        print(\"c0\\t= %d\"%c0, \"[m/s] \\tspeed of light in vacuum\")\n",
    "        print(\"ħ\\t= %.8e\"%ħ, \"[J*s] \\tPlanck constant\")\n",
    "        print()\n",
    "        print(\"geometrical parameters\")\n",
    "        print(\"R\\t= %.2e\"%R, \"[m ] \\tradius\")\n",
    "        print(\"w\\t= %.2e\"%w, \"[m ] \\twidth\")\n",
    "        print(\"h\\t= %.2e\"%h, \"[m ] \\theight\")\n",
    "        print(\"wga\\t= %.2e\"%wga, \"[m²] \\tcore area\")\n",
    "        print()\n",
    "        print(\"L\\t= %.4e\"%L, \"[m ] \\tcore length\")\n",
    "        print(\"V\\t= %.4e\"%V, \"[m³] \\tcore volume\")\n",
    "        print(\"Veff\\t= %.4e\"%Veff, \"[m³] \\teffective core volume\")\n",
    "        print(\"Γ\\t= %.2f\"%Γ, \"[1 ] \\t\\tmodal confinement factor\")\n",
    "        print()\n",
    "        print(\"EM field parameters\")\n",
    "        print(\"λ0\\t= %.4e\"%λ0, \"[m] \\tresonance wavelength\")\n",
    "        print(\"ω0\\t= %.4e\"%ω0, \"[Hz] \\tresonance frequency\")\n",
    "        print(\"λp\\t= %.4e\"%λp, \"[m] \\tpump wavelength\")\n",
    "        print(\"ωp\\t= %.4e\"%ωp, \"[Hz] \\tpump frequency\")\n",
    "        print()\n",
    "        print(\"Ep\\t= %.4e\"%Ep, \"[√W] \\tsquare of EM field power\")\n",
    "        print(\"Es\\t= %.4e\"%Es, \"[√W] \\tsquare of EM field power\")\n",
    "        print()\n",
    "        print(\"Silicon physical parameters\")\n",
    "        print(\"ρSi\\t= %.4e\"%ρSi, \"[kg/m³] \\tSilicon density\")\n",
    "        print(\"Mring\\t= %.4e\"%Mring, \"[kg] \\tmass of the microring\")\n",
    "        print(\"Cp\\t= %.2e\"%Cp, \"[J/kg/K] \\tSilicon specific heat at constant pressure\")\n",
    "        print(\"MCp\\t= %.3e\"%MCp, \"[mW/ω0/K] \\tMring*Cp\")\n",
    "        print()\n",
    "        print(\"𝛾TH\\t= %.3e\"%𝛾TH, \"[Hz] \\tphenomenological heat loss rate\")\n",
    "        print(\"𝛾FC\\t= %.3e\"%𝛾FC, \"[Hz] \\tphenomenological free carrier population loss rate\")\n",
    "        print()\n",
    "        print(\"nSi\\t= %.3f\"%nSi, \"[1] \\t\\tSilicon refractive index\")\n",
    "        print(\"n0\\t= %.3f\"%n0, \"[1] \\t\\tdefault system refractive index\")\n",
    "        print(\"n2\\t= %.3e\"%n2, \"[m²/W] \\tSilicon intensity dependent refractive index\")\n",
    "        print(\"dndT\\t= %.3e\"%dndT, \"[1/K] \\tSilicon refractive index expansion term in temperature\")\n",
    "        print(\"dndN\\t= %.3e\"%dndN, \"[m³] \\tSilicon refractive index real expansion term in free carrier population\")\n",
    "        print(\"dαdN\\t= %.3e\"%dαdN, \"[m²] \\tSilicon refractive index imaginary expansion term in free carrier population\")\n",
    "        print(\"βtpa\\t= %.3e\"%βtpa, \"[m/W] \\tSilicon TPA coefficient\")\n",
    "        print(\"vg\\t= %d\"%vg, \"[m/s] \\tgroup velocity near ω0\")\n",
    "        print()\n",
    "        print(\"Coupling parameters\")\n",
    "        print(\"ĸa\\t= %.2f\"%κa, \"[1] \\t\\tfirst coupling constant\")\n",
    "        print(\"ĸb\\t= %.2f\"%κb, \"[1] \\t\\tsecond coupling constant\")\n",
    "        print(\"τa\\t= %.3e\"%τa, \"[s] \\tfirst extrinsic time constant\")\n",
    "        print(\"τb\\t= %.3e\"%τb, \"[s] \\tsecond extrinsic time constant\")\n",
    "        print(\"τb\\t= %.3e\"%τb, \"[s] \\tintrinsic time constant\")\n",
    "    else:\n",
    "        print(\"CONSTANTS and PARAMETERS\")\n",
    "        print()\n",
    "        print(\"general physics constants* (*not-normalized)\")\n",
    "        print(\"ε0\\t= %.8e\"%ε0, \"[F/m] \\tvacuum permittivity\")\n",
    "        print(\"c0\\t= %d\"%c0, \"[m/s] \\tspeed of light in vacuum\")\n",
    "        print(\"ħ\\t= %.8e\"%ħ, \"[J*s] \\tPlanck constant\")\n",
    "        print()\n",
    "        print(\"geometrical parameters\")\n",
    "        print(\"R\\t= %.5f\"%ñR, \"[λ0 ] \\tradius\")\n",
    "        print(\"w\\t= %.5f\"%ñw, \"[λ0 ] \\twidth\")\n",
    "        print(\"h\\t= %.5f\"%ñh, \"[λ0 ] \\theight\")\n",
    "        print(\"wga\\t= %.5f\"%ñwga, \"[λ0²] \\tcore area\")\n",
    "        print()\n",
    "        print(\"L\\t= %.5f\"%ñL, \"[λ0 ] \\tcore length\")\n",
    "        print(\"V\\t= %.5f\"%ñV, \"[λ0³] \\tcore volume\")\n",
    "        print(\"Veff\\t= %.5f\"%ñVeff, \"[λ0³] \\teffective core volume\")\n",
    "        print(\"Γ\\t= %.2f\"%Γ, \"[1 ] \\t\\tmodal confinement factor\")\n",
    "        print()\n",
    "        print(\"EM field parameters\")\n",
    "        print(\"λ0\\t= %d\"%ñλ0, \"[λ0] \\t\\tresonance wavelength\")\n",
    "        print(\"ω0\\t= %d\"%ñω0, \"[ω0] \\t\\tresonance frequency\")\n",
    "        print(\"λp\\t= %.5f\"%ñλp, \"[λ0] \\t\\tpump wavelength\")\n",
    "        print(\"ωp\\t= %.5f\"%ñωp, \"[ω0] \\t\\tpump frequency\")\n",
    "        print()\n",
    "        print(\"Ep\\t= %.5f\"%ñEp, \"[√mW] \\tsquare of EM field power\")\n",
    "        print(\"Es\\t= %.5f\"%ñEs, \"[√mW] \\tsquare of EM field power\")\n",
    "        print()\n",
    "        print(\"Silicon physical parameters\")\n",
    "        print(\"ρSi\\t= %.4e\"%ρSi, \"[kg/m³] \\tSilicon density\")\n",
    "        print(\"Mring\\t= %.4e\"%ñMring, \"[kg] \\tmass of the microring\")\n",
    "        print(\"Cp\\t= %.2e\"%ñCp, \"[mW/ω0/kg/K] Silicon specific heat at constant pressure\")\n",
    "        print(\"MCp\\t= %.3e\"%ñMCp, \"[mW/ω0/K] \\tMring*Cp\")\n",
    "        print()\n",
    "        print(\"𝛾TH\\t= %.3e\"%ñ𝛾TH, \"[ω0] \\tphenomenological heat loss rate\")\n",
    "        print(\"𝛾FC\\t= %.3e\"%ñ𝛾FC, \"[ω0] \\tphenomenological free carrier population loss rate\")\n",
    "        print()\n",
    "        print(\"nSi\\t= %.3f\"%nSi, \"[1] \\t\\tSilicon refractive index\")\n",
    "        print(\"n0\\t= %.3f\"%ñn0, \"[1] \\t\\tdefault system refractive index\")\n",
    "        print(\"n2\\t= %.3e\"%ñn2, \"[λ0²/mW] \\tSilicon intensity dependent refractive index\")\n",
    "        print(\"dndT\\t= %.3e\"%ñdndT, \"[1/K] \\tSilicon refractive index expansion term in temperature\")\n",
    "        print(\"dndN\\t= %.3e\"%ñdndN, \"[λ0³] \\tSilicon refractive index real expansion term in free carrier population\")\n",
    "        print(\"dαdN\\t= %.3e\"%ñdαdN, \"[λ0²] \\tSilicon refractive index imaginary expansion term in free carrier population\")\n",
    "        print(\"βtpa\\t= %.3e\"%ñβtpa, \"[λ0/mW] \\tSilicon TPA coefficient\")\n",
    "        print(\"vg\\t= %.3f\"%ñvg, \"[λ0*ω0] \\tgroup velocity near ω0\")\n",
    "        print()\n",
    "        print(\"Coupling parameters\")\n",
    "        print(\"ĸa\\t= %.3f\"%κa, \"[1] \\t\\tfirst coupling constant\")\n",
    "        print(\"ĸb\\t= %.3f\"%κb, \"[1] \\t\\tsecond coupling constant\")\n",
    "        print(\"τa\\t= %.5f\"%ñτa, \"[1/ω0] \\tfirst extrinsic time constant\")\n",
    "        print(\"τb\\t= %.5f\"%ñτb, \"[1/ω0] \\tsecond extrinsic time constant\")\n",
    "        print(\"τb\\t= %.5f\"%ñτb, \"[1/ω0] \\tintrinsic time constant\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CONSTANTS and PARAMETERS\n",
      "\n",
      "general physics constants* (*not-normalized)\n",
      "ε0\t= 8.85418782e-12 [F/m] \tvacuum permittivity\n",
      "c0\t= 299792458 [m/s] \tspeed of light in vacuum\n",
      "ħ\t= 1.05457180e-34 [J*s] \tPlanck constant\n",
      "\n",
      "geometrical parameters\n",
      "R\t= 5.80645 [λ0 ] \tradius\n",
      "w\t= 0.32258 [λ0 ] \twidth\n",
      "h\t= 0.12903 [λ0 ] \theight\n",
      "wga\t= 0.04162 [λ0²] \tcore area\n",
      "\n",
      "L\t= 36.48301 [λ0 ] \tcore length\n",
      "V\t= 1.51854 [λ0³] \tcore volume\n",
      "Veff\t= 1.51854 [λ0³] \teffective core volume\n",
      "Γ\t= 0.90 [1 ] \t\tmodal confinement factor\n",
      "\n",
      "EM field parameters\n",
      "λ0\t= 1 [λ0] \t\tresonance wavelength\n",
      "ω0\t= 1 [ω0] \t\tresonance frequency\n",
      "λp\t= 1.00032 [λ0] \t\tpump wavelength\n",
      "ωp\t= 0.99968 [ω0] \t\tpump frequency\n",
      "\n",
      "Ep\t= 31.62278 [√mW] \tsquare of EM field power\n",
      "Es\t= 0.31623 [√mW] \tsquare of EM field power\n",
      "\n",
      "Silicon physical parameters\n",
      "ρSi\t= 2.3290e+03 [kg/m³] \tSilicon density\n",
      "Mring\t= 1.3170e-14 [kg] \tmass of the microring\n",
      "Cp\t= 1.35e+20 [mW/ω0/kg/K] Silicon specific heat at constant pressure\n",
      "MCp\t= 1.783e+06 [mW/ω0/K] \tMring*Cp\n",
      "\n",
      "𝛾TH\t= 3.878e-08 [ω0] \tphenomenological heat loss rate\n",
      "𝛾FC\t= 1.293e-06 [ω0] \tphenomenological free carrier population loss rate\n",
      "\n",
      "nSi\t= 3.480 [1] \t\tSilicon refractive index\n",
      "n0\t= 3.480 [1] \t\tdefault system refractive index\n",
      "n2\t= 1.873e-09 [λ0²/mW] \tSilicon intensity dependent refractive index\n",
      "dndT\t= 1.860e-04 [1/K] \tSilicon refractive index expansion term in temperature\n",
      "dndN\t= -4.646e-10 [λ0³] \tSilicon refractive index real expansion term in free carrier population\n",
      "dαdN\t= 4.579e-04 [λ0²] \tSilicon refractive index imaginary expansion term in free carrier population\n",
      "βtpa\t= 5.097e-09 [λ0/mW] \tSilicon TPA coefficient\n",
      "vg\t= 0.250 [λ0*ω0] \tgroup velocity near ω0\n",
      "\n",
      "Coupling parameters\n",
      "ĸa\t= 0.150 [1] \t\tfirst coupling constant\n",
      "ĸb\t= 0.150 [1] \t\tsecond coupling constant\n",
      "τa\t= 12971.73741 [1/ω0] \tfirst extrinsic time constant\n",
      "τb\t= 12971.73741 [1/ω0] \tsecond extrinsic time constant\n",
      "τb\t= 12971.73741 [1/ω0] \tintrinsic time constant\n"
     ]
    }
   ],
   "source": [
    "print_const(normalized=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
