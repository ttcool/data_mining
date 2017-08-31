from pyspark.files import SparkFiles
from pyspark import SparkContext,SparkConf
import matplotlib

conf = SparkConf().setAppName("test_exp").setMaster("local[2]")
sc = SparkContext(conf=conf)
sc.addFile("/home/syphcdh/ml-100k/u.user")
user_fields = sc.textFile(SparkFiles.get("/home/syphcdh/ml-100k/u.user")).map(lambda line:line.split("|"))
print user_fields.first()
num_users = user_fields.map(lambda fields: fields[0]).count()
num_genders = user_fields.map(lambda fields:fields[2]).distinct().count()
num_occupations = user_fields.map(lambda fields:fields[3]).distinct().count()
num_zipcodes = user_fields.map(lambda fields:fields[4]).distinct().count()
print "Users: %d, genders: %d, occupations: %d, ZIP codes: %d" % (num_users, num_genders,num_occupations, num_zipcodes)
ages = user_fields.map(lambda x: int(x[1])).collect()
hist(ages, bins=20, color='lightblue', normed=True)
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(16, 10)
