import numpy as np


def are_rectangular_prisms(prisms):
    """
    Check if prisms is a dictionary formed by 6 numpy arrays 1d.

    parameters
    ----------
    prisms : generic object 
        Python object to be verified.

    returns
    -------
    P : int
        Total number of prisms.
    """
    if type(prisms) != dict:
        raise ValueError("prisms must be a dictionary")
    if list(prisms.keys()) != ['x1', 'x2', 'y1', 'y2', 'z1', 'z2']:
        raise ValueError("prisms must have the following 6 keys: 'x1', 'x2', 'y1', 'y2', 'z1', 'z2'")
    for key in prisms.keys():
        if type(prisms[key]) != np.ndarray:
            raise ValueError("all keys in prisms must be numpy arrays")
    for key in prisms.keys():
        if prisms[key].ndim != 1:
            raise ValueError("all keys in prisms must be a numpy array 1d")
    P = prisms['x1'].size
    for key in prisms.keys():
        if prisms[key].size != P:
            raise ValueError("all keys in prisms must have the same number of elements")
    # check the x lower and upper limits
    if np.any(prisms['x2'] <= prisms['x1']):
        raise ValueError(
            "all 'x2' values must be greater than 'x1' values."
            )
    # check the y lower and upper limits
    if np.any(prisms['y2'] <= prisms['y1']):
        raise ValueError(
            "all 'y2' values must be greater than 'y1' values."
            )
    # check the z lower and upper limits
    if np.any(prisms['z2'] <= prisms['z1']):
        raise ValueError(
            "all 'z2' values must be greater than 'z1' values."
            )

    return P


def are_coordinates(coordinates):
    """
    Check if coordinates is a dictionary formed by 3 numpy arrays 1d.

    parameters
    ----------
    coordinates : generic object 
        Python object to be verified.

    returns
    -------
    D : int
        Total number of points.
    """
    if type(coordinates) != dict:
        raise ValueError("coordinates must be a dictionary")
    if list(coordinates.keys()) != ['x', 'y', 'z']:
        raise ValueError("coordinates must have the following 3 keys: 'x', 'y', 'z'")
    for key in coordinates.keys():
        if type(coordinates[key]) != np.ndarray:
            raise ValueError("all keys in coordinates must be numpy arrays")
    for key in coordinates.keys():
        if coordinates[key].ndim != 1:
            raise ValueError("all keys in coordinates must be a numpy array 1d")
    D = coordinates['x'].size
    if (coordinates['y'].size != D) or (coordinates['z'].size != D):
        raise ValueError("all keys in coordinates must have the same number of elements")
    
    return D


def is_scalar(x, positive=True):
    """
    Check if x is a float or int.

    parameters
    ----------
    x : generic object
        Python object to be verified.
    positive : boolean
        If True, impose that x must be positive.
    """
    if isinstance(x, (float, int)) is False:
        raise ValueError(
            "x must be in float or int"
        )
    if positive == True:
        if x <= 0:
            raise ValueError(
                "x must be positive"
            )


def is_integer(x, positive=True):
    """
    Check if x is an int.

    parameters
    ----------
    x : generic object
        Python object to be verified.
    positive : boolean
        If True, impose that x must be positive.
    """
    if isinstance(x, int) is False:
        raise ValueError(
            "x must be an int"
        )
    if positive == True:
        if x <= 0:
            raise ValueError(
                "x must be positive"
            )


def is_array(x, ndim, shape):
    """
    Check if x is a numpy array having specific ndim and shape.

    parameters
    ----------
    prop : generic object 
        Python object to be verified.
    ndim : int
        Positive integer defining the dimension of x.
    shape : tuple
        Tuple defining the shape of x.
    """
    if (type(ndim) != int) and (ndim <= 0):
        raise ValueError("'ndim' must be a positive integer")
    if (type(shape) != tuple) or (len(shape) != ndim):
        raise ValueError("'shape' must be a tuple of 'ndim' elements")
    for item in shape:
        if (type(item) != int) and (item <= 0):
            raise ValueError("'shape' must be formed by positive integers")
    if type(x) != np.ndarray:
        raise ValueError("x must be a numpy array")
    if x.ndim != ndim:
        raise ValueError(
            "x.ndim ({}) ".format(x.ndim) + "not equal to the predefined ndim {}".format(ndim)
        )
    if x.shape != shape:
        raise ValueError(
            "x.shape ({}) ".format(x.shape) + "not equal to the predefined shape {}".format(shape)
        )


# wavenumbers


def are_wavenumbers(wavenumbers):
    """
    Check if wavenumbers is a dictionary formed by 3 numpy arrays 2d. 
    (See function 'gravmag.transforms.wavenumbers').

    parameters
    ----------
    wavenumbers: generic objects
        Python objects to be verified.
    """
    if type(wavenumbers) != dict:
        raise ValueError("wavenumbers must be a dictionary")
    if list(wavenumbers.keys()) != ['x', 'y', 'z']:
        raise ValueError("wavenumbers must have the following 3 keys: 'x', 'y', 'z'")
    for key in wavenumbers.keys():
        if type(wavenumbers[key]) != np.ndarray:
            raise ValueError("all keys in wavenumbers must be numpy arrays")
    for key in wavenumbers.keys():
        if wavenumbers[key].ndim != 2:
            raise ValueError("all keys in wavenumbers must be a numpy array 2d")
    shape = wavenumbers['x'].shape
    if (wavenumbers['y'].shape != shape) or (wavenumbers['z'].shape != shape):
        raise ValueError("all keys in wavenumbers must have the same shape")
    if np.any(wavenumbers['x'][0, :] != 0):
        raise ValueError("first line of key 'x' must be 0")
    if np.any(wavenumbers['y'][:, 0] != 0):
        raise ValueError("first column of key 'y' must be 0")
    if np.any(wavenumbers['z'] < 0):
        raise ValueError("all elements of key 'z' must be positive or zero")


def sensibility_matrix_and_data(G, data):
    """
    Check if G and data are consistent numpy arrays.

    parameters
    ----------
    G , data : generic objects
        Python objects to be verified.
    """
    if type(G) != np.ndarray:
        raise ValueError("G must be a numpy array")
    if type(data) != np.ndarray:
        raise ValueError("data must be a numpy array")
    if G.ndim != 2:
        raise ValueError("G must be a matrix")
    if data.ndim != 1:
        raise ValueError("data must be a vector")
    if G.shape[0] != data.size:
        raise ValueError("Sensibility matrix rows mismatch data size")