import pymysql
import config

def bd_connect():
	db = pymysql.connect(
	host=config.HOST,
	database=config.DATABAZA,
	user=config.USER,
	password=config.PASSWORD
	)
	cur = db.cursor()

	db_cur = [db,cur]

	return db_cur