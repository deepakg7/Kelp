from sqlite3 import *

w = input("Welcome to bank app.\nDo you want to create or update details y/n -> ")

while w == "Y" or w == "y":

	cmd = input()
	command = command.upper()
	z = command.split(" ")
	print(z)

	if z[0] == "CREATE":
		con = None
		try:
			con = connect("bankapp.db")
			cursor = con.cursor()
			sql = "insert into account values('%s','%s','%d')"
			acc_id = z[1]
			name = z[2]
			balance_amt = 0
			cursor.execute(sql % (id,name,balance))
			con.commit()
			print("record created ")
		except Exception as e:
			con.rollback()
			print("issue ",e)
		finally:
			if con is not None:
				con.close()

	elif z[0] == "DEPOSIT":
		con = None
		try:
			con = connect("bankapp.db")
			cursor = con.cursor()
			sql = "update account set balance = balance + '%d' where id = '%s'"
			acc_id = z[1]
			balance_amt = int(z[2])
			cursor.execute(sql % (balance,id))
			con.commit()
			print("record created ")
		except Exception as e:
			con.rollback()
			print("issue ",e)
		finally:
			if con is not None:
				con.close()

	elif z[0] == "WITHDRAW":
		con = None
		try:
			con = connect("bankapp.db")
			cursor = con.cursor()
			sql = "update account set balance = balance - '%d' where id = '%s'"
			acc_id = z[1]
			balance_amt = int(z[2])
			cursor.execute(sql % (balance,id))
			con.commit()
			print("record created ")
		except Exception as e:
			con.rollback()
			print("issue ",e)
		finally:
			if con is not None:
				con.close()

	elif z[0] == "SHOW":
		con = None
		try:
			con = connect("bankapp.db")
			cursor = con.cursor()
			sql = "select id, balance from account"
			cursor.execute(sql)
			res = cursor.fetchall()
			for i in res:
				for j in i:
					print(j)
				print()
		except Exception as e:
			print("issue ",e)
		finally:
			if con is not None:
				con.close()

	else:
		print("invalid input")

	w = input("\n\nDo you want to continue ?  ->  ")
