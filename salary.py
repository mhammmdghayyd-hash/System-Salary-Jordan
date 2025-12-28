# نظام حساب الرواتب المطور - نسخة العقبة الخاصة
print("--- مرحباً بك في نظام رواتب شركات العقبة ---")

# المدخلات
name = input("أدخل اسم الموظف: ")
basic_salary = float(input("أدخل الراتب الأساسي: "))
overtime_hours = float(input("أدخل عدد ساعات الإضافي: "))
aqaba_allowance = float(input("أدخل قيمة علاوة العقبة: "))

# الحسابات
overtime_pay = overtime_hours * 5.0
total_before_deductions = basic_salary + overtime_pay + aqaba_allowance

# الخصومات (ضمان اجتماعي 7.5% وتأمين صحي ثابت 10 دنانير)
social_security = basic_salary * 0.075
health_insurance = 10.0
total_deductions = social_security + health_insurance

# الراتب النهائي
net_salary = total_before_deductions - total_deductions

# عرض النتيجة بشكل احترافي
print("-" * 30)
print(f"كشف راتب الموظف: {name}")
print(f"إجمالي المستحقات: {total_before_deductions} دينار")
print(f"إجمالي الخصومات: {total_deductions} دينار")
print(f"الراتب الصافي النهائي هو: {net_salary} دينار")
print("-" * 30)
