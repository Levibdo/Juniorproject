from pydantic import BaseModel


class UsuarioRequest(BaseModel):
    nome: str
    senha: str
    cargo: str
    setor: str


class Usuario(UsuarioRequest):
    matricula: str
    id: int


class UsuarioResponse(BaseModel):
    id: int
    nome: str
    matricula: str
    cargo: str
    setor: str    
