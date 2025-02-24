from __future__ import annotations

from pyiron_workflow import as_function_node, as_macro_node
from typing import Optional
from ase.atoms import Atoms

# from pyiron_workflow.workflow import Workflow


@as_function_node("structure")
def Bulk(
    name: str,
    crystalstructure: Optional[str] = None,
    a: Optional[float | int] = None,
    c: Optional[float | int] = None,
    c_over_a: Optional[float] | int = None,
    u: Optional[float | int] = None,
    orthorhombic: bool = False,
    cubic: bool = False,
):
    from pyiron_atomistics import _StructureFactory

    return _StructureFactory().bulk(
        name,
        crystalstructure,
        a,
        c,
        c_over_a,
        u,
        orthorhombic,
        cubic,
    )
