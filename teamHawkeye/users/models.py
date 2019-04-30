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


	def save(self, *args, **kwargs):
		#cursor.execute('''DROP TRIGGER teamHawkeye.ageCheckTrigger''')
		'''
		requestedAge = Profile.objects.raw('CREATE TRIGGER ageCheckTrigger BEFORE UPDATE ON users_profile ' +
										'FOR EACH ROW ' + 
										'BEGIN ' +
										'IF NEW.age < 0 THEN SET NEW.age = 0;' +
										'END IF;' + 
										'END')
		'''
		
		super().save()
		image = Image.open(self.profile_pic.path)
		if image.height > 300 or image.width > 300:
			output_size = (300, 300)
			image.thumbnail(output_size)
			image.save(self.profile_pic.path)
