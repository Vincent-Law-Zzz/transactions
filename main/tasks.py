from main.celery import app
from main.models import User
from django.db.utils import OperationalError
from django.db import transaction
import asyncio

@app.task
def change_balance(user , value):
	try:
		with transaction.atomic():
			user_db = User.objects.get(user_name=user)
			user_db.value += float(value)
			print(user_db.value)
			if user_db.value >= 0 and float(value) != 0:
				user_db.save()
	except OperationalError as exc:
		change_balance.apply_async([user,value],countdown = 10)