import csv
from lesson_020.HW_002.csv_operations import add_row_to_csv, \
    remove_row_from_csv  # Це припущення, що функції визначені в файлі csv_operations.py


def read_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)


def test_add_row_to_csv(tmpdir):
    # Створимо тимчасовий файл CSV
    p = tmpdir.join("test.csv")
    original_data = [
        ["first_name", "last_name", "age", "gender", "salary"],
        ["Elizabet", "Fork", "19", "Female", "3000"],
        ["Reginald", "Lidoo", "42", "Male", "2500"],
        ["Alexander", "Great", "30", "Male", "15000"]
    ]
    new_row = ["John", "Doe", "28", "Male", "5000"]

    # Запишемо оригінальні дані до файлу
    with open(str(p), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(original_data)

    # Додамо новий рядок
    add_row_to_csv(str(p), new_row)

    # Перевіримо, чи рядок додано
    result_data = read_csv(str(p))
    assert new_row in result_data, "New row was not added correctly"


def test_remove_row_from_csv(tmpdir):
    # Створимо тимчасовий файл CSV
    p = tmpdir.join("test.csv")
    original_data = [
        ["first_name", "last_name", "age", "gender", "salary"],
        ["Elizabet", "Fork", "19", "Female", "3000"],
        ["Reginald", "Lidoo", "42", "Male", "2500"],
        ["Alexander", "Great", "30", "Male", "15000"]
    ]
    row_to_remove = ["John", "Doe", "28", "Male", "5000"]
    p.write('\n'.join([','.join(line) for line in original_data]))

    # Видалимо рядок
    remove_row_from_csv(str(p), row_to_remove)

    # Перевіримо, чи рядок видалено
    result_data = read_csv(str(p))
    assert row_to_remove not in result_data
