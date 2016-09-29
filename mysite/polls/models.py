from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

# we can define anything here we want to store in our db

@python_2_unicode_compatible
class Question(models.Model):	# this is going to be a table
	question_text = models.CharField(max_length=200)
	# this is going to be column /field in the Question table
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text


@python_2_unicode_compatible
class Choice(models.Model):	# this is going to be a table
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text