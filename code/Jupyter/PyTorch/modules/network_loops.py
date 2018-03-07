import numpy as np

def run_training(obj, train_x, train_y, valid_x, valid_y):

    print('# # # # # # # # # # # # # #')
    print('\nepochs\terror\t\tvalidation')
    for t in range(obj[0][7]):
        # Sets the learning to the initial lr decayed by gamma every step_size epochs
        obj[6].step()
        # Forward pass: Compute predicted y by passing x to the model
        y_pred = obj[1](train_x, obj[0][4], obj[0][6])
        #
        # Compute and print loss, on training set
        loss = obj[2](y_pred, train_y)
        obj[-1].append(loss.data[0])
        #
        if (t+1)%(obj[0][7]//20) == 0:
            # compute prediction ad loss on validation test, each 5% of the total epochs
            y_pred_valid = obj[1](valid_x, obj[0][4], obj[0][6])
            loss_valid = obj[2](y_pred_valid, valid_y)
            obj[-2].append(loss_valid.data[0])
            
            # run test
            correctness = 0
            for jj in range(valid_x.shape[0]):
                if valid_y.data[jj] == np.argmax(y_pred_valid.data[jj,:]):
                    correctness += 1
            correctness = correctness/valid_x.shape[0]*100
            obj[-3].append(correctness)
            
            # print index, train loss, validation loss, % correct
            print(t+1, '\t%.5f'%loss.data[0], '\t%.5f'%loss_valid.data[0], '\t%.2f'%correctness)
        #
        # Zero gradients, perform a backward pass, and update the weights.
        obj[4].zero_grad()
        loss.backward()
        obj[4].step()
    return obj

def run_test(obj, test_x, test_y, verbose=False):
                     
    y_pred = obj[1](test_x, obj[0][4], obj[0][6])
    
    correctness = 0
    for jj in range(test_x.shape[0]):
        if test_y.data[jj] == np.argmax(y_pred.data[jj,:]):
            correctness += 1
    correctness = correctness/test_x.shape[0]*100
    
    if verbose:
        print('%3.2f'%correctness)
    return correctness
