# -*- coding: utf-8 -*-

"""
pydelta library
---------------

Stylometrics in Python
"""

__title__ = 'delta'
__version__ = '2.0.0'
__author__ = 'Fotis Jannidis, Thorsten Vitt'

from warnings import warn
from delta.corpus import Corpus, FeatureGenerator, LETTERS_PATTERN, WORD_PATTERN
from delta.deltas import registry as functions, normalization, Normalization, \
        DeltaFunction, PDistDeltaFunction, MetricDeltaFunction, \
        CompositeDeltaFunction
from delta.cluster import Clustering, FlatClustering

from delta.features import get_rfe_features
from delta.graphics import Dendrogram
from delta.tokenization import TokenType

__all__ = [ Corpus, FeatureGenerator, LETTERS_PATTERN, WORD_PATTERN,
           functions, Normalization, normalization,
           DeltaFunction, PDistDeltaFunction,
           MetricDeltaFunction, CompositeDeltaFunction,
           Clustering, FlatClustering,
           get_rfe_features, Dendrogram, TokenType ]

try:
        from delta.cluster import KMedoidsClustering
        __all__.append(KMedoidsClustering)
except (ImportError, NameError):
        warn("KMedoidsClustering not available")
