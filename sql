


INSERT INTO stockscreener_calendar (date,cdr)
SELECT "date","cdr"
FROM "calendar"


INSERT INTO stockscreener_batch_run("BBG","CDR","web_source","IDX","isWorking","mnemo")
SELECT "BBG","CDR","web_source","IDX","isWorking","mnemo"
FROM "batch_run"
