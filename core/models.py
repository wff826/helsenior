from django.db import models

# 고령자 모델
class Elder(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name


# 보호자 모델
class Caregiver(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    elder = models.ForeignKey(Elder, on_delete=models.CASCADE, related_name='caregivers')

    def __str__(self):
        return self.name


# 생체 건강 데이터 모델
class HealthData(models.Model):
    elder = models.ForeignKey(Elder, on_delete=models.CASCADE, related_name='health_data')
    timestamp = models.DateTimeField(auto_now_add=True)
    heart_rate = models.IntegerField(null=True, blank=True)
    blood_pressure_systolic = models.IntegerField(null=True, blank=True)  # 수축기 혈압
    blood_pressure_diastolic = models.IntegerField(null=True, blank=True) # 이완기 혈압
    spo2 = models.FloatField(null=True, blank=True)  # 산소포화도 (%)

    def __str__(self):
        return f"{self.elder.name} - {self.timestamp}"


# 이상 징후 알림 모델
class Alert(models.Model):
    elder = models.ForeignKey(Elder, on_delete=models.CASCADE, related_name='alerts')
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"[{self.elder.name}] {self.message[:30]}..."
