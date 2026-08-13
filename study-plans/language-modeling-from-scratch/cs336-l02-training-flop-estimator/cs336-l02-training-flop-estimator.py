from math import prod
def flop_estimator(matmuls, attention_flops=0):
    """
    Returns: dictionary containing exact forward, backward, and total FLOP counts
    """
    matmul_flops = sum(2 * prod(shape) for shape in matmuls)

    forward_flops = matmul_flops + attention_flops
    backward_flops = 2 * forward_flops
    total_flops = 3 * forward_flops

    return {
        "forward_flops": forward_flops,
        "backward_flops": backward_flops,
        "total_flops": total_flops,
    }