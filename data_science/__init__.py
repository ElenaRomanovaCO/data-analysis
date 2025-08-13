# data_science/__init__.py
"""Data Science and Data QnA Multi-Agent package."""

__version__ = "0.1"
__author__ = "Elena Romanova"

import os

from . import agent
from .agent import root_agent

__all__ = ["agent", "root_agent"]