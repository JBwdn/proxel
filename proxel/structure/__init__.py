"""
The main data class for proxel.

proxel.Structure is a class which holds a protein 3D structure and provides
transformations and encoders to prepare the data for machine learning.

Structure recieves atomic coordinates from a PDB file and encodes this into
a voxel grid per atom type.
"""

