import numpy

left = numpy.random.random((100, 10))
right = numpy.random.random((10, 100))

A = left.dot(right)


def nmf(A, rank, epsilon=1e-10, max_rounds=10000, debug=True):
    '''
        Nonnegative matrix factorization. Factor the nonnegative matrix A = WH
        Such that W and H are non-negative and have small rank.
    '''
    n, m = A.shape
    W = numpy.random.random((n, rank))
    H = numpy.random.random((rank, m))

    H_factor, W_factor = numpy.ones(H.shape), numpy.ones(W.shape)
    rounds = 0

    while (numpy.max(numpy.abs(H_factor - 1)) > epsilon and
           numpy.max(numpy.abs(W_factor - 1)) > epsilon and
           rounds < max_rounds) or rounds == 0:
        H = H * H_factor
        W = W * W_factor

        H_factor = W.T.dot(A) / W.T.dot(W).dot(H)
        W_factor = A.dot(H.T) / W.dot(H).dot(H.T)

        if rounds % 5000 == 0:
            error = numpy.sum((A - W.dot(H))**2)
            threshold1 = numpy.max(numpy.abs(W_factor - 1))
            threshold2 = numpy.max(numpy.abs(W_factor - 1))
            print('error = %.5f, max= %.3f' % (error, max(threshold1, threshold2)))

        rounds += 1

    error = numpy.sum((A - W.dot(H))**2)
    print('final error = %.5f' % error)
    return W, H
