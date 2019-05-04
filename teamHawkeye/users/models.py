from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from localflavor.us.us_states import STATE_CHOICES
from django.db import connection

cursor = connection.cursor()


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	firstName = models.CharField(max_length = 100, null = True, blank = True)
	lastName = models.CharField(max_length = 100, null = True, blank = True)
	age = models.IntegerField(null = True, blank = True)
	address = models.CharField(max_length = 255, null = True, blank = True)
	city = models.CharField(max_length = 255, null = True, blank = True)
	state = models.CharField(choices = STATE_CHOICES, max_length = 255, null = True, blank = True)
	zipCode = models.IntegerField(null = True, blank = True)
	profile_pic = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
	cursor.execute('''DROP TRIGGER IF EXISTS ageCheckTrigger''')
	cursor.execute('''CREATE TRIGGER ageCheckTrigger BEFORE UPDATE ON users_profile FOR EACH ROW BEGIN IF NEW.age < 0 THEN SET NEW.AGE = 0; END IF; END''')
	# SHOW TRIGGERS; (Triggers & Compound Statements)
	cursor.execute('''DROP TABLE IF EXISTS userInfo''')
	cursor.execute('''CREATE TABLE userInfo ( myUsername VARCHAR(100) PRIMARY KEY, myFirstName VARCHAR(100), myLastName VARCHAR(100), myAge INT CHECK (myAge >= 0))''')
	# SHOW TABLES; (Check Constraint)
	cursor.execute('''START TRANSACTION''')
	cursor.execute('''INSERT INTO userInfo VALUES ('testUser', 'Test', 'User', 1)''')
	cursor.execute('''ROLLBACK''')
	cursor.execute('''START TRANSACTION''')
	cursor.execute('''INSERT INTO userInfo VALUES ('testUser', 'Test', 'User', 5)''')
	cursor.execute('''COMMIT''')
	# (Transactions)
	cursor.close()

	def save(self, *args, **kwargs):
		super().save()
		image = Image.open(self.profile_pic.path)
		if image.height > 300 or image.width > 300:
			output_size = (300, 300)
			image.thumbnail(output_size)
			image.save(self.profile_pic.path)
