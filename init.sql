CREATE TABLE "participation"(
    "id" INTEGER NOT NULL,
    "user_id" INTEGER NOT NULL,
    "poll_id" INTEGER NOT NULL
);
ALTER TABLE
    "participation" ADD PRIMARY KEY("id");
CREATE TABLE "choice"(
    "id" INTEGER NOT NULL,
    "vote_id" INTEGER NOT NULL,
    "option_id" INTEGER NOT NULL
);
ALTER TABLE
    "choice" ADD PRIMARY KEY("id");
CREATE TABLE "question_field"(
    "id" INTEGER NOT NULL,
    "title" VARCHAR(255) NOT NULL,
    "max_qtd_choices" INTEGER NOT NULL,
    "poll_id" INTEGER NOT NULL
);
ALTER TABLE
    "question_field" ADD PRIMARY KEY("id");
CREATE TABLE "vote"(
    "id" INTEGER NOT NULL,
    "hash" VARCHAR(255) NOT NULL,
    "date" DATE NOT NULL
);
ALTER TABLE
    "vote" ADD PRIMARY KEY("id");
CREATE TABLE "option"(
    "id" INTEGER NOT NULL,
    "text" VARCHAR(255) NOT NULL,
    "img" bytea NOT NULL,
    "question_id" INTEGER NOT NULL
);
ALTER TABLE
    "option" ADD PRIMARY KEY("id");
CREATE TABLE "whitelist"(
    "id" INTEGER NOT NULL,
    "user_id" INTEGER NOT NULL,
    "poll_id" INTEGER NOT NULL
);
ALTER TABLE
    "whitelist" ADD PRIMARY KEY("id");
CREATE TABLE "report"(
    "id" INTEGER NOT NULL,
    "user_id" INTEGER NOT NULL,
    "poll_id" INTEGER NOT NULL,
    "text" VARCHAR(255) NULL
);
ALTER TABLE
    "report" ADD PRIMARY KEY("id");
CREATE TABLE "poll"(
    "id" INTEGER NOT NULL,
    "criation_date" DATE NOT NULL,
    "finish_date" DATE NOT NULL,
    "status" VARCHAR(255) CHECK
        ("status" IN('OPEN,CLOSED,BANNED,ARCHIVED')) NOT NULL,
        "title" VARCHAR(255) NOT NULL,
        "description" VARCHAR(255) NOT NULL,
        "privacy" VARCHAR(255)
    CHECK
        ("privacy" IN('PUBLIC,HIDDEN,RESTRICTED')) NOT NULL,
        "creator_id" INTEGER NOT NULL
);
ALTER TABLE
    "poll" ADD PRIMARY KEY("id");
CREATE TABLE "user"(
    "id" INTEGER NOT NULL,
    "cpf" CHAR(11) NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "lname" VARCHAR(255) NOT NULL,
    "username" CHAR(20) NOT NULL,
    "status" VARCHAR(255) CHECK
        ("status" IN('ACTIVE,INACTIVE,BANNED')) NOT NULL,
        "role" VARCHAR(255)
    CHECK
        ("role" IN('MODERATOR,USER')) NOT NULL,
        "password" CHAR(12) NOT NULL
);
ALTER TABLE
    "user" ADD PRIMARY KEY("id");
ALTER TABLE
    "choice" ADD CONSTRAINT "choice_option_id_foreign" FOREIGN KEY("option_id") REFERENCES "option"("id");
ALTER TABLE
    "choice" ADD CONSTRAINT "choice_vote_id_foreign" FOREIGN KEY("vote_id") REFERENCES "vote"("id");
ALTER TABLE
    "option" ADD CONSTRAINT "option_question_id_foreign" FOREIGN KEY("question_id") REFERENCES "question_field"("id");
ALTER TABLE
    "whitelist" ADD CONSTRAINT "whitelist_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "user"("id");
ALTER TABLE
    "participation" ADD CONSTRAINT "participation_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "user"("id");
ALTER TABLE
    "participation" ADD CONSTRAINT "participation_poll_id_foreign" FOREIGN KEY("poll_id") REFERENCES "poll"("id");
ALTER TABLE
    "report" ADD CONSTRAINT "report_poll_id_foreign" FOREIGN KEY("poll_id") REFERENCES "poll"("id");
ALTER TABLE
    "poll" ADD CONSTRAINT "poll_creator_id_foreign" FOREIGN KEY("creator_id") REFERENCES "user"("id");
ALTER TABLE
    "whitelist" ADD CONSTRAINT "whitelist_poll_id_foreign" FOREIGN KEY("poll_id") REFERENCES "poll"("id");

ALTER TABLE
    "report" ADD CONSTRAINT "report_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "user"("id");
ALTER TABLE
    "question_field" ADD CONSTRAINT "question_field_poll_id_foreign" FOREIGN KEY("poll_id") REFERENCES "poll"("id");