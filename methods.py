def euler(f, t, t0, x0, delta, t_amb, k):
    xs = [x0]
    ts = [t0]
    res_xs = []
    res_ts = []
    steps = int((t - t0) / delta)
    
    for i in range(steps):
        ts.append((i+1)*delta)
        xs.append(xs[i] + delta*f(ts[i], xs[i], t_amb, k))
        
        if((i!=0) and (i!=steps)):
            res_ts.append(ts[i])
            res_xs.append(xs[i])

    res_ts.append(ts[-1])
    res_xs.append(xs[-1])
    return res_ts, res_xs


def runge_kutta_4(f, t, t0, x0, delta, t_amb, k):
    xs = [x0]
    ts = [t0]
    res_xs = []
    res_ts = []
    derivadas = []
    steps = int((t-t0)/delta)

    for i in range(steps):
        ts.append((i+1)*delta)

        k1 = f(ts[i], xs[i], t_amb, k)
        k2 = f(ts[i] + delta/2, xs[i] + delta/2*k1, t_amb, k)
        k3 = f(ts[i] + delta/2, xs[i] + delta/2*k2, t_amb, k)
        k4 = f(ts[i] + delta, xs[i] + delta*k3, t_amb, k)
        xs.append(xs[i] + delta/6*(k1 + 2*k2 + 2*k3 + k4))
        derivadas.append(k1)

        if((i!=0) and (i!=steps)):
            res_ts.append(ts[i])
            res_xs.append(xs[i])

    res_ts.append(ts[-1])
    res_xs.append(xs[-1])
    return res_ts, res_xs, derivadas
