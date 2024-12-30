INSERT INTO examination.users (`id`,`name`,`surname`,`role`,`email`,`password`,`index`) VALUES (1,'Tomasz','Złomiarz','STUDENT','student@gmail.com','$2b$12$u102FZE6FGPSufN0GdnoM.Jf4bcUA6Ari6xkYKBHYo1RqqeGWKZ8S',310035);
INSERT INTO examination.users (`id`,`name`,`surname`,`role`,`email`,`password`,`index`) VALUES (2,'Jurek','Ogórek','LECTURER','lecturer@gmail.com','$2b$12$YBMGExd6uEcQTGl/lQi/GefhsUVagH2nZgyQhPKDQn3iBjG3IINTW',NULL);
INSERT INTO examination.users (`id`,`name`,`surname`,`role`,`email`,`password`,`index`) VALUES (3,'Karolina','Malina','LECTURER','malina@gmail.com','$2b$12$t7pCMwfJ2auex.cxwOhC3eStywbT2obVk08HhXGlO1ObqoUTFoIZ6',NULL);
INSERT INTO examination.users (`id`,`name`,`surname`,`role`,`email`,`password`,`index`) VALUES (4,'Zenek','Błazenek','STUDENT','blazenek@gmail.com','$2b$12$eoBJZ5p29yZYAvh235aEU.iaXJgc84eZAc9pvBrWKJvoTjQZ0RdN6',310333);

INSERT INTO examination.courses (`id`,`title`,`shortcut`) VALUES (1,'Algorytmy i struktury danych','AISDI');
INSERT INTO examination.courses (`id`,`title`,`shortcut`) VALUES (2,'Analiza i projektowanie systemów informacyjnych','APSI');
INSERT INTO examination.courses (`id`,`title`,`shortcut`) VALUES (3,'Bazy danych 2','BD2');
INSERT INTO examination.courses (`id`,`title`,`shortcut`) VALUES (4,'Sieci komputerowe','SKM');
INSERT INTO examination.courses (`id`,`title`,`shortcut`) VALUES (5,'Nanotechnologie','NAN');
INSERT INTO examination.courses (`id`,`title`,`shortcut`) VALUES (6,'Programowanie obiektowe','PROI');
INSERT INTO examination.courses (`id`,`title`,`shortcut`) VALUES (7,'Podstawy automatyki','PODA');

INSERT INTO examination.course_realizations (`id`,`semester`,`course_id`,`lecturer_id`) VALUES (1,'24L',3,3);
INSERT INTO examination.course_realizations (`id`,`semester`,`course_id`,`lecturer_id`) VALUES (2,'24Z',1,2);
INSERT INTO examination.course_realizations (`id`,`semester`,`course_id`,`lecturer_id`) VALUES (3,'24Z',2,3);
INSERT INTO examination.course_realizations (`id`,`semester`,`course_id`,`lecturer_id`) VALUES (4,'23Z',5,3);
INSERT INTO examination.course_realizations (`id`,`semester`,`course_id`,`lecturer_id`) VALUES (5,'23Z',6,3);
INSERT INTO examination.course_realizations (`id`,`semester`,`course_id`,`lecturer_id`) VALUES (6,'22Z',7,3);

INSERT INTO examination.students_course_realizations (`student_id`, `course_realization_id`) VALUES (1, 1);
INSERT INTO examination.students_course_realizations (`student_id`, `course_realization_id`) VALUES (1, 2);
INSERT INTO examination.students_course_realizations (`student_id`, `course_realization_id`) VALUES (1, 3);
INSERT INTO examination.students_course_realizations (`student_id`, `course_realization_id`) VALUES (4, 3);

INSERT INTO examination.exams (`id`,`title`,`start_date`,`end_date`,`duration_limit`,`status`,`questions_quantity`,`max_points`,`type`,`course_realization_id`) VALUES (1,'Sprawdzian 1','2025-01-06 15:00:00','2025-01-06 16:00:00',30,'ASSIGNED',4,20,'TEST',3);
INSERT INTO examination.exams (`id`,`title`,`start_date`,`end_date`,`duration_limit`,`status`,`questions_quantity`,`max_points`,`type`,`course_realization_id`) VALUES (2,'Kolokwium','2025-01-04 16:00:00','2025-01-04 17:30:00',60,'UNDEFINED',2,20,'TEST',3);
INSERT INTO examination.exams (`id`,`title`,`start_date`,`end_date`,`duration_limit`,`status`,`questions_quantity`,`max_points`,`type`,`course_realization_id`) VALUES (3,'Kolokwium - modele','2024-12-22 17:00:00','2024-12-22 17:00:00',45,'CLOSED',5,20,'TEST',3);
INSERT INTO examination.exams (`id`,`title`,`start_date`,`end_date`,`duration_limit`,`status`,`questions_quantity`,`max_points`,`type`,`course_realization_id`) VALUES (4,'Projekt','2024-11-11 17:00:00','2025-01-15 17:00:00',NULL,'ACTIVE',NULL,15,'PROJECT',3);

INSERT INTO examination.questions (`id`,`text`,`image`,`type`,`score`,`score_type`,`exam_id`) VALUES (1,'Zaznacz elementy charakterystyczne dla modelu relacyjnego.',NULL,'MULTI',3,'PROPORTIONAL',1);
INSERT INTO examination.questions (`id`,`text`,`image`,`type`,`score`,`score_type`,`exam_id`) VALUES (2,'Napisz zalety bazy danych Oracle.',NULL,'OPEN',5,'PROPORTIONAL',1);
INSERT INTO examination.questions (`id`,`text`,`image`,`type`,`score`,`score_type`,`exam_id`) VALUES (3,'Dlaczego MySQL jest najlepsze?',NULL,'OPEN',2,'PROPORTIONAL',1);
INSERT INTO examination.questions (`id`,`text`,`image`,`type`,`score`,`score_type`,`exam_id`) VALUES (4,'Zaznacz prawdziwe:',NULL,'MULTI',4,'PROPORTIONAL',1);
INSERT INTO examination.questions (`id`,`text`,`image`,`type`,`score`,`score_type`,`exam_id`) VALUES (5,'Dlaczego APSI jest takie fajne?',NULL,'OPEN',8,'PROPORTIONAL',1);
INSERT INTO examination.questions (`id`,`text`,`image`,`type`,`score`,`score_type`,`exam_id`) VALUES (6,'Zaznacz fałszywe:',NULL,'SINGLE',3,'FULL',1);

INSERT INTO examination.question_items (`id`,`text`,`image`,`correctness`,`question_id`) VALUES (1,'Relacja',NULL,1,1);
INSERT INTO examination.question_items (`id`,`text`,`image`,`correctness`,`question_id`) VALUES (2,'Encja',NULL,0,1);
INSERT INTO examination.question_items (`id`,`text`,`image`,`correctness`,`question_id`) VALUES (3,'Tabela',NULL,1,1);
INSERT INTO examination.question_items (`id`,`text`,`image`,`correctness`,`question_id`) VALUES (4,'BD2 jest najlepsze',NULL,1,4);
INSERT INTO examination.question_items (`id`,`text`,`image`,`correctness`,`question_id`) VALUES (5,'Słowo wrubel posiada literówkę',NULL,1,4);
INSERT INTO examination.question_items (`id`,`text`,`image`,`correctness`,`question_id`) VALUES (6,'BD1 jest najlepsze',NULL,0,4);
INSERT INTO examination.question_items (`id`,`text`,`image`,`correctness`,`question_id`) VALUES (7,'BD to rozwinięcie od Bazy Danych',NULL,1,4);
INSERT INTO examination.question_items (`id`,`text`,`image`,`correctness`,`question_id`) VALUES (8,'To zdanie jest fałszywe!',NULL,0,6);
INSERT INTO examination.question_items (`id`,`text`,`image`,`correctness`,`question_id`) VALUES (9,'To zdanie jest prawdziwe!',NULL,1,6);

INSERT INTO examination.exam_students (`id`,`score`,`status`,`start_date`,`end_date`,`duration`,`exam_id`,`student_id`) VALUES (1,NULL,'SCHEDULED',NULL,NULL,NULL,1,1);
INSERT INTO examination.exam_students (`id`,`score`,`status`,`start_date`,`end_date`,`duration`,`exam_id`,`student_id`) VALUES (2,NULL,'SCHEDULED',NULL,NULL,NULL,1,4);

INSERT INTO examination.exam_students_questions (`exam_student_id`,`question_id`) VALUES (1,1);
INSERT INTO examination.exam_students_questions (`exam_student_id`,`question_id`) VALUES (1,2);
INSERT INTO examination.exam_students_questions (`exam_student_id`,`question_id`) VALUES (1,3);
INSERT INTO examination.exam_students_questions (`exam_student_id`,`question_id`) VALUES (2,2);
INSERT INTO examination.exam_students_questions (`exam_student_id`,`question_id`) VALUES (2,3);
INSERT INTO examination.exam_students_questions (`exam_student_id`,`question_id`) VALUES (2,4);
