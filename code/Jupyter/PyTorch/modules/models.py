import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F

 # define baseline network with relu (clamp)
class BaseReLU(torch.nn.Module):
    def __init__(self, D_in, H, D_out, n):
        super(BaseReLU, self).__init__()
        self.linear0 = torch.nn.Linear(D_in, H)
        for jj in range(n):
            exec("self.linear%d = torch.nn.Linear(H, H)" %(jj+1) );
        self.linearOut = torch.nn.Linear(H, D_out)
        
        # initialize the weight uniformly from 0 to 1
        #nn.init.uniform(self.linear0.weight, a=0, b=1)
        #nn.init.constant(self.linear0.bias, 0.0)
        #for jj in range(n):
        #    exec("nn.init.uniform(self.linear%d.weight, a=0, b=1)" %(jj+1) )
        #    exec("nn.init.constant(self.linear%d.bias, 0.0)" %(jj+1) )
        #nn.init.uniform(self.linearOut.weight, a=0, b=1)
        #nn.init.constant(self.linearOut.bias, 0.0)

    def forward(self, x, n, NL_out=False):
        
        h = []
        # sum (linear1) and then relu (clamp)
        h.append( self.linear0(x).clamp(min=0) )
        # sum (linear2) and then relu (clamp)
        for jj in range(n):
            exec("h.append( self.linear%d(h[-1]).clamp(min=0) )" %(jj+1) );
        # sum (out) and the output
        if not NL_out:
            y_pred = self.linearOut(h[-1])
        elif NL_out:
            y_pred = self.linearOut(h[-1])
        else:
            raise ValueError('NL_out must be either True or False, but it isn\'t')
        
        return y_pred # output = y_pred(icted)
        
# define different network with sigmoid
class Sigmoid(torch.nn.Module):
    def __init__(self, D_in, H, D_out, n):
        super(Sigmoid, self).__init__()
        self.linear0 = torch.nn.Linear(D_in, H)
        for jj in range(n):
            exec("self.linear%d = torch.nn.Linear(H, H)" %(jj+1) );
        self.linearOut = torch.nn.Linear(H, D_out)
        
        # initialize the weight uniformly from 0 to 1
        #nn.init.uniform(self.linear0.weight, a=0, b=1)
        #nn.init.constant(self.linear0.bias, 0.5)
        #for jj in range(n):
        #    exec("nn.init.uniform(self.linear%d.weight, a=0, b=1)" %(jj+1) )
        #    exec("nn.init.constant(self.linear%d.bias, 0.5)" %(jj+1) )
        #nn.init.uniform(self.linearOut.weight, a=0, b=1)
        #nn.init.constant(self.linearOut.bias, 0.5)

    def forward(self, x, n, NL_out=False):
        h = []
        # sum (linear1) and then sigmoid (F.sigmoid)
        h.append( F.sigmoid(self.linear0(x)) )
        # sum (linear2) and then sigmoid (F.sigmoid)
        for jj in range(n):
            exec("h.append( F.sigmoid(self.linear%d(h[-1]) ) )" %(jj+1) );
        # sum (out) and the output
        if not NL_out :
            y_pred = self.linearOut(h[-1])
        elif NL_out :
            y_pred = F.sigmoid( self.linearOut(h[-1]) )
        else:
            raise ValueError('NL_out must be either True or False, but it isn\'t')
        
        return y_pred # output = y_pred(icted)

# define best fit class 
class BestFit(torch.nn.Module):
    def __init__(self, D_in, H, D_out, n):
        super(BestFit, self).__init__()
        self.linear0 = torch.nn.Linear(D_in, H)
        for jj in range(n):
            exec("self.linear%d = torch.nn.Linear(H, H)" %(jj+1) );
        self.linearOut = torch.nn.Linear(H, D_out)
        
        # initialize the weight uniformly from 0 to 1
        #nn.init.uniform(self.linear0.weight, a=0, b=1)
        #nn.init.constant(self.linear0.bias, 0.0)
        #for jj in range(n):
        #    exec("nn.init.uniform(self.linear%d.weight, a=0, b=1)" %(jj+1) )
        #    exec("nn.init.constant(self.linear%d.bias, 0.0)" %(jj+1) )
        #nn.init.uniform(self.linearOut.weight, a=0, b=1)
        #nn.init.constant(self.linearOut.bias, 0.0)

    def forward(self, x, n, NL_out=False):
        
        # parameters
        p = [ 689.651615, 0.433819208, 1.31042204, -0.975437185, -0.518489780, 0.403015568, 0.502495627]
        
        #p[0], p[1], p[2], p[3], p[4], p[5], p[6]
        #  a,    b,    c,    d,    g,   x0,   x1)
        #b*sigmoid(a*(arg-x0))+c*relu(arg)+d*relu(arg-x0)+g*relu(arg-x1)
        
        h = []
        h.append( torch.mul( torch.sigmoid( self.linear0(x).add_(-p[5]).mul_(p[0]) ), p[1] ) )
        h[0].add_( self.linear0(x).clamp(min=0).mul_(p[2]) )
        h[0].add_( self.linear0(x).clamp(min=p[5]).mul_(p[3]) )
        h[0].add_( self.linear0(x).clamp(min=p[6]).mul_(p[4]) )
        
        # sum (linear2) and then nonlinear function
        for jj in range(n):
            exec("h.append( torch.mul( torch.sigmoid( self.linear%d(h[-1]).add_(-p[5]).mul_(p[0]) ), p[1] ) )" %(jj+1) );
            exec("h[jj+1].add_( self.linear%d(h[-2]).clamp(min=0).mul_(p[2]) )" %(jj+1) );
            exec("h[jj+1].add_( self.linear%d(h[-2]).clamp(min=p[5]).mul_(p[3]) )" %(jj+1) );
            exec("h[jj+1].add_( self.linear%d(h[-2]).clamp(min=p[6]).mul_(p[4]) )" %(jj+1) );
                     
        # sum (out) and the output
        if not NL_out :
            y_pred = self.linearOut(h[-1])
        elif NL_out:
            y_pred = torch.mul( torch.sigmoid( self.linearOut(h[-1]).add_(-p[5]).mul_(p[0]) ), p[1] )
            y_pred.add_( self.linearOut(h[-1]).clamp(min=0).mul_(p[2]) )
            y_pred.add_( self.linearOut(h[-1]).clamp(min=p[5]).mul_(p[3]) )
            y_pred.add_( self.linearOut(h[-1]).clamp(min=p[6]).mul_(p[4]) )
        else:
            raise ValueError('NL_out must be either True or False, but it isn\'t')
                                
        return y_pred # output = y_pred(icted)

# define fit with ReLU class 
class FitReLU(torch.nn.Module):
    def __init__(self, D_in, D_H, D_out, n):
        super(FitReLU, self).__init__()
        self.linear0 = torch.nn.Linear(D_in, D_H)
        for jj in range(n):
            exec("self.linear%d = torch.nn.Linear(D_H, D_H)" %(jj+1) );
        self.linearOut = torch.nn.Linear(D_H, D_out)
        
        # initialize the weight uniformly from 0 to 1
        #nn.init.uniform(self.linear0.weight, a=0, b=1)
        #nn.init.constant(self.linear0.bias, -0.5)
        #for jj in range(n):
        #    exec("nn.init.uniform(self.linear%d.weight, a=0, b=1)" %(jj+1) )
        #    exec("nn.init.constant(self.linear%d.bias, -0.5)" %(jj+1) )
        #nn.init.uniform(self.linearOut.weight, a=0, b=1)
        #nn.init.constant(self.linearOut.bias, -0.5)

    def forward(self, x, n, NL_out=False):
        
        # parameters
        p = [1.310, 41.516, 0.399, -42.491, 0.409]
        
        #p[0], p[1], p[2], p[3], p[4]
        #  a,    b,    x0,    c,   x1
        #a*relu(arg-)+b*relu(arg-x0)+(c)*relu(arg-x1)
        
        h = []
        h.append( self.linear0(x).clamp(min=0).mul_(p[0]) )
        h[0].add_( self.linear0(x).add_(-p[2]).clamp(min=0).mul_(p[1]) )
        h[0].add_( self.linear0(x).add_(-p[4]).clamp(min=0).mul_(p[3]) )
        
        # sum (linear2) and then nonlinear function
        for jj in range(n):
            exec("h.append( self.linear%d(h[-1]).clamp(min=0).mul_(p[0]) )" %(jj+1) );
            exec("h[jj+1].add_( self.linear%d(h[-2]).add_(-p[2]).clamp(min=0).mul_(p[1]) )" %(jj+1) );
            exec("h[jj+1].add_( self.linear%d(h[-2]).add_(-p[4]).clamp(min=0).mul_(p[3]) )" %(jj+1) );
                     
        # sum (out) and the output
        if not NL_out :
            y_pred = self.linearOut(h[-1])
        elif NL_out:
            y_pred = self.linearOut(h[-1]).clamp(min=0).mul_(p[0])
            y_pred.add_( self.linearOut(h[-1]).add_(-p[2]).clamp(min=0).mul_(p[1]) )
            y_pred.add_( self.linearOut(h[-1]).add_(-p[4]).clamp(min=0).mul_(p[3]) )
        else:
            raise ValueError('NL_out must be either True or False, but it isn\'t')
                                
        return y_pred # output = y_pred(icted)

# define fit with ReLU class 
class FitFlatReLU(torch.nn.Module):
    def __init__(self, D_in, D_H, D_out, n):
        super(FitFlatReLU, self).__init__()
        self.linear0 = torch.nn.Linear(D_in, D_H)
        for jj in range(n):
            exec("self.linear%d = torch.nn.Linear(D_H, D_H)" %(jj+1) );
        self.linearOut = torch.nn.Linear(D_H, D_out)

    def forward(self, x, n, NL_out=False):
        
        # parameters
        a, b, x0, c, x1 = [1.310, 41.516, 0.399, -42.491, 0.409]
        #a*relu(arg-)+b*relu(arg-x0)+(c)*relu(arg-x1)
        
        h = []
        h.append( self.linear0(x).clamp(min=0).mul_(a)+self.linear0(x).add_(-x0).clamp(min=0).mul_(b)+self.linear0(x).add_(-x1).clamp(min=0).mul_(c))
        
        # sum (linear2) and then nonlinear function
        for jj in range(n):
            exec( "h.append(self.linear%d(h[-1]).clamp(min=0).mul_(a)+self.linear%d(h[-1]).add_(-x0).clamp(min=0).mul_(b)+self.linear%d(h[-1]).add_(-x1).clamp(min=0).mul_(c))"%(jj+1,jj+1,jj+1) )
                     
        # sum (out) and the output
        if not NL_out :
            y_pred = self.linearOut(h[-1])
        elif NL_out:
            y_pred = self.linearOut(h[-1]).clamp(min=0).mul_(a)+self.linearOut(h[-1]).add_(-x0).clamp(min=0).mul_(b)+self.linearOut(h[-1]).add_(-x1).clamp(min=0).mul_(c)
        else:
            raise ValueError('NL_out must be either True or False, but it isn\'t')
                                
        return y_pred # output = y_pred(icted)
        
def generate_entry(obj, verbose = False):       
    entry = [obj[0],]
    if verbose:
        print('model name:', entry[0][0])
        print('model settings:', entry[0][1:])
        
    # append model
    if obj[1]=='base':
        entry.append( BaseReLU(entry[0][2], entry[0][3], entry[0][5], entry[0][4]) )
    elif obj[1]=='sigmoid':
        entry.append( Sigmoid(entry[0][2], entry[0][3], entry[0][5], entry[0][4]) )
    elif obj[1]=='bestfit':
        entry.append( BestFit(entry[0][2], entry[0][3], entry[0][5], entry[0][4]) )
    elif obj[1]=='fitrelu':
        entry.append( FitReLU(entry[0][2], entry[0][3], entry[0][5], entry[0][4]) )
    elif obj[1]=='fitflatrelu':
        entry.append( FitFlatReLU(entry[0][2], entry[0][3], entry[0][5], entry[0][4]) )
    else:
        raise ValueError('model type not recognised')
    if verbose:
        print('model:', entry[1])
    
    # append criterion
    if obj[2]=='MSE':
        entry.append( torch.nn.MSELoss(size_average=obj[3][0] ) )
        entry.append( obj[3] )
    elif obj[2]=='CEL':
        entry.append( torch.nn.CrossEntropyLoss(size_average=obj[3][0] ) )
        entry.append( obj[3] )
    else:
        raise ValueError('criterion type not recognised')
        
    if verbose:
        print('criterion:', entry[2], '\ncriterion settings:', entry[3])
    
    # append optimizer
    if obj[4]=='SGD':
        entry.append( torch.optim.SGD(entry[1].parameters(), lr=obj[5][0], momentum=obj[5][1]) )
        entry.append( obj[5] )
    #elif obj[4]=='':
    else:
        raise ValueError('optimizer type not recognised')
    
    if verbose:
        print('optimizer:', entry[4], '\noptimizer settings:', entry[5])
    
    # append scheduler
    if obj[6]=='StepLR':
        entry.append( torch.optim.lr_scheduler.StepLR( entry[4] , step_size=obj[7][0], gamma=obj[7][1]) )
        entry.append( obj[7] )
    #elif obj[6]=='':
    else:
        raise ValueError('scheduler type not recognised')
    
    if verbose:
        print('scheduler:', entry[6], '\noptimizer settings:', entry[7])
    
    # append empty errors list
    # test
    entry.append( [] )
    # validation
    entry.append( [] )
    # train
    entry.append( [] )
    print()
    
    return entry
