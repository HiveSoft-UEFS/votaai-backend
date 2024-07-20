-- Inserir dados na tabela User
INSERT INTO app_user (cpf, email, name, lname, username, status, role, password, is_active, is_staff, is_admin) VALUES
('12345678901', 'user1@example.com', 'FirstName1', 'LastName1', 'user1', 'ACTIVE', 'USER', 'password1', TRUE, FALSE, FALSE),
('12345678902', 'user2@example.com', 'FirstName2', 'LastName2', 'user2', 'INACTIVE', 'MODERATOR', 'password2', TRUE, TRUE, FALSE),
('12345678903', 'amanda@example.com', 'Amanda', 'Silva', 'amandaS', 'ACTIVE', 'USER', 'pass', TRUE, FALSE, FALSE),
('12345678904', 'miguel@example.com', 'Miguel', 'Andrade', 'migueAnd', 'ACTIVE', 'USER', 'miguePass', TRUE, FALSE, FALSE),
('12345678905', 'admin@example.com', 'Admin', 'Silva', 'admin', 'ACTIVE', 'USER', 'admin', TRUE, FALSE, FALSE);

-- Inserir dados na tabela Poll
INSERT INTO app_poll (criation_date, finish_date, status, title, description, privacy, creator_id, category, tags) VALUES
('2024-07-01', '2024-07-31', 'OPEN', 'Melhor livro', 'Escolha o melhor livro', 'PUBLIC', 1, 'CULTURE', 'livro'),
('2024-07-01', '2024-07-20', 'CLOSED', 'Melhor feriado do ano', 'Escolha o melhor feriado do ano', 'PUBLIC', 1, 'RANDOM', 'feriado'),
('2024-07-05', '2024-07-20', 'CLOSED', 'Melhor cantor', 'Escolha o melhor cantor', 'RESTRICTED', 2, 'RANDOM', 'musica'),
('2024-07-05', '2024-07-20', 'CLOSED', 'Melhor anime', 'Escolha o melhor anime', 'RESTRICTED', 5, 'ANIMATION', 'anime'),
('2024-07-05', '2024-07-20', 'OPEN', 'Melhor mangá', 'Escolha o melhor mangá', 'PUBLIC', 5, 'CULTURE', 'manga');

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
