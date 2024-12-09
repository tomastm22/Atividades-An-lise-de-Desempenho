INSERT INTO Autor (Nome, Data_Nascimento) VALUES ('Arthur C. Clarke', '1917-12-16');
INSERT INTO Autor (Nome, Data_Nascimento) VALUES ('J.K. Rowling', '1965-07-31');
INSERT INTO Autor (Nome, Data_Nascimento) VALUES ('George Orwell', '1903-06-25');
INSERT INTO Autor (Nome, Data_Nascimento) VALUES ('Jane Austen', '1775-12-16');
INSERT INTO Autor (Nome, Data_Nascimento) VALUES ('Agatha Christie', '1890-09-15');
INSERT INTO Autor (Nome, Data_Nascimento) VALUES ('Ernest Hemingway', '1899-07-21');
INSERT INTO Autor (Nome, Data_Nascimento) VALUES ('F. Scott Fitzgerald', '1896-09-24');
INSERT INTO Autor (Nome, Data_Nascimento) VALUES ('Gabriel García Márquez', '1927-03-06');
INSERT INTO Autor (Nome, Data_Nascimento) VALUES ('Haruki Murakami', '1949-01-12');
INSERT INTO Autor (Nome, Data_Nascimento) VALUES ('Virginia Woolf', '1882-01-25');
INSERT INTO Autor (Nome, Data_Nascimento) VALUES ('Mark Twain', '1835-11-30');
INSERT INTO Autor (Nome, Data_Nascimento) VALUES ('Leo Tolstoy', '1828-09-09');
INSERT INTO Autor (Nome, Data_Nascimento) VALUES ('Isabel Allende', '1942-08-02');
INSERT INTO Autor (Nome, Data_Nascimento) VALUES ('J.R.R. Tolkien', '1892-01-03');
INSERT INTO Autor (Nome, Data_Nascimento) VALUES ('Stephen King', '1947-09-21');
INSERT INTO Autor (Nome, Data_Nascimento) VALUES ('Chimamanda Ngozi Adichie', '1977-09-15');
INSERT INTO Categoria (Nome) VALUES ('Fantasia');
INSERT INTO Categoria (Nome) VALUES ('Ficção Científica');
INSERT INTO Categoria (Nome) VALUES ('Aventura');
INSERT INTO Categoria (Nome) VALUES ('Mistério');
INSERT INTO Categoria (Nome) VALUES ('Romance');
INSERT INTO Categoria (Nome) VALUES ('Biografia');
INSERT INTO Categoria (Nome) VALUES ('Drama');
INSERT INTO Categoria (Nome) VALUES ('História');
INSERT INTO Categoria (Nome) VALUES ('Clássico');
INSERT INTO Categoria (Nome) VALUES ('Suspense');
INSERT INTO Categoria (Nome) VALUES ('Terror');
INSERT INTO Categoria (Nome) VALUES ('Poesia');
INSERT INTO Categoria (Nome) VALUES ('Infantil');
INSERT INTO Categoria (Nome) VALUES ('Autoajuda');
INSERT INTO Categoria (Nome) VALUES ('Filosofia');
INSERT INTO Categoria (Nome) VALUES ('Religião');
INSERT INTO Usuario (Nome, Email) VALUES ('Aline', 'aline@example.com');
INSERT INTO Usuario (Nome, Email) VALUES ('Bruce', 'bruce@example.com');
INSERT INTO Usuario (Nome, Email) VALUES ('Clara', 'clara@example.com');
INSERT INTO Usuario (Nome, Email) VALUES ('David', 'david@example.com');
INSERT INTO Usuario (Nome, Email) VALUES ('Elena', 'elena@example.com');
INSERT INTO Usuario (Nome, Email) VALUES ('Frank', 'frank@example.com');
INSERT INTO Usuario (Nome, Email) VALUES ('Grace', 'grace@example.com');
INSERT INTO Usuario (Nome, Email) VALUES ('Henry', 'henry@example.com');
INSERT INTO Usuario (Nome, Email) VALUES ('Irene', 'irene@example.com');
INSERT INTO Usuario (Nome, Email) VALUES ('James', 'james@example.com');
INSERT INTO Usuario (Nome, Email) VALUES ('Karla', 'karla@example.com');
INSERT INTO Usuario (Nome, Email) VALUES ('Liam', 'liam@example.com');
INSERT INTO Usuario (Nome, Email) VALUES ('Mia', 'mia@example.com');
INSERT INTO Usuario (Nome, Email) VALUES ('Noah', 'noah@example.com');
INSERT INTO Usuario (Nome, Email) VALUES ('Olive', 'olive@example.com');
INSERT INTO Usuario (Nome, Email) VALUES ('Peter', 'peter@example.com');
INSERT INTO Livro (Titulo, Ano_Publicacao, ID_Autor) VALUES ('Meio Sol Amarelo', 1997, 1);
INSERT INTO Livro (Titulo, Ano_Publicacao, ID_Autor) VALUES ('O Iluminado', 1996, 2);
INSERT INTO Livro (Titulo, Ano_Publicacao, ID_Autor) VALUES ('O Senhor dos Anéis: A Sociedade do Anel', 1954, 3);
INSERT INTO Livro (Titulo, Ano_Publicacao, ID_Autor) VALUES ('A Casa dos Espíritos', 1951, 4);
INSERT INTO Livro (Titulo, Ano_Publicacao, ID_Autor) VALUES ('Guerra e Paz', 1969, 5);
INSERT INTO Livro (Titulo, Ano_Publicacao, ID_Autor) VALUES ('As Aventuras de Tom Sawyer', 1986, 6);
INSERT INTO Livro (Titulo, Ano_Publicacao, ID_Autor) VALUES ('Mrs. Dalloway', 1934, 7);
INSERT INTO Livro (Titulo, Ano_Publicacao, ID_Autor) VALUES ('Norwegian Wood', 1968, 8);
INSERT INTO Livro (Titulo, Ano_Publicacao, ID_Autor) VALUES ('Cem Anos de Solidão', 1876, 9);
INSERT INTO Livro (Titulo, Ano_Publicacao, ID_Autor) VALUES ('O Grande Gatsby', 1813, 10);
INSERT INTO Livro (Titulo, Ano_Publicacao, ID_Autor) VALUES ('O Assassinato no Expresso do Oriente', 1952, 11);
INSERT INTO Livro (Titulo, Ano_Publicacao, ID_Autor) VALUES ('Orgulho e Preconceito', 1837, 12);
INSERT INTO Livro (Titulo, Ano_Publicacao, ID_Autor) VALUES ('A Revolução dos Bichos', 1925, 13);
INSERT INTO Livro (Titulo, Ano_Publicacao, ID_Autor) VALUES ('A Torre Negra', 1925, 14);
INSERT INTO Livro (Titulo, Ano_Publicacao, ID_Autor) VALUES ('As Ondas', 1869, 15);
INSERT INTO Livro (Titulo, Ano_Publicacao, ID_Autor) VALUES ('Para Sempre', 1895, 16);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (1, 1);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (1, 3);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (2, 1);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (2, 2);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (3, 1);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (3, 3);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (4, 2);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (4, 8);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (5, 2);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (5, 10);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (6, 11);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (7, 4);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (8, 2);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (9, 3);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (10, 5);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (11, 7);
INSERT INTO Emprestimo (ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (1, 1, '2024-09-02', '2024-09-10');
INSERT INTO Emprestimo (ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (2, 2, '2024-09-06', '2024-09-15');
INSERT INTO Emprestimo (ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (3, 3, '2024-09-11', NULL);
INSERT INTO Emprestimo (ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (4, 4, '2024-09-13', '2024-10-22');
INSERT INTO Emprestimo (ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (5, 5, '2024-09-16', '2024-09-25');
INSERT INTO Emprestimo (ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (6, 6, '2024-09-19', NULL);
INSERT INTO Emprestimo (ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (7, 7, '2024-09-21', '2024-09-30');
INSERT INTO Emprestimo (ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (8, 8, '2024-09-23', '2024-10-01');
INSERT INTO Emprestimo (ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (9, 9, '2024-09-26', '2024-10-05');
INSERT INTO Emprestimo (ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (10, 10, '2024-09-27', NULL);
INSERT INTO Emprestimo (ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (11, 11, '2024-09-30', '2024-10-10');
INSERT INTO Emprestimo (ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (12, 12, '2024-10-01', '2024-10-11');
INSERT INTO Emprestimo (ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (13, 13, '2024-10-03', '2024-10-13');
INSERT INTO Emprestimo (ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (14, 14, '2024-10-05', '2024-10-15');
INSERT INTO Emprestimo (ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (15, 15, '2024-10-07', NULL);
INSERT INTO Emprestimo (ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (16, 16, '2024-10-10', '2024-10-20');