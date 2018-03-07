import matplotlib
import matplotlib.pyplot as plt 
from cycler import cycler
import numpy as np
import itertools

def flip(items, ncol):
    return itertools.chain(*[items[i::ncol] for i in range(ncol)])

color_list = [
    (0.94117647, 0.63921569, 1.        ),
    (0.        , 0.45882353, 0.8627451 ),
    (0.6       , 0.24705882, 0.        ),
    (0.29803922, 0.        , 0.36078431),
    (0.09803922, 0.09803922, 0.09803922),
    (0.        , 0.36078431, 0.19215686),
    (0.16862745, 0.80784314, 0.28235294),
    (1.        , 0.8       , 0.6       ),
    (0.50196078, 0.50196078, 0.50196078),
    (0.58039216, 1.        , 0.70980392),
    (0.56078431, 0.48627451, 0.        ),
    (0.61568627, 0.8       , 0.        ),
    (0.76078431, 0.        , 0.53333333),
    (0.        , 0.2       , 0.50196078),
    (1.        , 0.64313725, 0.01960784),
    (1.        , 0.65882353, 0.73333333),
    (0.25882353, 0.4       , 0.        ),
    (1.        , 0.        , 0.0627451 ),
    (0.36862745, 0.94509804, 0.94901961),
    (0.        , 0.6       , 0.56078431),
    (0.87843137, 1.        , 0.4       ),
    (0.45490196, 0.03921569, 1.        ),
    (0.6       , 0.        , 0.        ),
    (1.        , 1.        , 0.50196078),
    (1.        , 1.        , 0.        ),
    (1.        , 0.31372549, 0.01960784)
]

### define settings for plots
def show_graph(obj, string='loglog'):
    fig = plt.figure(figsize=(3*6.4, 2*4.8)) # default = 6.4, 4.8
    ax1 = fig.add_subplot(111)
    
    ax1.set_prop_cycle( cycler('color', color_list ) )
    
    error = []
    valid = []
    if string=='loglog':
        for ii, ee in obj.items():
            ax1.plot(np.NaN, np.NaN, '-', color='none', label='%d %s'%(ii,ee[0][0]) )
            error.append( ax1.loglog( ee[-1][:], s='-', label='training') )
            valid.append( ax1.loglog( np.linspace(ee[0][7]//20,ee[0][7],len(ee[-2][:]) ), ee[-2][:], '.',
                                      label='validation', c=error[-1][0].get_color()) )
    elif string=='logy':
        for ii, ee in obj.items():
            ax1.plot(np.NaN, np.NaN, '-', color='none', label='%d %s'%(ii,ee[0][0]) )
            error.append( ax1.semilogy( ee[-1][:], ls='-', label='training') )
            valid.append( ax1.semilogy( np.linspace(ee[0][7]//20,ee[0][7],len(ee[-2][:])), ee[-2][:], '.',
                                        label='validation', c=error[-1][0].get_color() ) )
    elif string=='logx':
        for ii, ee in obj.items():
            ax1.plot(np.NaN, np.NaN, '-', color='none', label='%d %s'%(ii,ee[0][0]) )
            error.append( ax1.semilogx( ee[-1][:], ls='-', label='training' ) )
            valid.append( ax1.semilogx( np.linspace(ee[0][7]//20,ee[0][7],len(ee[-2][:])), ee[-2][:], '.',
                                        label='validation', c=error[-1][0].get_color() ) )
    else:
        for ii, ee in obj.items():
            ax1.plot(np.NaN, np.NaN, '-', color='none', label='%d %s'%(ii,ee[0][0]) )
            error.append( ax1.plot( ee[-1][:], ls='-', label='training' ) )
            valid.append( ax1.plot( np.linspace(ee[0][7]//20,ee[0][7],len(ee[-2][:])), ee[-2][:], '.',
                          label='validation', c=error[-1][0].get_color() ) )

    ax1.set_xlabel('epochs', fontsize = 16)
    ax1.set_ylabel('loss', fontsize = 16)
    title_string = '%d epochs'%obj[0][0][-1]
    ax1.set_title(title_string, fontsize = 16)

    handles, labels = ax1.get_legend_handles_labels()
    legend = ax1.legend(flip(handles, 6), flip(labels, 6), bbox_to_anchor=(0., -.05, 1., -.05),
                        loc=2, ncol=6, mode="expand", borderaxespad=0., fontsize=20)
    
#    legend = ax1.legend(bbox_to_anchor=(0., -.05, 1., -.05), loc=2, ncol=6, mode="expand", borderaxespad=0.)

#    plt.show()
#    plt.close()
    
    return [fig, ax1, error, valid]

def print_spec(obj):
	print()
