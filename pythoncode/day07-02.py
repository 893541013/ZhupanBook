from mysqltools import MysqlTools

mysql_tools = MysqlTools()
res = mysql_tools.query("select * from t_user where username ='liuyun1'")
print(res)