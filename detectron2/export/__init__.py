# -*- coding: utf-8 -*-

import warnings

from .flatten import TracingAdapter
from .torchscript import dump_torchscript_IR, scripting_with_instances

# TODO: Update ONNX Opset version and run tests when a newer PyTorch is supported
STABLE_ONNX_OPSET_VERSION = 16


def add_export_config(cfg):
    warnings.warn(
        "add_export_config has been deprecated and behaves as no-op function.", DeprecationWarning
    )
    return cfg


__all__ = [k for k in globals().keys() if not k.startswith("_")]
