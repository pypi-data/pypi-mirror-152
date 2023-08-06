"""
Utility Fireworks functions. Some of these functions are borrowed from the atomate package.
"""
import logging
import sys
from typing import Optional

from fireworks import FireTaskBase
from monty.serialization import loadfn

from rxn_network.entries.entry_set import GibbsEntrySet


def env_chk(
    val: str,
    fw_spec: dict,
    strict: Optional[bool] = True,
    default: Optional[str] = None,
):
    """
    Code borrowed from the atomate package.

    env_chk() is a way to set different values for a property depending
    on the worker machine. For example, you might have slightly different
    executable names or scratch directories on different machines.

    Args:
        val: any value, with ">><<" notation reserved for special env lookup values
        fw_spec: fw_spec where one can find the _fw_env keys
        strict: if True, errors if env format (>><<) specified but cannot be found in fw_spec
        default: if val is None or env cannot be found in non-strict mode,
                 return default
    """
    if val is None:
        return default

    if isinstance(val, str) and val.startswith(">>") and val.endswith("<<"):
        if strict:
            return fw_spec["_fw_env"][val[2:-2]]
        return fw_spec.get("_fw_env", {}).get(val[2:-2], default)
    return val


def get_logger(
    name: str,
    level=logging.DEBUG,
    log_format="%(asctime)s %(levelname)s %(name)s %(message)s",
    stream=sys.stdout,
):
    """
    Code borrowed from the atomate package.

    Helper method for acquiring logger.
    """

    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter(log_format)

    sh = logging.StreamHandler(stream=stream)
    sh.setFormatter(formatter)

    logger.addHandler(sh)

    return logger


def load_json(firetask: FireTaskBase, param: str, fw_spec: dict) -> dict:
    """
    Utility function for loading json file related to a parameter of a FireTask. This first looks
    within the task to see if the object is already serialized; if not, it looks for a
    file with the filename stored under the {param}_fn attribute either within the
    FireTask or the fw_spec.

    Args:
        firetask: FireTask object
        param: parmeter name
        fw_spec: Firework spec.

    Returns:
        A loaded object (dict)
    """
    obj = firetask.get(param)

    if not obj:
        param_fn = param + "_fn"
        obj_fn = firetask.get(param_fn)

        if not obj_fn:
            obj_fn = fw_spec[param_fn]

        obj = loadfn(obj_fn)

    return obj


def load_entry_set(firetask, fw_spec):
    """
    Loads a GibbsEntrySet, either from the firetask itself (or its fw_spec), or from a
    file given the entries_fn attribute.
    """
    entries = firetask["entries"]
    entries_fn = firetask.get("entries_fn")

    if not entries:
        entries_fn = entries_fn if entries_fn else fw_spec["entries_fn"]
        entries = loadfn(entries_fn)

    entries = GibbsEntrySet(entries)
    return entries
