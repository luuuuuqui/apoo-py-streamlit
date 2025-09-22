# models.py
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

# O decorador @dataclass cria automaticamente métodos como __init__ e __repr__
@dataclass
class Post:
    """Representa um post do blog."""
    title: str
    content: str
    id: Optional[int] = None
    created_at: Optional[datetime] = None