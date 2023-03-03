# H2 molecule-complete-solution

Copyright 2020-2021 Maxime Dion <maxime.dion@usherbrooke.ca>
This project has been modified by Obinna Uzoh during the
QSciTech-QuantumBC 2023 virtual workshop on quantum chemistry simulation.

This is a completed version of the solution to find the ground state of hydrogen molecule based on variational quantum eigen-solver (VQE) using quantum computing.

Description of the files :
- hamiltonian.py : This files defines the FermionicHamiltonian class and subclasses. 
- pauli_string.py : Defines PauliString and LinearCombinaisonPauliString class. 
- mapping.py : Defines the JordanWigner mapping. 
- estimator.py : Defines the abstract class Estimator and the BasicEstimator class.
- solver.py : Defines VQESolver and ExactSolver. You should be able to complete it after the lecture on VQE. 

Other files :
- hamiltonian_integrals_Colab.ipynb: Colab notebook to get the H2 hamiltonian integrals from the PYSCF compuational chemistry suite.
- H2_hamiltonian_integrals: Contains the one body and two body integrals (no spin) for a H2 molecule of various interatomic spacing, d.
- Integrals_sto-3g_H2_d_0.7350_no_spin.npz : Contains the one body and two body integrals (no spin) for a H2 molecule with d=0.735. The two body is given in the physicist order.
- activity_mapping.ipynb: Jupyter notebook implementing pauli strings, and the mapping of the fermionic operators to the Jordan-Wigner operators.
- activity_vqe.ipynb : Jupyter notebook implementing the ground state solution by VQE using quantum circuits. 
- dissociation_curve.ipynb: Jupyter notebook for post-processing. Obtains the dissociation curve of the H2 molecule. 
