'''
Created on Jun 26, 2015

@author: Aaron Klein
'''


import GPy
from robo.models.GPyModelMCMC import GPyModelMCMC
from robo.acquisition.EI import EI
from robo.maximizers.maximize import stochastic_local_search
from robo.recommendation.incumbent import compute_incumbent
from robo.benchmarks.branin import branin, get_branin_bounds
from robo.bayesian_optimization import BayesianOptimization


X_lower, X_upper, dims = get_branin_bounds()

maximizer = stochastic_local_search

kernel = GPy.kern.Matern52(input_dim=dims)
model = GPyModelMCMC(kernel, burnin=20, chain_length=100, n_hypers=10)

acquisition_func = EI(model, X_upper=X_upper, X_lower=X_lower, compute_incumbent=compute_incumbent, par=0.1)

bo = BayesianOptimization(acquisition_fkt=acquisition_func,
                          model=model,
                          maximize_fkt=maximizer,
                          X_lower=X_lower,
                          X_upper=X_upper,
                          dims=dims,
                          objective_fkt=branin,
                          save_dir="./test_output",
                          num_save=1)

bo.run(10)
