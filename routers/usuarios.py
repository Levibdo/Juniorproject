from fastapi import APIRouter
from models.usuarios import Usuario, UsuarioRequest, UsuarioResponse


router = APIRouter(tags=["Usuarios"])

"""
{
    "post": "Criar algo",
    "get": "Listar algo ou buscar algo",
    "put": "Atualizar algo",
    "delete": "Deletar algo"
}
"""


@router.post("/usuarios", response_model=UsuarioResponse)
async def create_user(usuario: UsuarioRequest):
    user = Usuario(**usuario.model_dump(), id=0, matricula="123456")
    # Salvar no banco de dados
    response = UsuarioResponse(**user.model_dump())
    return response


@router.get("/usuarios/{id}", response_model=Usuario)
async def ler_usuario(id: int):
    return Usuario(
        id=id,
        matricula="123456",
        nome="Fulano",
        senha="123456",
        cargo="Desenvolvedor",
        setor="TI",
    )
