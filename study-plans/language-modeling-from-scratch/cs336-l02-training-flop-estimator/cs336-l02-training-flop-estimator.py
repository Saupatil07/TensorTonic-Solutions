def flop_estimator(matmuls, attention_flops=0):
    """
    Returns: dictionary containing exact forward, backward, and total FLOP counts
    """
    mat_mul = len(matmuls)
    forward_flops = 2
    forward_list = []
    total_forward = 0
    for i in range(mat_mul):
        for j in range(3):
            forward_flops = forward_flops*matmuls[i][j]
        print(forward_flops)
        forward_list.append(forward_flops)
        forward_flops = 2
    for i in range(len(forward_list)):
        total_forward += forward_list[i]
    total_forward = total_forward + attention_flops
    backward_flops = total_forward*2
    total_flops = total_forward + backward_flops
    return {"forward_flops":total_forward,"backward_flops":backward_flops,"total_flops":total_flops}
