main_menu = ['Главное меню',
             'Открыть файл',
             'Сохранить файл',
             'Показать контакты',
             'Добавить контак',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход']

main_menu_input_error = f'Ошибка ввода! Введите число от 1 до {len(main_menu) - 1}: '
empty_book = "Телефонная книга пуста или не открыта!"
load_successful = "Телефонная книга успешно загружена!"
save_successful = "Телефонная книга успешно сохранена!"
input_search_word = "Что будем искать: "
input_del_uid = "Введите ID контакта, который хотите удалить:"
input_rename_uid = "Введите ID контакта, который хотите изменить:"
good_bye = "До свидания!"

fields_new_contact = ["Введите имя контакта: ", "Введите телефон: ", "Введите комментарий: "]
fields_rename_contact = ["Введите новое имя(или Enter - без изменений) контакта: ", "Введите новый телефон(или Enter - без изменений): ", "Введите новый комментарий(или Enter - без изменений): "]
def new_contact_successful(name: str) -> str:
    return f"Контакт {name} успешно добавлен!"


def empty_search(word: str) -> str:
    return f"Контакты содержащие '{word}' не найдены"

def contact_deleted(name: str) -> str:
    return f"Контактк {name} успешно удален!"

def rename_successful(name: str) -> str:
    return f"Контакт {name} умпешно изменен!"