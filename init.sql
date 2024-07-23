-- Inserir dados na tabela User
INSERT INTO app_user (cpf, email, name, lname, username, status, role, password, is_active, is_staff, is_admin) VALUES
('12345678901', 'user1@example.com', 'FirstName1', 'LastName1', 'user1', 'ACTIVE', 'USER', 'password1', TRUE, FALSE, FALSE),
('12345678902', 'user2@example.com', 'FirstName2', 'LastName2', 'user2', 'INACTIVE', 'MODERATOR', 'password2', TRUE, TRUE, FALSE),
('12345678903', 'amanda@example.com', 'Amanda', 'Silva', 'amandaS', 'ACTIVE', 'USER', 'pass', TRUE, FALSE, FALSE),
('12345678904', 'miguel@example.com', 'Miguel', 'Andrade', 'migueAnd', 'ACTIVE', 'USER', 'miguePass', TRUE, FALSE, FALSE),
('12345678905', 'admin@example.com', 'Admin', 'Silva', 'admin', 'ACTIVE', 'USER', 'admin', TRUE, FALSE, FALSE);

-- Inserir dados na tabela Poll
INSERT INTO app_poll (criation_date, finish_date, status, title, description, privacy, creator_id, category, tags) VALUES
('2024-07-01', '2024-07-31', 'OPEN', 'Melhor livro', 'Escolha o melhor livro', 'PUBLIC', 1, 'culture', 'livro'),
('2024-07-01', '2024-07-20', 'CLOSED', 'Melhor feriado do ano', 'Escolha o melhor feriado do ano', 'PUBLIC', 1, 'random', 'feriado'),
('2024-07-05', '2024-07-20', 'CLOSED', 'Melhor cantor', 'Escolha o melhor cantor', 'RESTRICTED', 2, 'random', 'musica'),
('2024-07-05', '2024-07-20', 'CLOSED', 'Melhor anime', 'Escolha o melhor anime', 'RESTRICTED', 5, 'animation', 'anime'),
('2024-07-05', '2024-07-20', 'OPEN', 'Melhor mangá', 'Escolha o melhor mangá', 'PUBLIC', 5, 'culture', 'manga');

-- Inserir dados na tabela Participation
INSERT INTO app_participation (user_id, poll_id) VALUES
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(1, 2),
(2, 2),
(3, 2),
(4, 2),
(5, 2),
(1, 5),
(2, 5),
(3, 5),
(4, 5);


-- Inserir dados na tabela QuestionField
INSERT INTO app_questionfield (title, max_qtd_choices, poll_id) VALUES
('Qual é o melhor livro?', 1, 1),
('Escolha os dois melhores feriados do ano:', 2, 2),
('Para você, qual é o melhor cantor?', 1, 3),
('Para você, qual é o melhor anime?', 1, 4),
('Para você, qual é o melhor mangá?', 1, 5);

-- Inserir dados na tabela Option
INSERT INTO app_option (text, img, question_id) VALUES
('Duna', '', 1),
('Neuromancer', '', 1),
('A Mão Esquerda da Escuridão', '', 1),
('Fahrenheit 451', '', 1),

('1º de janeiro - Confraternização Universal', '', 2),
('Carnaval', '', 2),
('Sexta-feira Santa', '', 2),
('Tiradentes', '', 2),
('Dia do Trabalhador', '', 2),
('Corpus Christi', '', 2),
('Independência do Brasil', '', 2),
('Nossa Senhora Aparecida', '', 2),
('Finados', '', 2),
('Proclamação da República', '', 2),
('Natal', '', 2),

('Caetano Veloso', '', 3),
('Gilberto Gil', '', 3),
('Gal Costa', '', 3),
('Chico Buarque', '', 3),
('Elis Regina', '', 3),

('Naruto', '', 4),
('Attack on Titan', '', 4),
('Fullmetal Alchemist: Brotherhood', '', 4),
('Death Note', '', 4),
('My Hero Academia', '', 4),


('One Piece', '', 5),
('Berserk', '', 5),
('Attack on Titan', '', 5),
('Fullmetal Alchemist', '', 5),
('Death Note', '', 5);



-- Inserir dados na tabela Vote
INSERT INTO app_vote (hash, date) VALUES
('hash1', '2024-07-05'),
('hash2', '2024-07-05'),
('hash3', '2024-07-05'),
('hash4', '2024-07-05'),
('hash5', '2024-07-05'),
('hash6', '2024-07-05'),
('hash7', '2024-07-05'),
('hash8', '2024-07-05'),
('hash9', '2024-07-05'),
('hash10', '2024-07-05'),
('hash11', '2024-07-05'),
('hash12', '2024-07-05'),
('hash13', '2024-07-05'),
('hash14', '2024-07-05'),
('hash15', '2024-07-05'),
('hash16', '2024-07-05');



-- Inserir dados na tabela Choice
INSERT INTO app_choice (vote_id, option_id) VALUES
-- Votos para livros 
(1, 1),
(2, 1),
(3, 2),
(4, 4),

-- Votos para Feriados Nacionais
(5, 5),
(5, 15),
(6,15),
(6,7),
(7,7),
(7,2),

-- Votos para cantor
(8, 17),
(9, 16),
(10, 17),

-- Votos para anime
(11, 21),
(12, 24),
(13, 21),

-- Votos para mangá
(14, 26),
(15, 26),
(16,30);

-- Inserir dados na tabela Whitelist
INSERT INTO app_whitelist (user_id, poll_id) VALUES
(1, 2),
(1, 3),
(1, 4),
(2, 2),
(2, 3),
(2, 4),
(3, 2),
(3, 3),
(3, 4),
(4, 2),
(4, 3),
(4, 4);

-- Inserir dados na tabela Report
INSERT INTO app_report (user_id, poll_id, text) VALUES
(1, 1, 'Report 1'),
(2, 2, 'Report 2');


-- Inserir dados na tabela Poll
INSERT INTO app_poll (criation_date, finish_date, status, title, description, privacy, creator_id, category, tags) VALUES
-- Polls públicas
('2024-07-10', '2024-07-20', 'OPEN', 'Melhor tecnologia do ano', 'Escolha a melhor tecnologia de 2024', 'PUBLIC', 2, 'technology', 'tecnologia'),
('2024-07-12', '2024-08-01', 'OPEN', 'Melhor filme de 2024', 'Escolha o melhor filme de 2024', 'PUBLIC', 3, 'entertainment', 'filme'),
('2024-07-15', '2024-08-05', 'OPEN', 'Melhor jogador de futebol', 'Escolha o melhor jogador de futebol', 'PUBLIC', 1, 'sports', 'futebol'),
('2024-07-18', '2024-08-10', 'OPEN', 'Melhor destino turístico', 'Escolha o melhor destino turístico', 'PUBLIC', 2, 'tourism', 'destino'),
('2024-07-20', '2024-08-15', 'OPEN', 'Melhor artista', 'Escolha o melhor artista do ano', 'PUBLIC', 3, 'art', 'artista'),
('2024-07-22', '2024-08-01', 'OPEN', 'Melhor restaurante da cidade', 'Escolha o melhor restaurante da cidade', 'RESTRICTED', 4, 'food', 'restaurante'),
('2024-07-25', '2024-08-05', 'OPEN', 'Melhor livro de ficção científica', 'Escolha o melhor livro de ficção científica', 'RESTRICTED', 5, 'culture', 'ficção'),
('2024-07-28', '2024-08-10', 'OPEN', 'Melhor inovação tecnológica', 'Escolha a melhor inovação tecnológica de 2024', 'RESTRICTED', 1, 'technology', 'inovação'),

-- Poll com várias questões
('2024-07-30', '2024-08-15', 'OPEN', 'Sua opinião sobre diversos tópicos', 'Responda a várias perguntas sobre diferentes tópicos.', 'PUBLIC', 4, 'random', 'opinião');

-- Inserir dados na tabela QuestionField
INSERT INTO app_questionfield (title, max_qtd_choices, poll_id) VALUES
-- Perguntas para novas polls
-- Tecnologia
('Qual é a melhor tecnologia do ano?', 1, 6),
-- Filmes
('Qual é o melhor filme de 2024?', 1, 7),
-- Futebol
('Quem é o melhor jogador de futebol?', 1, 8),
-- Destinos
('Qual é o melhor destino turístico?', 1, 9),
-- Artistas
('Quem é o melhor artista do ano?', 1, 10),

-- Restaurantes
('Qual é o melhor restaurante da cidade?', 1, 11),
-- Livros
('Qual é o melhor livro de ficção científica?', 1, 12),
-- Inovações
('Qual é a melhor inovação tecnológica?', 1, 13),

-- Perguntas para a poll com várias questões
('Qual é a sua cor favorita?', 1, 14),
('Qual é o seu hobby preferido?', 1, 14),
('Qual é a sua comida favorita?', 1, 14);

-- Inserir dados na tabela Option
INSERT INTO app_option (text, img, question_id) VALUES
-- Opções para novas perguntas
-- Tecnologia
('Inteligência Artificial', '', 6),
('Blockchain', '', 6),
('Realidade Aumentada', '', 6),
('Computação Quântica', '', 6),

-- Filmes
('Oppenheimer', '', 7),
('Duna', '', 7),
('Avatar 2', '', 7),
('Spider-Man: Across the Spider-Verse', '', 7),

-- Futebol
('Lionel Messi', '', 8),
('Cristiano Ronaldo', '', 8),
('Kylian Mbappé', '', 8),
('Neymar Jr.', '', 8),

-- Destinos
('Paris', '', 9),
('Tóquio', '', 9),
('Nova York', '', 9),
('Rio de Janeiro', '', 9),

-- Artistas
('Taylor Swift', '', 10),
('BTS', '', 10),
('Adele', '', 10),
('Ed Sheeran', '', 10),

-- Restaurantes
('Restaurante A', '', 11),
('Restaurante B', '', 11),
('Restaurante C', '', 11),
('Restaurante D', '', 11),

-- Livros
('Neuromancer', '', 12),
('Snow Crash', '', 12),
('Hyperion', '', 12),
('The Left Hand of Darkness', '', 12),

-- Inovações
('5G', '', 13),
('Tecnologia de Imunização', '', 13),
('Energia Renovável', '', 13),
('Veículos Elétricos', '', 13),

-- Opções para a poll com várias questões
-- Cor favorita
('Azul', '', 14),
('Verde', '', 14),
('Vermelho', '', 14),
('Amarelo', '', 14),

-- Hobby preferido
('Ler', '', 15),
('Esportes', '', 15),
('Viajar', '', 15),
('Cozinhar', '', 15),

-- Comida favorita
('Pizza', '', 16),
('Sushi', '', 16),
('Churrasco', '', 16),
('Hambúrguer', '', 16);


-- Inserir dados na tabela Vote
INSERT INTO app_vote (hash, date) VALUES
('hash17', '2024-07-05'),
('hash18', '2024-07-05'),
('hash20', '2024-07-05');


-- Inserir dados na tabela Choice
INSERT INTO app_choice (vote_id, option_id) VALUES
(17, 63),
(17, 69),
(17, 74);

INSERT INTO app_participation (user_id, poll_id) VALUES
(1, 14),
(2, 14),
(3, 14),
(4, 14),
(5, 14);

