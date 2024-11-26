import numpy as np

#Generate w workers
def G_worker(w, WTypes = [[1,2],[2,3],[3,4]]):
    n_wt = len(WTypes)
    WorkerT = list(range(n_wt))
    WorkerT.extend(np.random.randint(0,n_wt,w-n_wt)) # types of w workers
    WorkerV = np.random.randint(1,4,w) # velocities of w workers
    WorkerV.sort()
    return WorkerT, WorkerV

# Generate n orders, Arrive is a list of each order's arrival time, Product is a list of the index of each order's required products, Quantity is a list of each order's required quantity of products
# lam represents the average number of orders that arrive per unit time and reflects the frequency that orders arrive; the coefficient of variant cv represents the degree of quantity fluctuations (Larger cv provides more fluctuating demand); mean represents the average number of products that each order requires
def G_order(n, p_max, lam, cv, mean = 10):
    #mean = 10
    #Process = np.random.normal(mean, mean*cv, n)
    Arrive = np.zeros(n)
    i = 1
    while i < n:
        Arrive[i] = Arrive[i-1] + np.random.exponential(1/lam)
        i += 1
    #Arrive = np.round(Arrive)
    Product = np.random.randint(1,p_max+1,n)
    Quantity = np.zeros(n)
    i = 0
    while i < n:
        while Quantity[i] <= 0.5:
            Quantity[i] = round(np.random.normal(mean, mean*cv))
        i += 1
    return Arrive, Product, Quantity

