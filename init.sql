-- Inserir dados na tabela User
INSERT INTO app_user (cpf, email, name, lname, username, status, role, password, is_active, is_staff, is_admin) VALUES
('12345678901', 'user1@example.com', 'FirstName1', 'LastName1', 'user1', 'ACTIVE', 'USER', 'password1', TRUE, FALSE, FALSE),
('12345678902', 'user2@example.com', 'FirstName2', 'LastName2', 'user2', 'INACTIVE', 'MODERATOR', 'password2', TRUE, TRUE, FALSE);

-- Inserir dados na tabela Poll
INSERT INTO app_poll (criation_date, finish_date, status, title, description, privacy, creator_id) VALUES
('2024-01-01', '2024-01-31', 'OPEN', 'Poll 1', 'Description 1', 'PUBLIC', 1),
('2024-02-01', '2024-02-28', 'CLOSED', 'Poll 2', 'Description 2', 'RESTRICTED', 2);

-- Inserir dados na tabela Participation
INSERT INTO app_participation (user_id, poll_id) VALUES
(1, 1),
(2, 2);

-- Inserir dados na tabela QuestionField
INSERT INTO app_questionfield (title, max_qtd_choices, poll_id) VALUES
('Question 1', 3, 1),
('Question 2', 2, 2);

-- Inserir dados na tabela Option
INSERT INTO app_option (text, img, question_id) VALUES
('Option 1', '\\x89504e470d0a1a0a0000000d4948445200000001000000010806000000ff', 1),
('Option 2', '\\x89504e470d0a1a0a0000000d4948445200000002000000010806000000ff', 2);

-- Inserir dados na tabela Vote
INSERT INTO app_vote (hash, date) VALUES
('hash1', '2024-01-15'),
('hash2', '2024-02-15');

-- Inserir dados na tabela Choice
INSERT INTO app_choice (vote_id, option_id) VALUES
(1, 1),
(2, 2);

-- Inserir dados na tabela Whitelist
INSERT INTO app_whitelist (user_id, poll_id) VALUES
(1, 1),
(2, 2);

-- Inserir dados na tabela Report
INSERT INTO app_report (user_id, poll_id, text) VALUES
(1, 1, 'Report 1'),
(2, 2, 'Report 2');
