-- slide 9
create table watched(
                        title varchar,
                        my_rating int
)

-- slide 11
insert into watched (title, my_rating) values('Game Over, Man!', 6), ('Barry', 8), ('Sturgill Simpson Presents: Sound & Fury', 10),
                                             ('Da 5 Bloods', 7), ('A Futile and Stupid Gesture', 10), ('Always Be My Maybe', 7), ('Biggie: I Got a Story to Tell', 8), ('Dolemite Is My Name', 7),
                                             ('Dick Johnson Is Dead', 7), ('Invader Zim: Enter the Florpus', 8), ('The White Helmets', 9), ('Athlete A', 10), ('What Happened, Miss Simone?', 9),
                                             ('Beasts of No Nation', 8), ('Crip Camp: A Disability Revolution', 10), ('Roma', 10), ('The Irishman', 7), ('Icarus', 10),
                                             ('13th', 10)

-- slide 13
update watched set my_rating = 9 where title = 'Da 5 Bloods'


-- slide 16
drop table watched

-- slide 17
select title, genre from netflix_originals
select title, genre, premiere from netflix_originals

-- slide 18
select title as name, runtime as length from netflix_originals

-- slide 19
select * from netflix_originals

-- slide 21
select * from netflix_originals where runtime < 60
insert into my_playlist (movies)
select title as foreign_films from netflix_originals where language = 'Spanish'


INSERT INTO table2 (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
    FROM table1
WHERE condition;



-- slide 22
select distinct language from netflix_originals

-- slide 23
select * from netflix_originals limit(10)

-- slide 24
select * from netflix_originals where runtime between 60 and 120

-- slide 25
select title from netflix_originals where title like 'Christmas%'
select title from netflix_originals where title like '%Christmas%'
select title from netflix_originals where title ilike '%x%'

-- slide 26
select * from netflix_originals where genre in ('Documentary', 'Thriller')

-- slide 27
select * from netflix_originals order by imdb_score desc
select * from netflix_originals order by imdb_score asc

-- slide 29
select count(*) from netflix_originals
select min(imdb_score) from netflix_originals

-- slide 30
select genre, count(*) from netflix_originals group by genre order by count desc

-- slide 31
select genre, count(*) from netflix_originals group by genre having (count(*) > 3) order by count desc

-- slide 32
select title from watched
union
select title from netflix_originals

-- slide 33-36
select * from watched inner join netflix_originals on (watched.title = netflix_originals.title);
select * from watched left join netflix_originals on (watched.title = netflix_originals.title);
select * from watched right join netflix_originals on (watched.title = netflix_originals.title);
select * from watched full join netflix_originals on (watched.title = netflix_originals.title);

-- slide 37
select title from netflix_originals where imdb_score > (select avg(my_rating) from watched)
