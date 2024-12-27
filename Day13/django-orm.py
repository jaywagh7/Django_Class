'''
getting all data 

1. Student.objects.all()
2. Student.objects.filter(first_name='ram').
2. Student.objects.create(name='Student', age=4)
2. Student.objects.exclude(first_name='ram')
3. Student.objects.get(first_name='ram')
4. Student.objects.order_by('first_name')
5. Student.objects.filter(first_name='ram').order_by('first_name')
6. Student.objects.values('first_name')
7. Student.objects.values_list('first_name')
13. Student.objects.filter(first_name='ram').delete()
14. Student.objects.filter(first_name='ram').exists()
15. Student.objects.all().count()
16. Student.objects.first()
17. Student.objects.last()
18. Student.objects.filter(age=20).values('first_name', 'age')
19. Student.objects.filter(age=20).values_list('first_name', flat=True)
12. Student.objects.filter(first_name='ram').update(age=50)



from django.db.models import F
from django.db import models

20. Student.objects.filter(age=20).annotate(age_diff=models.F('age') - models.F('date_of_birth__year')).filter(age_diff__gt=10).values('first_name', 'age_diff')
21. Student.objects.filter(age=20).annotate(age_diff=models.F('age') - models.F('date_of_birth__year')).filter(age_diff__gt=10).values_list('first_name', 'age_diff')
8. Student.objects.annotate(age_diff=models.F('age') - models.F('date_of_birth__year')).filter(age_diff__gt=10)
9. Student.objects.annotate(age_diff=models.F('age') - models.F('date_of_birth__year')).order_by('-age_diff')
10. Student.objects.annotate(age_diff=models.F('age') - models.F('date_of_birth__year')).values('first_name', 'age_diff')
11. Student.objects.annotate(age_diff=models.F('age') - models.F('date_of_birth__year')).values_list('first_name', 'age_diff')

'''