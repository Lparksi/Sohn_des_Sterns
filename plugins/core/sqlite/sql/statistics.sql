create table statistics
(
	id integer
		constraint statistics_pk
			primary key autoincrement,
	item text,
	value integer
);