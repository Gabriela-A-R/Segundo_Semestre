from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Tabela UNIDADE_PRODUCAO
class UnidadeProducao(Base):
    __tablename__ = "unidade_producao"

    numero = Column(Integer, primary_key=True)
    peca_hora_nominal = Column(Float)

    # Relacionamentos com outras tabelas
    falhas = relationship(
        "RegistroFalha", back_populates="unidade_producao", cascade="all, delete-orphan"
    )
    pecas = relationship(
        "Peca", back_populates="unidade_producao", cascade="all, delete-orphan"
    )
    sopradora = relationship(
        "Sopradora",
        back_populates="unidade_producao",
        uselist=False,
        cascade="all, delete-orphan",
    )
    fresadora = relationship(
        "Fresadora",
        back_populates="unidade_producao",
        uselist=False,
        cascade="all, delete-orphan",
    )
    torno_cnc = relationship(
        "TornoCNC",
        back_populates="unidade_producao",
        uselist=False,
        cascade="all, delete-orphan",
    )
    impressora_3d = relationship(
        "Impressora3D",
        back_populates="unidade_producao",
        uselist=False,
        cascade="all, delete-orphan",
    )

# Tabela REGISTRO_FALHA
class RegistroFalha(Base):
    __tablename__ = "registro_falha"

    id = Column(Integer, primary_key=True)
    severidade = Column(Boolean)
    inicio = Column(DateTime)
    fim = Column(DateTime)
    numero_unidade_producao = Column(
        Integer,
        ForeignKey("unidade_producao.numero", ondelete="CASCADE", onupdate="CASCADE"),
    )

    # Relacionamento com a unidade de produção
    unidade_producao = relationship("UnidadeProducao", back_populates="falhas")


# Tabela PECA
class Peca(Base):
    __tablename__ = "peca"

    numero = Column(Integer, primary_key=True)
    status = Column(String(10), CheckConstraint("status IN ('Aprovada', 'Reprovada')"))
    inicio_fabricacao = Column(DateTime)
    fim_fabricacao = Column(DateTime)
    numero_unidade_producao = Column(
        Integer,
        ForeignKey("unidade_producao.numero", ondelete="CASCADE", onupdate="CASCADE"),
    )

    # Relacionamento com a unidade de produção
    unidade_producao = relationship("UnidadeProducao", back_populates="pecas")


# Tabela SOPRADORA
class Sopradora(Base):
    __tablename__ = "sopradora"

    numero = Column(Integer, primary_key=True)
    vazao_sopro = Column(Float)
    pressao_sopro = Column(Float)
    numero_unidade_producao = Column(
        Integer,
        ForeignKey("unidade_producao.numero", ondelete="CASCADE", onupdate="CASCADE"),
    )

    # Relacionamento com a unidade de produção
    unidade_producao = relationship("UnidadeProducao", back_populates="sopradora")


# Tabela FRESADORA
class Fresadora(Base):
    __tablename__ = "fresadora"

    numero = Column(Integer, primary_key=True)
    velocidade_rotacao = Column(Float)
    profundidade_corte = Column(Float)
    numero_unidade_producao = Column(
        Integer,
        ForeignKey("unidade_producao.numero", ondelete="CASCADE", onupdate="CASCADE"),
    )

    # Relacionamento com a unidade de produção
    unidade_producao = relationship("UnidadeProducao", back_populates="fresadora")


# Tabela TORNO_CNC
class TornoCNC(Base):
    __tablename__ = "torno_cnc"

    numero = Column(Integer, primary_key=True)
    velocidade_rotacao = Column(Float)
    tolerancia = Column(Float)
    numero_unidade_producao = Column(
        Integer,
        ForeignKey("unidade_producao.numero", ondelete="CASCADE", onupdate="CASCADE"),
    )

    # Relacionamento com a unidade de produção
    unidade_producao = relationship("UnidadeProducao", back_populates="torno_cnc")


# Tabela IMPRESSORA_3D
class Impressora3D(Base):
    __tablename__ = "impressora_3d"

    numero = Column(Integer, primary_key=True)
    espessura_camada = Column(Float)
    tipo_material = Column(String(30))
    numero_unidade_producao = Column(
        Integer,
        ForeignKey("unidade_producao.numero", ondelete="CASCADE", onupdate="CASCADE"),
    )

    # Relacionamento com a unidade de produção
    unidade_producao = relationship("UnidadeProducao", back_populates="impressora_3d")
