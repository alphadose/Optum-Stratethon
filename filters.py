import numpy as np

def lead_lag(mylist):
    '''
    Transforms a list by adding a delayed copy of the sameself.

    Arguments:
        mylist (list): List of dimensions len_stream x dim_stream.

    Returns:
        np.array: Lead-lag transform of mylist.
    '''

    leadlist = np.concatenate([[mylist[0]], mylist])
    laglist = np.concatenate([mylist, [mylist[-1]]])

    return np.concatenate([leadlist, laglist], axis=1)


def add_time(mylist, init_time = 0., total_time = 1.):
    '''
    adds a normalised time variable
    should only use a half interval at begining and end


    Arguments:
        mylist (list):      List of dimensions len_stream x dim_stream.
        init_time (float):  Initial time.
        total_time (float): Total time of the stream.

    Returns:
        np.array: mylist with normalized time as the first dimension.
    '''
    ans = [[init_time + xn * total_time/(len(mylist)-1)] + list(x) for (xn,x) in enumerate(mylist)]
    return np.array(ans) ## note that the elements of list have to be lists or tuples - a path in other words

def home_and_pen_off(mylist):
    '''
    adds a pen off co-ordinate at end and then returns the main signal to zero

    Arguments:
        mylist (list): List of dimensions len_stream x dim_stream.

    Returns:
        np.array: mylist with an extra dimension representing pen-on and pen-off,
                  as well as an extra final point.

    '''
    ## pen on
    ans = [list(x) + [1.] for x in mylist]
    last = list(ans[-1])
    ## pen off
    last[-1] = 0.
    ans.append(last)
    ## home
    ans.append([0 for item in last])
    return np.array(ans)

def refocus(path, centre):
    '''
    premultiplies the stream path by the stream centre run backwards

    Arguments:
        path (list): First path.
        centre (list): Second path.

    Returns:
        np.array: centre multiplied by path, run backwards.
    '''
    return np.concatenate((centre[::-1], path), axis=0)


if __name__ == "__main__":
    path = np.array([[1., 2.], [4., 3.], [1., 1.]])
