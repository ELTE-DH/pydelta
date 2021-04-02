#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""The different tokenization strategies."""

from enum import Enum


class Tokenizer:
    def __init__(self, token_pattern):
        self.token_pattern = token_pattern


class WordTokenizer(Tokenizer):
    def __call__(self, lines):
        for line in lines:
            for match in self.token_pattern.finditer(line):
                yield match.group(0)


class CharTokenizer(WordTokenizer):
    def __call__(self, lines):
        for word in super().__call__(lines):
            yield from word
            yield ' '


class TokenType(Enum):
    WORD = 'word'
    CHAR = 'character'


def tokenizer(token_type, token_pattern):
    if token_type == TokenType.WORD:
        return WordTokenizer(token_pattern)
    else:
        return CharTokenizer(token_pattern)
