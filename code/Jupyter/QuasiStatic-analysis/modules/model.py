from .ConstantsAndParameters import *

def equations(var, par):
    # variables
    oxUp, oxUs, oxUtot, oxΔN, oxΔT, oxΔω = var
    # parameters
    pωs, pωp, pω0, pEp, pEs, pτa, pτb, pτ0, p𝛾TH, p𝛾FC, pMCp, pn0, pn2, pdndT, pdndN, pdαdN, pβtpa, pΓ, pV, pVeff = par
    # constants
    # c0, ħ

    xUp   = -1.0J*np.sqrt(2/pτa)*pEp/(-1.0J*(pωp-pω0-oxΔω)-(1/pτa+1/pτb+1/pτ0))
    xUs   = -1.0J*np.sqrt(2/pτa)*pEs/(-1.0J*(pωs-pω0-oxΔω)-(1/pτa+1/pτb+1/pτ0))
    xUtot = np.abs(xUp)**2 + np.abs(xUs)**2
    
    xΔN = c0**2*pβtpa/p𝛾FC / ( 2*ħ*pωp*pV*pVeff*np.power(pn0,2) ) *np.power(xUtot,2)
    xΔT = 1/( p𝛾TH*pMCp ) * (2/pτ0 + pdαdN*c0*pΓ/pn0*xΔN + ( np.power(c0/pn0,2)*pβtpa )/pVeff *xUtot ) * xUtot
    
    xΔω_TOE  = (-2*pω0/pn0*pdndT)*pΓ*xΔT
    xΔω_FC   = (-2*pω0/pn0*pdndN + 1.0J*pdαdN*c0/pn0)*pΓ*xΔN
    xΔω_KERR = (-2*pω0*c0*pn2/np.power(pn0,2) + 1.0J*np.power(c0/pn0,2)*pβtpa)/pVeff*xUtot
    xΔω = (xΔω_TOE + xΔω_FC + xΔω_KERR)
    
    return (xUp, xUs, xUtot, xΔN, xΔT, xΔω)

def ñequations(var, par):
    # variables
    oxUp, oxUs, oxUtot, oxΔN, oxΔT, oxΔω = var
    # normalized parameters
    pωs, pωp, pω0, pEp, pEs, pτa, pτb, pτ0, p𝛾TH, p𝛾FC, pMCp, pn0, pn2, pdndT, pdndN, pdαdN, pβtpa, pΓ, pV, pVeff = par
    # constants
    # c0, ħ

    xUp   = -1.0J*np.sqrt(2/pτa)*pEp/(-1.0J*(pωp-1.0-oxΔω)-(1/pτa+1/pτb+1/pτ0))
    xUs   = -1.0J*np.sqrt(2/pτa)*pEs/(-1.0J*(pωs-1.0-oxΔω)-(1/pτa+1/pτb+1/pτ0))
    xUtot = np.abs(xUp)**2 + np.abs(xUs)**2
    
    xΔN = pβtpa/p𝛾FC / ( 8*3.94507e-03*pωp*pV*pVeff*np.power(np.pi*pn0,2) ) *np.power(xUtot,2)
    xΔT = 1/( p𝛾TH*pMCp ) * (2/pτ0 + pdαdN/(2*np.pi*pn0)*pΓ*xΔN + np.power(2*np.pi*pn0,-2)*pβtpa/pVeff *xUtot ) * xUtot
    
    xΔω_TOE  = (-2.0/pn0*pdndT)*pΓ*xΔT
    xΔω_FC   = (-2.0/pn0*pdndN + 1.0J*pdαdN/(2*np.pi*pn0))*pΓ*xΔN
    xΔω_KERR = (-2.0*pn2/(2*np.pi*np.power(pn0,2)) + 1.0J*np.power(2*np.pi*pn0,2)*pβtpa)/pVeff*xUtot
    xΔω = (xΔω_TOE + xΔω_FC + xΔω_KERR)
    
    return (xUp, xUs, xUtot, xΔN, xΔT, xΔω)

def system_eq(var, *par):
    # variables
    xUpR, xUpI, xUsR, xUsI, xUtot, xΔN, xΔT, xΔωR, xΔωI = var
    # parameters
    pωs, pωp, pω0, pEp, pEs, pτa, pτb, pτ0, p𝛾TH, p𝛾FC, pMCp, pn0, pn2, pdndT, pdndN, pdαdN, pβtpa, pΓ, pV, pVeff = par
    # constants
    # c0, ħ

    fUpR = -xUpR - np.sqrt(2/pτa)*pEp * (pωp-pω0-xΔωR) / (np.power(pωp-pω0-xΔωR, 2)+np.power(1/pτa+1/pτb+1/pτ0+xΔωI,2))
    fUpI = -xUpI - np.sqrt(2/pτa)*pEp * (1/pτa+1/pτb+1/pτ0+xΔωI) / (np.power(pωp-pω0-xΔωR, 2)+np.power(1/pτa+1/pτb+1/pτ0+xΔωI,2))
    
    fUsR = -xUsR - np.sqrt(2/pτa)*pEs * (pωs-pω0-xΔωR) / (np.power(pωs-pω0-xΔωR, 2)+np.power(1/pτa+1/pτb+1/pτ0+xΔωI,2))
    fUsI = -xUsI - np.sqrt(2/pτa)*pEs * (1/pτa+1/pτb+1/pτ0+xΔωI) / (np.power(pωs-pω0-xΔωR, 2)+np.power(1/pτa+1/pτb+1/pτ0+xΔωI,2))
    
    fUt  = -xUtot+ xUpR**2 + xUpI**2 + xUsR**2 + xUsI**2
    
    fΔN  = -xΔN  + c0**2*pβtpa/p𝛾FC / ( 2*ħ*pωp*pV*pVeff*np.power(pn0,2) ) *np.power(xUtot,2)
    fΔT  = -xΔT  + 1/( p𝛾TH*pMCp ) * (2/pτ0 + pdαdN*c0*pΓ/pn0*xΔN + ( np.power(c0/pn0,2)*pβtpa )/pVeff *xUtot ) * xUtot
        
    fΔωR = -xΔωR + (-2*pω0/pn0*pdndT)*pΓ*xΔT + (-2*pω0/pn0*pdndN) * pΓ*xΔN + (-2*pω0*c0*pn2/np.power(pn0,2)) / pVeff*xUtot
    fΔωI = -xΔωI + (pdαdN*c0/pn0) * pΓ*xΔN + (np.power(c0/pn0,2)*pβtpa) / pVeff*xUtot
    
    return (xUpR, xUpI, xUsR, xUsI, xUtot, xΔN, xΔT, xΔωR, xΔωI)

def ñsystem_eq(var, *par):
    # variables
    xUpR, xUpI, xUsR, xUsI, xUtot, xΔN, xΔT, xΔωR, xΔωI = var
    # normalized parameters
    pωs, pωp, pω0, pEp, pEs, pτa, pτb, pτ0, p𝛾TH, p𝛾FC, pMCp, pn0, pn2, pdndT, pdndN, pdαdN, pβtpa, pΓ, pV, pVeff = par
    # constants
    # c0, ħ

    fUpR = -xUpR - np.sqrt(2/pτa)*pEp * (pωp-1-xΔωR) / (np.power(pωp-1-xΔωR, 2)+np.power(1/pτa+1/pτb+1/pτ0+xΔωI,2))
    fUpI = -xUpI - np.sqrt(2/pτa)*pEp * (1/pτa+1/pτb+1/pτ0+xΔωI) / (np.power(pωp-1-xΔωR, 2)+np.power(1/pτa+1/pτb+1/pτ0+xΔωI,2))
    
    fUsR = -xUsR - np.sqrt(2/pτa)*pEs * (pωs-1-xΔωR) / (np.power(pωs-1-xΔωR, 2)+np.power(1/pτa+1/pτb+1/pτ0+xΔωI,2))
    fUsI = -xUsI - np.sqrt(2/pτa)*pEs * (1/pτa+1/pτb+1/pτ0+xΔωI) / (np.power(pωs-1-xΔωR, 2)+np.power(1/pτa+1/pτb+1/pτ0+xΔωI,2))
    
    fUt  = -xUtot+ xUpR**2 + xUpI**2 + xUsR**2 + xUsI**2
    
    fΔN  = -xΔN  + pβtpa/p𝛾FC / ( 8*3.94507e-03*pωp*pV*pVeff*np.power(np.pi*pn0,2) ) *np.power(xUtot,2)
    fΔT  = -xΔT  + 1/( p𝛾TH*pMCp ) * (2/pτ0 + pdαdN/(2*np.pi*pn0)*pΓ*xΔN + np.power(2*np.pi*pn0,-2)*pβtpa/pVeff *xUtot ) * xUtot

    fΔωR = -xΔωR + (-2.0/pn0*pdndT)*pΓ*xΔT + (-2.0/pn0*pdndN)*pΓ*xΔN + (-2.0*pn2/(2*np.pi*np.power(pn0,2)))/pVeff*xUtot
    fΔωI = -xΔωI + (pdαdN/(2*np.pi*pn0))*pΓ*xΔN + (np.power(2*np.pi*pn0,2)*pβtpa)/pVeff*xUtot
    
    return (xUpR, xUpI, xUsR, xUsI, xUtot, xΔN, xΔT, xΔωR, xΔωI)