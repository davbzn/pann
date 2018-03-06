from .ConstantsAndParameters import *

def norm_single_source(var, par):
    # variables
    oxEF, oxI, oxΔN, oxΔT, oxΔn, oxΔ𝛾 = var
    # constants
    # ñc0, ñħ
    # parameters
    pωs1, pIs1, pκ, p𝛾, p𝛾TH, p𝛾FC, pMCpV, pn0, pn2, pdndT, pdndN, pdαdN, pβtpa, pV, pR = par
        
    #xEF = p𝛾*oxΔ𝛾/( np.power(1-(1-pκ**2)*p𝛾*oxΔ𝛾,2) + 4*(1-pκ**2)*p𝛾*oxΔ𝛾*np.power(np.sin( (pn0+oxΔn)*pωs1/ñc0*np.pi*pR ),2) )
    xEF = pκ**2/( np.power(1-(1-pκ**2)*p𝛾*oxΔ𝛾,2) + 4*(1-pκ**2)*p𝛾*oxΔ𝛾*np.power(np.sin( (pn0+oxΔn)*pωs1/ñc0*np.pi*pR ),2) )
    xI = xEF*pIs1
    xΔN = 1/p𝛾FC * pβtpa/(2*ñħ*pωs1) * np.power(xI,2)
    xΔT = 1/p𝛾TH * 1/MCpV * ( -np.log(p𝛾)/(np.pi*pR) + pβtpa*xI + pdαdN*xΔN ) * xI
    xΔn = pn2 * xI + pdndN*xΔN + pdndT*xΔT
    xΔ𝛾 = np.exp( -( pβtpa*xI + pdαdN*xΔN )*np.pi*pR )
    
    return (xEF, xI, xΔN, xΔT, xΔn, xΔ𝛾)
