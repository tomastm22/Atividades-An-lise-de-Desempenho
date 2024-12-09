-- Mostra todos os livros com seus autores:
SELECT Livro.Titulo AS Livro, Autor.Nome AS Autor
FROM Livro
INNER JOIN Autor ON Livro.ID_Autor = Autor.ID_Autor;

-- Mostra todos os empréstimos e os usuários correspondentes:
SELECT Emprestimo.ID_Emprestimo AS Emprestimo_ID, Usuario.Nome AS Usuario
FROM Emprestimo
INNER JOIN Usuario ON Emprestimo.ID_Usuario = Usuario.ID_Usuario;

-- Mostra todos os livros e suas categorias:
SELECT Livro.Titulo AS Livro, Categoria.Nome AS Categoria
FROM Livro
INNER JOIN Livro_Categoria ON Livro.ID_Livro = Livro_Categoria.ID_Livro
INNER JOIN Categoria ON Livro_Categoria.ID_Categoria = Categoria.ID_Categoria;

-- Mostra todos os livros emprestados:
SELECT Livro.Titulo AS Livro, Usuario.Nome AS Usuario
FROM Livro
INNER JOIN Emprestimo ON Livro.ID_Livro = Emprestimo.ID_Livro
INNER JOIN Usuario ON Emprestimo.ID_Usuario = Usuario.ID_Usuario;

-- Mostra todos os autores e seus livros publicados:
SELECT Autor.Nome AS Autor, Livro.Titulo AS Livro
FROM Autor
INNER JOIN Livro ON Autor.ID_Autor = Livro.ID_Autor;
-- Mostra todas as categorias com o número de livros em cada uma:
SELECT Categoria.Nome AS Categoria, COUNT(Livro_Categoria.ID_Livro) AS Quantidade_Livros
FROM Categoria
LEFT JOIN Livro_Categoria ON Categoria.ID_Categoria = Livro_Categoria.ID_Categoria
GROUP BY Categoria.Nome;

-- Mostra todas as categorias com o número de livros em cada uma:
SELECT Categoria.Nome AS Categoria, COUNT(Livro_Categoria.ID_Livro) AS Quantidade_Livros
FROM Categoria
LEFT JOIN Livro_Categoria ON Categoria.ID_Categoria = Livro_Categoria.ID_Categoria
GROUP BY Categoria.Nome;

-- Mostra todos os usuários que estão em atraso:
SELECT Usuario.Nome AS Usuario, Livro.Titulo AS Livro, Emprestimo.Data_Emprestimo AS Data_Emprestimo
FROM Usuario
INNER JOIN Emprestimo ON Usuario.ID_Usuario = Emprestimo.ID_Usuario
INNER JOIN Livro ON Emprestimo.ID_Livro = Livro.ID_Livro
WHERE Emprestimo.Data_Devolucao IS NULL;

-- Mostra todos os livros que pertencem a mais de uma categoria:
SELECT Livro.Titulo AS Livro, COUNT(Livro_Categoria.ID_Categoria) AS Quantidade_Categorias
FROM Livro
INNER JOIN Livro_Categoria ON Livro.ID_Livro = Livro_Categoria.ID_Livro
GROUP BY Livro.Titulo
HAVING COUNT(Livro_Categoria.ID_Categoria) > 1;