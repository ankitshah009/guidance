import os
import time
import collections
import regex
import pygtrie
import queue
import threading
import logging
from .._llm import LLM, LLMSession, SyncSession
from ._llama import LLaMA

class Vicuna(LLaMA):
    """ A HuggingFace transformers version of the Vicuna language model with Guidance support.
    """

    cache = LLM._open_cache("_vicuna.diskcache")

    @staticmethod
    def role_start(role):
        if role == 'user':
            return 'USER: '
        elif role == 'assistant':
            return 'ASSISTANT: '
        else:
            return ''
    
    @staticmethod
    def role_end(role):
        if role == 'user':
            return ''
        elif role == 'assistant':
            return '</s>'
        else:
            return ''