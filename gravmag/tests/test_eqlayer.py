import numpy as np
from scipy.linalg import toeplitz, circulant, hankel
from numpy.testing import assert_almost_equal as aae
from numpy.testing import assert_equal as ae
from pytest import raises
from .. import eqlayer


# #### kernel_matrix_monopoles

# def test_kernel_matrix_monopoles_invalid_field():
#     "Verify if passing an invalid field raises an error"
#     # single source
#     S = {
#         'x' : np.array([0.]),
#         'y' : np.array([0.]),
#         'z' : np.array([0.])
#     }
#     # singe data point
#     P = {
#         'x' : np.array([  0.]),
#         'y' : np.array([  0.]),
#         'z' : np.array([-10.])
#     }
#     # string
#     with raises(ValueError):
#         eqlayer.kernel_matrix_monopoles(data_points=P, source_points=S, field='invalid-field')
#     # float
#     with raises(ValueError):
#         eqlayer.kernel_matrix_monopoles(data_points=P, source_points=S, field=3.4)
#     # tuple
#     with raises(ValueError):
#         eqlayer.kernel_matrix_monopoles(data_points=P, source_points=S, field=(9,0))
#     # list
#     with raises(ValueError):
#         eqlayer.kernel_matrix_monopoles(data_points=P, source_points=S, field=[4., 5.6, 3])
#     # uppercase
#     with raises(ValueError):
#         eqlayer.kernel_matrix_monopoles(data_points=P, source_points=S, field='X')


# def test_kernel_matrix_monopoles_shape():
#     "Verify if returns the correct shape"
#     # single source
#     S = {
#         'x' : np.ones(5),
#         'y' : np.ones(5),
#         'z' : np.ones(5)
#     }
#     # singe data point
#     P = {
#         'x' : np.zeros(5),
#         'y' : np.zeros(5),
#         'z' : np.zeros(5)
#     }
#     G = eqlayer.kernel_matrix_monopoles(data_points=P, source_points=S, field='y')
#     ae(G.shape, (5,5))


##### kernel_matrix_dipoles


def test_kernel_matrix_dipoles_invalid_field():
    "Verify if passing an invalid field raises an error"
    # single source
    S = {"x": np.array([0.0]), "y": np.array([0.0]), "z": np.array([0.0])}
    # singe data point
    P = {"x": np.array([0.0]), "y": np.array([0.0]), "z": np.array([-10.0])}
    # inc, dec, inct, dect
    inc, dec = -34.5, 19.0
    inct, dect = 10, 28.1

    # string
    with raises(ValueError):
        eqlayer.kernel_matrix_dipoles(
            data_points=P,
            source_points=S,
            inc=inc,
            dec=dec,
            field="invalid-field",
            inct=inct,
            dect=dect,
        )
    # float
    with raises(ValueError):
        eqlayer.kernel_matrix_dipoles(
            data_points=P,
            source_points=S,
            inc=inc,
            dec=dec,
            field=3.4,
            inct=inct,
            dect=dect,
        )
    # tuple
    with raises(ValueError):
        eqlayer.kernel_matrix_dipoles(
            data_points=P,
            source_points=S,
            inc=inc,
            dec=dec,
            field=(9, 0),
            inct=inct,
            dect=dect,
        )
    # list
    with raises(ValueError):
        eqlayer.kernel_matrix_dipoles(
            data_points=P,
            source_points=S,
            inc=inc,
            dec=dec,
            field=[4.0, 5.6, 3],
            inct=inct,
            dect=dect,
        )
    # uppercase
    with raises(ValueError):
        eqlayer.kernel_matrix_dipoles(
            data_points=P,
            source_points=S,
            inc=inc,
            dec=dec,
            field="X",
            inct=inct,
            dect=dect,
        )


def test_kernel_matrix_dipoles_invalid_inc_dec():
    "Verify if passing invalid inc and/or dec raises an error for field not 't'"
    # single source
    S = {"x": np.array([0.0]), "y": np.array([0.0]), "z": np.array([0.0])}
    # singe data point
    P = {"x": np.array([0.0]), "y": np.array([0.0]), "z": np.array([-10.0])}
    # inct, dect
    inct, dect = "invalid-inct", "invalid-dect"

    # inc string, dec ok
    inc, dec = "invalid-inc", 23.0
    with raises(ValueError):
        eqlayer.kernel_matrix_dipoles(
            data_points=P,
            source_points=S,
            inc=inc,
            dec=dec,
            field="x",
            inct=inct,
            dect=dect,
        )
    # inc ok, dec string
    inc, dec = 34.0, "invalid-dec"
    with raises(ValueError):
        eqlayer.kernel_matrix_dipoles(
            data_points=P,
            source_points=S,
            inc=inc,
            dec=dec,
            field="y",
            inct=inct,
            dect=dect,
        )
    # inc tuple, dec ok
    inc, dec = (1.6,), 32
    with raises(ValueError):
        eqlayer.kernel_matrix_dipoles(
            data_points=P,
            source_points=S,
            inc=inc,
            dec=dec,
            field="z",
            inct=inct,
            dect=dect,
        )
    # inc ok, dec list
    inc, dec = 12, [23.0]
    with raises(ValueError):
        eqlayer.kernel_matrix_dipoles(
            data_points=P,
            source_points=S,
            inc=inc,
            dec=dec,
            field="x",
            inct=inct,
            dect=dect,
        )
    # inc complex, dec ok
    inc, dec = 1 - 5j, 23.0
    with raises(ValueError):
        eqlayer.kernel_matrix_dipoles(
            data_points=P,
            source_points=S,
            inc=inc,
            dec=dec,
            field="y",
            inct=inct,
            dect=dect,
        )


def test_kernel_matrix_dipoles_ignore_inct_dect():
    "Verify if passing invalid inct and/or dect raises an error for the case in which field is 't'"
    # single source
    S = {"x": np.array([0.0]), "y": np.array([0.0]), "z": np.array([0.0])}
    # singe data point
    P = {"x": np.array([0.0]), "y": np.array([0.0]), "z": np.array([-10.0])}
    # inc, dec
    inc, dec = 10, 28.1

    # inc, dec string
    inct, dect = "invalid-inc", "invalid-dec"
    with raises(ValueError):
        eqlayer.kernel_matrix_dipoles(
            data_points=P,
            source_points=S,
            inc=inc,
            dec=dec,
            field="t",
            inct=inct,
            dect=dect,
        )
    # inc, dec complex
    inct, dect = 28 + 3j, 14.5
    with raises(ValueError):
        eqlayer.kernel_matrix_dipoles(
            data_points=P,
            source_points=S,
            inc=inc,
            dec=dec,
            field="t",
            inct=inct,
            dect=dect,
        )
    # inc, dec list
    inct, dect = [
        13.0,
    ], 24.0
    with raises(ValueError):
        eqlayer.kernel_matrix_dipoles(
            data_points=P,
            source_points=S,
            inc=inc,
            dec=dec,
            field="t",
            inct=inct,
            dect=dect,
        )
    # inc, dec tuple
    inct, dect = 13.0, (24.0,)
    with raises(ValueError):
        eqlayer.kernel_matrix_dipoles(
            data_points=P,
            source_points=S,
            inc=inc,
            dec=dec,
            field="t",
            inct=inct,
            dect=dect,
        )


def test_kernel_matrix_dipoles_shape():
    "Verify if returns the correct shape"
    # single source
    S = {"x": np.ones(5), "y": np.ones(5), "z": np.ones(5)}
    # singe data point
    P = {"x": np.zeros(5), "y": np.zeros(5), "z": np.zeros(5)}
    G = eqlayer.kernel_matrix_dipoles(
        data_points=P, source_points=S, inc=4.0, dec=5, field="y"
    )
    ae(G.shape, (5, 5))


##### method_CGLS


def test_method_CGLS_invalid_sensibility_matrices():
    "Check if passing an invalid list of sensibility matrices raises an error"
    data = [np.zeros(4), np.empty(6), np.ones(3)]
    eps = 1e-3
    ITMAX = 10
    # sensibility not array 2d
    G = [np.zeros((4, 5)), np.empty((6, 5)), ["invalid-matrix"]]
    with raises(ValueError):
        eqlayer.method_CGLS(
            sensibility_matrices=G,
            data_vectors=data,
            epsilon=eps,
            ITMAX=ITMAX,
            check_input=True,
        )
    # less matrices than datasets
    G = [np.zeros((4, 5)), np.empty((6, 5))]
    with raises(ValueError):
        eqlayer.method_CGLS(
            sensibility_matrices=G,
            data_vectors=data,
            epsilon=eps,
            ITMAX=ITMAX,
            check_input=True,
        )
    # one matrix with wrong number of columns
    G = [np.zeros((4, 6)), np.empty((6, 5)), np.ones((3, 5))]
    with raises(ValueError):
        eqlayer.method_CGLS(
            sensibility_matrices=G,
            data_vectors=data,
            epsilon=eps,
            ITMAX=ITMAX,
            check_input=True,
        )


def test_method_CGLS_invalid_data_vectors():
    "Check if passing an invalid list of data vectors raises an error"
    G = [np.zeros((4, 5)), np.empty((6, 5)), np.ones((3, 5))]
    eps = 1e-3
    ITMAX = 10
    # not array 1d
    data = [np.zeros(4), ['invalid-data-vector'], np.ones(3)]
    with raises(ValueError):
        eqlayer.method_CGLS(
            sensibility_matrices=G,
            data_vectors=data,
            epsilon=eps,
            ITMAX=ITMAX,
            check_input=True,
        )
    # less datasets than matrices
    data = [np.empty(6), np.ones(3)]
    with raises(ValueError):
        eqlayer.method_CGLS(
            sensibility_matrices=G,
            data_vectors=data,
            epsilon=eps,
            ITMAX=ITMAX,
            check_input=True,
        )
    # one data vector with wrong number of elements
    data = [np.zeros(4), np.empty(7), np.ones(3)]
    with raises(ValueError):
        eqlayer.method_CGLS(
            sensibility_matrices=G,
            data_vectors=data,
            epsilon=eps,
            ITMAX=ITMAX,
            check_input=True,
        )


# def test_method_CGLS_stop_criterion():
#     "Check if passing an invalid list of data vectors raises an error"
#     eps = 1e-3
#     ITMAX = 10
#     # define square matrices with order 5
#     G = [
#         np.toeplitz(np.arange(1,6)),
#         np.circulant(np.linspace(3.1, 11., 5)),
#         np.hankel([2, 3.5, 7., 1,. 9.3])
#     ]
#     # compute data vectors for null parameter vectors

#     with raises(ValueError):
#         eqlayer.method_CGLS(
#             sensibility_matrices=G,
#             data_vectors=data,
#             epsilon=eps,
#             ITMAX=ITMAX,
#             check_input=True,
#         )