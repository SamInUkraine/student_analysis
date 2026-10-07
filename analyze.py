"""
Кейс-стаді — аналіз CSV-файлу

Ваше завдання — пройти весь шлях від порожньої папки до проєкту на GitHub:

1. Створити папку з проєктом
2. Завантажити туди дані
3. Зробити аналіз
4. Зберегти результат у .txt файл
5. Запушити все на GitHub
"""


# ============================================================
# Крок 1. Створіть папку з проєктом
# ============================================================
# У терміналі:
#
#   mkdir students_analysis
#   cd students_analysis
#
# Усі наступні файли мають лежати всередині цієї папки.


# ============================================================
# Крок 2. Завантажте туди дані
# ============================================================
# Скопіюйте файл students.csv у папку students_analysis.
# Формат файлу: name,math,python,english
# (перший рядок — заголовок, далі по одному студенту в рядку)
#
# Також збережіть цей скрипт у ту саму папку як analyze.py.


# ============================================================
# Крок 3. Зробіть аналіз
# ============================================================
# Потрібно порахувати:
#   - середній бал по класу з кожного предмета (math, python, english);
#   - ім'я студента з найвищим середнім балом (по трьох предметах).

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"


total_math = 0
total_python = 0
total_english = 0
# TODO 1: відкрийте INPUT_FILE через with open(...) as f:
#   і пропустіть рядок заголовка (next(f))

with open(INPUT_FILE, "r") as f:
    next(f)

    # TODO 2: пройдіться по рядках файлу (for line in f:), для кожного рядка:
    #   - приберіть символ переносу рядка (line.strip())
    #   - розбийте рядок по комі (line.split(","))
    #   - перетворіть оцінки на числа (int або float)

    students = 0
    students_gpa = {}
    best_student = ""
    for line in f:
        line = line.strip()
        grades = [int(grade) for grade in line.split(",")[1:]]
        total_grades = sum(grades)
        students += 1

        name = line.split(",")[0]
        
        students_gpa[name] = total_grades / len(grades)

        if best_student:
            if students_gpa[name] > students_gpa[best_student]:
                best_student = name
        else:
            best_student = name

        total_math += grades[0]
        total_python += grades[1]
        total_english += grades[2]

class_gpa_math = total_math / students
class_gpa_python = total_python / students
class_gpa_english = total_english / students

# TODO 3: по ходу циклу накопичуйте:
#   - суми оцінок з кожного предмета та кількість студентів
#   - найкращого студента (ім'я та його середній бал) — порівнюйте
#     середній бал поточного студента з найкращим на цей момент

# TODO 4: після циклу порахуйте середній бал по класу з кожного предмета
#   (сума / кількість студентів)


# ============================================================
# Крок 4. Збережіть результат у .txt файл
# ============================================================
# TODO 5: відкрийте OUTPUT_FILE в режимі 'w' і запишіть туди результат
#   у такому вигляді (числа округліть до одного знака після коми):
#
#   Середній бал по класу:
#   math: 67.8
#   python: 67.9
#   english: 67.9
#
#   Найкращий студент: Ім'я Прізвище (97.0)
#
# Також виведіть цей самий текст на екран через print().
#
# Запустіть скрипт (python analyze.py) і перевірте, що в папці
# з'явився файл result.txt.

with open(OUTPUT_FILE, "w") as f:
    f.write(f"Середній бал по класу:\n")
    f.write(f"math: {class_gpa_math:.1f}\n")
    f.write(f"python: {class_gpa_python:.1f}\n")
    f.write(f"english: {class_gpa_english:.1f}\n")
    f.write(f"Найкращий студент: {best_student} ({students_gpa[best_student]:.1f})")


print(f"Середній бал по класу:")
print(f"math: {class_gpa_math:.1f}")
print(f"python: {class_gpa_python:.1f}")
print(f"english: {class_gpa_english:.1f}\n")
print(f"Найкращий студент: {best_student} ({students_gpa[best_student]:.1f})")
# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
#   git init
#   git add .
#   git commit -m "Students analysis"
#   git branch -M main
#   git remote add origin <посилання_на_ваш_репозиторій>
#   git push -u origin main
#
# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.
