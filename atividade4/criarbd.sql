PRAGMA foreign_keys = ON;

CREATE TABLE Autor (
    ID_Autor INTEGER PRIMARY KEY AUTOINCREMENT, -- Adicionado AUTOINCREMENT para facilitar a inserção
    Nome TEXT NOT NULL,
    Data_Nascimento DATE NOT NULL
);

-- Criação da tabela Categoria
CREATE TABLE Categoria (
    ID_Categoria INTEGER PRIMARY KEY AUTOINCREMENT, -- Adicionado AUTOINCREMENT para facilitar a inserção
    Nome TEXT NOT NULL UNIQUE -- UNIQUE para evitar duplicidade de categorias
);

-- Criação da tabela Livro
CREATE TABLE Livro (
    ID_Livro INTEGER PRIMARY KEY AUTOINCREMENT, -- Adicionado AUTOINCREMENT para facilitar a inserção
    Titulo TEXT NOT NULL,
    ID_Autor INTEGER NOT NULL,
    Ano_Publicacao INTEGER NOT NULL,
    FOREIGN KEY (ID_Autor) REFERENCES Autor(ID_Autor) ON DELETE CASCADE
);

-- Criação da tabela associativa Livro_Categoria (Muitos-para-Muitos)
CREATE TABLE Livro_Categoria (
    ID_Livro INTEGER NOT NULL,
    ID_Categoria INTEGER NOT NULL,
    PRIMARY KEY (ID_Livro, ID_Categoria),
    FOREIGN KEY (ID_Livro) REFERENCES Livro(ID_Livro) ON DELETE CASCADE, -- Exclui relação se o livro for removido
    FOREIGN KEY (ID_Categoria) REFERENCES Categoria(ID_Categoria) ON DELETE CASCADE -- Exclui relação se a categoria for removida
);

-- Criação da tabela Usuario
CREATE TABLE Usuario (
    ID_Usuario INTEGER PRIMARY KEY AUTOINCREMENT, -- Adicionado AUTOINCREMENT para facilitar a inserção
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE -- UNIQUE para evitar duplicidade de emails
);

-- Criação da tabela Emprestimo
CREATE TABLE Emprestimo (
    ID_Emprestimo INTEGER PRIMARY KEY AUTOINCREMENT, -- Adicionado AUTOINCREMENT para facilitar a inserção
    ID_Livro INTEGER NOT NULL,
    ID_Usuario INTEGER NOT NULL,
    Data_Emprestimo DATE NOT NULL,
    Data_Devolucao DATE,
    FOREIGN KEY (ID_Livro) REFERENCES Livro(ID_Livro) ON DELETE CASCADE, -- Remove empréstimos se o livro for excluído
    FOREIGN KEY (ID_Usuario) REFERENCES Usuario(ID_Usuario) ON DELETE CASCADE -- Remove empréstimos se o usuário for excluído
);