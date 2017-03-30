import xml.etree.ElementTree as ET
import MySQLdb
dsn_database = "patent"   # e.g. "MySQLdbtest"
dsn_hostname = "localhost"       # e.g.: "mydbinstance.xyz.us-east-1.rds.amazonaws.com"
#dsn_port = 3306                        # e.g. 3306 
dsn_uid = "root"             # e.g. "user1"
dsn_pwd = "password@123"      
conn = MySQLdb.connect(host=dsn_hostname, user=dsn_uid, passwd=dsn_pwd, db=dsn_database)

count = 0
output = []
for i in range(0,10):
    
    f = open("ipgb20060103.xml-{}".format(i),encoding="utf8")
    
    tree = ET.parse(f)
    root = tree.getroot()
    for c in root.findall('us-bibliographic-data-grant/././'):
        if c.tag == "publication-reference":
            names = [node.tag for node in c.getiterator()]
            values = [node.text for node in c.getiterator()]
            print (values)
            print (names)
            sql1 = """CREATE TABLE IF NOT EXISTS `{0}` (`{1[1]}` varchar(100) ,`{1[2]}` varchar(100) ,`{1[3]}` varchar(100), {1[4]} varchar(100),{1[5]} varchar(100));""" .format(c.tag,names)
            conn.query(sql1)
            x = conn.cursor()
            x.execute("""INSERT INTO `{0}` VALUES ('1','{1[2]}','{1[3]}','{1[4]}','{1[5]}');""".format(c.tag,values))
            conn.commit()
            
            #print ("""INSERT INTO `{0}` VALUES ('1','{1[2]}','{1[3]}','{1[4]}','{1[5]}');""".format(c.tag,values))
            
       
            
            
  
        
        
