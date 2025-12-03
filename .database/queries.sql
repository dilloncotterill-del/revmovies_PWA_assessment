-- CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        -- username TEXT NOT NULL,
                        -- password TEXT NOT NULL,
                        -- display_name TEXT);

-- CREATE TABLE Movies (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        -- movie_name TEXT NOT NULL,
                        -- release_date DATE,
                        -- movie_description TEXT NOT NULL,
                        -- genre TEXT NOT NULL);

-- CREATE TABLE Reviews (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        -- title TEXT NOT NULL,
                        -- review_date DATE,
                        -- rating INTEGER
                        -- review_text TEXT NOT NULL,
                        -- movie_id INTEGER,
                        -- user_id INTEGER);

INSERT INTO Users (username, password, display_name) VALUES
                    ('awesomejim14', 'scrypt:32768:8:1$ZIUB1D5lCNl2GZ5w$4de3cadd75e3f03617e0c7423a3aab85a84fd9dea009295ce41d438e52da3cbc0b64def6ecbaaef13255c4918585c15e6c313d8d98d64f37c37d22b3e25bf04e', 'Jim'),
                    ('cleverfred29', 'scrypt:32768:8:1$YfnN0EtmRGYdDphU$6803d35904ca054bc23232df87abd76ec9fe75eae8fe21301146f8bcfc1649715a787e218cb2a7463ab1d11b4e0186cf0541144aaf554d022cd9fc9395b2cae8', 'Fred'),
                    ('greatesteddie98', 'scrypt:32768:8:1$LaSx68XLEuZ1TWJU$0aa3b35c461bcf8343554773d6a3957b7b22af7a902403b5f7e1574d42b4e7630959b483af7a5d22e3bc1659ccd6eb1209917c8537417fddc1e6960bb43a4b04', 'Eddie'),
                    ('bestjohn19', 'scrypt:32768:8:1$FdOgvhXqmAAY5465$192fa886bc701dd88b4b73be9ee356af23c83fc9918fcfa8cb40cbc65ff3c31f0d99ac02fd12f6c2b218ef8a518055b1391ef02a5456daa277711d7ee5c02a05', 'John'),
                    ('funnywill43', 'scrypt:32768:8:1$19yCXh84aS6I31Z3$9cf8bf32640359830b8bac6a8f8ea46ca4c6f78dbc607769ea887c9415bd7c8754dad12cdc41c9570fa849b3a26a0d55aedaca2f770ac7ea74342f5728686109', 'Will');

INSERT INTO Movies (movie_name, release_date, movie_description, genre) VALUES
                    ('Taxi Driver', '1976-02-08', 'Taxi Driver is a 1976 psychological drama directed by Martin Scorcese. The film follows Travis Bickle, a Vietnam War veteran who becomes takes on a career as a taxi driver. He becomes obsessed with cleaning up the "scum" of the crime and urban decay that he notices nightly.', 'Crime/Noir'),
                    ('Whiplash', '2014-01-16', 'Whiplash tells the story of Andrew Neiman, who enrols in a music conservatory to become a drummer. Andrew is mentored by Terence Fletcher, who pushes him past the boundaries of reason and stability.', 'Drama/Indie'),
                    ('Joker', '2019-10-04', 'Joker follows Arthur Fleck, a party clown who lives an impoverished life with his ailing mother. When society shuns him and labels him as a freak, he descends into madness and embraces a life of crime and chaos.', 'Thriller/Crime'),
                    ('Mid90s', '2018-10-19', 'In Mid90s, a 13 year old boy in the 1990s grapples with an unstable home life during summer, however he finds new friends and solace at a motor avenue skate shop.', 'Comedy/Drama');

INSERT INTO Reviews (title, review_date, rating, review_text, movie_id, user_id) VALUES
                    ('Witty and sentimental', '2025-12-03', '8', 'This film really touched my heart in the best way possible. The characters felt so real and perfect that it didnt even feel like a film.', '4', '2'),
                    ('conseqences of societal rejection', '2025-12-03', '9', 'Joker underlines the impact that the widespread shunning of society can have on an individuals mind and character. It portrays Arthurs consquential descent into paranoia and madness at the hands of rejecting societies.', '3', '4');