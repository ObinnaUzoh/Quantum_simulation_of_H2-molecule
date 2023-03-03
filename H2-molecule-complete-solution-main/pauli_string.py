"""
pauli_string.py - Define PauliString and LinearCombinaisonPauliString

Copyright 2020-2021 Maxime Dion <maxime.dion@usherbrooke.ca>
This file has been modified by <Your,Name> during the
QSciTech-QuantumBC virtual workshop on gate-based quantum computing.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import numpy as np
from typing import Union, Tuple, List
from numpy.typing import NDArray


class PauliString:

    def __init__(self, z_bits: NDArray[np.bool_], x_bits: NDArray[np.bool_]):
        """
        Describe a Pauli string as 2 arrays of booleans.
        The PauliString represents (-1j)**(z_bits*x_bits) Z**z_bits X**x_bits.

        Args:
            z_bits (np.ndarray<bool>): True where a Z Pauli is applied.
            x_bits (np.ndarray<bool>): True where a X Pauli is applied.

        Raises:
            ValueError: [description]
        """

        if len(z_bits) != len(x_bits):
            raise ValueError('z_bits and x_bits must have the same number of elements')
        self.z_bits = z_bits
        self.x_bits = x_bits

    def __str__(self) -> str:
        """
        String representation of the PauliString.

        Returns:
            str: String of I, Z, X and Y.
        """

        pauli_labels = 'IZXY'
        pauli_choices = (self.z_bits + 2*self.x_bits).astype(int)
        out = ''
        for i in reversed(pauli_choices):
            out += pauli_labels[i]
        return out

    def __len__(self) -> int:
        """
        Number of Pauli in the PauliString.
        Also the number of qubits.

        Returns:
            int: Length of the PauliString, also number of qubits.
        """

        return len(self.z_bits)

    def __mul__(self, other: Union['PauliString', complex, float, int]) -> Union[Tuple['PauliString', complex], 'LinearCombinaisonPauliString']:
        """
        Allow the use of '*' with other PauliString or with a coef (numeric).

        Args:
            other (PauliString): Will compute the product 
            or
            other (float): [description]

        Returns:
            PauliString, complex: When other is a PauliString
            or
            LinearCombinaisonPauliString : When other is numeric
        """

        if isinstance(other, PauliString):
            return self.mul_pauli_string(other)
        else:
            return self.mul_coef(other)

    def __rmul__(self, other: Union['PauliString', complex, float, int]) -> Union[Tuple['PauliString', float], 'LinearCombinaisonPauliString']:
        """
        Same as __mul__. Allow the use of '*' with a preceding coef (numeric) Like in 0.5 * PauliString

        Args:
            other (PauliString): Will compute the product 
            or
            other (float): [description]

        Returns:
            PauliString, complex: When other is a PauliString
            or
            LinearCombinaisonPauliString : When other is numeric
        """

        return self.__mul__(other)

    @classmethod
    def from_zx_bits(cls, zx_bits: NDArray[np.bool_]) -> 'PauliString':
        """
        Construct a PauliString from a single array<bool> of len 2n.

        Args:
            zx_bits (np.array<bool>): An array of bools. First n bits specify the Zs. Second half specify the Xs.

        Returns:
            PauliString: The Pauli string specified by the 'zx_bits'.
        """

        z_bits = x_bits = None

        ################################################################################################################
        # YOUR CODE HERE
        # TO COMPLETE (after lecture on mapping)

        nbits = int(len(zx_bits)/2)
        z_bits = zx_bits[:nbits]
        x_bits = zx_bits[nbits:]
    
        
        ################################################################################################################
        
#         raise NotImplementedError()

        return cls(z_bits, x_bits)

    @classmethod
    def from_str(cls, pauli_str: str) -> 'PauliString':
        """
        Construct a PauliString from a str (as returned by __str__).

        Args:
            pauli_str (str): String of length n made of 'I', 'X', 'Y' and 'Z'.

        Returns:
            PauliString: The Pauli string specified by the 'pauli_str'.
        """

        z_bits = x_bits = None

        ################################################################################################################
        # YOUR CODE HERE
        # TO COMPLETE (after lecture on mapping)
        z_bits = []
        x_bits = []
        for _ in pauli_str:
            if _ == 'Z':
                z_bits.append(1)    
                x_bits.append(0)    
            if _ == 'X':
                z_bits.append(0)
                x_bits.append(1)
            if _ == 'I':
                z_bits.append(0)
                x_bits.append(0)
            if _ == 'Y':
                z_bits.append(1)
                x_bits.append(1)
        z_bits.reverse()
        x_bits.reverse()
        z_bits = np.array(z_bits, dtype = bool)
        x_bits = np.array(x_bits, dtype = bool)     
        ################################################################################################################
        
#         raise NotImplementedError()
        
        return cls(z_bits, x_bits)

    def to_zx_bits(self) -> NDArray[np.bool_]:
        """
        Return the zx_bits representation of the PauliString.
        Useful to compare PauliString together.

        Returns:
            np.array<bool>: zx_bits representation of the PauliString of length 2n
        """

        zx_bits = None

        ################################################################################################################
        # YOUR CODE HERE
        # TO COMPLETE (after lecture on mapping)
        x_bits = self.x_bits 
        z_bits = self.z_bits
        zx_bits = np.concatenate((z_bits, x_bits))
        ################################################################################################################
        
#         raise NotImplementedError()

        return zx_bits

    def to_xz_bits(self) -> NDArray[np.bool_]:
        """
        Return the xz_bits representation of the PauliString.
        Useful to check commutativity.

        Returns:
            np.array<bool>: xz_bits representation of the PauliString of length 2n
        """

        ################################################################################################################
        # YOUR CODE HERE
        # TO COMPLETE (after lecture on mapping)
        xz_bits = None
        x_bits = self.x_bits 
        z_bits = self.z_bits
        xz_bits = np.concatenate((x_bits, z_bits))
        ################################################################################################################
        
#         raise NotImplementedError()

        return xz_bits

    def mul_pauli_string(self, other: 'PauliString') -> 'PauliString':
        """
        Product with an 'other' PauliString.

        Args:
            other (PauliString): An other PauliString.

        Raises:
            ValueError: If the other PauliString is not of the same length.

        Returns:
            PauliString, complex: The resulting PauliString and the product phase.
        """
        
        if len(self) != len(other):
            raise ValueError('PauliString must be of the same length')

        new_z_bits = new_x_bits = phase = None

        ################################################################################################################
        # YOUR CODE HERE
        # TO COMPLETE (after lecture on mapping)
        z1bits = self.z_bits
        x1bits = self.x_bits
        
        z2bits = other.z_bits
        x2bits = other.x_bits
        
        z3bits = np.logical_xor(z1bits, z2bits)
        x3bits = np.logical_xor(x1bits, x2bits)
        
        new_z_bits = z3bits
        new_x_bits = x3bits
        

        a = np.sum(np.logical_and(z2bits, x1bits))
        b = np.sum(np.logical_and(z1bits, x1bits))
        c = np.sum(np.logical_and(z2bits, x2bits))
        d = np.sum(np.logical_and(z3bits, x3bits))

        w =  2*a +b+c-d
        phase = (-1j)**w
        ################################################################################################################
        
#         raise NotImplementedError()
        
        return self.__class__(new_z_bits, new_x_bits), phase

    def mul_coef(self, coef: Union[int, float, complex]) -> 'LinearCombinaisonPauliString':
        """
        Build a LCPS from a PauliString (self) and a numeric (coef).

        Args:
            coef (int, float or complex): A numeric coefficient.

        Returns:
            LinearCombinaisonPauliString: A LCPS with only one PauliString and coef.
        """

        coefs = pauli_strings = None

        ################################################################################################################
        # YOUR CODE HERE
        # TO COMPLETE (after lecture on mapping)
    
        coefs = np.array([coef],dtype = complex)
        pauli_strings = PauliString(self.z_bits, self.x_bits)
        pauli_strings =  np.array([pauli_strings],dtype = PauliString)
        ################################################################################################################

#         raise NotImplementedError()

        return LinearCombinaisonPauliString(coefs, pauli_strings)

    def ids(self) -> NDArray[np.bool_]:
        """
        Position of Identity in the PauliString.

        Returns:
            np.array<bool>: True where both z_bits and x_bits are False.
        """

        ids = None

        ################################################################################################################
        # YOUR CODE HERE
        # TO COMPLETE (after lecture on mapping)
        zbits = self.z_bits
        xbits = self.x_bits
        ids = np.logical_or(zbits, xbits)
        ids = np.logical_not(ids)
        ################################################################################################################

#         raise NotImplementedError()

        return ids

    def copy(self) -> 'PauliString':
        """
        Build a copy of the PauliString.

        Returns:
            PauliString: A copy.
        """

        return PauliString(self.z_bits.copy(), self.x_bits.copy())

    def to_matrix(self) -> NDArray[np.complex128]:
        """
        Build the matrix representation of the PauliString using the Kroenecker product.

        Returns:
            np.array<complex>: A 2**n side square matrix.
        """

        I_MAT = np.array([[1, 0], [0, 1]])
        X_MAT = np.array([[0, 1], [1, 0]])
        Y_MAT = np.array([[0, -1j], [1j, 0]])
        Z_MAT = np.array([[1, 0], [0, -1]])

        matrix = None

        ################################################################################################################
        # YOUR CODE HERE (OPTIONAL)
        # TO COMPLETE (after lecture on mapping)
        # Hints : start with
        # matrix = np.ones((1,1),dtype = np.complex128)
        # And then use the np.kron() method to build the matrix
        
        matrix = np.ones((1,1),dtype = np.complex128)
        string = self.__str__()
        
        for i in string:
            if i == 'I':
                matrix = np.kron(matrix, I_MAT)
            if i == 'X':
                matrix = np.kron(matrix, X_MAT)
            if i == 'Y':
                matrix = np.kron(matrix, Y_MAT)
            if i == 'Z':
                matrix = np.kron(matrix, Z_MAT)     
                
        ################################################################################################################

#         raise NotImplementedError()
        
        return matrix


class LinearCombinaisonPauliString:
    def __init__(self, coefs: NDArray[np.complex128], pauli_strings: NDArray[PauliString]):
        """
        Describes a Linear Combinaison of Pauli Strings.

        Args:
            coefs (np.array): Coefficients multiplying the respective PauliStrings.
            pauli_strings (np.array<PauliString>): PauliStrings.

        Raises:
            ValueError: If the number of coefs is different from the number of PauliStrings.
            ValueError: If all PauliStrings are not of the same length.
        """

        if len(coefs) != len(pauli_strings):
            raise ValueError('Must provide a equal number of coefs and PauliString')

        n_qubits = len(pauli_strings[0])
        for pauli in pauli_strings:
            if len(pauli) != n_qubits:
                raise ValueError('All PauliString must be of same length')

        self.n_terms = len(pauli_strings)
        self.n_qubits = len(pauli_strings[0])

        self.coefs = np.array(coefs, dtype=complex)
        self.pauli_strings = np.array(pauli_strings, dtype=PauliString)
        
    def __str__(self) -> str:
        """
        String representation of the LinearCombinaisonPauliString.

        Returns:
            str: Descriptive string.
        """

        out = f'{self.n_terms:d} pauli strings for {self.n_qubits:d} qubits (Real, Imaginary)'
        for coef, pauli in zip(self.coefs, self.pauli_strings):
            out += '\n' + f'{str(pauli)} ({np.real(coef):+.5f},{np.imag(coef):+.5f})'
        return out

    def __getitem__(self, key: Union[int, slice]) -> 'LinearCombinaisonPauliString':
        """
        Return a subset of the LinearCombinaisonPauliString array-like.

        Args:
            key (int or slice): Elements to be returned.

        Returns:
            LinearCombinaisonPauliString: LCPS with the element specified in key.
        """
        
        if isinstance(key, slice):
            new_coefs = np.array(self.coefs[key])
            new_pauli_strings = self.pauli_strings[key]
        else:
            if isinstance(key, int):
                key = [key]
            new_coefs = self.coefs[key]
            new_pauli_strings = self.pauli_strings[key]

        return self.__class__(new_coefs, new_pauli_strings)

    def __len__(self) -> int:
        """
        Number of PauliStrings in the LCPS.

        Returns:
            int: Number of PauliStrings/coefs.
        """

        return len(self.pauli_strings)

    def __add__(self, other: 'LinearCombinaisonPauliString') -> 'LinearCombinaisonPauliString':
        """
        Allow the use of + to add two LCPS together.

        Args:
            other (LinearCombinaisonPauliString): An other LCPS.

        Returns:
            LinearCombinaisonPauliString: New LCPS of len = len(self) + len(other).
        """

        return self.add_pauli_string_linear_combinaison(other)

    def __mul__(self, other: Union[int, float, complex, 'LinearCombinaisonPauliString']) -> 'LinearCombinaisonPauliString':
        """
        Allow the use of * with other LCPS or numeric value(s)

        Args:
            other (LinearCombinaisonPauliString): An other LCPS

        Returns:
            LinearCombinaisonPauliString: New LCPS of len = len(self) * len(other)
            or
            LinearCombinaisonPauliString: New LCPS of same length with modified coefs
        """

        if isinstance(other, LinearCombinaisonPauliString):
            return self.mul_linear_combinaison_pauli_string(other)
        else:
            return self.mul_coef(other)

    def __rmul__(self, other: 'LinearCombinaisonPauliString') -> 'LinearCombinaisonPauliString':
        """
        Same as __mul__.
        Allow the use of '*' with a preceding coef (numeric).
        Like in 0.5 * LCPS.

        Args:
            other (LinearCombinaisonPauliString): An other LCPS.

        Returns:
            LinearCombinaisonPauliString: New LCPS of len = len(self) * len(other)
            or
            LinearCombinaisonPauliString: New LCPS of same length with modified coefs
        """

        return self.__mul__(other)

    def add_pauli_string_linear_combinaison(self, other: 'LinearCombinaisonPauliString') -> 'LinearCombinaisonPauliString':
        """
        Adding with an other LCPS. Merging the coefs and PauliStrings arrays.

        Args:
            other (LinearCombinaisonPauliString): An other LCPS.

        Raises:
            ValueError: If other is not an LCPS.
            ValueError: If the other LCPS has not the same number of qubits.

        Returns:
            LinearCombinaisonPauliString: New LCPS of len = len(self) + len(other).
        """

        if not isinstance(other, LinearCombinaisonPauliString):
            raise ValueError('Can only add with an other LCPS')

        if self.n_qubits != other.n_qubits:
            raise ValueError('Can only add with LCPS of identical number of qubits')

        new_coefs = new_pauli_strings = None

        ################################################################################################################
        # YOUR CODE HERE
        # TO COMPLETE (after lecture on mapping)
        # Hints : use np.concatenate
        
        coef1 = self.coefs
        lcps1 = self.pauli_strings
        
        coef2 = other.coefs
        lcps2 = other.pauli_strings
        new_coefs = np.concatenate((coef1, coef2))
        new_pauli_strings = np.concatenate((lcps1, lcps2))
        ################################################################################################################

#         raise NotImplementedError()

        return self.__class__(new_coefs, new_pauli_strings)

    def mul_linear_combinaison_pauli_string(self, other: 'LinearCombinaisonPauliString') -> 'LinearCombinaisonPauliString':
        """
        Multiply with an other LCPS.

        Args:
            other (LinearCombinaisonPauliString): An other LCPS.

        Raises:
            ValueError: If other is not an LCPS.
            ValueError: If the other LCPS has not the same number of qubits.

        Returns:
            LinearCombinaisonPauliString: New LCPS of len = len(self) * len(other).
        """

        if not isinstance(other, LinearCombinaisonPauliString):
            raise ValueError()

        if self.n_qubits != other.n_qubits:
            raise ValueError('Can only add with LCPS of identical number of qubits')

        new_coefs = np.zeros((len(self)*len(other),), dtype=np.complex128)
        new_pauli_strings = np.zeros((len(self)*len(other),), dtype=PauliString)
        
        ################################################################################################################
        # YOUR CODE HERE
        # TO COMPLETE (after lecture on mapping)
        coef1 = self.coefs
        lcps1 = self.pauli_strings
        
        coef2 = other.coefs
        lcps2 = other.pauli_strings
        
        for i, cf1 in enumerate(coef1):
            for j, cf2 in enumerate(coef2):
                k = j + i*len(coef2)
                new_pauli_strings[k], phase = PauliString.mul_pauli_string(lcps1[i], lcps2[j])  #lcps1[i]*lcps2[j] 
                new_coefs[k] = cf1*cf2*phase
        
        ################################################################################################################
        
#         raise NotImplementedError()

        return self.__class__(new_coefs, new_pauli_strings)
    
#     def mul_coef(self, other: 'LinearCombinaisonPauliString') -> 'LinearCombinaisonPauliString':
    def mul_coef(self, coef: Union[int, float, complex]) -> 'LinearCombinaisonPauliString':
        """
        Multiply the LCPS by a coef (numeric) or an array of the same length.

        Args:
            other (float, complex or np.array): One numeric factor or one factor per PauliString.

        Raises:
            ValueError: If other is np.array should be of the same length as the LCPS.

        Returns:
            [type]: [description]
        """

        new_coefs = new_pauli_strings = None

        ################################################################################################################
        # YOUR CODE HERE
        # TO COMPLETE (after lecture on mapping)
        
        coef2 = self.coefs
        
        new_coefs = coef*coef2
        new_pauli_strings = self.pauli_strings
        
        
        # new_coefs =
        # new_pauli_strings = 
        ################################################################################################################
        
#         raise NotImplementedError()

        return self.__class__(new_coefs, new_pauli_strings)

    def to_zx_bits(self) -> NDArray[np.bool_]:
        """
        Build an array that contains all the zx_bits for each PauliString.

        Returns:
            np.array<bool>: A 2d array of booleans where each line is the zx_bits of a PauliString.
        """

        zx_bits = np.zeros((len(self), 2*self.n_qubits), dtype=np.bool_)

        ################################################################################################################
        # YOUR CODE HERE
        # TO COMPLETE (after lecture on mapping)
        lcps_array = self.pauli_strings
        
        for i, ps in enumerate(lcps_array):
            zx_bits[i] = ps.to_zx_bits()
        
        
        ################################################################################################################
        
#         raise NotImplementedError()

        return zx_bits

    def to_xz_bits(self) -> NDArray[np.bool_]:
        """
        Build an array that contains all the xz_bits for each PauliString.

        Returns:
            np.array<bool>: A 2d array of booleans where each line is the xz_bits of a PauliString.
        """

        xz_bits = np.zeros((len(self), 2*self.n_qubits), dtype=np.bool_)

        ################################################################################################################
        # YOUR CODE HERE
        # TO COMPLETE (after lecture on mapping)
        
        lcps_array = self.pauli_strings   #Get an array of Pauli strings using the LCPS class
        
        for i, ps in enumerate(lcps_array):
            xz_bits[i] = ps.to_xz_bits()    #apply to a Pauli String 'to_xz_bits' from the 'PauliString' class
        
        ################################################################################################################
        
#         raise NotImplementedError()

        return xz_bits

    def ids(self) -> NDArray[np.bool_]:
        """
        Build an array that identifies the position of all the I for each PauliString.

        Returns:
            np.array<bool>: A 2d array of booleans where each line identifies the I on a PauliString.
        """

        ids = np.zeros((len(self), self.n_qubits), dtype=np.bool_)

        ################################################################################################################
        # YOUR CODE HERE
        # TO COMPLETE (after lecture on mapping)
        
        lcps_array = self.pauli_strings   #Get an array of Pauli strings using the LCPS class
        
        for i, ps in enumerate(lcps_array):
            ids[i] = ps.ids()    #apply to a Pauli String 'ids' from the 'PauliString' class
        
        ################################################################################################################
        
#         raise NotImplementedError()

        return ids

    def combine(self) -> 'LinearCombinaisonPauliString':
        """
        Finds unique PauliStrings in the LCPS and combines the coefs of identical PauliStrings.
        Reduces the length of the LCPS.

        Returns:
            LinearCombinaisonPauliString: LCPS with combined coefficients.
        """

        new_coefs = new_pauli_strings = None

        ################################################################################################################
        # YOUR CODE HERE
        # TO COMPLETE (after lecture on mapping)
        # hint : make use to_zx_bits and np.unique
        
        cf_array = self.coefs                  # all coef
        zx_array = self.to_zx_bits()           # all zx_bits
        
        # list of tuples of all zx_bits and their coefficients
        zx_cf = []                       
        for _, cf in enumerate(cf_array):
            zx_cf.append((zx_array[_], cf))
            
        # Construct a list of tuples of unique zx_bits and their counts)
        zx_array_uq, counts = np.unique(self.to_zx_bits(), axis = 0, return_counts=True)   #unique zx_bits and their counts
        zx_counts = []  # list of tuples of unique zx_bits and their counts
        for _, ct in enumerate(counts):
            zx_counts.append((zx_array_uq[_], ct))
         
        
        
        
        zx_gt_1 = []     # list of zx_bits occuring more than once
        zx_eq_1 = []     # list of zx_bits occuring just once
        # 0 indexes the zx_bits, 1 indexes the counts
        for _ in range(len(zx_counts)):
            if zx_counts[_][1] > 1:
                zx_gt_1.append(zx_counts[_][0])
            if zx_counts[_][1] == 1:
                zx_eq_1.append(zx_counts[_][0])
                
        
#         new_zx_cf_gt_1 = []
        new_zx_gt_1 = np.zeros((len(zx_gt_1),  2*self.n_qubits), dtype=np.bool_)
        new_cf_gt_1 = np.zeros(len(zx_gt_1) , dtype=np.complex128)
        # 0 indexes the zx_bits, 1 indexes the counts       
        for i in range(len(zx_gt_1)):
            cf_gt_1 = 0
            for j in range(len(zx_cf)):
                is_zx_unique = (list(zx_cf[j][0]) == list(zx_gt_1[i]))
                if is_zx_unique == True:
                    cf_gt_1 += zx_cf[j][1]
                else:
                    cf_gt_1 += 0
#                
#                 print(np.array(zx_cf[j][0]), np.array(zx_gt_1[i]))
#                 if np.array(zx_cf[j][0]).all() == np.array(zx_gt_1[i]).all():
            new_zx_gt_1[i] = np.array(zx_gt_1[i])
            new_cf_gt_1[i] = np.array(cf_gt_1)
        
#             new_zx_gt_1 = np.array(new_zx_gt_1)
#             new_cf_gt_1 = np.array(new_cf_gt_1)
            
            
#         new_zx_cf_eq_1 = []
        new_zx_eq_1 = np.zeros((len(zx_eq_1),2*self.n_qubits), dtype=np.bool_)
        new_cf_eq_1 = np.zeros(len(zx_eq_1), dtype=np.complex128)
        for i in range(len(zx_eq_1)):
            for j in range(len(zx_cf)):
                is_zx_unique = (list(zx_cf[j][0]) == list(zx_eq_1[i]))
                if is_zx_unique == True:
                    new_zx_eq_1[i] = np.array(zx_eq_1[i])
                    new_cf_eq_1[i] = np.array(zx_cf[j][1])
#                 if np.array(zx_cf[j][0]).all()  == np.array(zx_eq_1[i]).all():
#                     new_zx_cf_eq_1.append((zx_eq_1[i], zx_cf[j][1]))
                    
        

                
                
        new_coefs = np.concatenate((new_cf_gt_1,   new_cf_eq_1))
        new_zx_bits = np.concatenate((new_zx_gt_1,   new_zx_eq_1 ))
        
        new_pauli_strings = np.zeros(len(new_zx_bits), dtype = PauliString)
        
        for i, n_z_bits in enumerate(new_zx_bits):
            new_pauli_strings[i] = PauliString.from_zx_bits(n_z_bits)
            
     
                    
           
        
        ################################################################################################################
        
#         raise NotImplementedError()
#         return zx_gt_1
        return self.__class__(new_coefs, new_pauli_strings)

    def apply_threshold(self, threshold: float = 1e-6) -> 'LinearCombinaisonPauliString':
        """
        Remove PauliStrings with coefficients smaller than threshold.

        Args:
            threshold (float, optional): PauliStrings with coef smaller than 'threshold' will be removed. 
                                         Defaults to 1e-6.

        Returns:
            LinearCombinaisonPauliString: LCPS without coefficients smaller than threshold.
        """

        new_coefs = new_pauli_strings = None
        ################################################################################################################
        # YOUR CODE HERE
        # TO COMPLETE (after lecture on mapping)
        # Hint : create a np.array<bool> and use this array to get the subset of the lcps where this array is True
#         cf_array = self.coefs                  # all coef
#         zx_array = self.pauli_strings           # all zx_bits
#         cf_array = list(cf_array)
#         zx_array = list(zx_array)
#         for _, cf in enumerate(cf_array):
#             if (np.real(cf) < 1e-4) and (np.imag(cf) < 1e-4):
#                 del cf_array[_]
#                 del zx_array[_]
        
#         new_coefs =  np.array(cf_array, dtype = complex)
#         new_pauli_strings = np.array(zx_array, dtype = PauliString)

        #From Kithmin, I added np.abs
        
        
        new_coefs = self.coefs[np.abs(self.coefs) > threshold]       
        new_pauli_strings = self.pauli_strings[np.abs(self.coefs)  > threshold]
        ################################################################################################################

#         raise NotImplementedError()

        return self.__class__(new_coefs, new_pauli_strings)

    def divide_in_bitwise_commuting_cliques(self) -> List['LinearCombinaisonPauliString']:
        """
        Find bitwise commuting cliques in the LCPS.

        Returns:
            list<LinearCombinaisonPauliString>: List of LCPS where all elements of one LCPS bitwise commute with each
                                                other.
        """

        cliques = list()

        ################################################################################################################
        # YOUR CODE HERE
        # TO COMPLETE (after activity 3.2)
        # This one can be hard to implement
        # Use to_zx_bits
        # Transform all I into Z and look for unique PauliStrings
        ################################################################################################################

#         raise NotImplementedError()

        return cliques

    def sort(self) -> 'LinearCombinaisonPauliString':
        """
        Sort the PauliStrings by order of the zx_bits.

        Returns:
            LinearCombinaisonPauliString: Sorted.
        """

        order = None

        ################################################################################################################
        # YOUR CODE HERE
        # TO COMPLETE (after lecture on mapping)
        # COMPLETED BY Kithmin 
        order = self.to_zx_bits() @ 2**np.arange(2*self.n_qubits)
        order = np.argsort(order)
        
        ################################################################################################################

#         raise NotImplementedError()

        new_coefs = self.coefs[order]
        new_pauli_strings = self.pauli_strings[order]

        return self.__class__(new_coefs, new_pauli_strings)
    
    def to_matrix(self) -> NDArray[np.complex128]:
        """
        Build the total matrix representation of the LCPS.

        Returns:
            np.array<complex>: A 2**n side square matrix.
        """

        size = 2**self.n_qubits
        matrix = np.zeros((size, size), dtype=np.complex128)

        ################################################################################################################
        # YOUR CODE HERE (OPTIONAL)
        # TO COMPLETE (after lecture on mapping)
        # Hints : sum all the matrices of all PauliStrings weighted by their coef
        for i in range(self.n_terms):
            matrix += self.coefs[i] * self.pauli_strings[i].to_matrix() 
        
        ################################################################################################################

#         raise NotImplementedError()

        return matrix
