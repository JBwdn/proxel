"""
Parse PDB files into proxel.Structure objects.
"""


import pathlib


def pdb_parser(pdb_file: pathlib.Path) -> None:
    """WIP to get alpha carbons from PDB file"""

    with open(pdb_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    atoms = [line for line in lines if line.startswith("ATOM")]
    atom_details = [line.split() for line in atoms]
    alphas = [line for line in atom_details if line[2] == "CA"]
    print(len(alphas))


if __name__ == "__main__":
    pdb_parser(pathlib.Path(".test_data/8cm5.pdb"))
