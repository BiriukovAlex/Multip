import random

life=3
time=1

print ("This program will test your knowledge of multiplication tables.")
print ("Эта программа проверит твои знания таблицы умножения.")

while 1:
	a=random.randrange(0, 10, 1)
	b=random.randrange(0, 10, 1)
	
	while 1:
		try:
			c=int(input("Жизнь #{} Пример#{} Решай:{}*{}=".format(life,time,a,b)))
			break
		except ValueError:
			print ("ОШИБКА! Не верное число. Повторите ввод!")
			continue
			
	d=a*b
	if d==c:
		print ("Правильно")
	else:
		print ("Не правильно! минус жизнь.")
		life=life-1
	
	time+=1;#time=time+1 time++
	
	if life==0:
		print ("Учи таблицу!")
		break

	if time>10:
		print ("Поздравляемс! Ты гений умножения!")
		break


